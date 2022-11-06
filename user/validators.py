from datetime import date
from dateutil.relativedelta import relativedelta

from django.core.exceptions import ValidationError
from rest_framework import serializers


def not_rambler_validator(value):
    domain = value.split('@')[1]
    if 'rambler.ru' in domain:
        raise ValidationError(
            'Domain %(value)s is not permitted',
            params={'domain': domain},
        )


def check_date_lt_minus_nine_years(value: date):
    if value < date.today() - relativedelta(years=9):
        raise ValidationError(
            'You are younger than 9 years'
        )


class NotRamblerValidator:

    def __call__(self, value):
        domain = value.split('@')[1]
        if 'rambler.ru' in domain:
            raise serializers.ValidationError(
                f'Domain {domain} is not permitted'
            )


class DateLtMinusNineYears:

    def __call__(self, value):
        if value < date.today() - relativedelta(years=9):
            raise serializers.ValidationError(
                'You are younger than 9 years'
            )
