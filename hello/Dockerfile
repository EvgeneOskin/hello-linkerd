FROM pypi/muffin

RUN pip install muffin py_zipkin gunicorn==19.6.0

ADD app.py config.py /app/

WORKDIR /app

CMD ["muffin", "app", "run", "--config", "config", "--bind", "0.0.0.0:80"]
