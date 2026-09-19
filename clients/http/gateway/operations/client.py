from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient


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
