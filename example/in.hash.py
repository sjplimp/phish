# hash test
# S procs send to R procs
# each source proc sends N/S messages

#set safe

variable n 10000000
variable len 0
variable s 1
variable r 1

minnow 1 source.py $n ${len}
minnow 2 reduce.py

hook 1 hashed 2
hook 2 direct 1

school 1 $s
school 2 $r
