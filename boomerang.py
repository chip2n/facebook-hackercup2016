#!/usr/bin/env python

import itertools
import sys
import math
from collections import Counter

def parse_tuple(s):
  x, y = s.split(' ')
  return int(x), int(y)

def group(ls):
    counter = Counter()
    for l in ls:
        counter[l] += 1
    return list(counter.values())

def boom(count):
    if count < 2:
        return 0
    if count == 2:
        return 1
    return int(math.factorial(count) / (2 * math.factorial(count - 2)))

def boomerang_count(origin, universe):
  """Time complexity: O(|universe|)"""
  distances = [distance(origin, point) for point in universe]

  groups = group(distances)
  groups = [boom(x) for x in groups]

  return sum(groups)

def distance(c1, c2):
  x1, y1 = c1
  x2, y2 = c2
  x = (x2-x1)
  y = (y2-y1)
  return x*x + y*y

def get_input(filename):
  with open(filename) as f:
    lines = [l.strip() for l in f.readlines()]
    groups = itertools.groupby(lines, lambda x: ' ' in x)
    data = [list(y) for x, y in groups if x]
    data = [[parse_tuple(x) for x in d] for d in data]
  return data

def main():
  universes = get_input(sys.argv[1])

  for i, universe in enumerate(universes):
    count = sum([boomerang_count(point, universe) for point in universe])

    print('Case #' + str(i) + ': ' + str(count))

if __name__ == '__main__':
  main()
