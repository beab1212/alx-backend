#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache algorithm
    """
    def put(self, key, item):
        """
        add new dict to the case_date
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get case_data item by key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
