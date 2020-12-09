#!/usr/bin/env python3

def strSplit(str):
  return str.split()

with open('input.txt', 'r') as inputFile:
  inputList = list(map(strSplit, inputFile.readlines()))

  valid = 0

  for i in inputList:
    policy = list(map(int, i[0].split('-')))
    firstChar = policy[0] - 1
    secondChar = policy[1] - 1

    letter = i[1][:-1]
    password = i[2]

    first = password[firstChar] == letter
    second = password[secondChar] == letter
    
    if (first != second):
      valid += 1
  
  print(valid)
    