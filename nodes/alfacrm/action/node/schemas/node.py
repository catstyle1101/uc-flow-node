
from typing import Union
from uc_flow_nodes.schemas import NodeRunContext as BaseNodeRunContext
from uc_flow_schemas.flow import Node as BaseNode

from nodes.alfacrm.action.node.provider.alfacrm import Authenticate, CreateCustomer, GetCustomers



class NodeRunContext(BaseNodeRunContext):
    class Node(BaseNode):
        class Data(BaseNode.Data):
            properties: Union[
                Authenticate,
                GetCustomers,
                CreateCustomer,
            ]
        data: Data

    node: Node
