from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.pk}]"


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images')
    first = models.ImageField(upload_to='profile_images', default='')
    second = models.ImageField(upload_to='profile_images', default='')
    third = models.ImageField(upload_to='profile_images', default='')
    forth = models.ImageField(upload_to='profile_images', default='')
    description = models.TextField(default='')
    city = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=False,
        db_index=True,
        null=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f"Todo: {self.title} {self.description[:30]} [{self.pk}]"


class Task(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=False,
        db_index=True,
        null=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"Task: {self.title} {self.description[:30]} [{self.pk}]"


class Product(models.Model):
    label = models.CharField("Наименование", max_length=100, unique=True)
    amount = models.IntegerField("Количество")
    not_bubble_price = models.IntegerField("Стоимость без накрутки")
    bubble_percentage = models.IntegerField("Процент накрутки")
    final_price = models.IntegerField("Итоговая стоимость")
    vat_price = models.IntegerField("Стоимость с НДС")
    overall = models.IntegerField("Итоговая")

    def __repr__(self):
        return str(self.label)

    def __str__(self):
        return str(self.label)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"






