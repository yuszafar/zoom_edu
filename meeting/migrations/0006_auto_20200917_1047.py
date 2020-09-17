# Generated by Django 3.1.1 on 2020-09-17 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0005_auto_20200911_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='group',
        ),
        migrations.AddField(
            model_name='lesson',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.studentgroup'),
        ),
    ]
