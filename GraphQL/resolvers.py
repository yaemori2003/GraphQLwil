def resolve_getProduct(obj, info, id):
    return products_db.get(id)

def resolve_getAllProducts(obj, info):
    return list(products_db.values())

products_db = {
    "1": {
        "id": "1",
        "name": "Galaxy S24",
        "price": 4000.0,
        "brand": "Samsung",
        "productType": "Smartphone",
    },
    "2": {
        "id": "2",
        "name": "MacBook Pro",
        "price": 12000.0,
        "brand": "Apple",
        "productType": "Laptop",
    },
}