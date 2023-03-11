"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

from first_app.views import HomePages, BlogDetail
from portfolio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('first_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', TemplateView.as_view(template_name='home_page.html')),
    path('', HomePages.as_view(template_name='home_page.html')),
    # path('single', TemplateView.as_view(template_name='single.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),
    path('thank-you', TemplateView.as_view(template_name='thank-you.html')),
    path('<slug:slug>/', BlogDetail.as_view(), name='blog_inner1'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('robots.txt', RedirectView.as_view(url="/robots.txt"), name="robot"),
    path('sitemap.xml/', TemplateView.as_view(template_name="sitemap.xml", content_type='text/plain')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
