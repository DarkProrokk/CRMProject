FROM python:3.9.13

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD cd ./CRM && python manage.py migrate && python manage.py runserver 0.0.0.0:8000