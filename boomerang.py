#!/usr/bin/env python

import itertools
import sys
import math

lookup_table = { 4: 6, 3: 3, 2: 1,1: 0 }

def parse_tuple(s):
  x, y = s.split(' ')
  return int(x), int(y)

def boomerang_count(origin, universe):
  """Time complexity: O(|universe|)"""
  distances = [distance(origin, point) for point in universe]
  distances.sort()

  groups = itertools.groupby(distances, lambda d: d)
  groups = [lookup_table[len(list(y))] for x, y in groups]
  # lookup and sum 

  return sum(groups)

def distance(c1, c2):
  x1, y1 = c1
  x2, y2 = c2
  return math.hypot(x2 - x1, y2 - y1)

def get_input(filename):
  with open(filename) as f:
    lines = [l.strip() for l in f.readlines()]
    groups = itertools.groupby(lines, lambda x: ' ' in x)
    data = [list(y) for x, y in groups if x]
    data = [[parse_tuple(x) for x in d] for d in data]
  return data

def main():
  universes = get_input(sys.argv[1])

  for universe in universes:
    count = sum([boomerang_count(point, universe) for point in universe])

    print(count)

if __name__ == '__main__':
  main()

  #print filter(lambda x: len(x.split(' ')) == 2, lines)
