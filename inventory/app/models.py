from redis_om import HashModel
from .database import redis

class Product(HashModel):
    name: str
    price: int
    quantity: int

    class Meta:
        database = redis
