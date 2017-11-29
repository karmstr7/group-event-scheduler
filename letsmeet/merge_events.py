import copy


def merge_main(master_schedule, new_schedule):
    """
    Merge a new schedule with the main schedule found in the database.
    :param master_schedule: [{"": [[],[],...]},...]
    :param new_schedule: [{"": [[],[],...]},...]
    :return: master_schedule
    """
    nm = copy.deepcopy(master_schedule)
    for i in range(len(nm)):
        for key, value in nm[i].items():
            for j in range(len(value)):
                if new_schedule[i][key][j][1]:
                    value[j][1] = True
    return nm
