# Generated by Django 5.0 on 2023-12-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('fishbread', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fishbread',
            field=models.ManyToManyField(blank=True, to='fishbread.fishbread'),
        ),
    ]
