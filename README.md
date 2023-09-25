# Assignment Documentation 
- Updated basic auth to token auth
- user docker-compose insted of docker, it will automatically setup the postgres database as well(docker -> just copying and prepareing the env, docker-composer runs the commands inside the docker ).
* -- run : docker-compose up -d --build  (if the server didn't come up, just run docker-compose down -v , then again the docker-compose up -d --build)
* -- DB Migration : docker-compose exec app python manage.py migrate
* -- Create Super User : docker-compose exec app python manage.py createsuperuser

- API endpoints updated 
- USE POSTMAN insted of broweser, use the attached postman collection and import to postman -> https://www.postman.com/janithau/workspace/pub/collection/10324899-edbaf9c6-ebef-4f87-ba02-4a3e523e4a9c?action=share&creator=10324899
- read the Assignment Documentation.pdf carefully.
- removed the hard-coded environment variables and secrets(make sure the .env file is available)
