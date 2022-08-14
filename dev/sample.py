from __future__ import annotations


def run_query(a, b):
    temp = a + b
    print('value of temp is', temp)
    return temp*temp


def mul_data(b, c):
    return (b * c)


def add_data(a, b):
    return (a + b)


def query_vsim_table(a, b):

    temp = mul_data(a, b)
    temp1 = add_data(a, b)
    print('value of query_vsim_table', temp, temp1)
    return (temp + temp1)

    # if a_count == temp:
    #     print('in the if loop')
    #     return True
    # else:
    #     print('in the else loop')
    #     temp = run_query(a, b)
    #     temp = mul_data(a, b)
    #     return False

