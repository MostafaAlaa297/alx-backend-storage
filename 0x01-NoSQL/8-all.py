#!/usr/bin/env python3
"""
==============
Pymongo module
==============
"""


def list_all(mongo_collection):
	"""Return an empty list if no document in the collection"""
	return [document for document in mongo_collection.find()]
