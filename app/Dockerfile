FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN  pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

RUN python setup.py sdist bdist_wheel
RUN cp dist/*.whl /app/wheels/


FROM python:3.9-slim

WORKDIR /app
COPY kafkaspam/ .

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

ENTRYPOINT ["python"]
CMD ["-m", "kafkaspam"]
