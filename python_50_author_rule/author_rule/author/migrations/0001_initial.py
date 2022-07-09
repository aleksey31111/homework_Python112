# Generated by Django 4.0.5 on 2022-07-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=40)),
                ('born_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('name_project', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]