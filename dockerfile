FROM python:3.9.13

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD cd ./CRM \
    && python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && python manage.py runserver 0.0.0.0:8000 \
