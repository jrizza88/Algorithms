#!/usr/bin/python

import argparse

# need to loop through array
# likely need to have the array have two for loops so that you can compare values
# array j comes after array i, i array will loop from start (index 0) to n - 1 index.
# j array will start from index 1 and loop until the end as well, will list index i in parameter of the loop. 
# edge cases! If only one number in loop, make sure to return price? perhaps no edge case needed here...

## make sure that value doesn't subtract to the right.. 
# prices = [10, 7, 5, 8, 11, 9]
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
      print(f'current max: {cur_min}')
      
      print(f'prices[i]: (ELIF) {prices[i]}')
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
  print(f'max profit: {max_profit}')
  return max_profit

print(find_max_profit([10, 7, 5, 8, 11, 9]))
# find_max_profit([10, 7, 5, 8, 11, 9])
      
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))