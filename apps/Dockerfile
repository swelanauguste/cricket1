FROM python:3.10.0a6-buster


COPY requirements.txt /app/requirements.txt


RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache -r /app/requirements.txt

WORKDIR /apps



ADD . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "-w", "3", "cf.wsgi:application"]

CMD gunicorn cf.wsgi:application --bind 0.0.0.0:$PORT
