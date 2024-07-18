#!/usr/bin/env python3
"""
Redis Python
"""
import redis
import uuid
from typing import Union


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
