from django.contrib import admin
from first_app.models import *
# Register your models here.


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(EducationDetail)
class EducationDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name')


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    list_display = ('category_name',)
    list_filter = ("category_name",)
    search_fields = ['category_name']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):

    list_display = ('comment',)
    list_filter = ("comment",)
    search_fields = ['comment']


@admin.register(OurProject)
class OurProjectAdmin(admin.ModelAdmin):

    list_display = ('project_name',)
    # list_filter = ("comment",)
    search_fields = ['comment']