import numpy as np
from apr_max_sub_seq_test import measure_times, run_tests



# algorithm with double for loop and prices as list
def get_best_options_double_for(change_rates):

    if len(change_rates) == 0:
        return 0

    prices = np.cumsum(change_rates).tolist()
    prices.insert(0, 0)
    diff = 0

    for (i, price_i) in enumerate(prices):
        for j in range(i, len(prices)):
            if prices[j] - price_i > diff:
                diff = prices[j] - price_i

    return diff


# reverse for loop over prices
def get_best_options_reversed_for(change_rates):

    if len(change_rates) == 0:
        return 0

    prices = np.cumsum(change_rates).tolist()
    prices.insert(0, 0)
    diff = 0
    max_price = prices[-1]

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        
        if max_price - price > diff: 
            diff = max_price - price


    return diff
        


# reverse for loop over rates
def get_max_span(changes): 
    max_diff, current_diff = 0, 0
    for change in changes:
        if b > 0:
            b = b + c
        else:
            b = c
        if b > a:
            a = b
    return a


def max_sub_seq_3_py(data):
    max_sum, cur_sum = 0, 0
    for change in data:
        if cur_sum > 0:
            cur_sum = cur_sum + change
        else:
            cur_sum = change
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum



run_tests(get_max_span)
run_tests(max_sub_seq_3_py)



measure_times(get_max_span)
 
measure_times(max_sub_seq_3_py)
