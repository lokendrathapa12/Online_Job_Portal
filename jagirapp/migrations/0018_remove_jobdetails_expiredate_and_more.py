# Generated by Django 4.0.3 on 2022-04-20 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jagirapp', '0017_alter_jobdetails_expiredate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='expiredate',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='jobtype',
        ),
    ]