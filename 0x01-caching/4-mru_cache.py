#!/usr/bin/env python3
"""
MRUCache implementation
"""
from base_caching import BaseCaching


# ['A', 'B', 'C', 'D']

class MRUCache(BaseCaching):
    """MRUCache implementation"""
    def __init__(self):
        super(MRUCache, self).__init__()
        self.used_key = []

    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                print("DISCARD:", self.used_key[-1])
                self.cache_data.pop(self.used_key[-1])
                self.used_key[-1] = key
            else:
                if key in self.cache_data:
                    self.used_key.remove(key)
                    self.used_key.append(key)
            self.used_key.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get case_data item by key
        """
        if key in self.cache_data:
            self.used_key.remove(key)
            self.used_key.append(key)
        return self.cache_data.get(key, None)
