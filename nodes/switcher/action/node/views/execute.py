from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute

from nodes.switcher.action.node.schemas.enums import FirstDropdown, SecondDropdown, Switch


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            data: dict = json.node.data.properties
            result = {}
            match data:
                case {
                    'switch': Switch.enable,
                    'first_field':FirstDropdown.first_value,
                    'second_field':SecondDropdown.first_value,
                    'email': email,
                }:
                    result['switch'] = Switch.enable
                    result['first_field'] =FirstDropdown.first_value
                    result['second_field'] =SecondDropdown.first_value
                    result['email'] = email
                case {
                    'switch': Switch.enable,
                    'first_field':FirstDropdown.second_value,
                    'second_field':SecondDropdown.second_value,
                    'datetime': datetime_value,
                }:
                    result['switch'] = Switch.enable
                    result['first_field'] =FirstDropdown.second_value
                    result['second_field'] =SecondDropdown.second_value
                    result['datetime'] = datetime_value
                case _:
                    ...

            await json.save_result(result)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
