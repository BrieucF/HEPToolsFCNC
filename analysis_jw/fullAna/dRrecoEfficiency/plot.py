import os
#from ROOT import *
from ROOT import TStyle, TF1, TFile, TCanvas, gDirectory, TTree, TH1D, TH1F, THStack, TLegend, gROOT
import ROOT
from style import *

c1 = TCanvas( 'c1', 'c1', 450, 450 ) 

hct_gendR = TH1D('hct_gendR','#Delta R of gen b jets (Hct)', 40, 0, 4)
hut_gendR = TH1D('hut_gendR','#Delta R of gen b jets (Hut)', 40, 0, 4)
hct_recodR = TH1D('hct_recodR','#Delta R of reco b jets (Hct)', 40, 0, 4)
hut_recodR = TH1D('hut_recodR','#Delta R of reco b jets (Hut)', 40, 0, 4)

hct_genHm = TH1D('hct_genHm','Mass of gen H (Hct)', 24, 0, 240)
hut_genHm = TH1D('hut_genHm','Mass of gen H (Hut)', 24, 0, 240)
hct_recoHm = TH1D('hct_recoHm','Mass of reco H (Hct)', 24, 0, 240)
hut_recoHm = TH1D('hut_recoHm','Mass of reco H (Hut)', 24, 0, 240)

hct_matchHm = TH1D('hct_matchHm','Mass of gen matched H (Hct)', 24, 0, 240)
hut_matchHm = TH1D('hut_matchHm','Mass of gen matched H (Hut)', 24, 0, 240)

tch = TFile.Open('~/fcnc/analysis_jw/fullAna/dRrecoEfficiency/hist_Top_Hct.root')
atch = TFile.Open('~/fcnc/analysis_jw/fullAna/dRrecoEfficiency/hist_AntiTop_Hct.root')
tuh = TFile.Open('~/fcnc/analysis_jw/fullAna/dRrecoEfficiency/hist_Top_Hut.root')
atuh = TFile.Open('~/fcnc/analysis_jw/fullAna/dRrecoEfficiency/hist_AntiTop_Hut.root')

label = TPaveText()
label.SetX1NDC(gStyle.GetPadLeftMargin())
label.SetY1NDC(1.0-gStyle.GetPadTopMargin())
label.SetX2NDC(1.0-gStyle.GetPadRightMargin()+0.03)
label.SetY2NDC(1.0)
label.SetTextFont(62)
label.AddText("Work in Progress        CMS, 35.9 fb^{-1} at #sqrt{s} = 13 TeV")
label.SetFillStyle(0)
label.SetBorderSize(0)
label.SetTextSize(0.035)
label.SetTextAlign(32)

##all histos with event selection!
###########################################################

tch_gendR_ch0 = tch.Get('h_HbjetsDR_Ch0_S1_Top_Hct')
atch_gendR_ch0 = atch.Get('h_HbjetsDR_Ch0_S1_AntiTop_Hct')
tuh_gendR_ch0 = tuh.Get('h_HbjetsDR_Ch0_S1_Top_Hut')
atuh_gendR_ch0 = atuh.Get('h_HbjetsDR_Ch0_S1_AntiTop_Hut')
tch_gendR_ch1 = tch.Get('h_HbjetsDR_Ch1_S1_Top_Hct')
atch_gendR_ch1 = atch.Get('h_HbjetsDR_Ch1_S1_AntiTop_Hct')
tuh_gendR_ch1 = tuh.Get('h_HbjetsDR_Ch1_S1_Top_Hut')
atuh_gendR_ch1 = atuh.Get('h_HbjetsDR_Ch1_S1_AntiTop_Hut')

hct_gendR = tch_gendR_ch0.Clone('hct_gendR')
hct_gendR.Add(atch_gendR_ch0,1.0)
hct_gendR.Add(tch_gendR_ch1,1.0)
hct_gendR.Add(atch_gendR_ch1,1.0)
hct_gendR.Scale(0.05)
#hct_gendR.SetTitle('#Delta R of gen b jets (Hct)')
hct_gendR.SetTitle('')
hct_gendR.GetYaxis().SetTitle("Events")

c1.cd()
hct_gendR.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_gendR.pdf')

hut_gendR = tuh_gendR_ch0.Clone('hut_gendR')
hut_gendR.Add(atuh_gendR_ch0,1.0)
hut_gendR.Add(tuh_gendR_ch1,1.0)
hut_gendR.Add(atuh_gendR_ch1,1.0)
hut_gendR.Scale(0.05)
#hut_gendR.SetTitle('#Delta R of gen b jets (Hut)')
hut_gendR.SetTitle('')
hut_gendR.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_gendR.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_gendR.pdf')

###########################################################

tch_recodR_ch0 = tch.Get('h_DRFCNHkinDR_Ch0_S1_Top_Hct')
atch_recodR_ch0 = atch.Get('h_DRFCNHkinDR_Ch0_S1_AntiTop_Hct')
tuh_recodR_ch0 = tuh.Get('h_DRFCNHkinDR_Ch0_S1_Top_Hut')
atuh_recodR_ch0 = atuh.Get('h_DRFCNHkinDR_Ch0_S1_AntiTop_Hut')
tch_recodR_ch1 = tch.Get('h_DRFCNHkinDR_Ch1_S1_Top_Hct')
atch_recodR_ch1 = atch.Get('h_DRFCNHkinDR_Ch1_S1_AntiTop_Hct')
tuh_recodR_ch1 = tuh.Get('h_DRFCNHkinDR_Ch1_S1_Top_Hut')
atuh_recodR_ch1 = atuh.Get('h_DRFCNHkinDR_Ch1_S1_AntiTop_Hut')

hct_recodR = tch_recodR_ch0.Clone('hct_recodR')
hct_recodR.Add(atch_recodR_ch0,1.0)
hct_recodR.Add(tch_recodR_ch1,1.0)
hct_recodR.Add(atch_recodR_ch1,1.0)
hct_recodR.Scale(0.05)
#hct_recodR.SetTitle('#Delta R of reco b jets (Hct)')
hct_recodR.SetTitle('')
hct_recodR.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hct_recodR.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_recodR.pdf')

hut_recodR = tuh_recodR_ch0.Clone('hut_recodR')
hut_recodR.Add(atuh_recodR_ch0,1.0)
hut_recodR.Add(tuh_recodR_ch1,1.0)
hut_recodR.Add(atuh_recodR_ch1,1.0)
hut_recodR.Scale(0.05)
#hct_recodR.SetTitle('#Delta R of reco b jets (Hut)')
hut_recodR.SetTitle('')
hut_recodR.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_recodR.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_recodR.pdf')

###########################################################

c1.cd()
c1.Clear()
hct_gendR.SetLineColor(2)
hct_recodR.SetLineColor(4)
hct_recodR.SetStats(0)
#hct_recodR.SetTitle('#Delta R gen and reco b jets (Hct)')
hct_recodR.SetTitle('')
hct_recodR.DrawNormalized('HIST')
hct_gendR.DrawNormalized('SAME HIST')
l1 = TLegend(0.68, 0.76, 0.85, 0.86)
l1.AddEntry(hct_gendR, 'Gen', 'l')
l1.AddEntry(hct_recodR, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_comp_dR_nor.pdf')

c1.cd()
c1.Clear()
#hct_recodR.SetTitle('#Delta R gen and reco b jets (Hct)')
hct_recodR.SetTitle('')
hct_recodR.Draw('HIST')
hct_gendR.Draw('SAME HIST')
l1.Clear()
l1.AddEntry(hct_gendR, 'Gen', 'l')
l1.AddEntry(hct_recodR, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_comp_dR.pdf')

c1.cd()
c1.Clear()
hut_gendR.SetLineColor(2)
hut_recodR.SetLineColor(4)
hut_recodR.SetStats(0)
#hut_recodR.SetTitle('#Delta R gen and reco b jets (Hut)')
hut_recodR.SetTitle('')
hut_recodR.DrawNormalized('HIST')
hut_gendR.DrawNormalized('SAME HIST')
l1.Clear()
l1.AddEntry(hut_gendR, 'Gen', 'l')
l1.AddEntry(hut_recodR, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_comp_dR_nor.pdf')

c1.cd()
c1.Clear()
#hut_recodR.SetTitle('#Delta R gen and reco b jets (Hut)')
hut_recodR.SetTitle('')
hut_recodR.Draw('HIST')
hut_gendR.Draw('SAME HIST')
l1.Clear()
l1.AddEntry(hut_gendR, 'Gen', 'l')
l1.AddEntry(hut_recodR, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_comp_dR.pdf')

###########################################################
###########################################################

tch_genHm_ch0 = tch.Get('h_genHm_Ch0_S1_Top_Hct')
atch_genHm_ch0 = atch.Get('h_genHm_Ch0_S1_AntiTop_Hct')
tuh_genHm_ch0 = tuh.Get('h_genHm_Ch0_S1_Top_Hut')
atuh_genHm_ch0 = atuh.Get('h_genHm_Ch0_S1_AntiTop_Hut')
tch_genHm_ch1 = tch.Get('h_genHm_Ch1_S1_Top_Hct')
atch_genHm_ch1 = atch.Get('h_genHm_Ch1_S1_AntiTop_Hct')
tuh_genHm_ch1 = tuh.Get('h_genHm_Ch1_S1_Top_Hut')
atuh_genHm_ch1 = atuh.Get('h_genHm_Ch1_S1_AntiTop_Hut')

hct_genHm = tch_genHm_ch0.Clone('hct_genHm')
hct_genHm.Add(atch_genHm_ch0,1.0)
hct_genHm.Add(tch_genHm_ch1,1.0)
hct_genHm.Add(atch_genHm_ch1,1.0)
hct_genHm.Scale(0.05)
#hct_genHm.SetTitle('Mass of gen H (Hct)')
hct_genHm.SetTitle('')
hct_genHm.GetXaxis().SetRangeUser(0,250)
hct_genHm.GetYaxis().SetTitle("Events")

c1.cd()
hct_genHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_genHm.pdf')

hut_genHm = tuh_genHm_ch0.Clone('hut_genHm')
hut_genHm.Add(atuh_genHm_ch0,1.0)
hut_genHm.Add(tuh_genHm_ch1,1.0)
hut_genHm.Add(atuh_genHm_ch1,1.0)
hut_genHm.Scale(0.05)
#hut_genHm.SetTitle('Mass of gen H (Hut)')
hut_genHm.SetTitle('')
hut_genHm.GetXaxis().SetRangeUser(0,250)
hut_genHm.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_genHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_genHm.pdf')

###########################################################

tch_recoHm_ch0 = tch.Get('h_DRFCNHkinHMass_Ch0_S1_Top_Hct')
atch_recoHm_ch0 = atch.Get('h_DRFCNHkinHMass_Ch0_S1_AntiTop_Hct')
tuh_recoHm_ch0 = tuh.Get('h_DRFCNHkinHMass_Ch0_S1_Top_Hut')
atuh_recoHm_ch0 = atuh.Get('h_DRFCNHkinHMass_Ch0_S1_AntiTop_Hut')
tch_recoHm_ch1 = tch.Get('h_DRFCNHkinHMass_Ch1_S1_Top_Hct')
atch_recoHm_ch1 = atch.Get('h_DRFCNHkinHMass_Ch1_S1_AntiTop_Hct')
tuh_recoHm_ch1 = tuh.Get('h_DRFCNHkinHMass_Ch1_S1_Top_Hut')
atuh_recoHm_ch1 = atuh.Get('h_DRFCNHkinHMass_Ch1_S1_AntiTop_Hut')

hct_recoHm = tch_recoHm_ch0.Clone('hct_recoHm')
hct_recoHm.Add(atch_recoHm_ch0,1.0)
hct_recoHm.Add(tch_recoHm_ch1,1.0)
hct_recoHm.Add(atch_recoHm_ch1,1.0)
hct_recoHm.Scale(0.05)
#hct_recoHm.SetTitle('Mass of reco H (Hct)')
hct_recoHm.SetTitle('')
hct_recoHm.GetXaxis().SetRangeUser(0,250)
hct_recoHm.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hct_recoHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_recoHm.pdf')

hut_recoHm = tuh_recoHm_ch0.Clone('hut_recoHm')
hut_recoHm.Add(atuh_recoHm_ch0,1.0)
hut_recoHm.Add(tuh_recoHm_ch1,1.0)
hut_recoHm.Add(atuh_recoHm_ch1,1.0)
hut_recoHm.Scale(0.05)
#hut_recoHm.SetTitle('Mass of reco H (Hut)')
hut_recoHm.SetTitle('')
hut_recoHm.GetXaxis().SetRangeUser(0,250)
hut_recoHm.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_recoHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_recoHm.pdf')

###########################################################

c1.cd()
c1.Clear()
hct_genHm.SetLineColor(2)
hct_recoHm.SetLineColor(4)
hct_genHm.SetStats(0)
#hct_genHm.SetTitle('Mass of gen and reco H (Hct)')
hct_genHm.SetTitle('')
hct_genHm.GetXaxis().SetRangeUser(0,250)
hct_genHm.DrawNormalized('HIST')
hct_recoHm.DrawNormalized('SAME HIST')
l1.Clear()
l1.AddEntry(hct_genHm, 'Gen', 'l')
l1.AddEntry(hct_recoHm, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_comp_Hm_nor.pdf')

c1.cd()
c1.Clear()
#hct_genHm.SetTitle('Mass of gen and reco H (Hct)')
hct_genHm.SetTitle('')
hct_genHm.GetXaxis().SetRangeUser(0,250)
hct_genHm.Draw('HIST')
hct_recoHm.Draw('SAME HIST')
l1.Clear()
l1.AddEntry(hct_genHm, 'Gen', 'l')
l1.AddEntry(hct_recoHm, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_comp_Hm.pdf')

c1.cd()
c1.Clear()
hut_genHm.SetLineColor(2)
hut_recoHm.SetLineColor(4)
hut_genHm.SetStats(0)
#hut_genHm.SetTitle('Mass of gen and reco H (Hut)')
hut_genHm.SetTitle('')
hut_genHm.GetXaxis().SetRangeUser(0,250)
hut_genHm.DrawNormalized('HIST')
hut_recoHm.DrawNormalized('SAME HIST')
l1.Clear()
l1.AddEntry(hut_genHm, 'Gen', 'l')
l1.AddEntry(hut_recoHm, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_comp_Hm_nor.pdf')

c1.cd()
c1.Clear()
#hut_genHm.SetTitle('Mass of gen and reco H (Hut)')
hut_genHm.SetTitle('')
hut_genHm.GetXaxis().SetRangeUser(0,250)
hut_genHm.Draw('HIST')
hut_recoHm.Draw('SAME HIST')
l1.Clear()
l1.AddEntry(hut_genHm, 'Gen', 'l')
l1.AddEntry(hut_recoHm, 'Reco', 'l')
l1.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_comp_Hm.pdf')

###########################################################
###########################################################

tch_matchHm_ch0 = tch.Get('h_matchHm_Ch0_S1_Top_Hct')
atch_matchHm_ch0 = atch.Get('h_matchHm_Ch0_S1_AntiTop_Hct')
tuh_matchHm_ch0 = tuh.Get('h_matchHm_Ch0_S1_Top_Hut')
atuh_matchHm_ch0 = atuh.Get('h_matchHm_Ch0_S1_AntiTop_Hut')
tch_matchHm_ch1 = tch.Get('h_matchHm_Ch1_S1_Top_Hct')
atch_matchHm_ch1 = atch.Get('h_matchHm_Ch1_S1_AntiTop_Hct')
tuh_matchHm_ch1 = tuh.Get('h_matchHm_Ch1_S1_Top_Hut')
atuh_matchHm_ch1 = atuh.Get('h_matchHm_Ch1_S1_AntiTop_Hut')

hct_matchHm = tch_matchHm_ch0.Clone('hct_matchHm')
hct_matchHm.Add(atch_matchHm_ch0,1.0)
hct_matchHm.Add(tch_matchHm_ch1,1.0)
hct_matchHm.Add(atch_matchHm_ch1,1.0)
hct_matchHm.Scale(0.05)
#hct_matchHm.SetTitle('Mass of gen matched H (Hct)')
hct_matchHm.SetTitle('')
hct_matchHm.GetXaxis().SetRangeUser(0,250)
hct_matchHm.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hct_matchHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_matchHm.pdf')
hut_matchHm = tuh_matchHm_ch0.Clone('hut_matchHm')
hut_matchHm.Add(atuh_matchHm_ch0,1.0)
hut_matchHm.Add(tuh_matchHm_ch1,1.0)
hut_matchHm.Add(atuh_matchHm_ch1,1.0)
hut_matchHm.Scale(0.05)
#hut_matchHm.SetTitle('Mass of gen matched H (Hut)')
hut_matchHm.SetTitle('')
hut_matchHm.GetXaxis().SetRangeUser(0,250)
hut_matchHm.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_matchHm.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_matchHm.pdf')

###########################################################

c1.cd()
c1.Clear()
hct_matchHm.SetLineColor(2)
hct_matchHm.SetLineStyle(7)
hct_recoHm.SetLineColor(4)
hct_matchHm.SetStats(0)
#hct_matchHm.SetTitle('#Delta R reco and gen matched b jets (Hct)')
hct_matchHm.SetTitle('')
hct_matchHm.GetXaxis().SetRangeUser(0,250)
hct_matchHm.DrawNormalized('HIST')
hct_recoHm.DrawNormalized('SAME HIST')
l2 = TLegend(0.68, 0.76, 0.85, 0.86)
l2.AddEntry(hct_matchHm, 'matched', 'l')
l2.AddEntry(hct_recoHm, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_reco_match_Hm_nor.pdf')

c1.cd()
c1.Clear()
hct_recoHm.Draw('HIST')
hct_recoHm.SetStats(0)
hct_matchHm.Draw('SAME HIST')
l2.Clear()
l2.AddEntry(hct_matchHm, 'matched', 'l')
l2.AddEntry(hct_recoHm, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_reco_match_Hm.pdf')

c1.cd()
c1.Clear()
hut_matchHm.SetLineColor(2)
hut_matchHm.SetLineStyle(7)
hut_recoHm.SetLineColor(4)
hut_matchHm.SetStats(0)
#hut_matchHm.SetTitle('#Delta R reco and gen matched b jets (Hut)')
hut_matchHm.SetTitle('')
hut_matchHm.GetXaxis().SetRangeUser(0,250)
hut_matchHm.DrawNormalized('HIST')
hut_recoHm.DrawNormalized('SAME HIST')
l2.Clear()
l2.AddEntry(hut_matchHm, 'matched', 'l')
l2.AddEntry(hut_recoHm, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_reco_match_Hm_nor.pdf')

c1.cd()
c1.Clear()
hut_recoHm.Draw('HIST')
hut_recoHm.SetStats(0)
hut_matchHm.Draw('SAME HIST')
l2.Clear()
l2.AddEntry(hut_matchHm, 'matched', 'l')
l2.AddEntry(hut_recoHm, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_reco_match_Hm.pdf')

############################3

tch_matchdR_ch0 = tch.Get('h_matchDR_Ch0_S1_Top_Hct')
atch_matchdR_ch0 = atch.Get('h_matchDR_Ch0_S1_AntiTop_Hct')
tuh_matchdR_ch0 = tuh.Get('h_matchDR_Ch0_S1_Top_Hut')
atuh_matchdR_ch0 = atuh.Get('h_matchDR_Ch0_S1_AntiTop_Hut')
tch_matchdR_ch1 = tch.Get('h_matchDR_Ch1_S1_Top_Hct')
atch_matchdR_ch1 = atch.Get('h_matchDR_Ch1_S1_AntiTop_Hct')
tuh_matchdR_ch1 = tuh.Get('h_matchDR_Ch1_S1_Top_Hut')
atuh_matchdR_ch1 = atuh.Get('h_matchDR_Ch1_S1_AntiTop_Hut')

hct_matchdR = tch_matchdR_ch0.Clone('hct_matchdR')
hct_matchdR.Add(atch_matchdR_ch0,1.0)
hct_matchdR.Add(tch_matchdR_ch1,1.0)
hct_matchdR.Add(atch_matchdR_ch1,1.0)
hct_matchdR.Scale(0.05)
#hct_matchdR.SetTitle('#Delta R of gen matched reco b jets (Hct)')
hct_matchdR.SetTitle('')
hct_matchdR.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hct_recodR.Draw('HIST')
label.Draw("same")
c1.Print('h_hct_matchdR.pdf')

hut_matchdR = tuh_recodR_ch0.Clone('hut_matchdR')
hut_matchdR.Add(atuh_matchdR_ch0,1.0)
hut_matchdR.Add(tuh_matchdR_ch1,1.0)
hut_matchdR.Add(atuh_matchdR_ch1,1.0)
hut_matchdR.Scale(0.05)
#hut_matchdR.SetTitle('#Delta R of gen matched reco b jets (Hut)')
hut_matchdR.SetTitle('')
hut_matchdR.GetYaxis().SetTitle("Events")

c1.cd()
c1.Clear()
hut_recodR.Draw('HIST')
label.Draw("same")
c1.Print('h_hut_matchdR.pdf')

#########################

c1.cd()
c1.Clear()
hct_recodR.SetLineColor(4)
hct_matchdR.SetLineColor(2)
hct_matchdR.SetLineStyle(7)
hct_recodR.Draw('HIST')
hct_recodR.SetStats(0)
hct_matchdR.Draw('SAME HIST')
l2.Clear()
l2.AddEntry(hct_matchdR, 'matched', 'l')
l2.AddEntry(hct_recodR, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hct_reco_match_DR.pdf')

c1.cd()
c1.Clear()
hut_recodR.SetLineColor(4)
hut_matchdR.SetLineColor(2)
hut_matchdR.SetLineStyle(7)
hut_recodR.Draw('HIST')
hut_recodR.SetStats(0)
hut_matchdR.Draw('SAME HIST')
l2.Clear()
l2.AddEntry(hut_matchdR, 'matched', 'l')
l2.AddEntry(hut_recodR, 'Reco', 'l')
l2.Draw('SAME')
label.Draw("same")
c1.Print('h_hut_reco_match_DR.pdf')
