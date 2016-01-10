#!/usr/bin/env python

import random
import re
import itertools
import sys

length = 100

def random_row(length):
  row = []
  for i in range(length):
    row.append(random.choice(['.', '.', 'X']))

  return ''.join(row)

def something(row1, row2):
  new_row1 = list('X' + row1 + 'X')
  new_row2 = list('X' + row2 + 'X')
  count = 0

  for i in range(len(new_row1)):
    if new_row1[i] == '.' and new_row1[i-1] == 'X' and new_row1[i+1] == 'X':
      count = count + 1
      if is_empty(new_row2[i]):
        new_row2, new_row1 = expand_index(new_row2, new_row1, i)
      else:
        new_row1, new_row2 = expand_index(new_row1, new_row2, i)

  return count, ''.join(new_row1[1:-1]), ''.join(new_row2[1:-1])

def expand(row1, row2):
  pass

def expand_index(row1, row2, index):
  pre = row1[:index]
  middle = ['o']
  post = row1[index+1:]

  if row2[index] == '.':
    row2[index] = '-'

  for i in range(len(pre) - 1, -1, -1):
    if pre[i] == 'X' or pre[i] == 'o':
      break
    pre[i] = '-'

  for i in range(len(post)):
    if post[i] == 'X' or post[i] == 'o':
      break
    post[i] = '-'

  return (pre + middle + post), row2

def is_empty(s):
  return s == '.' or s == '-'

def overwrite(index):
  pass

def allX(row1,row2):
  print(row1.replace("o",'X').replace("-",'X'))
  print(row2.replace("o",'X').replace("-",'X'))
 
def replace(row):
  return row.replace("o",'X').replace("-",'X')

def count_holes(row):
  groups = [list(g) for k, g in itertools.groupby(row)]
  return len(list(filter(lambda x: '.' in x, groups)))

with open(sys.argv[1]) as f:
  # Initial value for # runs - THROW IT AWAY!
  f.readline()
  i = 1
  while f.readline() != "":
    row1 = f.readline().strip()
    row2 = f.readline().strip()
    c1, new_row1, new_row2 = something(row1, row2)
    c2, new_row2, new_row1 = something(new_row2, new_row1)
    #print(row1)
    #print(row2)
    #print()
    #print(new_row1)
    #print(new_row2)
    count = c1 + c2 + count_holes(new_row1) + count_holes(new_row2)
    print('Case #' + str(i) + ': ' + str(count))
    #print('------------')
    i = i + 1

#row1 = random_row(length)
#row2 = random_row(length)
#print(row1)
#print(row2)
#print()
#
#new_row1, new_row2 = something(row1, row2)
#print()
#new_row2, new_row1 = something(new_row2, new_row1)
#print(new_row1)
#print(new_row2)
#print()
#allX(new_row1,new_row2)
#
## TODO: count the actual guards
#count = count_holes(new_row1) + count_holes(new_row2)
#print(count)

def is_single(row1, row2, index):
  pass
