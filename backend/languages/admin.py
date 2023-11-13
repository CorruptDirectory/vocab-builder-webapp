from django.contrib import admin

from .models import Language, Translation, Word


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['name', 'code']
    list_filter = ['code']
    search_fields = ['name']
    ordering = ['name']


class TranslationAdmin(admin.ModelAdmin):
    model = Translation
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
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Word, WordAdmin)

