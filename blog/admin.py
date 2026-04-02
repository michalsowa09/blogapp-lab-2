from django.contrib import admin
from .models import Post

@admin.register(Post) #tu rejestruję model Post w panelu admina
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "published_at")
    #widoczne kolumny na liście postów - admin

    list_filter = ("status", "published_at", "author")
    #filtry

    search_fields = ("title", "content")
    #pole wyszukiwania

    date_hierarchy = "published_at"
    #nawigacja po dacie

