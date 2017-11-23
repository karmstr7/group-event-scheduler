import arrow
from calc_freetime import create_available_block

import nose
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

begin1 = "2017-11-25T13:00:00-08:00"
end1 = "2017-11-28T16:00:00-08:00"

begin2 = arrow.get("2017-11-25T13:00:00-08:00")
end12 = arrow.get("2017-11-28T16:00:00-08:00")

begin3 = "Hello"
end3 = "Bye"

begin4 = []
end4 = []


def test_str_times():
    """
    input are valid string
    """
    i, j = create_available_block(begin1, end1)
    assert str(i) == "[datetime.time(13, 0), datetime.time(16, 0)]"
    assert str(j) == "[{datetime.date(2017, 11, 25): []}, {datetime.date(2017, 11, 26): []}, {datetime.date(2017, 11, 27): []}, {datetime.date(2017, 11, 28): []}]"


def test_arrow_times():
    """
    input are valid arrow objects
    """
    i, j = create_available_block(begin2, end12)
    assert str(i) == "[datetime.time(13, 0), datetime.time(16, 0)]"
    assert str(j) == "[{datetime.date(2017, 11, 25): []}, {datetime.date(2017, 11, 26): []}, {datetime.date(2017, 11, 27): []}, {datetime.date(2017, 11, 28): []}]"


def test_improper_date():
    """
    input are improper strings
    """
    try:
        i, j = create_available_block(begin3, end3)
        assert False
    except:
        assert True


def test_improper_datatype():
    """
    input values are not strings
    """
    try:
        i, j = create_available_block(begin4, end4)
        assert False
    except TypeError:
        assert True
