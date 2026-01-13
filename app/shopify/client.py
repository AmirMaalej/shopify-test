"""Shopify GraphQL client helpers."""

from typing import Any, Dict

import requests

from app.config import Settings


class ShopifyGraphQLClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def execute(self, query: str, variables: Dict[str, Any] | None = None) -> Dict[str, Any]:
        payload = {"query": query, "variables": variables or {}}
        headers = {"X-Shopify-Access-Token": self.settings.shopify_access_token}
        response = requests.post(
            self.settings.shopify_graphql_endpoint,
            json=payload,
            headers=headers,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
