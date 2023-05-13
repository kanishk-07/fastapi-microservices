from redis_om import get_redis_connection
from .config import settings

redis = get_redis_connection(
    host = settings.REDIS_DB_URL,
    port = settings.REDIS_DB_PORT,
    password = settings.REDIS_DB_PASSWORD,
    decode_responses = True
)