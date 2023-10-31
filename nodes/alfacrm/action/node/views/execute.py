from urllib.parse import urljoin

from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_http_requester.requester import Request

from nodes.alfacrm.action.node.schemas.enums import (
    ActionEnum, Api, AUTH_HEADER, URL_API_GENERAL, RequestEnum, RequestTypeEnum)



class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        data = json.node.data.properties
        result: dict = {}
        try:
            match data:
                case {
                    'action': ActionEnum.authorization,
                    'hostname': hostname,
                    'branch_id': branch_id,
                    'email': email,
                    'api_key': api_key,
                }:
                    result['branch_id'] = branch_id
                    result['hostname'] = hostname
                    url = urljoin(urljoin(hostname, URL_API_GENERAL), Api.login)
                    request = Request(
                        url=url,
                        method=Request.Method.post,
                        json={'email': email, 'api_key': api_key}
                    )
                    response = await request.execute()
                    result.update(response.json())
                case {
                    'action': ActionEnum.request,
                    'resource':  RequestEnum.customer,
                    'operation': RequestTypeEnum.index,
                    'auth_data': auth_data,
                }:
                    url = urljoin(auth_data['hostname'], URL_API_GENERAL)
                    url = urljoin(urljoin(url, str(auth_data['branch_id'])), Api.customer)
                    payload = {}
                    for param in data['parameters'].values():
                        if len(param) != 0:
                            payload.update(param[0])
                    headers = {AUTH_HEADER: auth_data['token']}
                    request = Request(
                        url=url,
                        method=Request.Method.post,
                        json=payload,
                        headers=headers,
                    )
                    response = await request.execute()
                    result.update(response.json())
                case {
                    'action': ActionEnum.request,
                    'resource': RequestEnum.customer,
                    'operation': RequestTypeEnum.create,
                    'auth_data': auth_data,
                }:
                    pass
                case {
                    'action': ActionEnum.request,
                    'resource': RequestEnum.customer,
                    'operation': RequestTypeEnum.update,
                    'auth_data': auth_data,
                }:
                    pass
            await json.save_result(result)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
