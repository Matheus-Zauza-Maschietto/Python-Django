import math
from tracemalloc import stop


def make_pagination_range(
    page_range,
    qty_pages,
    current_page,
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    return page_range[start_range:stop_range]


def make_pagination_range_my_func(
    page_range,
    qty_pages,
    current_page,
):

    start_range = current_page - qty_pages if current_page-qty_pages > 0 else 0
    stop_range = current_page + \
        qty_pages if current_page <= page_range[-1] else page_range[-1]
    return page_range[start_range:stop_range]
