#!/usr/bin/env python3
"""
start and end
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    start and end
    """
    start = (page - 1) * page_size
    end = page * page_size
    return(start, end)
