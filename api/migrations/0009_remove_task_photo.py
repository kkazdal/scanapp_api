# Generated by Django 3.1.2 on 2020-10-27 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201027_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='photo',
        ),
    ]