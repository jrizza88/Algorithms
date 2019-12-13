#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  # cache = {}
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    # print(n)
    return 1
  elif n == 2:
    # print(n)
    return 2
  elif n == 3:
    # print(n)
    return 4
  elif cache and cache[n] > 0:
    return cache[n]
  # if n in cache:
  #   return cache[n]
  else:
    if not cache:
      cache = {
        i:0 
        for i in range(n+1)
      }
      print('testing to see if n returns correctly', n)
      return eating_cookies(n,cache)
    else:
      cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
      print(f'the cache[n] result: {cache[n]}')
      return cache[n]
      # cache[n] = result
      # print(f'the cache[n] result: {cache[n]}')
  return cache[n]
print(eating_cookies(0), 1)
print(eating_cookies(1), 1)
print(eating_cookies(2), 2)
print(eating_cookies(3), 3)
print(eating_cookies(5), 13)
print(eating_cookies(10), 274)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')