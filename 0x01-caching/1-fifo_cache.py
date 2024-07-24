#!/usr/bin/python3
"""
fifo
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    fifo module
    """

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put func
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first}")
            self.cache_data[key] = item

    def get(self, key):
        """
        get func
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
