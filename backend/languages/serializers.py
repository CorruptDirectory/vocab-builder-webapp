from rest_framework import serializers
from .models import Language, Sentence, SentenceTranslation, Topic, TranslatedWord, Word


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'code']


class TopicSerializer():
    class Meta:
        model = Topic
        fields = ['name']


class TranslatedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedWord
        fields = ['word', 'language', 'translated_text']


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['text']


class SentenceTranslationSerializer(serializers.ModelSerializer):
    sentence_eng = SentenceSerializer()
    class Meta:
        model = SentenceTranslation
        fields = ['text', 'sentence_eng']


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['eng_word', 'image']


# Nested serializers
class SentencesSerializer (serializers.ModelSerializer):
    pass

class TranslatedWordExpandedSerializer(serializers.ModelSerializer):
    sentences = SentenceTranslationSerializer(many=True, read_only=True)
    word = WordSerializer()
        
    class Meta:
        model = TranslatedWord
        fields = ['sentences', 'translated_text', 'word']


