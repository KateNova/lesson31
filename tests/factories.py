from datetime import date

import factory

from ads.models import Ad, Category
from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('name')
    username = factory.Faker('name')
    birth_date = date(2000, 1, 1)
    email = factory.Faker('email')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test'
    slug = factory.Sequence(lambda n: 'slug_%03d' % n)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = 'test'
    price = 50
    description = 'test description'
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
