Product Test

### Requirements
- Django
- Django Rest Framework
- Celery
- Redis
- Docker

### Setup
```shell
docker compose build
docker compose up
```

### API Documentation
`https://localhost:8000/api/`

### Dummy Email Server
check `http://localhost:8025/` for email notification from testing

### Implemented APIs
```json
{
    "customers": "http://localhost:8000/api/customers/",
    "products": "http://localhost:8000/api/products/",
    "products_available": "http://localhost:8000/api/products/available/",
    "products_out_of_stock": "http://localhost:8000/api/products/out_of_stock/",
    "products_status_update": "http://localhost:8000/api/products/<pk>/update_status/",
    "orders": "http://localhost:8000/api/orders/"
}
```

### Sample Request
```python
import requests

url = "http://localhost:8000/api/orders/"

payload = {
    "order_number": "12368",
    "items": [
        {
            "sku": "ABCD1234",
            "quantity": 2
        },
        {
            "sku": "EFGH5678",
            "quantity": 1
        }
    ],
    "customer": {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "address": "123 Main St, Anytown USA"
    }
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
```

