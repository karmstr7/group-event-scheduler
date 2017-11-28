import datetime
import copy
import arrow


def get_available_times(events, begin_datetime, end_datetime):
    """
    This acts as the main function for calc_freetime.py
    :param events: A list of events, each as a tuple.
    :param begin_datetime: str
    :param end_datetime: str
    :return: list of available intervals
    """
    block_bounds, time_blocks = create_available_block(begin_datetime, end_datetime)
    calc_available_block(events, block_bounds, time_blocks)
    to_string_blocks(time_blocks)
    return to_string_bounds(block_bounds), time_blocks


def create_available_block(begin_datetime, end_datetime):
    """
    Create a time table for each day.
    :param begin_datetime: str
    :param end_datetime: str
    :return: list, list
    """
    # initialize variables
    block_bounds = []
    time_blocks = []

    # convert string to arrow objects
    d1 = arrow.get(begin_datetime)
    d2 = arrow.get(end_datetime)
    day_delta = (d2 - d1).days + 1

    # convert datetime to time
    t1 = d1.time()
    t2 = d2.time()

    block_bounds.append(t1)
    block_bounds.append(t2)

    temp_date = arrow.get(end_datetime).shift(days=-(day_delta - 1))
    time_table = []

    while d1 <= temp_date:
        time_table.append([d1.time(), False])
        d1 += datetime.timedelta(minutes=15)

    d1 = arrow.get(begin_datetime)
    for i in range(day_delta):
        date = (d1.shift(days=+i).date())
        time_block_dict = {date: copy.deepcopy(time_table)}
        time_blocks.append(time_block_dict)
    return block_bounds, time_blocks


def calc_available_block(events, bounds, blocks):
    """
    Mark each 15 minute as busy/free in the timetable, for each date.
    :param events: A list of events, each is a tuple.
    :param bounds: A list containing times of the starting bound and ending bound.
    :param blocks: An empty list
    :return: void
    """
    for event in events:
        start_date = arrow.get(event[2]['start']['dateTime']).date()
        end_date = arrow.get(event[3]['end']['dateTime']).date()
        start_time = arrow.get(event[2]['start']['dateTime']).time()
        end_time = arrow.get(event[3]['end']['dateTime']).time()
        day_delta = (end_date - start_date).days
        if day_delta == 0:  # same day event.
            if start_time < bounds[0] and end_time <= bounds[0]:  # event begins and ends before block.
                continue
            elif start_time >= bounds[1]:  # event begins after block ends.
                continue
            else:
                if start_time <= bounds[0]:  # event begins at or before beginning of block
                    for d in blocks:
                        if start_date in d:
                            for t in d[start_date]:
                                if t[0] <= end_time:
                                    t[1] = True
                elif end_time >= bounds[1]:  # event ends at or after end of block
                    for d in blocks:
                        if start_date in d:
                            for t in d[start_date]:
                                if t[0] >= start_time:
                                    t[1] = True
                else:  # event is well bounded by block
                    for d in blocks:
                        if start_date in d:
                            for t in d[start_date]:
                                if start_time <= t[0] <= end_time:
                                    t[1] = True
        elif day_delta == 1:  # two day event.
            for i in range(2):
                if i == 0:  # check for first day.
                    if start_time >= bounds[1]:  # If starts after block.
                        continue
                    else:  # Starts before block ends.
                        for d in blocks:
                            if start_date in d:
                                for t in d[start_date]:
                                    if t[0] >= start_time:
                                        t[1] = True
                else:  # check for second day.
                    if end_time <= bounds[0]:  # Ends before second day's block begins.
                        continue
                    else:  # Ends after second day's blocks begins.
                        for d in blocks:
                            if end_date in d:
                                for t in d[end_date]:
                                    if t[0] <= end_time:
                                        t[1] = True
        else:  # multi-day (more than two) event.
            full_days = []  # days between first and last.
            for i in range(1, day_delta):
                full_days.append(arrow.get(event[2]['start']['dateTime']).shift(days=+i).date())
            for i in range(len(full_days)):  # fill busy for entire block(s) for days between
                for d in blocks:
                    if full_days[i] in d:
                        for t in d[full_days[i]]:
                            t[1] = True
            for i in range(2):  # handle first and last days
                if i == 0:
                    if start_time >= bounds[1]:  # check for first day.
                        continue
                    else:
                        for d in blocks:
                            if start_date in d:
                                for t in d[start_date]:
                                    if t[0] >= start_time:
                                        t[1] = True
                else:
                    if end_time <= bounds[0]:  # check for last day.
                        continue
                    else:
                        for d in blocks:
                            if end_date in d:
                                for t in d[end_date]:
                                    if t[0] <= end_time:
                                        t[1] = True


def to_string_bounds(bounds):
    str_bounds = []
    for bound in bounds:
        nb = bound.strftime('%H:%M')
        str_bounds.append(nb)
    return str_bounds


def to_string_blocks(blocks):
    for d in blocks:
        for key in d:
            nk = key.strftime('%Y-%m-%d')
            d[nk] = d.pop(key)
            break

    for d in blocks:
        for key in d:
            for n in d[key]:
                n[0] = n[0].strftime('%H:%M')
