#!/usr/bin/env python3
"""
LFUCache implementation
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache
    """
    def __init__(self):
        super(LFUCache, self).__init__()
        self.used_key = {}

    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.used_key, key=self.used_key.get)
                self.used_key.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.used_key):
                self.used_key[key] = 0
            else:
                self.used_key[key] += 1

    def get(self, key):
        """
        get case_data item by key
        """
        if key is not None and key in self.cache_data.keys():
            self.used_key[key] += 1
        return self.cache_data.get(key, None)
