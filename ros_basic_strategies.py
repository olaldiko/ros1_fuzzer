import hypothesis.strategies as st
from collections import namedtuple
from hypothesis.errors import InvalidArgument

STRING_MIN_SIZE = 0
"""int: Minimal string size."""
STRING_MAX_SIZE = 1000
"""int: Maximal string size."""


@st.defines_strategy
def string(min_size=STRING_MIN_SIZE, max_size=STRING_MAX_SIZE):
    if not STRING_MIN_SIZE <= min_size <= max_size <= STRING_MAX_SIZE:
        raise InvalidArgument
    return st.binary(min_size=min_size, max_size=max_size)


@st.composite
def time(draw, secs=st.integers(min_value=0), nsecs=st.integers(min_value=0)):
    _Time = namedtuple('Time', 'secs nsecs')
    secs_value, nsecs_value = draw(secs), draw(nsecs)
    assert isinstance(secs_value, int), 'drew invalid sec={secs_value} from {secs} for integer field'. \
        format(secs_value, secs)
    assert isinstance(nsecs_value, int), 'drew invalid nsec={nsecs_value} from {nsecs} for integer field'. \
        format(nsecs_value, nsecs)
    return _Time(secs_value, nsecs_value)


@st.composite
def duration(draw, secs=st.integers(min_value=0), nsecs=st.integers(min_value=0)):
    _Duration = namedtuple('Duration', 'secs nsecs')
    secs_value, nsecs_value = draw(secs), draw(nsecs)
    assert isinstance(secs_value, int), 'drew invalid sec={secs_value} from {secs} for integer field'. \
        format(secs_value, secs)
    assert isinstance(nsecs_value, int), 'drew invalid nsec={nsecs_value} from {nsecs} for integer field'. \
        format(nsecs_value, nsecs)
    return _Duration(secs_value, nsecs_value)


@st.defines_strategy
def array(elements=None, min_size=None, max_size=None, unique_by=None, unique=None):
    # TODO: Assert that strategy for elements is from supported strategies.
    if not min_size:
        min_size = 0
    return st.lists(elements=elements, min_size=min_size, max_size=max_size, unique_by=unique_by, unique=unique)
