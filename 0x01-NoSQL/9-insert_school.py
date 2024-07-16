#!/usr/bin/env python3
"""
==============
Pymongo module
==============
"""


def insert_school(mongo_collection, **kwargs):
	"""Return an empty list if no document in the collection"""
	result = mongo_collection.insert_one(kwargs)
	return result.insertd_id
