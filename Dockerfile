FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY backend /code/
# netcat lets me probe TCP connections, which I use to check if I can connect to the db
RUN apt update; \
   apt install netcat -y
# I have to copy the file to a different directory in the container, so I can
# change its permisions
COPY entrypoint.sh /usr/bin/entrypoint
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["entrypoint"]