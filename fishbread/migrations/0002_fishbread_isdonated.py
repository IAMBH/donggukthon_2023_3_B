# Generated by Django 5.0 on 2023-12-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishbread', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishbread',
            name='isDonated',
            field=models.BooleanField(default=False),
        ),
    ]