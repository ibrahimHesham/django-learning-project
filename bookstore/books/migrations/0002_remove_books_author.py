# Generated by Django 3.2 on 2021-04-22 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
    ]