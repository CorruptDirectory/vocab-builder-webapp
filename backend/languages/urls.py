from django.urls import path
from .views import LanguageList, TranslatedWordList, WordList, WordListView,WordListSpecifiedLanguage

urlpatterns = [
    path('language/', LanguageList.as_view()),
    path('translated-word-list/', TranslatedWordList.as_view()),
    path('words/languange', WordListSpecifiedLanguage.as_view()),
    path('words/', WordList.as_view()),
    path('word/', WordListView.as_view()),
]
