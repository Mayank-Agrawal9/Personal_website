from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from rest_framework import viewsets
from taggit.models import Tag

from first_app.models import *
from first_app.serailizers import ContactFormSerializer


# Create your views here.


class ContactFormViewSet(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()


class HomePages(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePages, self).get_context_data(**kwargs)
        context['home_page'] = HomePage.objects.latest('id')
        context['projects'] = OurProject.objects.all()
        context['skills'] = Skill.objects.all()
        context['services'] = Service.objects.all().order_by('-created_on')
        context['education_details'] = EducationDetail.objects.all().order_by('-id')
        context['blog_details'] = BlogModel.objects.filter(status=1).order_by('-created_on')[:2]
        return context


class BlogDetail(DetailView):
    model = BlogModel
    template_name = 'single.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_page'] = HomePage.objects.latest('id')
        context['tag'] = Tag.objects.all()
        context['blog_category'] = BlogCategory.objects.all()
        context['services'] = Service.objects.all().order_by('-created_on')
        context['projects'] = OurProject.objects.all()
        context['blog_details'] = BlogModel.objects.filter(status=1).order_by('-created_on')[:2]
        context['comments'] = CommentsModel.objects.select_related().filter(post=self.get_object())
        return context

    def post(self, *args, **kwargs):
        comment = self.request.POST.get('message')
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        phone = self.request.POST.get('phone')
        post = self.get_object()
        if comment and name and email and phone:
            comments = CommentsModel.objects.create(post=post, name=name, email=email, phone=phone, comment=comment)
            comments.save()
            return redirect('blog_inner1', slug=post.slug)
        return redirect('blog_inner1', slug=post.slug)
