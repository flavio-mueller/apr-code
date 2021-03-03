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
def get_max_span(change_rates): 

    if len(change_rates) == 0:
        return 0

    max_diff = 0
    current_price = change_rates[-1]
    max_price = change_rates[-1]

    for change_rate in reversed(change_rates):
        current_price -= change_rate

        if current_price > max_price:
            max_price = current_price

        current_diff = max_price - current_price

        if current_diff > max_diff:
            max_diff = current_diff
    
    return max_diff



run_tests(get_best_options_double_for)
run_tests(get_best_options_reversed_for)
run_tests(get_max_span)


measure_times(get_best_options_double_for)
measure_times(get_best_options_reversed_for)
measure_times(get_max_span)
 
