FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y gettext \
  && rm -rf /var/lib/apt/lists/*

# Sphinx 관련 패키지 설치
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

# start-docs 스크립트 복사 및 권한 설정
COPY ./compose/local/docs/start-docs /start-docs
RUN sed -i 's/\r$//g' /start-docs
RUN chmod +x /start-docs

WORKDIR /docs

CMD ["/start-docs"]
