# Generated by Django 3.0.6 on 2020-07-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.URLField(default='https://incablet-tests.s3.ap-south-1.amazonaws.com/conference-content/photos/sponsors/Anand.jpeg', max_length=300),
            preserve_default=False,
        ),
    ]