from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as BaseNodeType, DisplayOptions, OptionValue,
)
from nodes.alfacrm.action.node.static.icon import ICON
from nodes.alfacrm.action.node.schemas.enums import ActionEnum


class NodeType(flow.NodeType):
    id: str = '60096456-c5cf-4541-a26d-82158e02e39a'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'AlfaCRM module'
    icon: str = ICON
    version: int = 1
    description: str = 'AlfaCRM integrate module'
    defaults: Defaults = Defaults(name='alfacrm-action', color='#00FF00')
    properties: List[Property] = [
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            description='Выберите действие кубика',
            options=[
                OptionValue(
                    name='Авторизация',
                    value=ActionEnum.authorization,
                    description='Авторизация пользователя',
                ),
                OptionValue(
                    name='Customer',
                    value=ActionEnum.customer,
                    description='Customer request',
                ),
            ],
        ),
    ]
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name='alfacrm_api_auth', required=True)
    ]
