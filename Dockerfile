FROM python:3.6

RUN pip install devpi-client
RUN devpi use --set-cfg https://devpi.realworld.net.au/realworld/prod
RUN mkdir /opt/app
COPY ./app/requirements.txt /opt/app/requirements.txt
RUN pip install -U -r /opt/app/requirements.txt
COPY docker_entrypoint.sh /
COPY wait-for-it.sh /
RUN chmod a+x /wait-for-it.sh
RUN chmod a+x /docker_entrypoint.sh
WORKDIR /opt/app/src
CMD /wait-for-it.sh pg:5432 -- python /opt/app/src/manage.py runserver 0.0.0.0:8000
