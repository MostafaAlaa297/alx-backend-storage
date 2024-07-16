#!/usr/bin/env python3
"""
======
logsDB
======
"""
from pymongo import MongoClient


def log_stats(nginx):
	"""return log stats"""

	logs_count = nginx.count_documents({})
	get_count = nginx.count_documents({"method": "GET"})
	post_count = nginx.count_documents({"method": "POST"})
	put_count = nginx.count_documents({"method": "PUT"})
	patch_count = nginx.count_documents({"method": "PATCH"})
	delete_count = nginx.count_documents({"method": "DELETE"})
	status_check_count = nginx.count_documents({"method": "GET", "path": "/status"})

	print("{} logs".format(logs_count))
	print("Methods:")
	print("\tmethod GET: {}".format(get_count))
	print("\tmethod POST: {}".format(post_count))
	print("\tmethod PUT: {}".format(put_count))
	print("\tmethod PATCH: {}".format(patch_count))
	print("\tmethod DELETE: {}".format(delete_count))
	print("{} status check".format(status_check_count))

if __name__ == "__main__":
	client = MongoClient('mongodb://127.0.0.1:27017')
        nginx = client.logs.nginx
	log_stats(nginx)

