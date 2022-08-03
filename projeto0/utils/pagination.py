def make_pagination_range(
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
