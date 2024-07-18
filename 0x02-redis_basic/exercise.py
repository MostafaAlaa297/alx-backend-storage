#!/usr/bin/env python3
"""
Redis Python
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
	"""Cache class"""
	def __init__(r):
		"""Initialization method"""
		self._redis = redis.Redis(host='localhost', port=6379, db=0)
        	self._redis.flushdb()
	
	def store(self, data: Union[str, bytes, int, float]) -> str:
        	"""Method that stores data in Redis with a random key and returns the key"""
        	key = str(uuid.uuid4())
        	self._redis.set(key, data)
        	return key

	def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
		"""used to convert key data back to the desired format"""
		value = self._redis.get(key)

		if value is None:
			return None
		if fn:
			return fn(value)
		return value

	def get_str(self, key: str) -> Optional[str]:
        	"""Retrieve a string from Redis"""
		return self.get(key, lambda d: d.decode(key))

	def get_str(self, key: str) -> Optional[str]:
                """Retrieve an integer from Redis"""
                return self.get(key, lambda d: int(d))
