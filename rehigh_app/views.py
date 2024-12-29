from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from . import models
from rest_framework.response import Response
from .serializers import BlogSerializer, SwiperSerializer, AppointmentSerializer, VariationSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def blog_list(request):
    if request.method == 'GET':
        blogs = models.Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def blog_detail(request, pk):
    try:
        blog = models.Blog.objects.get(pk=pk)
    except models.Blog.DoesNotExist:
        return Response({"error": "Blog Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def swiper_list(request):
    if request.method == 'GET':
        swipers = models.Swiper.objects.all()
        serializer = SwiperSerializer(swipers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SwiperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def swiper_detail(request, pk):
    try:
        swiper = models.Swiper.objects.get(pk=pk)
    except models.Swiper.DoesNotExist:
        return Response({"error": "Swiper Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SwiperSerializer(swiper)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SwiperSerializer(swiper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        swiper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def appointment_list(request):
    if request.method == 'GET':
        appointments = models.Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def appointment_detail(request, pk):
    try:
        appointment = models.Appointment.objects.get(pk=pk)
    except models.Appointment.DoesNotExist:
        return Response({"error": "Appointment Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def variation_list(request):
    if request.method == 'GET':
        variations = models.Variation.objects.all()
        serializer = VariationSerializer(variations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VariationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def variation_detail(request, pk):
    try:
        variation = models.Variation.objects.get(pk=pk)
    except models.Variation.DoesNotExist:
        return Response({"error": "Variation not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VariationSerializer(variation)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VariationSerializer(variation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        variation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
