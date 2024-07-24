#!/usr/bin/python3
"""
fifo
"""


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
        self.order = []

    def put(self, key, item):
        """
        put func
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = self.order.pop(0)
                print(f"DISCARD: {first}")
                del self.cache_data[first]
            self.cache_data[key] = item

        self.order.append(key)

    def get(self, key):
        """
        get func
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
