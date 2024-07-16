#!/usr/bin/env python3
"""
==============
Pymongo module
==============
"""


def schools_by_topic(mongo_collection, topic):
	"""changes all topics of a school document based on the name"""
	return [doc for doc in mongo_collection.find_many({ "topic": topic })]
