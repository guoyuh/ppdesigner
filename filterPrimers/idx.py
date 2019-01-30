import os

binsize = 10000

def idx(txt):
    fp = open(txt)
    idxs = []
    i = 0
    while True:
        line = fp.readline()
        if not line:
            idxs.append([chr,start,str(pre),str(cur)])
            break
        n = len(line)
        cur = fp.tell()
        pre = cur - n
        items = line.strip().split()
        chr,start = items
        if i % 10000==0 :
            idxs.append([chr,start,str(pre),str(cur)])
        i = i + 1

    fp = open(txt+".idx","w")
    for ix in idxs:
        line = "\t".join(ix) + "\n"
        fp.write(line) 
    fp.close()
       
if __name__ == "__main__":
    import sys
    txt = sys.argv[1]
    idx(txt)
