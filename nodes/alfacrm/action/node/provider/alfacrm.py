from json import JSONDecodeError
from typing import Literal, List, Optional
from urllib.parse import urljoin

from pydantic import BaseModel, AnyHttpUrl, parse_obj_as
from uc_http_requester.requester import Request, Response

from nodes.alfacrm.action.node.schemas.enums import (
    ActionEnum,
    Api,
    AUTH_HEADER,
    Parameters,
    RequestEnum,
    RequestTypeEnum,
    URL_API_GENERAL,
)
from nodes.alfacrm.action.node.schemas.models import (
    BalanceContractFrom,
    BranchIds,
    ClientIdItem,
    DateFrom,
    IsStudy,
    LegalType,
    Name,
)


class Config:
    arbitrary_types_allowed = True


class BaseParameters(BaseModel):
    ...


class Action(BaseModel):
    action: Optional[str]
    resource: Optional[str]
    operation: Optional[str]

    @staticmethod
    def validate_response(response: Response) -> [dict, List[dict]]:
        try:
            if response.status_code != 200:
                raise Exception(
                    f"{response.get('status_code') =} {response.get('content') = }")
            if response.content:
                content = response.json()
                if content.get('errors'):
                    raise Exception(f'content errors: {content = }')
            else:
                content = dict()
        except JSONDecodeError:
            raise Exception(JSONDecodeError)
        return content

    @staticmethod
    def get_attr(params, attr):
        obj = params.__getattribute__(attr)
        return obj[0].__getattribute__(attr) if obj else None

    @staticmethod
    def params_delete_none_object(params) -> dict:
        res: dict = {}
        for key, value in params.items():
            res.update({key: value}) if value is not None else ...

        return res
    def get_request_url(
            self, base_url: str, api_endpoint: str, branch_id: str | None = None) -> str:
        api_url: str = URL_API_GENERAL
        url = urljoin(base_url, api_url)
        if branch_id:
            url = urljoin(url, f'{branch_id}/')
        url = urljoin(url, api_endpoint)
        return url

    def get_request_params(self) -> dict:
        return dict()

    def get_headers(self) -> dict:
        if hasattr(self, 'auth_data'):
            return {AUTH_HEADER: self.auth_data['token']}
        return dict()

    def process_content(self, response: dict) -> [dict, List[dict]]:
        return response

    def get_request(self, base_url: str, auth_key: str, branch_id: int) -> Request:
        return Request(
            url=parse_obj_as(AnyHttpUrl, self.get_request_url(base_url)),
            method=Request.Method.post,
            data={
                **self.get_request_params()
            },
            headers={
                AUTH_HEADER: auth_key,
            },
        )


class Authenticate(Action):
    action: Literal[ActionEnum.authorization]
    hostname: str
    branch_id: int
    email: str
    api_key: str

    def get_request(self) -> Request:
        url = self.get_request_url(self.hostname, Api.login)
        return Request(
            url=url,
            method=Request.Method.post,
            json={
                'email': self.email,
                'api_key': self.api_key,
            }
        )

    def process_content(self, response: dict) -> [dict, List[dict]]:
        response.update(
            {
                'branch_id': self.branch_id,
                'hostname': self.hostname,
            }
        )
        return response

    def validate_response(self, response: Response) -> [dict, List[dict]]:
        result = Action.validate_response(response)
        result.update(
            {
                'branch_id': self.branch_id,
                'hostname': self.hostname,
            }
        )
        return result

class GetCustomers(Action):
    class Parameters(BaseParameters):
        id: Optional[List[ClientIdItem]]
        is_study: Optional[List[IsStudy]]
        name: Optional[List[Name]]
        date_from: Optional[List[DateFrom]]
        balance_contract_from: Optional[List[BalanceContractFrom]]

    action: Literal[ActionEnum.request]
    resource: Literal[RequestEnum.customer]
    operation: Literal[RequestTypeEnum.index_]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            params['id'] = self.get_attr(f, Parameters.id)
            is_study = self.get_attr(f, Parameters.is_study)
            params['is_study'] = None if not is_study else int(is_study)
            params['name'] = self.get_attr(f, Parameters.name)
            params['date_from'] = self.get_attr(f, Parameters.date_from)
            params['balance_contract_from'] = self.get_attr(f, Parameters.balance_contract_from)
        params = self.params_delete_none_object(params)
        return params

    def get_request(self) -> Request:
        auth_data = self.auth_data
        url = self.get_request_url(
            auth_data['hostname'], Api.get_customer, branch_id=auth_data['branch_id'])
        headers = self.get_headers()
        return Request(
            url=url,
            method=Request.Method.post,
            headers=headers,
            json=self.get_request_params()
        )


class CreateCustomer(Action):
    class Parameters(BaseParameters):
        id: Optional[List[ClientIdItem]]
        is_study: Optional[List[IsStudy]]
        name: Optional[List[Name]]
        branch_ids: Optional[List[BranchIds]]
        legal_type: Optional[List[LegalType]]

    action: Literal[ActionEnum.request]
    resource: Literal[RequestEnum.customer]
    operation: Literal[RequestTypeEnum.create]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            is_study = self.get_attr(f, Parameters.is_study)
            params['is_study'] = None if not is_study else int(is_study)
            params['name'] = self.get_attr(f, Parameters.name)
            params['branch_ids'] = self.get_attr(f, Parameters.branch_ids)
            params['legal_type'] = int(self.get_attr(f, Parameters.legal_type))
        params = self.params_delete_none_object(params)
        return params

    def get_request(self) -> Request:
        auth_data = self.auth_data
        url = self.get_request_url(
            auth_data['hostname'], Api.create_customer, branch_id=auth_data['branch_id'])
        headers = self.get_headers()
        return Request(
            url=url,
            method=Request.Method.post,
            headers=headers,
            json=self.get_request_params(),
        )


class UpdateCustomer(Action):
    class Parameters(BaseParameters):
        id: Optional[List[ClientIdItem]]
        name: Optional[List[Name]]

    action: Literal[ActionEnum.request]
    resource: Literal[RequestEnum.customer]
    operation: Literal[RequestTypeEnum.update]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            params['id'] = self.get_attr(f, Parameters.id)
            params['name'] = self.get_attr(f, Parameters.name)
        params = self.params_delete_none_object(params)
        return params

    def get_request(self) -> Request:
        auth_data = self.auth_data
        url = self.get_request_url(
            auth_data['hostname'], Api.update_customer, branch_id=auth_data['branch_id'])
        headers = self.get_headers()
        params = self.get_request_params()
        query_params = {'id': params.pop('id')}
        return Request(
            url=url,
            method=Request.Method.post,
            headers=headers,
            json=params,
            params=query_params,
        )
