# Generated by Django 5.1.2 on 2024-11-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
