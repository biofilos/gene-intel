#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."
  # these variables are specified in the environment section of the docker-compose
  # the nc command checks that the container can connect to the db
  while ! nc -z $SQL_HOST $SQL_PORT
  do
    sleep 0.1
  done
  echo "PostgreSQL started"
fi
# things to do before running server

# Then, run whatever I put in the command section of the docker-compose
"$@"
exec "$@"