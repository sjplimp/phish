# ping-pong test between 2 processes

set memory 2

minnow 1 mpi-ping 1000000 2000
minnow 2 mpi-pong

connect 1 single 2
connect 2 single 1

layout 1 1
layout 2 1