#!/usr/bin/python

import argparse

# need to loop through array
# likely need to have the array have two for loops so that you can compare values
# array j comes after array i, i array will loop from start (index 0) to n - 1 index.
# j array will start from index 1 and loop until the end as well, will list index i in parameter of the loop. 
# edge cases! If only one number in loop, make sure to return price? perhaps no edge case needed here...

## make sure that value doesn't subtract to the right.. 

# def find_max_profit(prices):

#   for i in range(0, len(prices) - 1):
#     current_min_price_so_far = i
#     for j in range(current_min_price_so_far, len(prices)):
     
#       current_max_profit = max(prices)
#       max_profit = current_max_profit

#       # keep_prices_to_left = max_profit(prices[:j])

#       # elim_prices_to_right = max_profit.remove(prices[j:])
#       # max_profit.remove(prices[j:])
#       prices[j:]
#       print(f'the max profit is {max_profit}')


#       # highest_price = max(prices)
#       # highest_price.remove()
#       print(f'max value = {max_profit}, here is the array {prices}')

#       find_lowest_price = min(prices[j])

#       if prices[current_min_price_so_far] < prices[find_lowest_price]:
#         current_min_price_so_far = find_lowest_price
#         print(f'find_lowest_price value {find_lowest_price}')
#         print(f'maxprofit subtracts {max_profit} - find_lowest_price {find_lowest_price}')
#         return max_profit - find_lowest_price

#   return prices

def find_max_profit(prices):
  if len(prices) <= 1:
    return 0
  # set the current max to subtract from current min
  cur_max = prices[1] 
  cur_min = prices[0]
  max_profit = cur_max - cur_min
  for i in range (1, len(prices)):
    if prices[i] > cur_max:
      print(f'current max: {cur_max}')
      print(f'prices[i]: {prices[i]}')
      cur_max = prices[i]
      max_profit = cur_max - cur_min
    elif prices[i] < cur_min:
      print(f'current min: {cur_min}')
      print(f'prices[i]: {prices[i]}')
      cur_min = prices[i]
    # for j in range(start_value, len(prices)):
    #   profit_value = prices[j] - prices[i]
    
    #   print(f'profit value {profit_value}')
    #   # net_return = highest_price - profit_value
    #   # print(f'net return: {net_return}')
    #   if profit_value > highest_price:



    #     print(f'profit value {profit_value}')
    #     return profit_value
  # pass
  return max_profit
# find_max_profit([10, 7, 5, 8, 11, 9])
      
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))