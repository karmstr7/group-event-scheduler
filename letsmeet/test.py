import arrow


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


b = arrow.get("2017-11-25T13:00:00-08:00")
e = arrow.get("2017-11-28T16:00:00-08:00")

begin3 = "Hello"
end3 = "Bye"

begin4 = []
end4 = []

sample_events = [({'calendar': 'hj5519742@gmail.com'}, {'summary': 'a'},
                  {'start': {'dateTime': '2017-11-25T13:00:00-08:00', 'timeZone': 'America/Los_Angeles'}},
                  {'end': {'dateTime': '2017-11-25T17:00:00-08:00', 'timeZone': 'America/Los_Angeles'}}),
                 ({'calendar': 'hj5519742@gmail.com'}, {'summary': 'b'},
                  {'start': {'dateTime': '2017-11-26T14:00:00-08:00', 'timeZone': 'America/Los_Angeles'}},
                  {'end': {'dateTime': '2017-11-26T17:00:00-08:00', 'timeZone': 'America/Los_Angeles'}}),
                 ({'calendar': 'hj5519742@gmail.com'}, {'summary': 'c'},
                  {'start': {'dateTime': '2017-11-27T15:00:00-08:00', 'timeZone': 'America/Los_Angeles'}},
                  {'end': {'dateTime': '2017-11-27T17:00:00-08:00', 'timeZone': 'America/Los_Angeles'}}),
                 ({'calendar': 'hj5519742@gmail.com'}, {'summary': 'd'},
                  {'start': {'dateTime': '2017-11-28T16:00:00-08:00', 'timeZone': 'America/Los_Angeles'}},
                  {'end': {'dateTime': '2017-11-28T17:00:00-08:00', 'timeZone': 'America/Los_Angeles'}})]

if __name__ == "__main__":
    i, j = create_available_block(begin3, end3)
    print(i, j)
