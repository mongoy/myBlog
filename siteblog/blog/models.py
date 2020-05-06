from django.db import models


class MyPost(models.Model):
    """
        Сообщения
    """
    title = models.CharField(max_length=150, unique=True)
    text = models.TextField()
    img = models.ImageField(upload_to='post')
    data_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ('data_stamp',)  # сортировка

