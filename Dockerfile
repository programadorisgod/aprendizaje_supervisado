ARG ALPINEVERSION=alpine3.18
ARG DIR=/project

FROM python:${ALPINEVERSION}

WORKDIR /${DIR}

COPY . .

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.frameworks.main:app", "--bind", "--reload"]
