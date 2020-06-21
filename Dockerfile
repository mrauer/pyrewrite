FROM alpine:3.7

RUN apk add --no-cache python3 bash gcc python3-dev jpeg-dev zlib-dev build-base linux-headers

WORKDIR /usr/src/app
COPY . .
RUN pip3 install --upgrade pip -r requirements.txt
RUN cp -R /usr/src/app/samples /tmp
