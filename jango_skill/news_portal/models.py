from django.db import models

# Create your models here.


class News(models.Model):
    """Новости."""
    name = models.CharField(verbose_name="Имя", max_length=50, unique=True)
    chapter = models.PositiveIntegerField(verbose_name="Разделы")

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Новости"