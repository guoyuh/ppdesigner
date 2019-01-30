
import os
from getRefseq import getRefseq

dirname = os.path.dirname(os.path.abspath(__file__))
p3default = os.path.join(dirname,"p3.config")
p3lines = open(p3default).readlines()

def readP3(lines):
    p3dict = {}
    for line in lines:
        k,v = line.strip().split("=")
        p3dict[k] = v
    return p3dict 

def locus2config(locus,pan):
    p3dict = readP3(p3lines)
    seq = getRefseq(locus,pan)     
    nlen = len(seq)
    tlen = nlen/2
    target = "%s,5" % tlen
    p3dict["SEQUENCE_ID"] = locus
    p3dict["SEQUENCE_TEMPLATE"] = seq
    p3dict["SEQUENCE_TARGET"] =  target
    return p3dict
   


if __name__ == "__main__":
    locus = "chr17|7579472"
    print locus2config(locus)
     
