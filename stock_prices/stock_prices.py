#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices) - 1):
    current_min_price_so_far = i
    # max_profit_so_far

    for j in range(current_min_price_so_far, len(prices) - 2):
      max_profit_so_far = j 
      if prices[max_profit_so_far] < prices[current_min_price_so_far]:
        print(f'lowest is {prices[current_min_price_so_far]}, maximum is {prices[current_min_price_so_far]}')

        new_max_profit = max_profit_so_far
        max_profit_so_far = current_min_price_so_far
        print(f'old max profit is {prices[max_profit_so_far]}, new is {prices[new_max_profit]}')
        


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))