import json
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '60096456-c5cf-4541-a26d-82158e02e39a'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'Calculator'
    displayName: str = 'MyFirstNode'
    icon: str = '<svg><text x="8" y="50" font-size="50">😜</text></svg>'
    description: str = 'sum of two fields: text and numeric'
    properties: List[Property] = [
        Property(
            displayName='Текстовое поле',
            name='text_field',
            type=Property.Type.JSON,
            placeholder='Text field placeholder',
            description='Текстовое поле',
            required=True,
            default='0',
        ),
        Property(
            displayName='Числовое поле',
            name='numeric_field',
            type=Property.Type.NUMBER,
            placeholder='Numeric field placeholder',
            description='Числовое поле',
            required=True,
            default=0,
        ),
        Property(
            displayName='Отправить как число?',
            name='switch',
            type=Property.Type.BOOLEAN,
            placeholder='Switch placeholder',
            description='Send response in numeric/text format',
            required=True,
            default=False,
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            data: dict = json.node.data.properties

            text_field_value: str = data.get('text_field', "0")
            numeric_field_value: int | float = data.get('numeric_field', 0)
            send_as_num: bool = data.get('switch', False)

            result_sum = int(text_field_value) + numeric_field_value
            result: str | int = (result_sum if send_as_num else str(result_sum))

            await json.save_result({"result": result})
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
