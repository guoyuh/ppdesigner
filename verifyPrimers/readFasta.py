
def readFasta(fa):
    fp = open(fa)

    seqids = []
    seqs = []
    for line in fp.readlines():
        line = line.strip("\n")
        if line.startswith(">"):
            seqid = line[1:]
            seqids.append(seqid)
            seq = ""
        else:
            seq = seq + line
            seqs.append(seq)

    fadict = {}
    for seqid,seq in zip(seqids,seqs):
        fadict[seqid] = seq

    return fadict
    

if __name__ == "__main__":
    readFasta("example.fa")
