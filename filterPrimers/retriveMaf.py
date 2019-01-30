import os
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
mafidx = os.path.join(absdir,"maf01.txt.idx")
maf = os.path.join(absdir,"maf01.txt")
fp = open(mafidx)
lines = fp.readlines()

ixs = []
for line in lines:
    items = line.strip("\n").split("\t")
    chr,loc,sts,end = items
    ixs.append([chr,int(loc),int(sts),int(end)])

def retriveMaf(ichr,loc1,loc2):
    loc1 = int(loc1)
    loc2 = int(loc2)

    fileidx1 = 0
    fileidx2 = 0
    for i in range(len(ixs)):
        item = ixs[i]
        chr,loc,pos1,pos2 = item
        if not ichr  == chr:
            continue
        if loc1 <= loc:
            fileidx1 = ixs[i-1][2]
        if loc2 <= loc:
            fileidx2 = pos1
        if fileidx1 and fileidx2:
            break
        
    return fileidx1,fileidx2        

def readMaf(pos1,pos2):
    lines = []
    fp = open(maf)
    fp.seek(pos1)
    while True:
        line = fp.readline()
        lines.append(line)
        pos = fp.tell()
        if pos > pos2:
            break        
    return lines


def checkMaf(ichr,loc1,loc2):
    loc1 = int(loc1)
    loc2 = int(loc2)
    p1,p2 = retriveMaf(ichr,loc1,loc2)
    lines = readMaf(p1,p2)
    locs = []
    for line in lines:
        item = line.strip().split()
        loc = int(item[-1])
        if loc >= loc1 and loc <= loc2:
            locs.append(loc)
    return locs
                               
if __name__ == "__main__":
    print checkMaf("Y","28769019","28769103")    



        
