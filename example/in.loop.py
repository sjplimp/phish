# loop test for P-processor ring

#set safe

variable p 10
variable n 1000000
variable m 0

minnow 1 loop.py $n $m

hook 1 ring 1

school 1 $p
