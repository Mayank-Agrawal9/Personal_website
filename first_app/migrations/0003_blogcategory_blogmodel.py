# Generated by Django 4.1.5 on 2023-03-10 20:10

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('first_app', '0002_homepage_blog_title_homepage_project_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('subtitle', models.CharField(max_length=100, null=True, unique=True)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=200, null=True)),
                ('meta_description', models.CharField(max_length=250, null=True)),
                ('icon', models.ImageField(upload_to='images/')),
                ('banner_img', models.ImageField(upload_to='images/')),
                ('outer_page_info', models.CharField(max_length=90, null=True)),
                ('inner_bg_img', models.ImageField(null=True, upload_to='images/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.blogcategory')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]