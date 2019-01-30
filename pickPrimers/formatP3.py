import tempfile

def formatP3(p3out):
    id2primers = {}
    fp = open(p3out)
    lefts = []
    rights = []
    seqid = None
    lines = fp.readlines()
    nl = len(lines)
    i = 0
    for line in lines:
        i = i + 1
        if line.startswith("PRIMER PICKING RESULTS FOR")  or i == nl:
            if lefts and rights and seqid:
                pair = []
                for lef,rig in zip(lefts,rights):
                    pair.append([lef,rig])
                id2primers[seqid]  = pair
            seqid= line.strip()[27:]
            lefts = []
            rights = []
        if line.find("LEFT PRIMER") != -1:
            left = line.strip().split()[-1]
            tm = line.strip().split()[-6]
            pos = line.strip().split()[-8]
            lefts.append([left,tm,pos])
        if line.find("RIGHT PRIMER") != -1:
            right = line.strip().split()[-1]
            tm = line.strip().split()[-6]
            pos = line.strip().split()[-8]
            rights.append([right,tm,pos])
    return id2primers

def pri2fasta(id2pri,prefix):
    tmpfa = prefix + ".fa"
    tm = prefix + ".tm"
    po = prefix + ".loc"
    fp = open(tmpfa,"w")
    fp2 = open(tm,"w")
    fp3 = open(po,"w")        
    for id,pairs in id2pri.items():
        i = 1
        for pair in pairs:

            k =  ">" + id + "_" + "%s" % i

            fk = k + "_F" + "\n"
            fseq = pair[0][0]  + "\n"
            ftm = pair[0][1]
            fpos = pair[0][2]
            fposinfo = fpos + "," + str(len(fseq))

            rk = k + "_R" + "\n"
            rseq = pair[1][0] + "\n"
            rtm = pair[1][1]
            rpos = str(int(pair[1][2]) - len(rseq) + 2)
            rposinfo = rpos + "," + str(len(rseq))

            i = i + 1
            fp.write(fk)
            fp.write(fseq)
            fp.write(rk)
            fp.write(rseq)
            ftmline = "\t".join([k[1:]+"_F",ftm]) + "\n"
            rtmline = "\t".join([k[1:]+"_R",rtm]) + "\n"
            fp2.write(ftmline)
            fp2.write(rtmline)
            fpoline = "\t".join([k[1:]+"_F",fposinfo]) + "\n" 
            rpoline = "\t".join([k[1:]+"_R",rposinfo]) + "\n" 
            fp3.write(fpoline)
            fp3.write(rpoline)

    fp.close()
    fp2.close()
    fp3.close()
    return tmpfa,tm,po 
if __name__ == "__main__":
    import sys
    id2pris = formatP3(sys.argv[1])
    pri2fasta(id2pris,"example")
