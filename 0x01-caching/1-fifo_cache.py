#!/usr/bin/env python3
"""
FIFO Cache Module
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the given key.

        If the cache exceeds the maximum size, the first item is discarded.

        Args:
            key (str): The key of the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key)
