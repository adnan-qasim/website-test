# Generated by Django 4.1.2 on 2022-11-14 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='email',
            new_name='e_Mail',
        ),
        migrations.RenameField(
            model_name='accounts',
            old_name='passw',
            new_name='password',
        ),
    ]