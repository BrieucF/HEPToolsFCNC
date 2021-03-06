#!/usr/bin/python

#from ROOT import TChain, TProof, TFile, TH1D, TH1F, TCanvas, gROOT, TTree
from ROOT import *
import os, sys
gROOT.SetBatch(True)
import numpy as np

inputdir = sys.argv[1]
dataset = sys.argv[2]
tuples = sys.argv[3]
name = sys.argv[4]

def runAna(dir, file, name):
  chain = TChain("fcncLepJets/tree","events")
  chain.Add(dir+"/"+file)
  chain.Process("makeTuple.C+",name)

  f = TFile.Open("temp/tmva_"+name+".root","update")
  tr = f.Get("tmva_tree")
  totalnevt = np.zeros(1, dtype=float)
  tr.Branch('totnevt', totalnevt, 'totnevt/D')
  nevt = tr.GetEntries()
  for i in xrange(nevt):
    #tr.GetEntry(i)
    totalnevt[0] = nevt
  tr.Fill()
  f.Write()
  f.Close()

runAna(inputdir+'/'+dataset, tuples, name)
