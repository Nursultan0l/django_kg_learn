from rest_framework import serializers
from kg_lang_pro_app.models import Lesson , Documents, Letter, Numbers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'

class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'


