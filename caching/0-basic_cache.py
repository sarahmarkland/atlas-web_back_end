#!/usr/bin/env python3
''' Basic dictionary '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' limitless caching system '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' add item to cache '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
