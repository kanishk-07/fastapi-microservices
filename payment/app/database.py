from redis_om import get_redis_connection
from .config import settings

redis = get_redis_connection(
    host = settings.PAYMENT_DB_URL,
    port = settings.PAYMENT_DB_PORT,
    password = settings.PAYMENT_DB_PASSWORD,
    decode_responses = True
)