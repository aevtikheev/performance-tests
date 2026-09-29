from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client

# Создаём gRPC API-клиенты
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()

# Создаём пользователя с помощью клиентского метода create_user
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

# Получаем пользователя по ID, используя метод get_user
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)

# Открываем дебитовый счёт для только что созданного пользователя
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    get_user_response.user.id
)
print('Open debit card account data:', open_debit_card_account_response)

# Создаём операцию пополнения счета
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id
)
print('Make top up operation response:', make_top_up_operation_response)
