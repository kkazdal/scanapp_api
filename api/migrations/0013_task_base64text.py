# Generated by Django 3.1.2 on 2020-10-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201027_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='base64Text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
