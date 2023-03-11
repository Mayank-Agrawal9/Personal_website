from rest_framework import serializers
from first_app.models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactForm
        fields = '__all__'
