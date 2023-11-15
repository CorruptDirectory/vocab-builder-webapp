from rest_framework import serializers
from .models import Language, Translation, Word


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'code']


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['word', 'language', 'translated_text']


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['eng_word', 'image']
