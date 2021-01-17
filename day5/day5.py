#!/usr/bin/env python3
import math

ROWS = 128
COLUMNS = 8


def strSplit(str):
  return str.split()


def getRow(rowList):
  lower = 0
  upper = ROWS - 1
  for i, v in enumerate(rowList):
    if i == len(rowList) - 1:
      if v == 'F':
        return lower
      elif v == 'B':
        return upper

    if v == 'F':
      upper = upper - math.ceil((upper - lower) / 2)
    elif v == 'B':
      lower = upper - int((upper - lower) / 2)


def getCol(colList):
  lower = 0
  upper = COLUMNS - 1
  for i, v in enumerate(colList):
    if i == len(colList) - 1:
      if v == 'L':
        return lower
      elif v == 'R':
        return upper

    if v == 'L':
      upper = upper - math.ceil((upper - lower) / 2)
    elif v == 'R':
      lower = upper - int((upper - lower) / 2)


def getId(bPass):
  rowList = bPass[:7]
  colList = bPass[7:]

  row = getRow(rowList)
  col = getCol(colList)

  return row * 8 + col


def findMissing(idList):
  last = idList[0]

  for id in idList[1:]:
    if id - 1 != last:
      return id - 1
    else:
      last = id


with open('input.txt', 'r') as inputFile:
  inputList = list(map(strSplit, inputFile.readlines()))
  boardingPasses = [value for sublist in inputList for value in sublist]

  max = 0
  for bPass in boardingPasses:
    id = getId(bPass)
    if id > max:
      max = id

  print(max)

  idList = list(map(getId, boardingPasses))
  idList.sort()
  myId = findMissing(idList)
  print(myId)
