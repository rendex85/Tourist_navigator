# Generated by Django 2.2.6 on 2020-04-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourist_app', '0002_auto_20200405_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routecomposition',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]