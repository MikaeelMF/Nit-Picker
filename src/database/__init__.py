import redis

r = redis.Redis(decode_responses=True)

from .redis import set, get
__all__ = ['set', 'get']
