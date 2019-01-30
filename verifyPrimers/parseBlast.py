import os
blastn = "blastn"
def runBlast(fa):
    out = fa.split(".")[0] + ".blt"
    blp = fa.split(".")[0] + ".blp"
    cmd = '%s -query %s -subject %s -strand minus -word_size 6 -max_hsps 1 -evalue 10000 -perc_identity 100 -outfmt "6 qseqid sseqid sstrand pident length  qlen slen qstart qend sstart send" > %s ' % ( blastn,fa,fa,out)
    os.system(cmd)
    cmd = '%s -query %s -subject %s -strand minus -word_size 6 -max_hsps 1 -evalue 10000 -perc_identity 100  > %s ' % ( blastn,fa,fa,blp)
    os.system(cmd)
    return out


def parseBlast(fa):
    prex = fa.split(".")[0]  + ".out"   
    blt = runBlast(fa)
    fp = open(blt)
    pri2pri = {}
    outs = []
    for line in fp.readlines():
        items = line.strip().split("\t")
        fprimer = items[0]
        fid = fprimer.rsplit("_")[0]
        rprimer = items[1]
        rid = rprimer.rsplit("_")[0]
        strand = items[2]
        mlen = int(items[4])
        qlen = int(items[5])
        slen = int(items[6])
        qstart = int(items[7])
        qend = int(items[8])
        sstart = int(items[9])
        send = int(items[10])

        if strand == "plus":
            continue
        if fid == rid :
            continue
        if qlen - qend <= 0 or slen - sstart <= 0:
            outs.append(line)
            print line
    return outs


if __name__ == "__main__":
    import sys
    fa = sys.argv[1]
    parseBlast(fa)
