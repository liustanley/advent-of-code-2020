#!/usr/bin/env python3

with open('input.txt', 'r') as inputFile:  
  rawNumberList = inputFile.readlines();

  numberList = [];

  # remove \n from raw string and parse as int
  for i in rawNumberList:
    str = i[:len(i)-1]
    numberList.append(int(str))

  # O(log n)
  numberList.sort()

  length = len(numberList)
  values = set()

  # O(n)
  for i, val in enumerate(numberList):
    values.add(val)
    target = 2020 - val

    # O(1)
    if (target in values):
      print(target * val)
      exit()