from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """Описание структуры операции."""

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """Описание структуры чека по операции."""

    url: HttpUrl
    document: str


class OperationSummarySchema(BaseModel):
    """Описание структуры сводки операций."""

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """Описание структуры ответа получения операции."""

    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """Описание структуры ответа получения чека по операции."""

    receipt: OperationReceiptSchema


class MakeFeeOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции списания комиссии."""

    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """Описание структуры ответа получения списка операций."""

    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """Описание структуры ответа получения сводки операций."""

    summary: OperationSummarySchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции пополнения."""

    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции начисления кешбэка."""

    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции перевода."""

    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции покупки."""

    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции оплаты счёта."""

    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции снятия наличных."""

    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """Структура параметров для получения списка операций по счёту."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """Структура параметров для получения сводки операций по счёту."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseModel):
    """Структура данных для создания операции списания комиссии."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationRequestSchema(BaseModel):
    """Структура данных для создания операции пополнения."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationRequestSchema(BaseModel):
    """Структура данных для создания операции начисления кешбэка."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationRequestSchema(BaseModel):
    """Структура данных для создания операции перевода."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(BaseModel):
    """Структура данных для создания операции покупки."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """Структура данных для создания операции оплаты счёта."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """Структура данных для создания операции снятия наличных."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
