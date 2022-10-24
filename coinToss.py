#!/usr/bin/env python3
#
# Simple coin flip guessing game for a python example
#
# v0.1 24oct2022 rkeepers@sparksonline.net
##########################################################

import random

print("Let's flip a coin")
def flip():
  side = random.randint(0,1)
  if side == 0:
    result = 'tails'
  if side == 1:  # could use else, but I want to make SURE we only entertain 1 and 0s
    result = 'heads'
  print("Coin lands ", result, " up.")
  return(result)

def call():
  guess = input("Call it. heads or tails? ")
  result = flip()
  if guess == result:
    print( guess, " is correct!")
  else:
    print( guess, " is incorrect")

call()
