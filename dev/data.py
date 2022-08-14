from __future__ import annotations

from dev.math import add_num
from dev.math import sub_num


def func(a, b):
    temp = add_num(a, b)
    temp1 = sub_num(a, b)
    print('add_num value should be', temp)
    print('sub_num value should be', temp1)
    return (temp + temp1)
    # return (temp + 2)
