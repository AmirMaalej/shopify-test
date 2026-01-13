"""ASGI entrypoint."""

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.graphql.schema import schema

app = FastAPI(title="Shopify GraphQL Service")
app.include_router(GraphQLRouter(schema), prefix="/graphql")


@app.get("/")
def health_check() -> dict:
    return {"status": "ok"}
