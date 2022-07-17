release: python manage.py migrate
web: gunicorn wajeProject.wsgi:application --log-file - --log-level debug