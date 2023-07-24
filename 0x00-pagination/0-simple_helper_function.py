#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the index range from a given page and page size.
        Args:
            page (int):
            page_size (int):
        Returns:
            return (Tuple):
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
