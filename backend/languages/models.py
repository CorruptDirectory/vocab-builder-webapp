from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.code}"
     

class Word(models.Model):
    eng_word = models.CharField(max_length=100, help_text="Word in English language.")
    image = models.ImageField(upload_to='word_images/', blank=True, null=True)

    def __str__(self):
        return self.eng_word
    

class Translation(models.Model):
    word = models.ForeignKey(Word, related_name="translations", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    translated_text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.translated_text} ({ self.language.name})"
    
    
