from retriveMaf import checkMaf

def parseMaf(chrloc):
    fails = set()
    fp = open(chrloc)
    for line in fp.readlines():
        items = line.strip().split("\t")
        id = items[0]
        chr = items[1]
        chr = chr.replace("chr","")
        sts = int(items[2])
        if id.endswith("F"):
            end_end = int(items[3])
            end_sts = end_end - 5
        if id.endswith("R"):
            end_sts = sts
            end_end = sts + 5
        mafs = checkMaf(chr,end_sts,end_end)
        if mafs:
            kid = id.rsplit("_",1)[0] 
            fails.add(kid)

    return  fails
        


if __name__ == "__main__":
    import sys
    locfile = sys.argv[1]
    parseMaf(locfile)

