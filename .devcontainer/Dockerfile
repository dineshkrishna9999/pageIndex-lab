FROM mcr.microsoft.com/devcontainers/python:3.14-trixie

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install --no-install-recommends build-essential \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV SHELL=/bin/zsh
