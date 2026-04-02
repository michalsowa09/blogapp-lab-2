from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):  #definicja modelu (czyli tabeli w bazie danych)
    STATUS_CHOICES = (
        ('draft', 'Szkic'), #wersja robocza posta
        ('published', 'Opublikowano'), #opublikowany post
    )

    title = models.CharField(max_length=200, verbose_name="Tytuł")  #krótki tekst (max 200 znaków)
    content = models.TextField(verbose_name="Treść") #dłuższy tekst (bez limitu znaków)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor") #powiązanie z użytkownikiem, CASCADE = jak usunie się użytkownika, jego posty też znikną
    created_at = models.DateTimeField(auto_now_add=True) #data utworzenia (ustawiana automatycznie tylko raz)
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Data publikacji")   #data publikacji (domyślnie teraz)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='published') #status posta (draft lub published)

    class Meta:
        ordering = ["-published_at"] #Najnowsze na górze
        verbose_name = "Post"
        verbose_name_plural = "Posty"

    def __str__(self):
        return self.title