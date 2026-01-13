"""Raw Shopify GraphQL queries."""

SHOP_INFO_QUERY = """
query ShopInfo {
  shop {
    name
    primaryDomain {
      url
    }
  }
}
"""
