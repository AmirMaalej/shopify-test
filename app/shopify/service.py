"""Business logic wrapper for Shopify operations."""

from app.shopify.client import ShopifyGraphQLClient
from app.shopify.queries import SHOP_INFO_QUERY


class ShopifyService:
    def __init__(self, client: ShopifyGraphQLClient) -> None:
        self.client = client

    def get_shop_info(self) -> dict:
        return self.client.execute(SHOP_INFO_QUERY)
