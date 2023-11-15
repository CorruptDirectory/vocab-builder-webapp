from django.urls import path
from .views import LanguageList, TranslationList, WordList

urlpatterns = [
    path('language/', LanguageList.as_view()),
    path('translation/', TranslationList.as_view()),
    path('word/', WordList.as_view()),
]
