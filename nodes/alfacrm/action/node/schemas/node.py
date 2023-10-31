
from uc_flow_nodes.schemas import NodeRunContext as BaseNodeRunContext
from uc_flow_schemas.flow import Node as BaseNode



class NodeRunContext(BaseNodeRunContext):
    class Node(BaseNode):
        class Data(BaseNode.Data):
            pass
        data: Data

    node: Node
