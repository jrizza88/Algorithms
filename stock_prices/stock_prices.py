#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices) - 1):
    current_min_price_so_far = i
    # highest_price = max(prices)
    # print(f'max value = {highest_price}, here is the array {prices}')

    # find_lowest_price = min(prices)

    # print(f'lowest value = {find_lowest_price}')

    # max_profit_so_far

    for j in range(current_min_price_so_far, len(prices)):
      highest_price = max(prices)
      highest_price.remove()
      print(f'max value = {highest_price}, here is the array {prices}')

      find_lowest_price = min(prices)

      print(f'lowest value = {find_lowest_price}')
      #  if prices[max_profit_so_far] < prices[current_min_price_so_far]:
    #     print(f'lowest is {prices[current_min_price_so_far]}, maximum is {prices[max_profit_so_far]}')
    #     # current_min_price_so_far += 1
    #     len(prices).remove(prices[current_min_price_so_far])
    #     print(len(prices).remove(prices[current_min_price_so_far]))
        # new_max_profit = max_profit_so_far
        # max_profit_so_far = current_min_price_so_far
        # print(f'old max profit is {prices[max_profit_so_far]}, new is {prices[new_max_profit]}')
      # elif prices[max_profit_so_far] > prices[current_min_price_so_far]:
      #   prices[current_min_price_so_far].remove()
      #   return max_profit_so_far


  # result = max_profit_so_far - current_min_price_so_far
  # print(f'the result: {result}')
  # return result


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))