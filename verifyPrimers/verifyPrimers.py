import os
from readFasta import readFasta
from parseBlast import parseBlast
from getRefseq import getRefseq
blastn = "blastn"

def getfa(com,fa,prefix):
    com2seq = {}
    fadict = readFasta(fa)
    ofa = prefix + ".fa"
    fp = open(ofa,"w")
    for pair  in com :
        
        fpri = pair + "_F" 
        rpri = pair + "_R" 

        fpriseq = fadict[fpri] 
        rpriseq = fadict[rpri] 
        com2seq[pair] = [ fpriseq,rpriseq ]
        line = ">%s\n" % fpri
        fp.write(line)
        line = fpriseq + "\n"
        fp.write(line)
        line = ">%s\n" % rpri
        fp.write(line)
        line = rpriseq + "\n"
        fp.write(line)

    fp.close() 
    return ofa

def getseq(com,fa):
    com2seq = {}
    fadict = readFasta(fa)
    for pair  in com :

        fpri = pair + "_F"
        rpri = pair + "_R"

        fpriseq = fadict[fpri]
        rpriseq = fadict[rpri]
        com2seq[pair] = [ fpriseq,rpriseq ]
    return com2seq


def gettm(com,tm):
    primer2tm = {}
    fp = open(tm)
    for line in fp.readlines():
        items = line.strip().split("\t")
        pri = items[0]
        tm = items[1]
        primer2tm[pri] = tm

    com2tm = {}
    for pair in com:
        fpri = pair + "_F"
        rpri = pair + "_R"
        ftm = primer2tm[fpri]
        rtm = primer2tm[rpri]
        com2tm[pair] = [ftm,rtm]
    return com2tm

def getregion(com,pos):
    fp = open(pos) 
    com2pos = {}
    for line in fp.readlines():
        items = line.strip().split("\t") 
        pri = items[0]
        chr = items[1] 
        sts = items[2] 
        end = items[3] 
        id = pri.rsplit("_",1)[0]
        
        if id in com2pos:
            com2pos[id].append(end)
        else:
            com2pos[id] = [chr,sts]
    com2region = {}
    for pair in com:
        chr,start,end =  com2pos[pair]
        seq = getRefseq(chr,start,end)
        size = len(seq)
        com2region[pair] = [seq,size]
        
    return com2region
        
def verifyPrimers(com,reffa,tm,pos,prefix):
    fp = open(com)
    i = 1
    out = prefix + ".verify.out"
    fpw = open(out,"w")
    bests = []
    for line in fp.readlines():
        items = line.strip().split("\t") 
        coms = items[:-1] 
        prex = prefix + "_%s" % i
        fa = getfa(coms,reffa,prex)
        outs = parseBlast(fa)
        comstr = "\t".join(coms)
        bests.append([coms,len(outs)])
        comline = comstr + "\n\n"
        fpw.write(comline)
        for out in outs:
            out = ">>>" + out
            fpw.write(out)
        fpw.write("\n")
        i = i + 1
    fpw.close()
    bests = sorted(bests,key=lambda x:x[1])
    best = bests[0][0]
    bestfa = getfa(best,reffa,prefix+".verify")
    bestseq= getseq(best,reffa)
    besttm = gettm(best,tm)
    bestregion = getregion(best,pos)
   
    fp = open(prefix+".format.out","w")
    head = "\t".join(["locus","5-primer","3-primer","5-Tm","3-Tm","product","productSize"]) + "\n"
    fp.write(head)

    for id in best:
        fseq,rseq = bestseq[id]
        ftm,rtm= besttm[id]
        reg,leng = bestregion[id]
        
        line = "\t".join([id,fseq,rseq,ftm,rtm,reg,str(leng)]) + "\n"
        fp.write(line)
    fp.close()

    return out
if __name__ == "__main__":
    import sys
    com = sys.argv[1]
    fa = sys.argv[2]
    tm = sys.argv[3]
    po = sys.argv[4]
    prex = sys.argv[5]
    verifyPrimers(com,fa,tm,po,prex)
