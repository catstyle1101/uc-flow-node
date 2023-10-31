from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)

from nodes.alfacrm.action.node.static.icon import ICON


class CredentialType(flow.CredentialType):
    id: str = 'alfacrm_api_auth'
    is_public: bool = True
    displayName: str = 'AlfaCRM API Auth'
    protocol: CredentialProtocol = CredentialProtocol.ApiKey
    protected_properties: List[Property] = []
    properties: List[Property] = [
        Property(
            displayName='Office ID',
            name='office_id',
            type=Property.Type.NUMBER,
            default='',
            description='Введите ID филиала',
        ),
        Property(
            displayName='URL',
            name='base_url',
            type=Property.Type.STRING,
            default='',
            placeholder='http://example.com',
            description='Введите URL сервера',
        ),
        Property(
            displayName='API key',
            name='auth.token',
            type=Property.Type.STRING,
            default='',
            description='Введите ваш API ключ',
        ),
    ]
    extends: Optional[List[str]] = []
    icon: Optional[str] = ICON
