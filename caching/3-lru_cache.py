#!/usr/bin/env python3
''' LRU caching system '''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' LRU caching system '''
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        ''' add item to cache '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
