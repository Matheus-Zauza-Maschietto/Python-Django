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
    page_range: list,
    qty_pages_before_after: int,
    current_page: int,
):
    if current_page-qty_pages_before_after < 0:
        start_range = 0
        stop_range = start_range+(qty_pages_before_after*2)
    elif current_page+qty_pages_before_after > len(page_range):
        stop_range = len(page_range)
        start_range = len(page_range)-(qty_pages_before_after*2)
    else:
        start_range = current_page - qty_pages_before_after
        stop_range = current_page + qty_pages_before_after

    return list(range(start_range, stop_range))


print(make_pagination_range_my_func(list(range(1, 21)), 2, 21))
