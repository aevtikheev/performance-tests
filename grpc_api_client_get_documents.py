from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client

# Создаём gRPC API-клиенты
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
documents_gateway_client = build_documents_gateway_grpc_client()

# Создаём пользователя с помощью клиентского метода create_user
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

# Получаем пользователя по ID, используя метод get_user
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)

# Открываем кредитный счёт для только что созданного пользователя
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    get_user_response.user.id
)
print('Open credit card account data:', open_credit_card_account_response)

# Получение тарифного документа
get_tariff_document_response = documents_gateway_client.get_tariff_document(
    open_credit_card_account_response.account.id
)
print('Get tariff document response:', open_credit_card_account_response)

# Получение контракта
get_contract_document_response = documents_gateway_client.get_contract_document(
    open_credit_card_account_response.account.id
)
print('Get contract document response:', get_contract_document_response)
