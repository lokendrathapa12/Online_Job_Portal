# Generated by Django 4.0.3 on 2022-04-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagirapp', '0008_remove_feedback_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='expiredate',
            field=models.DateField(default='', max_length=50),
        ),
    ]
