from datetime import time
import arrow

# block_bounds = []  # storing only the dates
# time_blocks = []  # storing dates and their time blocks


def get_available_times(events, begin_datetime, end_datetime):
    """
    This acts as the main function for calc_freetime.py
    :param events: A list of events, each as a tuple.
    :param begin_datetime: str
    :param end_datetime: str
    :return: list of available intervals
    """
    block_bounds, time_blocks = create_available_block(begin_datetime, end_datetime)
    print(block_bounds)
    print(time_blocks)
    calc_available_block(events, block_bounds, time_blocks)
    to_string_blocks(time_blocks)
    return to_string_bounds(block_bounds), time_blocks


def create_available_block(begin_datetime, end_datetime):
    """
    Create a global available time block that can be manipulated.
    :param begin_datetime: str
    :param end_datetime: str
    :return: list, list
    """
    block_bounds = []
    time_blocks = []
    d1 = arrow.get(begin_datetime)
    d2 = arrow.get(end_datetime)
    day_delta = (d2 - d1).days + 1  # Block multiplier

    t1 = d1.time()  # Start time
    block_bounds.append(t1)
    t2 = d2.time()  # End time
    block_bounds.append(t2)

    for i in range(day_delta):
        date = (d1.shift(days=+i).date())
        time_block_dict = {date: []}

        time_blocks.append(time_block_dict)
    return block_bounds, time_blocks


def calc_available_block(events, bounds, blocks):
    """
    Manipulate the available blocks.
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
                # print("{event} happens before".format(event=event[1]['summary']))
                continue
            elif start_time >= bounds[1]:  # event begins after after.
                continue
            else:
                # print("{event} happens in between".format(event=event[1]['summary']))
                for d in blocks:
                    if start_date in d:
                        d[start_date].append(event)
        elif day_delta == 1:  # two day event.
            for i in range(2):
                if i == 0:
                    if start_time >= bounds[1]:  # check for first day.
                        continue
                    else:
                        for d in blocks:
                            if start_date in d:
                                d[start_date].append(event)
                else:
                    if end_time <= bounds[0]:  # check for second day.
                        continue
                    else:
                        for d in blocks:
                            if end_date in d:
                                d[end_date].append(event)
        else:  # multi-day (more than two) event.
            full_days = []  # days between first and last.
            for i in range(1, day_delta):
                full_days.append(arrow.get(event[2]['start']['dateTime']).shift(days=+i).date())
            for i in range(len(full_days)):
                for d in blocks:
                    if full_days[i] in d:
                        d[full_days[i]].append(event)
            for i in range(2):
                if i == 0:
                    if start_time >= bounds[1]:  # check for first day.
                        continue
                    else:
                        for d in blocks:
                            if start_date in d:
                                d[start_date].append(event)
                else:
                    if end_time <= bounds[0]:  # check for last day.
                        continue
                    else:
                        for d in blocks:
                            if end_date in d:
                                d[end_date].append(event)


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
