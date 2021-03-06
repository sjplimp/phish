import sys
import phish

# process an edge = (Vi,Vj)
# ignore self edges and duplicate edges
# store edge with Vi and Vj

def edge(nvalues):
  type,vi,tmp = phish.unpack()
  type,vj,tmp = phish.unpack()
  if vi == vj: return
  if vi in graph and vj in graph[vi]: return
  if vi not in graph: graph[vi] = [vj]
  else: graph[vi].append(vj)
  if vj not in graph: graph[vj] = [vi]
  else: graph[vj].append(vi)
  
# process graph to find triangles
# double loop over edges of each vertex = vj,vk
# look for wedge-closing vj,vk edges
# only emit triangle if vi is smallest vertex to avoid duplicates

def find():
  for vi,list in graph.items():
    for j,vj in enumerate(list):
      vjlist = graph[vj]
      for vk in list[:j]:
        if vk in vjlist:
          if vi > vj or vi > vk: continue
          phish.pack_uint64(vi)
          phish.pack_uint64(vj)
          phish.pack_uint64(vk)
          phish.send(0)

# main program
  
args = phish.init(sys.argv)
phish.input(0,edge,find,1)
phish.output(0)
phish.check()

if len(args) != 1: phish.error("Tri_one syntax: tri_one")
if phish.query("nlocal",0,0) != 1:
  phish.error("Can only be a single tri_one minnow")

graph = {}

time_start = phish.timer()

phish.loop()

time_stop = phish.timer()
print "Elapsed time for tri_one = %g secs" % (time_stop-time_start)

phish.exit()
