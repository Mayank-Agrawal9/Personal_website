# Generated by Django 4.1.5 on 2023-03-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_homepage_facebook_link_homepage_instagram_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='quote_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='quote_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='quote_title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
