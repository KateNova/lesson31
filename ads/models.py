from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(10)
        ],
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True
    )
    lat = models.FloatField(
        null=True,
        blank=True
    )
    lng = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Ad(models.Model):
    name = models.CharField(
        max_length=250,
        validators=[
            MinLengthValidator(10),
        ],
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads'
    )
    price = models.PositiveIntegerField()
    description = models.CharField(
        max_length=2000,
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        validators=[
            BaseValidator(False),
        ]
    )
    image = models.ImageField(
        upload_to='images/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('id', )


class Selection(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='selections'
    )
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
