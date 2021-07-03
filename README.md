### Start
docker-compose up -d

docker exec -it django ./manage.py migrate

docker exec -it django ./manage.py loaddata sample_db.json

docker exec -it django ./manage.py createsuperuser

npm install

gulp watch

./manage.py runserver 0.0.0.0:8000
