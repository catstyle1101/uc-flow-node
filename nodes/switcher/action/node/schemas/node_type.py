from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as BaseNodeType, DisplayOptions, OptionValue,
)
from nodes.switcher.action.node.static.icon import ICON
from nodes.switcher.action.node.schemas.enums import FirstDropdown, Parameters, SecondDropdown, Switch


class NodeType(flow.NodeType):
    id: str = '60096456-c5cf-4541-a26d-82158e02e39a'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'Switcher'
    icon: str = ICON
    version: int = 1
    description: str = 'simple switcher for fields'
    defaults: Defaults = Defaults(name='switcher-action', color='#00FF00')
    properties: List[Property] = [
        Property(
            displayName='switch',
            name=Parameters.switch_field,
            type=Property.Type.BOOLEAN,
            placeholder='switch placeholder',
            description='Switch, which enables fields',
            required=True,
            default=False,
        ),
        Property(
            displayName='Поле №1',
            name=Parameters.first_field,
            type=Property.Type.OPTIONS,
            description='Введите значение для поля №1',
            required=True,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'switch': [Switch.enable],
                },
            ),
            options=[
                OptionValue(
                    name=FirstDropdown.first_value.value,
                    value=FirstDropdown.first_value,
                ),
                OptionValue(
                    name=FirstDropdown.second_value.value,
                    value=FirstDropdown.second_value,
                ),
            ],
        ),
        Property(
            displayName='Поле №2',
            name=Parameters.second_field,
            type=Property.Type.OPTIONS,
            required=True,
            noDataExpression=True,
            description='Введите значение для поля №2',
            displayOptions=DisplayOptions(
                show={
                    'switch': [Switch.enable],
                },
            ),
            options=[
                OptionValue(
                    name=SecondDropdown.first_value.value,
                    value=SecondDropdown.first_value,
                ),
                OptionValue(
                    name=SecondDropdown.second_value.value,
                    value=SecondDropdown.second_value,
                ),
            ],
        ),
        Property(
            displayName='Электронная почта',
            name=Parameters.email_field,
            type=Property.Type.EMAIL,
            placeholder='mymail@google.com',
            description='Введите электронную почту',
            displayOptions=DisplayOptions(
                show={
                    'switch': [Switch.enable],
                    'first_field': [FirstDropdown.first_value],
                    'second_field': [SecondDropdown.first_value],
                },
            ),
        ),
        Property(
            displayName='Поле даты/времени',
            name=Parameters.datetime_field,
            type=Property.Type.DATETIME,
            description='Введите необходимую дату и время',
            displayOptions=DisplayOptions(
                show={
                    'switch': [Switch.enable],
                    'first_field': [FirstDropdown.second_value],
                    'second_field': [SecondDropdown.second_value],
                },
            ),
        ),
    ]
