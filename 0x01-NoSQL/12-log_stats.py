#!/usr/bin/env python3
"""
======
logsDB
======
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx

logs_count = nginx.count_documents()
get_count = nginx.count_documents({ "method": "GET" })
post_count = nginx.count_documents({ "method": "POST" })
put_count = nginx.count_documents({ "method": "PUT" })
patch_count = nginx.count_documents({ "method": "PATCH" })
delete_count = nginx.count_documents({ "method": "DELETE" })
path = nginx.count_documents({ "method": "GET" }, { "path": "/status" })

print("{} logs".format(logs_count))
print("Methods:")
print("\t method GET: {}".format(get_count))
print("\t method POST: {}".format(post_count))
print("\t method PUT: {}".format(put_count))
print("\t method PATCH: {}".format(patch_count))
print("\t method DELETE: {}".format(delete_count))

print("{} status check".format(path))
