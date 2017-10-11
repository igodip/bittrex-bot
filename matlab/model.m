clear all;
close all;
clc;

a = 1;
b = 2;

% Loading data from sqlite

conn = sqlite('E:\git\bittrex\bitcoin.db');
history_data = fetch(conn,'SELECT * FROM history');

