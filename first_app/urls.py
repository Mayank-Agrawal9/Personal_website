from django.urls import path, include

from rest_framework.routers import DefaultRouter

from first_app.views import ContactFormViewSet

router = DefaultRouter()

router.register(r'contact-form', ContactFormViewSet, basename="company")


urlpatterns = [
    path('', include(router.urls)),

]