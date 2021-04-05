FROM python:3
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=flask-server.py
WORKDIR /code
COPY ./python /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
