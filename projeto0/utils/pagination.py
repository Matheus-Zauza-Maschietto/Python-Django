'''def make_pagination_range(
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

    return {'page-range': list(range(start_range:stop_range))}'''

import math


def make_pagination_range(
    page_range,
    qty_pages,
    current_page,
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]
    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }
