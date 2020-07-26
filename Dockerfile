FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code_atlas
WORKDIR /code_atlas
COPY requirements.txt /code_atlas/
RUN pip install -r requirements.txt
COPY . /code_atlas/
