#!/usr/local/bin/python

import sys
import phish

args = phish.init(sys.argv)
phish.input(0,None,None,1)
phish.output(0)
phish.check()

if len(args) != 0: phish.error("Reduce syntax: reduce")

phish.loop()
phish.exit()