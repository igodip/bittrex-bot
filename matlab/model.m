clear all;
close all;
clc;

a = 1;
b = 2;

% Loading data from sqlite

conn = sqlite('E:\git\bittrex\bitcoin.db');
history_data = fetch(conn,'SELECT * FROM history');

%% Print bid and ask price during time
[rows,cols] = size(history_data);

bid_row = [];
ask_row = [];

for k = 1:rows
    bid_row = [bid_row ;cell2mat(history_data(k,2))];
    ask_row = [ask_row ;cell2mat(history_data(k,3))];
end

x = linspace(1,rows,rows);
rsi = rsindex(bid_row,26);

subplot(2,1,1);
plot(x,bid_row,x,ask_row)

subplot(2,1,2);
plot(x,rsi);

%%

% 1 timestamp
% 2 bd
% 3 ask
% 4 bought
% 5 sold

% Algorithm parameter

threshold_up = linspace(-1,1,100);
threshold_down = linspace(-1,1,100);

result = [];

max = 0;

for i = threshold_up
    
    temp = [];
    
    for j = threshold_down
        
        if j > i
            temp = [temp 0];
            continue
        end
        
        balance_usd = 10000;
        balance_coin = 0;
        
        
        
        for k = 1:rows
            
            bought = cell2mat(history_data(k,4));
            sold = cell2mat(history_data(k,5));
            
            bid = cell2mat(history_data(k,2));
            ask = cell2mat(history_data(k,3));
            
            ratio = ((bought - sold)/(bought+sold));
            
            if ratio > i
                balance_coin = balance_coin + balance_usd/ask;
                balance_usd = 0;
            elseif ratio < j
                balance_usd = balance_usd + balance_coin*bid;
                balance_coin = 0;
            end
            
        end
        
        balance_usd = balance_usd + balance_coin*bid;
        
        if balance_usd > max
            max = balance_usd
            disp(i);
            disp(j);
            
        end
        
        temp = [temp balance_usd];
        
    end
    
    result = [result; temp];
    
end


%% Plotting gradient for optimization

[px,py] = gradient(result);

%Plot the contour lines and vectors in the same figure.

figure
contour(x,y,result)
hold on
quiver(x,y,px,py)
hold off
