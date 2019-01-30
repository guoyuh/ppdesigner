from locus2config import locus2config
from formatP3 import formatP3,pri2fasta
import tempfile
import os
from transloc import transloc

dirname = os.path.dirname(os.path.abspath(__file__))
p3core = os.path.join(dirname,"primer3_core")
pan = 300

def genPrimer(infile,pan,prefix):
    fp = open(infile)
    loces = []
    for line in fp:
        locus = line.strip()
        loces.append(locus)
    
    p3s = []
    for loc in loces:
        p3dict = locus2config(loc,pan)
        p3s.append(p3dict)

    lines = []
    for p3d in p3s:
        for k,v in p3d.items():
            line = "%s=%s" % (k,v)
            lines.append(line)
        lines.append("=")
    p3tmp = prefix  + ".p3"
    fp = open(p3tmp,"w")
    for line in lines:
        line = line + "\n"
        fp.write(line)
    fp.close()
    return p3tmp
    
def runPrimer(p3,prefix):
    out = prefix + ".raw.out"
    cmd = "%s -format_output -output=%s %s" % (p3core,out,p3)
    print cmd
    os.system(cmd)
    return out

def parsePrimer(p3out,prefix):
    primers = formatP3(p3out)
    out = pri2fasta(primers,prefix) 
    return out

def pickPrimers(infile,prefix):
    p3tmp = genPrimer(infile,pan,prefix)
    raw = runPrimer(p3tmp,prefix)
    prifa,pritm,pripo = parsePrimer(raw,prefix)
    pripo = transloc(pripo,pan)
    return prifa,pritm,pripo

if __name__ == "__main__":
    import sys
    inp = sys.argv[1]
    prex = sys.argv[2]
    pickPrimers(inp,prex) 
