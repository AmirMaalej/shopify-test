"""GraphQL resolver implementations."""

from app.config import get_settings
from app.graphql.schema import Shop
from app.shopify.client import ShopifyGraphQLClient
from app.shopify.service import ShopifyService


def resolve_shop_info() -> Shop:
    settings = get_settings()
    client = ShopifyGraphQLClient(settings)
    service = ShopifyService(client)
    payload = service.get_shop_info()
    shop = payload["data"]["shop"]
    return Shop(name=shop["name"], primary_domain_url=shop["primaryDomain"]["url"])
