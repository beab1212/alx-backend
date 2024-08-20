#!/usr/bin/env python3
"""
LFUCache implementation
"""
from base_caching import BaseCaching


#  { 'A': 1, 'B': 1, 'C': 1, 'D': 1 }

# E{ 'E': 1, 'B': 1, 'C': 1, 'D': 1 }
class LFUCache(BaseCaching):
    """LFUCache"""
    def __init__(self):
        super(LFUCache, self).__init__()
        self.used_key = {}

    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                pass




    def get(self, key):
        """
        get case_data item by key
        """
        if key in self.cache_data:
            self.used_key[key] += 1
        return self.cache_data.get(key, None)
