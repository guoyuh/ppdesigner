import re
def transloc(locfile,pan):
    fp = open(locfile)
    locs = []
    for line in fp.readlines():
        items = line.strip("\n").split("\t")
        id = items[0]
        va = items[1]
        chr = id.split("|")[0]
        loc = id.split("|")[-1].split("_")[0]
        rloc = va.split(",")[0]
        rlen = va.split(",")[-1]
        
        chrloc1 = int(loc) + int(rloc) - pan + 1
        chrloc2 = chrloc1 + int(rlen) - 2
        locs.append([id,chr,str(chrloc1),str(chrloc2)])
    fp.close()

    chrloc = locfile+".chr"
    fp = open(chrloc,"w")
    for loc in locs:
        line = "\t".join(loc) + "\n" 
        fp.write(line) 
    fp.close()
    return chrloc   



if __name__ == "__main__":
    import sys
    transloc(sys.argv[1],300)

