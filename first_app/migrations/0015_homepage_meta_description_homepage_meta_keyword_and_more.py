# Generated by Django 4.1.5 on 2023-03-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_alter_homepage_about_me_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='meta_description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='meta_keyword',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='meta_title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]