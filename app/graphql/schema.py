"""GraphQL schema definitions."""

import strawberry

from app.graphql.resolvers import resolve_shop_info


@strawberry.type
class Shop:
    name: str
    primary_domain_url: str


@strawberry.type
class Query:
    shop_info: Shop = strawberry.field(resolver=resolve_shop_info)


schema = strawberry.Schema(query=Query)
