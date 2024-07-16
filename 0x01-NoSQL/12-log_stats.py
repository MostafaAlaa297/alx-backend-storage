#!/usr/bin/env python3
"""
nginx stats model
"""
from pymongo import MongoClient


def log_stats(nginx_collection):
    """
    get nginx data
    """
    log_count = nginx_collection.count_documents({})
    get_count = nginx_collection.count_documents({"method": "GET"})
    post_count = nginx_collection.count_documents({"method": "POST"})
    put_count = nginx_collection.count_documents({"method": "PUT"})
    patch_count = nginx_collection.count_documents({"method": "PATCH"})
    delete_count = nginx_collection.count_documents({"method": "DELETE"})

    path = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print("{} logs".format(log_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(delete_count))
    print("{} status check".format(path))

if __name__ == "__main__":
    client = MongoClient('localhost',27017)
    nginx_collection = client.logs.nginx

    log_stats(nginx_collection)
