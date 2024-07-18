#!/usr/bin/env python3
"""
Redis Python
"""
import redis
import uuid
r = redis.Redis(host='localhost', port=6379, db=0)


class Cache:
	"""Cache class"""
	def __init__(r):
		"""Initialization method"""
		self._redis = r
		r.flushdb()
	def store(data: str | int | bytes | float) -> str:
		"""Method that returns a uuid string"""
		key = str(uuid.uuid4())
		r.set(key, data)
		return key
