from ROOT import *
import itertools

#def MakeHists(name,title,nbin,low,high):
 #   hists = []
for set in itertools.combinations_with_replacement('bcj',2):
    print(set)
