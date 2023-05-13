from redis_om import HashModel
from .database import redis

class Order(HashModel):
    product_id: str
    quantity: int
    price: int
    fee: int
    total: int
    status: str

    class Meta:
        database = redis
