#!/usr/bin/python

import sys
from thefuzz import process

with open("spisak.txt", "r", encoding="utf-8") as f:
  names = [line.strip() for line in f.readlines()]

if len(sys.argv) < 2:
  print("needs search parameters")
  exit(1)

search_param = " ".join([param.strip() for param in sys.argv[1:]])

for name, score in process.extract(search_param, names):
  print(name + " (score: " + str(score) + ")")

