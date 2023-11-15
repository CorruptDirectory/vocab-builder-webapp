from rest_framework import generics
from .models import Language, Translation, Word
from .serializers import LanguageSerializer, TranslationSerializer, WordSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class TranslationList(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
