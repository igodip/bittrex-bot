FROM python:2.7-alpine

ENV TZ 'Asia/Dubai'
#ENV DEBUG_LEVEL 'INFO'

RUN apk add --no-cache tzdata

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
	pip install -r /tmp/requirements.txt

# Cleaning up
RUN rm -Rf /root/.cache && \
	rm -Rf /tmp/*

ADD conf/supervisord.conf /etc/supervisord.conf

CMD supervisord -c /etc/supervisord.conf