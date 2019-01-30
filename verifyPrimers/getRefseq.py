import os

bedtools = "bedtools"
ref = "/4_disk/genomes/hg19/hg19.fa" 


def getRefseq(chr,sts,end):
    sts = str(sts)
    end = str(end)
    bedcont = "%s\t%s\t%s\n" % (chr,sts,end)
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
