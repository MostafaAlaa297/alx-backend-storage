#!/usr/bin/env python3
"""
==============
Pymongo module
==============
"""


def insert_school(mongo_collection, **kwargs):
	"""Return an empty list if no document in the collection"""
	new_doc = mongo_collection.insert({key: value for key, value in kwargs.items()})
	return new_doc.insertd_id
