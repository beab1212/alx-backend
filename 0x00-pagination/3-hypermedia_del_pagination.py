#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        """
        current = []
        data = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(data.keys())
        assert index >= 0 and index <= keys[-1]
        [current.append(i)
         for i in keys if i >= index and len(current) <= page_size]
        data = [data[v] for v in current[:-1]]
        next_index = current[-1] if len(current) - page_size == 1 else None
        return {'index': index,
                'data': data,
                'page_size': len(data),
                'next_index': next_index
                }
