#!/usr/local/bin/python

# MINNOW file2words
# read file and emit words

import sys
import phish

def read_file(nvalues):
  if nvalues != 1: phish.error("File2words processes one-value datums")
  type,filename,tmp = phish.unpack()
  if type != phish.STRING:
    phish.error("File2words processes string values")
  lines = open(filename,"r").readlines()
  for line in lines:
    words = line.split()
    for word in words:
      phish.pack_string(word)
      phish.send_key(0,word)

phish.init(sys.argv)
phish.input(0, read_file, None, 1)
phish.output(0)
phish.check()

phish.loop()
phish.exit()
