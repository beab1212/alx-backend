#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        super().__init__()
        self.key_freq = {}

    def put(self, key, item):
        """ssign to the dictionary self.cache_data the item value for
            the key key.
            =>If key or item is None, this method should not do anything.
            =>If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                =>you must discard the least frequency used item
                (LFU algorithm)
                =>if you find more than 1 item to discard, you must use the
                LRU algorithm to discard only the least recently used
                =>you must print DISCARD: with the key discarded and
                following by a new line
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.key_freq, key=self.key_freq.get)
                self.key_freq.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.key_freq):
                self.key_freq[key] = 0
            else:
                self.key_freq[key] += 1

    def get(self, key):
        """Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """
        if key is not None and key in self.cache_data.keys():
            self.key_freq[key] += 1
        return self.cache_data.get(key, None)
