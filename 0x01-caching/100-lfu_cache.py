#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class
"""
from threading import RLock
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        super().__init__()
        self.current_stats = {}
        self.rlock = RLock()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for
        the key key.
            =>If key or item is None, this method should not do anything.
            =>If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:

                =>you must discard the least frequency used item
                (LFU algorithm)
                =>if you find more than 1 item to discard, you must use
                the LRU algorithm to discard only the least recently used
                =>you must print DISCARD: with the key discarded and
                following by a new line
        """
        if key is not None and item is not None:
            delete_key = self.remove(key)
            with self.rlock:
                self.cache_data.update({key: item})
            if delete_key is not None:
                print('DISCARD: {}'.format(delete_key))

    def get(self, key):
        """
        """
        with self.rlock:
            value = self.cache_data.get(key, None)
            if key in self.current_stats:
                self.current_stats[key] += 1
        return value

    def remove(self, add):
        """
        """
        delete_key = None
        with self.rlock:
            if add not in self.current_stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    delete_key = min(self.current_stats,
                                     key=self.current_stats.get)
                    self.cache_data.pop(delete_key)
                    self.current_stats.pop(delete_key)
            self.current_stats[add] = self.current_stats.get(add, 0) + 1
        return delete_key
