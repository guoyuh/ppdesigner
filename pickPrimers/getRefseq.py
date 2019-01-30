import os

bedtools = "bedtools"
ref = "/4_disk/genomes/hg19/hg19.fa" 


def getRefseq(locus,pan):
    chr,sts = locus.split("|")
    nsts = int(sts) - pan
    end = int(sts) + pan
    bedcont = "%s\t%s\t%s\n" % (chr,nsts,end)
    bedfile = chr + "." + sts + ".bed"
    bedfp = open(bedfile,"w")
    bedfp.write(bedcont)
    bedfp.close()
    fafile = chr + "." + sts + ".fa"
    cmd = "%s getfasta -fi %s -bed %s -fo %s" % (bedtools,ref,bedfile,fafile)
    os.system(cmd)
    fp = open(fafile)
    fp.readline()
    seq = fp.read()
    seq = seq[:-1].upper()
    #os.remove(fafile)
    #os.remove(bedfile)
    return seq


if __name__ == "__main__":
    import sys
    fp = open(sys.argv[1])
    for line in fp.readlines():
        loc = line.strip()
        getRefseq(loc,300)
