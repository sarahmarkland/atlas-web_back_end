#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes in pagination parameters and returns a tuple containing
    two values: a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize instance"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """getter function"""
        return self.__dataset

    def get_dataset(self) -> List[List]:
        """get dataset"""
        if not self.__dataset:
            with open(self.DATA_FILE, "r") as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
            return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1 and
        page_size with default value 10"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        self.get_dataset()
        if self.__dataset is None:
            return []
        idx_range = index_range(page, page_size)
        return self.__dataset[idx_range[0]:idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dictionary containing the following key-value pairs"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
