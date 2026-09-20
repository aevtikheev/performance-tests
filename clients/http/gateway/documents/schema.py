from pydantic import BaseModel, HttpUrl


class ContractSchema(BaseModel):
    """
    Описание структуры контракта.
    """
    url: HttpUrl
    document: str


class TariffSchema(BaseModel):
    """
    Описание структуры тарифа.
    """
    url: HttpUrl
    document: str


class GetContractResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта.
    """
    contract: ContractSchema


class GetTariffResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифа.
    """
    tariff: TariffSchema
