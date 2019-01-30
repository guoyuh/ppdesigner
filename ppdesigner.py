import os

from pickPrimers.pickPrimers import pickPrimers
from filterPrimers.filterPrimers import filterPrimers
from properPrimers.properPrimers import properPrimers
from compPrimers.greedySearch import greedySearch
from compPrimers.formatOut import formatOut
from verifyPrimers.verifyPrimers import verifyPrimers


def ppdesigner(locs,prefix):
    
    pfa,ptm,ppo = pickPrimers(locs,prefix)
    ffa = filterPrimers(pfa,ppo)
    pid2pids,sid2pids = properPrimers(ffa,prefix)
    greedySearch(sid2pids,pid2pids,prefix)
    out = formatOut(prefix)
    verifyPrimers(out,pfa,ptm,ppo,prefix)    


if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        ppdesigner.py -i <input> -p <prefix>

    Options:
        -i,--input=<input>        input file in "chr|locus" format.
        -p,--prefix=<prefix>      output prefix

    Description:
        ppdesigner is used for design human multiplex pcr primer .

    """

    args = docopt(usage)
    pi = args["--input"]
    px = args["--prefix"]
    ppdesigner(pi,px)


