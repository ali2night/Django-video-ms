service nginx start
python manage.py migrate
python manage.py makemigrations movies
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
