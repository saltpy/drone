FROM python:3.7-alpine

ADD dist/drone-0.1.0-py3-none-any.whl /srv

WORKDIR /srv

RUN pip install drone-0.1.0-py3-none-any.whl

CMD python -m drone
