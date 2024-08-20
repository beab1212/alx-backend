#!/usr/bin/env python3
"""
FIFOCache implementation
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache
    """
    def __init__(self):
        super(FIFOCache, self).__init__()

    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD:", first_key)
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get case_data item by key
        """
        return self.cache_data.get(key, None)
