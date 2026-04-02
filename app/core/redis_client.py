import redis

redis_client = redis.Redis(host='127.0.0.1',
                     port=6379,
                     decode_responses=True,
                     socket_connect_timeout=5
                     )

def get_redis_client() -> redis.Redis:
    return redis_client