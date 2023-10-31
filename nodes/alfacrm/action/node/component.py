from uc_flow_nodes.service import NodeService

from nodes.alfacrm.action.node.views import info, execute


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = info.InfoView
        Execute = execute.ExecuteView
