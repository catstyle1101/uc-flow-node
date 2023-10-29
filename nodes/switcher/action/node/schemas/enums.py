from enum import Enum


class Switch(Enum):
    enable = True
    disable = False


class FirstDropdown(str, Enum):
    first_value = 'Значение 1'
    second_value = 'Значение 2'


class SecondDropdown(str, Enum):
    first_value = 'Значение 1'
    second_value = 'Значение 2'


class Parameters(str, Enum):
    switch_field = 'switch'
    first_field = 'first_field'
    second_field = 'second_field'
    email_field = 'email'
    datetime_field = 'datetime'
