#!/usr/bin/python

import sys
# def eating_cookies(n, cache=None):
#   # pass
#   if n < 0:
#     return 0
#   elif n == 0 or n == 1:
#     return 1
#   else:
#     val = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
#     print(f'value: {val}')
#     return val

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  else:
    cache = dict()
    for n in cache:
      return cache[n]
    else:
      cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
      # cache[n] = val
      print(f'{cache[n]}')
      return cache[n]
#     # try:
    #   if cache[n] > 0:
    # # if n in cache:
    #   # print(f' first if statement...: {cache[n]}')
    #     return cache[n]
    # except:
    #   val = eating_cookies(n - 1, cache[n]) + eating_cookies(n - 2, cache[n]) + eating_cookies(n - 3, cache[n])
    #   cache[n] = val
    #   return val



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')