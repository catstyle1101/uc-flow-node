from datetime import datetime

from pydantic import BaseModel


class ClientIdItem(BaseModel):
    id: int


class IsStudy(BaseModel):
    is_study: int


class Name(BaseModel):
    name: str


class DateFrom(BaseModel):
    date_from: datetime


class BalanceContractFrom(BaseModel):
    balance_contract_from: float


class HostName(BaseModel):
    hostname: str


class BranchId(BaseModel):
    branch_id: str


class Email(BaseModel):
    email: str


class ApiKey(BaseModel):
    api_key: str
