# Generated by Django 3.2 on 2021-05-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='office',
            field=models.CharField(default='Office not set', max_length=20),
        ),
    ]
