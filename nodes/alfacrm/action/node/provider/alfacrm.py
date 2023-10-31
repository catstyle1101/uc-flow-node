from json import JSONDecodeError
from typing import Literal, List, Optional
from urllib.parse import urljoin

import ujson
from pydantic import BaseModel, AnyHttpUrl, parse_obj_as
from uc_http_requester.requester import Request

from nodes.alfacrm.action.node.schemas.enums import URL_API_GENERAL

class Action(BaseModel):
    path: Optional[str]
    api: Optional[str]
    resource: Optional[str]
    operation: Optional[str]
    method: Optional[str]

    @staticmethod
    def validate_response(response: dict) -> [dict, List[dict]]:
        try:
            if response.get('status_code') != 200:
                raise Exception(f'{response.get("status_code") =} {response.get("content") = }')
            if response.get('content'):
                content = ujson.loads(response.get('content'))
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

    def get_request_url(self, base_url: str) -> str:
        api_url: str = URL_API_GENERAL
        url = urljoin(urljoin(base_url, api_url), self.path)
        return url

    def get_request_params(self) -> dict:
        return dict()

    def process_content(self, response: dict) -> [dict, List[dict]]:
        return response

    def get_request(self, credential_id: str, base_url: str, auth_key: str) -> Request:
        return Request(
            auth=credential_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url(base_url)),
            method=Request.Method.post,
            data={
                'authkey': auth_key,
                **self.get_request_params()
            },
        )
