from dependency_injector import containers, providers

from client.NotionBlockProvider import NotionBlockProvider
from client.NotionDatabaseProvider import NotionDatabaseProvider
from client.NotionPageProvider import NotionPageProvider
from client.requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from client.requests.utils.NotionHeaderProvider import NotionHeaderProvider
from client.requests.utils.RequestsClient import RequestsClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    header_provider: NotionHeaderProvider = providers.Singleton(
        NotionHeaderProvider,
        config.api_key
    )

    requests_client: RequestsClient = providers.Singleton(
        RequestsClient,
        header=providers.Callable(
            lambda notion_header_provider: notion_header_provider.create_header(),
            header_provider)
    )

    notion_api_blocks_client: NotionAPIBlocksClient = providers.Singleton(
        NotionAPIBlocksClient,
        requests_provider=requests_client
    )

    notion_api_pages_client: NotionAPIPagesClient = providers.Singleton(
        NotionAPIPagesClient,
        requests_provider=requests_client
    )

    notion_api_databases_client: NotionAPIDatabasesClient = providers.Singleton(
        NotionAPIDatabasesClient,
        requests_provider=requests_client
    )

    notion_block_provider: NotionBlockProvider = providers.Singleton(
        NotionBlockProvider,
        notion_client=notion_api_blocks_client
    )

    notion_page_provider: NotionPageProvider = providers.Singleton(
        NotionPageProvider,
        notion_client=notion_api_pages_client
    )

    notion_database_provider: NotionDatabaseProvider = providers.Singleton(
        NotionDatabaseProvider,
        notion_client=notion_api_databases_client
    )
