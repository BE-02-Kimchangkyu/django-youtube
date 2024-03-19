# 도커 이미지 구축
# alpine: linux의 경량화 버전
FROM python:3.11-alpine3.19

LABEL maintainer == 'okyuo'

# 파이썬 관련 로그를 확인할 수 있는 옵션(기본값은 0 = False)
ENV PYTHONUNBUFFERED 1

# 로컬에서 작업한 파일들을 가상환경으로 복사하는 코드
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# 리눅스 -> venv  // && \ <= 리눅스에서 엔터
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps build-base \
        postgresql-dev musl-dev && \

    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \ 
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
    

ENV PATH="/py/bin:$PATH"

USER django-user
