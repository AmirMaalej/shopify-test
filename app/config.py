"""Application configuration."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    shopify_api_key: str
    shopify_api_secret: str
    shopify_access_token: str
    shopify_shop_name: str
    shopify_api_version: str

    @property
    def shopify_graphql_endpoint(self) -> str:
        return (
            f"https://{self.shopify_shop_name}.myshopify.com/"
            f"admin/api/{self.shopify_api_version}/graphql.json"
        )


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_settings() -> Settings:
    return Settings(
        shopify_api_key=_get_env("SHOPIFY_API_KEY"),
        shopify_api_secret=_get_env("SHOPIFY_API_SECRET"),
        shopify_access_token=_get_env("SHOPIFY_ACCESS_TOKEN"),
        shopify_shop_name=_get_env("SHOPIFY_SHOP_NAME"),
        shopify_api_version=os.getenv("SHOPIFY_API_VERSION", "2024-10"),
    )
