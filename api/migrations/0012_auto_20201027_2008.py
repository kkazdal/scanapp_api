# Generated by Django 3.1.2 on 2020-10-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201027_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deneme',
        ),
        migrations.AddField(
            model_name='task',
            name='photo',
            field=models.ImageField(default=1, upload_to='media/photo/'),
            preserve_default=False,
        ),
    ]
