from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class ContactForm(models.Model):
    objects = None
    name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'


class HomePage(models.Model):
    meta_title = models.CharField(max_length=250, null=True)
    meta_keyword = models.CharField(max_length=250, null=True)
    meta_description = models.CharField(max_length=250, null=True)
    image_one = models.ImageField(blank=True, upload_to='personal_image')
    image_two = models.ImageField(blank=True, upload_to='personal_image')
    about_me_title = models.TextField(null=True, blank=True)
    about_image = models.ImageField(null=True, blank=True, upload_to='personal_image', )
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    total_complete_project = models.CharField(max_length=255, null=True, blank=True)
    resume_title = models.TextField(null=True, blank=True)
    resume = models.ImageField(null=True, blank=True, upload_to='personal_image', )
    service_title = models.TextField(null=True, blank=True)
    skill_title = models.TextField(null=True, blank=True)
    project_title = models.TextField(null=True, blank=True)
    blog_title = models.TextField(null=True, blank=True)
    award = models.CharField(max_length=255, null=True, blank=True)
    happy_customer = models.CharField(max_length=255, null=True, blank=True)
    cup_of_coffee = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    contact_us_title = models.TextField(null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    footer_title = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'


class EducationDetail(models.Model):
    year = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Education Detail'
        verbose_name_plural = 'Education Details'


class Service(models.Model):
    icon = models.ImageField(blank=True, upload_to='personal_image')
    title = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Skill(models.Model):
    skill_name = models.CharField(max_length=255, null=True, blank=True)
    percentage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.skill_name)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class BlogCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class BlogModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=100, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=200, null=True)
    meta_description = models.CharField(max_length=250, null=True)
    icon = models.ImageField(upload_to="images/")
    banner_img = models.ImageField(upload_to="images/")
    outer_page_info = models.CharField(max_length=255, null=True)
    blog_category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    inner_bg_img = models.ImageField(upload_to="images/", null=True)
    content = RichTextUploadingField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    quote_title = models.CharField(max_length=250, null=True)
    quote_description = models.TextField(null=True, blank=True)
    quote_image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class OurProject(models.Model):
    project_image = models.ImageField(upload_to="images/", null=True, blank=True)
    project_name = models.CharField(max_length=250, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    project_link = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.project_name
