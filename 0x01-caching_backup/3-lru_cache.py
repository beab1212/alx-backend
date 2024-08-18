#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        super().__init__()
        self.used_key = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
            for the key key.
            =>If key or item is None, this method should not
            do anything.
            =>If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:

                =>you must discard the least recently used item
                (LRU algorithm)
                =>you must print DISCARD: with the key discarded and
                following by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_key:
                self.used_key.append(key)
            else:
                self.used_key.append(
                    self.used_key.pop(self.used_key.index(key)))
            if len(self.used_key) > BaseCaching.MAX_ITEMS:
                discard = self.used_key.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """
        if key is not None and key in self.cache_data.keys():
            self.used_key.append(self.used_key.pop(self.used_key.index(key)))
        return self.cache_data.get(key, None)
