# shopify-test

Basic GraphQL service scaffold for interacting with Shopify's API.

## Setup

1. Copy the example env file and fill in values:

```bash
cp .env.example .env
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the service:

```bash
uvicorn app.main:app --reload
```

Then open `http://localhost:8000/graphql` for the GraphQL playground.
