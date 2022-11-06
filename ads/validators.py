from rest_framework import serializers


class MinValueValidator:

    def __init__(self, minimum):
        self.minimum = minimum

    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError(
                f'Value should be greater or equal to 0 (zero)'
            )


class MinLengthValidator:

    def __init__(self, minimum):
        self.minimum = minimum

    def __call__(self, value):
        if len(value) < self.minimum:
            raise serializers.ValidationError(
                f'Value should be greater or equal to {self.minimum}'
            )


class MaxLengthValidator:

    def __init__(self, maximum):
        self.maximum = maximum

    def __call__(self, value):
        if len(value) > self.maximum:
            raise serializers.ValidationError(
                f'Value should be less or equal to {self.maximum}'
            )
