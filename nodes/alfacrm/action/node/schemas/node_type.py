from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as BaseNodeType, DisplayOptions, OptionValue,
)
from nodes.alfacrm.action.node.static.icon import ICON
from nodes.alfacrm.action.node.schemas.enums import ActionEnum, RequestEnum, RequestTypeEnum, Parameters


class NodeType(flow.NodeType):
    id: str = '202390d8-d663-4f5b-89e4-ba1c13d5c173'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'AlfaCRM module'
    icon: str = ICON
    version: int = 1
    description: str = 'AlfaCRM integrate module'
    defaults: Defaults = Defaults(name='alfacrm-action', color='#00FF00')
    properties: List[Property] = [
        Property(
            displayName='Action',
            name='action',
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
                    name='Request',
                    value=ActionEnum.request,
                    description='Customer request',
                ),
            ],
        ),
        Property(
            displayName='Hostname',
            name='hostname',
            type=Property.Type.STRING,
            description='Введите адрес вашей CRM',
            noDataExpression=True,
            placeholder='https://example.com',
            default='https://uiscom.s20.online',
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Branch ID',
            name='branch_id',
            type=Property.Type.NUMBER,
            description='Введите ID филиала',
            default=1,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='E-mail',
            name='email',
            type=Property.Type.EMAIL,
            description='Введите email для авторизации',
            noDataExpression=True,
            placeholder='mail@mail.ru',
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='API key (v2api)',
            name='api_key',
            type=Property.Type.STRING,
            description='Введите ваш API ключ (v2api)',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Auth data',
            name='auth_data',
            type=Property.Type.STRING,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                },
            ),
        ),
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            description='Выберите модель для работы',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Customer',
                    value=RequestEnum.customer,
                    description='Пользователь',
                ),

            ],
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            description='Выберите операцию для работы',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                    'resource': [
                        RequestEnum.customer,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Index',
                    value=RequestTypeEnum.index_,
                    description='Получение сущностей',
                ),
                OptionValue(
                    name='Create',
                    value=RequestTypeEnum.create,
                    description='Создание сущностей',
                ),
                OptionValue(
                    name='Update',
                    value=RequestTypeEnum.update,
                    description='Изменение сущностей',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                    'resource': [
                        RequestEnum.customer,
                    ],
                    'operation': [
                        RequestTypeEnum.index_,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='ID клиента',
                    name=Parameters.id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=1,
                            name=Parameters.id,
                        ),
                    ],
                ),
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.is_study,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='234а 34а234 3а 4а',
                            name=Parameters.name,
                        ),
                    ],
                ),
                Property(
                    displayName='date_from',
                    name=Parameters.date_from,
                    description='дата добавления от, date',
                    values=[
                        Property(
                            type=Property.Type.DATETIME,
                            name=Parameters.date_from,
                        ),
                    ],
                ),
                Property(
                    displayName='balance_contract_from',
                    name=Parameters.balance_contract_from,
                    description='баланс договора от',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=0.0,
                            name=Parameters.balance_contract_from,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                    'resource': [
                        RequestEnum.customer,
                    ],
                    'operation': [
                        RequestTypeEnum.create,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.is_study,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='Ivan Ivanov',
                            name=Parameters.name,
                        ),
                    ],
                ),
                Property(
                    displayName='branch_ids',
                    name=Parameters.branch_ids,
                    description='массив идентификаторов филиалов (Branch)',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=Parameters.branch_ids,
                        ),
                    ],
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.legal_type,
                    description='тип клиента (1 - физ. лицо, 2 - юр. лицо)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.legal_type,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        ActionEnum.request,
                    ],
                    'resource': [
                        RequestEnum.customer,
                    ],
                    'operation': [
                        RequestTypeEnum.update,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='ID клиента',
                    name=Parameters.id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=13,
                            name=Parameters.id,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='New User Name',
                            name=Parameters.name,
                        ),
                    ],
                ),
            ],
        ),
    ]
