# Generated by Django 3.1.1 on 2020-09-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='zoom_start_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
