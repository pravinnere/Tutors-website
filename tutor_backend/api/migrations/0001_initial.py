# Generated by Django 4.0.1 on 2022-02-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('semail', models.EmailField(max_length=30, unique=True)),
                ('spassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=30)),
                ('temail', models.EmailField(max_length=30, unique=True)),
                ('tpassword', models.CharField(max_length=20)),
            ],
        ),
    ]