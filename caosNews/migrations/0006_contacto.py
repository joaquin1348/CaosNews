# Generated by Django 3.2.3 on 2021-07-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caosNews', '0005_auto_20210702_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('nombre', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('apellidos', models.TextField(max_length=20)),
                ('correo', models.TextField()),
                ('comentario', models.TextField(max_length=350)),
            ],
        ),
    ]