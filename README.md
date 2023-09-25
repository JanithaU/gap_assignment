# Assignment Documentation 
- Updated basic auth to token auth
- user docker-compose insted of docker, it will automatically setup the postgres database as well(docker -> just copying and prepareing the env, docker-composer runs the commands inside the docker ).
-- run : docker-compose up -d --build  (if the server didn't come up, just run docker-compose down -v , then again the docker-compose up -d --build)
-- DB Migration : docker-compose exec app python manage.py migrate
-- Create Super User : docker-compose exec app python manage.py createsuperuser

- API endpoints updated 
- USE POSTMAN insted of broweser, use the attached postman collection and import to postman -> https://api.postman.com/collections/10324899-7a89e1b0-ec16-4733-93de-8b3ab0e01051?access_key=PMAT-01HB6V6VNZTGVDPS2R40BX7D8K 
- read the Assignment Documentation.pdf carefully.
- removed the hard-coded environment variables and secrets(make sure the .env file is available)
