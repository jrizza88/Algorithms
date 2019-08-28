#!/usr/bin/python

import sys
def eating_cookies(n, cache=None):
  # pass
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  else:
    val = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    print(f'value: {val}')
    return val

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
#   # pass
#   # print(f'printing n: {n}')
#   # if n == 0 or n == 1:
#   #   return 1
#   if n < 0:
#     return 0
#   elif n == 0 or n == 1:
#     return 1
#   else:
#     if cache[n] > 0:
#       # print(f' first if statement...: {cache[n]}')
#       return cache[n]
#     else:
#       val = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
#       # print(f'value: {val}')
#       print(f'cache with n passed to it: {cache[n]}')
#       cache[n] = val
#       return val



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')