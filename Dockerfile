FROM python:3.9-slim as base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./src /code/src
COPY metadata.csv /code
ENV PYTHONPATH "${PYTHONPATH}:$(pwd)"

FROM base as test
COPY ./tests /code/tests
CMD ["pytest"]

FROM base as development
CMD ["uvicorn", "--reload", "--app-dir", "src", "main:app"]