from django.contrib import admin
from .models import MyPost


@admin.register(MyPost)
class MyPost(admin.ModelAdmin):
    """
        Перечень сообщений
    """
    list_display = [field.name for field in MyPost._meta.fields]  # все поля выводит в цикле
    search_fields = ["title"]
    list_filter = ["title"]
