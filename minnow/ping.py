# MINNOW ping
# reflect messages to a receiver

import sys
import phish

def ping(nvalues):
  global count
  count += 1
  if count < n:
    phish.repack()
    phish.send(0)
  else: phish.close(0)
    
args = phish.init(sys.argv)
phish.input(0,ping,None,1)
phish.output(0)
phish.check()

idglobal = phish.query("idglobal",0,0)
print "PHISH host ping %d: %s" % (idglobal,phish.host())

if len(args) != 3: phish.error("Ping syntax: ping N M")

n = int(args[1])
m = int(args[2])

buf = m*"a"
count = 0

time_start = phish.timer()

phish.pack_string(buf)
phish.send(0)
phish.loop()

time_stop = phish.timer()
print "Elapsed time for %d pingpong exchanges of %d bytes = %g secs" % \
    (n,m,time_stop-time_start)

phish.exit()
