# Generated by Django 3.1.2 on 2020-10-29 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_task_base64text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='base64Text',
        ),
    ]
