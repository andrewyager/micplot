#!/bin/bash

cd /opt/app/src
/wait-for-it.sh pg:5432
python3 manage.py migrate
python3 manage.py createcachetable
python3 manage.py collectstatic --noinput

touch /srv/logs/gunicorn.log
touch /srv/logs/access.log

chown -R www-data:www-data /srv/logs
chown -R www-data:www-data /opt/static/media

echo Starting Gunicorn.
exec gunicorn micplot.wsgi:application \
    --name micplot \
    --bind 0.0.0.0:8000 \
    --workers 10 \
    --user www-data \
    --group www-data \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    --timeout=300 \
    "$@"