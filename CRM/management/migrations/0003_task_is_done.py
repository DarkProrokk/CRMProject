# Generated by Django 4.2.7 on 2023-11-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]