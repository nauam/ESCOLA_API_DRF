# Generated by Django 3.2.9 on 2021-11-26 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='date_nascimento',
            new_name='data_nascimento',
        ),
    ]
