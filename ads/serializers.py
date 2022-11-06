from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import Location, Ad, Selection, Category
from ads.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from user.models import User


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        validators=[
            UniqueValidator(queryset=Ad.objects.all()),
            MinLengthValidator(5),
            MaxLengthValidator(10)
        ]
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class AdSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    name = serializers.CharField(
        validators=[
            MinLengthValidator(10),
        ]
    )
    price = serializers.IntegerField(
        validators=[
            MinValueValidator(0),
        ]
    )

    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ('author', 'image', )


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Selection
        fields = ('id', 'name', 'owner', 'items')


class SelectionDetailsSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = ('id', 'name', 'owner', 'items')


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('id', 'name')
