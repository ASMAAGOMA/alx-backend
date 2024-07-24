#!/usr/bin/env python3
"""
LIFO Cache Module
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    and implements a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the given key.

        If the cache exceeds the maximum size, the last item inserted is discarded.

        Args:
            key (str): The key of the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key)
