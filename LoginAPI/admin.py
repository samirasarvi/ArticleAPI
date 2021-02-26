from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title','descripton')
    list_display = ('title','descripton')