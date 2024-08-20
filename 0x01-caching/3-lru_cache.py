#!/usr/bin/env python3
"""
LRUCache implementation
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache"""
    def __init__(self):
        super(LRUCache, self).__init__()
        self.used_key = []

    def put(self, key, item):
        """
        add new dict to the case_date
        new keys added to the end of used_key
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                print("DISCARD:", self.used_key[0])
                self.cache_data.pop(self.used_key[0])
                self.used_key.pop(0)
                self.used_key.append(key)
            else:
                if key in self.cache_data:
                    self.used_key.remove(key)
                self.used_key.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get case_data item by key
        used key move to the end of the used_key
        """
        if key in self.cache_data:
            self.used_key.remove(key)
            self.used_key.append(key)

        return self.cache_data.get(key, None)
