from uc_flow_schemas.flow import RunState
# from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute

from nodes.alfacrm.action.node.schemas.enums import ActionEnum
from nodes.alfacrm.action.node.provider.alfacrm import Action
from nodes.alfacrm.action.node.schemas.node import NodeRunContext


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            credentials = await json.get_credentials()
            credentials_id = credentials.id
            base_url = credentials.data['hostname']
            api_key = credentials.data['api_key']
            email = credentials.data['email']


            path = 'auth/login' # это будет из ресурса браться

            action: Action = Action(**json.node.data.properties, path=path, email=email)
            request = action.get_request(credentials_id, base_url, api_key)
            base_response = await json.requester.request(request)
            response = json.node.data.properties.validate_response(base_response)
            await json.save_result({})
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
