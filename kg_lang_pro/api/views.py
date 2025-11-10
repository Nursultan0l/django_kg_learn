from django.shortcuts import render
from rest_framework import viewsets
from kg_lang_pro_app.models import Lesson, Documents, Letter, Numbers
from .serializers import *

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer
