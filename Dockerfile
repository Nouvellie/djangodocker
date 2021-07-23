FROM python:3.9.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip setuptools

RUN useradd -ms /bin/bash myproject

USER myproject

WORKDIR /home/myproject

RUN python3 -m venv env

COPY --chown=myproject ./src/myproject/requirements /home/myproject/requirements/

RUN ./env/bin/pip3 install -r /home/myproject/requirements/base.txt

COPY --chown=myproject ./src/myproject /home/myproject/