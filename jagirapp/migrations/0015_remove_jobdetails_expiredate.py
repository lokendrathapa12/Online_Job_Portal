# Generated by Django 4.0.3 on 2022-04-20 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jagirapp', '0014_alter_jobdetails_expiredate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='expiredate',
        ),
    ]
