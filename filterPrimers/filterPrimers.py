import os
import json
import tempfile
from readFasta import readFasta
from parseMaf import parseMaf

common = os.path.join(os.path.dirname( os.path.abspath(__file__) ),"commonPrimers.fa")
blastn = "blastn"

def runBlast(fa):
    out = fa.split(".")[0] + ".blt"
    cmd = '%s -query %s -subject %s -word_size 6 -max_hsps 1 -evalue 10000 -perc_identity 100 -outfmt  "6 qseqid sseqid sstrand pident length  qlen slen qstart qend sstart send" > %s ' % ( blastn,fa,common,out)
    print cmd
    os.system(cmd)
    return out
def parseBlast(blt):
    fp = open(blt)
    failprimers = set()
    pri2pri = {}
    for line in fp.readlines():
        items = line.strip().split("\t")
        fprimer = items[0]
        fid = fprimer.rsplit("_",1)[0]
        rprimer = items[1]
        rid = rprimer.rsplit("_",1)[0]
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
        if qlen - qend <= 0 :
            failprimers.add(fid)
    return failprimers

def filterPrimers(fa,ppo):
    blt = runBlast(fa)
    fails = parseBlast(blt)
    fails2 = parseMaf(ppo)
    print fails,fails2
    fails = fails | fails2
    falist = readFasta(fa)
    filts = []
    for f in falist:
        pid = f[0].rsplit("_",1)[0]
        seq = f[1]
        if pid in fails:
            continue
        filts.append(f)
    out = fa.split(".")[0] + ".filt.fa"
    fp = open(out,"w")
    for filt in filts:
        sid = filt[0]
        seq = filt[1]
        line = ">%s\n" % sid
        fp.write(line)
        line = seq + "\n"
        fp.write(line)
    fp.close()
    return out

if __name__ == "__main__":
    import sys
    fa = sys.argv[1]
    po = sys.argv[2]
    filterPrimers(fa,po)
