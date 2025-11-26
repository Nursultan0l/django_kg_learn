from http.client import responses

from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Register
class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                'message': 'success',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'tokens':{
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }
            return Response(response_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Letters CRUD
class LettersAPIList(generics.ListCreateAPIView):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer
class LettersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer
class LettersAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer

# Lessons CRUD
class LessonsAPIList(generics.ListCreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
class LessonsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
class LessonsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

# Documents CRUD
class DocumentsAPIList(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
class DocumentsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
class DocumentsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


# Numbers CRUD
class NumbersAPIList(generics.ListCreateAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer
class NumbersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer
class NumbersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer