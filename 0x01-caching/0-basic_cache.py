#!/usr/bin/python3
"""
put and get
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache module
    """

    def put(self, key, item):
        """
        put func
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get func
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
