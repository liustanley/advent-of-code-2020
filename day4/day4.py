#!/usr/bin/env python3

def strSplit(str):
  return str.split()


def validatePassportFields(passport):
  for field in passport:
    key = field[:3]
    value = field[4:]
    valid = True

    if key == 'byr':
      valid = 1920 <= int(value) <= 2002
    elif key == 'iyr':
      valid = 2010 <= int(value) <= 2020
    elif key == 'eyr':
      valid = 2020 <= int(value) <= 2030
    elif key == 'hgt':
      unit = value[len(value) - 2:]
      number = int(value[:len(value) - 2])
      if unit == 'cm':
        valid = 150 <= number <= 193
      elif unit == 'in':
        valid = 59 <= number <= 76
      else:
        valid = False
    elif key == 'hcl':
      valid = len(value) == 7 and value[0] == '#' and value[1:].isalnum()
    elif key == 'ecl':
      valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    elif key == 'pid':
      valid = value.isdigit() and len(value) == 9

    if not valid:
      return False

  return True


with open('input.txt', 'r') as inputFile:
  inputList = list(map(strSplit, inputFile.readlines()))

  passports = []
  curPassport = []
  for sublist in inputList:
    if len(sublist) == 0:
      passports.append(curPassport)
      curPassport = []
    curPassport += sublist

  count = 0
  for passport in passports:
    if len(passport) == 8 and validatePassportFields(passport):
      count += 1
    elif len(passport) == 7:
      hasCid = False
      for field in passport:
        if field[:3] == 'cid':
          hasCid = True
      if not hasCid and validatePassportFields(passport):
        count += 1
  print(count)
