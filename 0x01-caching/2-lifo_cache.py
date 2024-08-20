#!/usr/bin/env python3
"""
LIFOCache implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache"""
    def __init__(self):
        super(LIFOCache, self).__init__()

    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                last_key, value = self.cache_data.popitem()
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get case_data item by key
        """
        return self.cache_data.get(key, None)
