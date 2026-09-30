from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import (
    build_gateway_grpc_client,
    build_gateway_locust_grpc_client
)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse,
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse,
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse,
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse,
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет методы для получения и создания операций.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """Низкоуровневый вызов GetOperation через gRPC."""
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(
        self, request: GetOperationReceiptRequest,
    ) -> GetOperationReceiptResponse:
        """Низкоуровневый вызов GetOperationReceipt через gRPC."""
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """Низкоуровневый вызов GetOperations через gRPC."""
        return self.stub.GetOperations(request)

    def get_operations_summary_api(
        self, request: GetOperationsSummaryRequest,
    ) -> GetOperationsSummaryResponse:
        """Низкоуровневый вызов GetOperationsSummary через gRPC."""
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(
        self, request: MakeFeeOperationRequest,
    ) -> MakeFeeOperationResponse:
        """Низкоуровневый вызов MakeFeeOperation через gRPC."""
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequest,
    ) -> MakeTopUpOperationResponse:
        """Низкоуровневый вызов MakeTopUpOperation через gRPC."""
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequest,
    ) -> MakeCashbackOperationResponse:
        """Низкоуровневый вызов MakeCashbackOperation через gRPC."""
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequest,
    ) -> MakeTransferOperationResponse:
        """Низкоуровневый вызов MakeTransferOperation через gRPC."""
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequest,
    ) -> MakePurchaseOperationResponse:
        """Низкоуровневый вызов MakePurchaseOperation через gRPC."""
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequest,
    ) -> MakeBillPaymentOperationResponse:
        """Низкоуровневый вызов MakeBillPaymentOperation через gRPC."""
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequest,
    ) -> MakeCashWithdrawalOperationResponse:
        """Низкоуровневый вызов MakeCashWithdrawalOperation через gRPC."""
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """Получение информации об операции по её идентификатору."""
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """Получение чека по идентификатору операции."""
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """Получение списка операций по идентификатору счёта."""
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """Получение статистики операций по идентификатору счёта."""
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(
        self, card_id: str, account_id: str,
    ) -> MakeFeeOperationResponse:
        """Создание операции комиссии с фейковой суммой и статусом."""
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(
        self, card_id: str, account_id: str,
    ) -> MakeTopUpOperationResponse:
        """Создание операции пополнения с фейковой суммой и статусом."""
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(
        self, card_id: str, account_id: str,
    ) -> MakeCashbackOperationResponse:
        """Создание операции кэшбэка с фейковой суммой и статусом."""
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(
        self, card_id: str, account_id: str,
    ) -> MakeTransferOperationResponse:
        """Создание операции перевода с фейковой суммой и статусом."""
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(
        self, card_id: str, account_id: str,
    ) -> MakePurchaseOperationResponse:
        """Создание операции покупки с фейковой суммой, категорией и статусом."""
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            category=fake.category(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(
        self, card_id: str, account_id: str,
    ) -> MakeBillPaymentOperationResponse:
        """Создание операции оплаты счёта с фейковой суммой и статусом."""
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str,
    ) -> MakeCashWithdrawalOperationResponse:
        """Создание операции снятия наличных с фейковой суммой и статусом."""
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_operations_locust_grpc_client(environment: Environment) -> OperationsGatewayGRPCClient:
    """
    Функция создаёт экземпляр OperationsGatewayGRPCClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayGRPCClient с хуками сбора метрик.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
