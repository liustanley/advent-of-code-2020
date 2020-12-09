#!/usr/bin/env python3

def strSplit(str):
  return str.split()

with open('input.txt', 'r') as inputFile:
  inputList = list(map(strSplit, inputFile.readlines()))

  valid = 0

  for i in inputList:
    policy = list(map(int, i[0].split('-')))
    min = policy[0]
    max = policy[1]

    letter = i[1][:-1]
    password = i[2]

    count = 0
    for j, val in enumerate(password):
      if (val == letter):
        count += 1
    
    if (count >= min and count <= max):
      valid += 1
  
  print(valid)
    