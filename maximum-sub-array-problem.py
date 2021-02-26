import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create sample and ad prices up
sample_data = [random.randint(-0, 100) for _ in range(100)]
sample_cumsum = np.cumsum(sample_data)



# algorithm with double for loop
def get_Best_Options_double_for(prices):

    span, max_i, min_i = (0,)*3

    for (i, price_i) in enumerate(prices):
        for j in range(i, len(prices)):
            if prices[j] - price_i > span:
                span = prices[j] - price_i
                min_i = i
                max_i = j

    return max_i, min_i



def get_Best_Options_reversed_for(prices):

    prices = prices.tolist()
    span, max_i, min_i = (0,)*3
    max_price = prices[-1]

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        
        if max_price - price > span: 
            span = max_price - price
            min_i = prices.index(price)
            max_i = prices.index(max_price)


    return max_i, min_i
        

#call both algos to test
print(get_Best_Options_double_for(sample_cumsum))
print(get_Best_Options_reversed_for(sample_cumsum))


#plot results

max_i, min_i = get_Best_Options_double_for(sample_cumsum)

plt.plot(sample_cumsum)
plt.scatter(max_i, sample_cumsum[max_i], color="green")
plt.scatter(min_i, sample_cumsum[min_i], color="red")
plt.show()
