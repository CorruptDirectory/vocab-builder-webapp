from django.contrib import admin

from .models import Language, Topic, TranslatedWord, Word, Sentence, SentenceTranslation


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['name', 'code']
    list_filter = ['code']
    search_fields = ['name']
    ordering = ['name']


class TranslatedWordAdmin(admin.ModelAdmin):
    model = TranslatedWord
    list_display = ['word', 'language', 'translated_text']
    list_filter = ['language__name']
    search_fields = ['translated_text']
    ordering = ['word']


class WordAdmin(admin.ModelAdmin):
    model = Word
    list_display = ['eng_word', 'image']
    search_fields = ['eng_word']
    ordering = ['eng_word']

admin.site.register(Language, LanguageAdmin)
admin.site.register(Topic)
admin.site.register(TranslatedWord, TranslatedWordAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Sentence)
admin.site.register(SentenceTranslation)

