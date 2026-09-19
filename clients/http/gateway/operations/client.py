from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationSummaryDict(TypedDict):
    """
    Описание структуры сводки операций.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения чека по операции.
    """
    receipt: OperationReceiptDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции списания комиссии.
    """
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения сводки операций.
    """
    summary: OperationSummaryDict


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции начисления кешбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции оплаты счёта.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    operation: OperationDict


class GetOperationsQueryDict(TypedDict):
    """
    Структура параметров для получения списка операций по счёту.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура параметров для получения сводки операций по счёту.
    """
    accountId: str


class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции списания комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции начисления кешбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты счёта.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получить список операций по счёту.

        :param query: Словарь с идентификатором счёта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(
        self,
        query: GetOperationsSummaryQueryDict,
    ) -> Response:
        """
        Получить сводку операций по счёту.

        :param query: Словарь с идентификатором счёта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            "/api/v1/operations/operations-summary",
            params=QueryParams(**query),
        )

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить операцию по идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/operation-receipt/{operation_id}",
        )

    def make_fee_operation_api(
        self,
        request: MakeFeeOperationRequestDict,
    ) -> Response:
        """
        Создать операцию списания комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(
        self,
        request: MakeTopUpOperationRequestDict,
    ) -> Response:
        """
        Создать операцию пополнения.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request,
        )

    def make_cashback_operation_api(
        self,
        request: MakeCashbackOperationRequestDict,
    ) -> Response:
        """
        Создать операцию начисления кешбэка.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cashback-operation",
            json=request,
        )

    def make_transfer_operation_api(
        self,
        request: MakeTransferOperationRequestDict,
    ) -> Response:
        """
        Создать операцию перевода.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-transfer-operation",
            json=request,
        )

    def make_purchase_operation_api(
        self,
        request: MakePurchaseOperationRequestDict,
    ) -> Response:
        """
        Создать операцию покупки.

        :param request: Словарь с данными операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-purchase-operation",
            json=request,
        )

    def make_bill_payment_operation_api(
        self,
        request: MakeBillPaymentOperationRequestDict,
    ) -> Response:
        """
        Создать операцию оплаты счёта.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-bill-payment-operation",
            json=request,
        )

    def make_cash_withdrawal_operation_api(
        self,
        request: MakeCashWithdrawalOperationRequestDict,
    ) -> Response:
        """
        Создать операцию снятия наличных.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation",
            json=request,
        )

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить операцию по идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Json ответа от сервера (объект GetOperationResponseDict).
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(
        self,
        operation_id: str,
    ) -> GetOperationReceiptResponseDict:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Json ответа от сервера (объект GetOperationReceiptResponseDict).
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счёту.

        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект GetOperationsResponseDict).
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(
        self,
        account_id: str,
    ) -> GetOperationsSummaryResponseDict:
        """
        Получить сводку операций по счёту.

        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект GetOperationsSummaryResponseDict).
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeFeeOperationResponseDict:
        """
        Создать операцию списания комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeFeeOperationResponseDict).
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeTopUpOperationResponseDict).
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashbackOperationResponseDict:
        """
        Создать операцию начисления кешбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeCashbackOperationResponseDict).
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTransferOperationResponseDict:
        """
        Создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeTransferOperationResponseDict).
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakePurchaseOperationResponseDict:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakePurchaseOperationResponseDict).
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="taxi",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeBillPaymentOperationResponseDict:
        """
        Создать операцию оплаты счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeBillPaymentOperationResponseDict).
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создать операцию снятия наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Json ответа от сервера (объект MakeCashWithdrawalOperationResponseDict).
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
