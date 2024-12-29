from rest_framework import serializers
from .models import Blog, Swiper, Appointment, Variation

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'

class SwiperSerializer(serializers.ModelSerializer):
    variation = VariationSerializer(read_only=True, many=True, source='variations')

    class Meta:
        model = Swiper
        fields = ['id','title', 'description', 'desktop_image', 'phone_image', 'button_text', 'button_link', 'variation']


