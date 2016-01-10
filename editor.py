#!/usr/bin/env python
import sys
import itertools
PRINT_COST = 1
def get_input(fn):
  with open(fn) as f:
    lines = [l.strip() for l in f.readlines()]
# Does not need value representing nr of jobs
    del lines[0]
# make list -> [[int, str,...,str]] , where each element is a job  
    return [ [int(val.split(' ')[1])] + lines[idx+1:idx+1+int(lines[idx].split(' ')[0])] for idx ,val in enumerate(lines) if ' ' in val]

def dijkstra(words):
  vertex.finish_value = words.pop(0)
  list = [vertex(0,[])]
  while list:
    cheapest_node = list.pop(0)
    if isFinished(cheapest_node):
      return cheapest_node.currentCost
    list = list + expand_node(cheapest_node, words)
    list.sort(key=lambda x: x.currentCost, reverse=False)

# calculate cost from word1 to go to word2
# Doesnt include cost of printing
def word_diff_cost(w1,w2):
  if w1 is None:
    return len(w2)
  common = len(list(itertools.takewhile(lambda x: x[0]==x[1],zip(w1,w2))))
  cost = len(w1[common:]) + len(w2[common:])
  return cost
    
class vertex:
  finish_value = 0
  currentCost = 0
  words = []
  def __init__ (self, currentCost, words):
    self.words = words
    self.currentCost = currentCost if len(words) < vertex.finish_value else currentCost + len(words[-1])
  def __str__(self):
    return str(len(self.words)) + " " + str(self.words) + " " + str(self.currentCost)

# Returns true if a node is a leaf, such that x words has been found
def isFinished(v):
  return len(v.words) == vertex.finish_value
 
# input: vertex and list of words
# output: list of vertices that are adjacent to input vertex in the graph
def expand_node(v, words):
  unused_words = [ x for x in words if x not in v.words ] 
  if v.words:
    res= [ vertex( v.currentCost + word_diff_cost(v.words[-1] ,x) + PRINT_COST, v.words + [x]) for x in unused_words ]
    return [x for x in res if len(x.words) > len(v.words)]
  res = [ vertex( v.currentCost + word_diff_cost("" ,x) + PRINT_COST, v.words + [x]) for x in unused_words ]
  return [x for x in res if len(x.words) > len(v.words)]
jobs = get_input(sys.argv[1])
for idx,job in enumerate(jobs):
  print("Case #" + str(idx+1) + ": " + str(dijkstra(job)))
