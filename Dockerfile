FROM alpine:latest

MAINTAINER Jakob Runge <sicarius@g4t3.de>

RUN apk update \
 && apk add git python3-dev \
 && rm /var/cache/apk/APKINDEX*tar.gz

RUN git clone https://github.com/runjak/hoodedFigure /srv/hoodedFigure

WORKDIR /srv/hoodedFigure
ENTRYPOINT python3 main.py
