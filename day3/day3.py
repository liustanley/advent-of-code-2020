#!/usr/bin/env python3

def strSplit(str):
  return str.split()


def numTrees(right, down):
  with open('input.txt', 'r') as inputFile:
    inputList = list(map(strSplit, inputFile.readlines()))
    inputList = [item for sublist in inputList for item in sublist]

    width = len(inputList[0])
    height = len(inputList)

    curX, curY, count = 0, 0, 0

    while curY < height - down:
      curX += right
      curY += down

      if curX >= width:
        curX -= width

      if inputList[curY][curX] == '#':
        count += 1

    return count


oneOne = numTrees(1, 1)
threeOne = numTrees(3, 1)
fiveOne = numTrees(5, 1)
sevenOne = numTrees(7, 1)
oneTwo = numTrees(1, 2)

print(oneOne * threeOne * fiveOne * sevenOne * oneTwo)
