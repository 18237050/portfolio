# Generated by Django 3.2.5 on 2021-08-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='description_work',
            field=models.TextField(blank=True, null=True, verbose_name='概要文'),
        ),
    ]
