# Generated by Django 3.0.6 on 2021-06-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routerapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routerdetails',
            name='payload',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
