from enum import Enum


class DropdownWithTwoValues(str, Enum):
    first_value = 'Значение 1'
    second_value = 'Значение 2'
