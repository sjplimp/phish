// MINNOW map
// read hashed messages from source, rehash them and send to reduce

#include "stdlib.h"
#include "stdio.h"
#include "phish.h"

void process(int);

/* ---------------------------------------------------------------------- */

int main(int argc, char **argv)
{
  phish_init(&argc,&argv);
  phish_input(0,process,NULL,1);
  phish_output(0);
  phish_check();

  if (argc != 1) phish_error("Map syntax: map");

  srand48(54321);

  phish_loop();
  phish_exit();
}

/* ---------------------------------------------------------------------- */

void process(int nvalues)
{
/*
  phish_repack();
  double rn = drand48();
  phish_send_key(0,(char *) &rn,sizeof(double));
*/
}