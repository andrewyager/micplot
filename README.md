# MicPlot

This is a Django App for managing show scripts, characters and mic plots.

It's a work in progress, and PR's are welcome.

It's docker based, and designed to be run in a docker container. The easiest way is to use docker-compose

## running the dev version

```
% cp env.env .env
% echo "DJANGO_DEBUG=True" >> .env
% docker-compose build app
% docker-compose run --rm app ./manage.py migrate
% docker-compose run --rm app ./manage.py createsuperuser
% docker-compose up app
```

The app lives at http://localhost:8002/admin and you can log in using the credentials you set up above.

## running the prod version

You can run the app more permanently using the uwsgi and nginx container:

```
% docker-compose build uwsgi nginx
% docker-compose up -d uwsgi nginx
```

(The production version will run migrate, collectstatic and other django actions on reload)

@todo

- Add microphone detail
- Add better import/export
- Create some views to handle all the exports we want
- move these to github issues