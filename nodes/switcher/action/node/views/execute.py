from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute

from nodes.switcher.action.node.schemas.enums import DropdownWithTwoValues


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            data: dict = json.node.data.properties
            result = {}
            match data:
                case {
                    'switch': True,
                    'first_field': DropdownWithTwoValues.first_value,
                    'second_field': DropdownWithTwoValues.first_value,
                    'email': email,
                }:
                    result['switch'] = True
                    result['first_field'] = DropdownWithTwoValues.first_value
                    result['second_field'] = DropdownWithTwoValues.first_value
                    result['email'] = email
                case {
                    'switch': True,
                    'first_field': DropdownWithTwoValues.second_value,
                    'second_field': DropdownWithTwoValues.second_value,
                    'datetime': datetime_value,
                }:
                    result['switch'] = True
                    result['first_field'] = DropdownWithTwoValues.second_value
                    result['second_field'] = DropdownWithTwoValues.second_value
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
