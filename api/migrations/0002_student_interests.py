# Generated by Django 5.1.3 on 2024-11-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='interests',
            field=models.CharField(default='General', max_length=255),
        ),
    ]
