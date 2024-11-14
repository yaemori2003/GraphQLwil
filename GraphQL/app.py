
from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
import uvicorn
from resolvers import resolve_getProduct, resolve_getAllProducts

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()

# Asignar los resolvers a sus respectivos campos
query.set_field("getProduct", resolve_getProduct)
query.set_field("getAllProducts", resolve_getAllProducts)

# Crear el esquema ejecutable
schema = make_executable_schema(type_defs, query)

app = GraphQL(schema)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

