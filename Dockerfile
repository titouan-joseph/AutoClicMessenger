FROM python:3.9-slim

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.31.0
ENV FIREFOX_VER 91.13.0esr

ARG TARGETPLATFORM

RUN set -x \
    && apt update \
    && apt upgrade -y \
    && apt install -y \
    firefox-esr \
    curl \
    bzip2 \
    && pip install  \
    requests \
    selenium 

# Add latest FireFox
RUN set -x \
    && apt install -y \
    libx11-xcb1 \
    libdbus-glib-1-2 \
    && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
    && tar -jxf firefox-* \
    && mv firefox /opt/ \
    && chmod 755 /opt/firefox \
    && chmod 755 /opt/firefox/firefox

# Add geckodriver
RUN set -x \
    && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
    && tar zxf geckodriver-*.tar.gz \
    && mv geckodriver /usr/bin/

COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python ./Auto_clic_react.py