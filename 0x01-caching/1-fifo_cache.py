#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
            for the key key
            =>If key or item is None, this method should not do anything
            =>If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                =>you must discard the first item put in cache
                (FIFO algorithm)
                =>you must print DISCARD: with the key discarded and
                following by a new line
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """

        return self.cache_data.get(key, None)
