#!/usr/bin/python

"""
usage:
  python check_list.py <list file>
"""

import sys
from thefuzz import process
import transliterate

with open("spisak.txt", "r", encoding="utf-8") as f:
  names = [line.strip() for line in f.readlines()]

list_file = sys.argv[1]

with open(list_file, "r", encoding="utf-8") as f:
  check_list = [line.strip() for line in f.readlines()]
  check_list = [transliterate.translit(item, 'sr', reversed=True) for item in check_list]

for check_param in check_list:
  name, score = process.extractOne(check_param, names)
  print("check: " + check_param + ",  result: " + name + ",  score: " + str(score))

