from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import Language, TranslatedWord, Word
from .serializers import LanguageSerializer, TranslatedWordExpandedSerializer, TranslatedWordSerializer, WordSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class TranslatedWordList(generics.ListCreateAPIView):
    queryset = TranslatedWord.objects.all()
    serializer_class = TranslatedWordSerializer

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordListView(APIView):
    def get(self, request, format=None):
        count = request.query_params.get('count', None)
        print(count)
        if count is not None and count.isdigit():
            count = int(count)
            words = Word.objects.all()[:count]
        else:
            words = Word.objects.all()
        
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)


class WordListSpecifiedLanguage(APIView):
    def get(self, request, format=None):
        language_code = request.query_params.get("code", None) 
        words = TranslatedWord.objects.filter(language__code=language_code)
        serializer = TranslatedWordExpandedSerializer(words, many=True)
        return Response(serializer.data)

        