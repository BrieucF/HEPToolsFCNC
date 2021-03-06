import os
from ROOT import *

tmva_version = 'v8'

for ch in ['Hct29']:
#for ch in ['Hct29','Hut29']:
#for ch in ['Hct30','Hut30']:

  ttbar = 0.0911727864721

  target = TFile('shape_'+tmva_version+'_'+ch+'.root','RECREATE')

  for scores in os.listdir('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'):

    if scores == 'shape_'+ch+'_ttbb.root':
      ttbb = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)

      bdt_ttbb = ttbb.Get('h_scoreBDT_'+ch+'_ttbb')
      bdt_ttbb.Scale(ttbar*1.25)
      bdt_ttbb.SetName('bdt_ttbb')
      bdt_ttbb.Scale(4938.9/bdt_ttbb.Integral())

      keras_ttbb = ttbb.Get('h_scoreKeras_'+ch+'_ttbb')
      keras_ttbb.Scale(ttbar*1.25)
      keras_ttbb.SetName('keras_ttbb')
      keras_ttbb.Scale(4938.9/keras_ttbb.Integral())

      target.cd()
      bdt_ttbb.Write()
      keras_ttbb.Write()
   
    elif scores == 'shape_'+ch+'_ttLF.root':
      ttLF = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)
      tt = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_ttother.root')
      
      bdt_ttLF = ttLF.Get('h_scoreBDT_'+ch+'_ttLF')
      bdt_ttLF.Scale(ttbar)
      bdt_ttLF.Scale(17190.7/bdt_ttLF.Integral())
      bdt_tt = tt.Get('h_scoreBDT_'+ch+'_ttother')
      bdt_tt.Scale(ttbar)   
      bdt_tt.Scale(23754.6/bdt_tt.Integral()) 
      bdt_ttLF.Add(bdt_ttLF, bdt_tt, 1.0, 1.0)
      bdt_ttLF.SetName('bdt_ttLF')

      keras_ttLF = ttLF.Get('h_scoreKeras_'+ch+'_ttLF')
      keras_ttLF.Scale(ttbar)
      keras_ttLF.Scale(17190.7/keras_ttLF.Integral())
      keras_tt = tt.Get('h_scoreKeras_'+ch+'_ttother')
      keras_tt.Scale(ttbar)
      keras_tt.Scale(23754.6/keras_tt.Integral())
      keras_ttLF.Add(keras_ttLF, keras_tt, 1.0, 1.0)
      keras_ttLF.SetName('keras_ttLF')

      target.cd()
      bdt_ttLF.Write()
      keras_ttLF.Write()
   
    elif scores == 'shape_'+ch+'_ttcc.root':
      ttcc = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)

      bdt_ttcc = ttcc.Get('h_scoreBDT_'+ch+'_ttcc')
      bdt_ttcc.Scale(ttbar)
      bdt_ttcc.SetName('bdt_ttcc')
      bdt_ttcc.Scale(1682.1/bdt_ttcc.Integral())

      keras_ttcc = ttcc.Get('h_scoreKeras_'+ch+'_ttcc')
      keras_ttcc.Scale(ttbar)
      keras_ttcc.SetName('keras_ttcc')
      keras_ttcc.Scale(1682.1/keras_ttcc.Integral())

      target.cd()
      bdt_ttcc.Write()
      keras_ttcc.Write()
   
    elif scores == 'shape_'+ch+'_ttbj.root':
      ttbj = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)

      bdt_ttbj = ttbj.Get('h_scoreBDT_'+ch+'_ttbj')
      bdt_ttbj.Scale(ttbar)
      bdt_ttbj.SetName('bdt_ttbj')
      bdt_ttbj.Scale(5457.6/bdt_ttbj.Integral())

      keras_ttbj = ttbj.Get('h_scoreKeras_'+ch+'_ttbj')
      keras_ttbj.Scale(ttbar)
      keras_ttbj.SetName('keras_ttbj')
      keras_ttbj.Scale(5457.6/keras_ttbj.Integral())

      target.cd()
      bdt_ttbj.Write()
      keras_ttbj.Write()

    elif scores == 'shape_'+ch+'_tchannel.root':
      st = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)
      stbar = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_tbarchannel.root')
      tw = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_tWchannel.root')
      tbarw = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_tbarWchannel.root')

      bdt_singletop = st.Get('h_scoreBDT_'+ch+'_tchannel')
      bdt_singletop.Scale(0.0732767154777)
      bdt_singletop.Scale(419.2/bdt_singletop.Integral())
      bdt_stbar = stbar.Get('h_scoreBDT_'+ch+'_tbarchannel')
      bdt_stbar.Scale(0.0755276009929)
      bdt_stbar.Scale(263.4/bdt_stbar.Integral())
      bdt_singletop.Add(bdt_singletop, bdt_stbar, 1.0, 1.0)
      bdt_tw = tw.Get('h_scoreBDT_'+ch+'_tWchannel')
      bdt_tw.Scale(0.190627583042)
      bdt_tw.Scale(884.6/bdt_tw.Integral())
      bdt_singletop.Add(bdt_singletop, bdt_tw, 1.0, 1.0)
      bdt_tbarw =tbarw.Get('h_scoreBDT_'+ch+'_tbarWchannel')
      bdt_tbarw.Scale(0.193322932135)
      bdt_tbarw.Scale(889.9/bdt_tbarw.Integral())
      bdt_singletop.Add(bdt_singletop, bdt_tbarw, 1.0, 1.0)
      bdt_singletop.SetName('bdt_singletop')

      keras_singletop = st.Get('h_scoreKeras_'+ch+'_tchannel')
      keras_singletop.Scale(0.0732767154777)
      keras_singletop.Scale(419.2/keras_singletop.Integral())
      keras_stbar = stbar.Get('h_scoreKeras_'+ch+'_tbarchannel')
      keras_stbar.Scale(0.0755276009929)
      keras_stbar.Scale(263.4/keras_stbar.Integral())
      keras_singletop.Add(keras_singletop, keras_stbar, 1.0, 1.0)
      keras_tw = tw.Get('h_scoreKeras_'+ch+'_tWchannel')
      keras_tw.Scale(0.190627583042)
      keras_tw.Scale(884.6/keras_tw.Integral())
      keras_singletop.Add(keras_singletop, keras_tw, 1.0, 1.0)
      keras_tbarw = tbarw.Get('h_scoreKeras_'+ch+'_tbarWchannel')
      keras_tbarw.Scale(0.193322932135)
      keras_tbarw.Scale(889.9/keras_tbarw.Integral())
      keras_singletop.Add(keras_singletop, keras_tbarw, 1.0, 1.0)
      keras_singletop.SetName('keras_singletop')

      target.cd()
      bdt_singletop.Write()
      keras_singletop.Write()

    elif scores == 'shape_'+ch+'_zjets.root':
      zjets = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+scores)
      zjets10to50 = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_zjets10to50V2.root')
      wjets = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_wjetsV2.root')
      ww = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_ww.root')
      wz = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_wz.root')
      zz = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_zz.root')

      bdt_others = zjets.Get('h_scoreBDT_'+ch+'_zjets')
      bdt_others.Scale(2.65956499509)
      bdt_zjets10to50 = zjets10to50.Get('h_scoreBDT_'+ch+'_zjets10to50V2')
      bdt_zjets10to50.Scale(6.69636342062)
      bdt_others.Add(bdt_others, bdt_zjets10to50, 1.0, 1.0)
      bdt_wjets = wjets.Get('h_scoreBDT_'+ch+'_wjetsV2')
      bdt_wjets.Scale(12.4461324996)
      bdt_others.Add(bdt_others, bdt_wjets, 1.0, 1.0)
      bdt_ww = ww.Get('h_scoreBDT_'+ch+'_ww')
      bdt_ww.Scale(4.70407414855)
      bdt_others.Add(bdt_others, bdt_ww, 1.0, 1.0)
      bdt_wz = wz.Get('h_scoreBDT_'+ch+'_wz')
      bdt_wz.Scale(1.69041171)
      bdt_others.Add(bdt_others, bdt_wz, 1.0, 1.0)
      bdt_zz = zz.Get('h_scoreBDT_'+ch+'_zz')
      bdt_zz.Scale(0.598577911125)
      bdt_others.Add(bdt_others, bdt_zz, 1.0, 1.0)
      bdt_others.SetName('bdt_others')

      keras_others = zjets.Get('h_scoreKeras_'+ch+'_zjets')
      keras_others.Scale(2.65956499509)
      keras_zjets10to50 = zjets10to50.Get('h_scoreKeras_'+ch+'_zjets10to50V2')
      keras_zjets10to50.Scale(6.69636342062)
      keras_others.Add(keras_others, keras_zjets10to50, 1.0, 1.0)
      keras_wjets = wjets.Get('h_scoreKeras_'+ch+'_wjetsV2')
      keras_wjets.Scale(12.4461324996)
      keras_others.Add(keras_others, keras_wjets, 1.0, 1.0)
      keras_ww = ww.Get('h_scoreKeras_'+ch+'_ww')
      keras_ww.Scale(4.70407414855)
      keras_others.Add(keras_others, keras_ww, 1.0, 1.0)
      keras_wz = wz.Get('h_scoreKeras_'+ch+'_wz')
      keras_wz.Scale(1.69041171)
      keras_others.Add(keras_others, keras_wz, 1.0, 1.0)
      keras_zz = zz.Get('h_scoreKeras_'+ch+'_zz')
      keras_zz.Scale(0.598577911125)
      keras_others.Add(keras_others, keras_zz, 1.0, 1.0)
      keras_others.SetName('keras_others')

      target.cd()
      bdt_others.Write()
      keras_others.Write()

    elif scores == 'shape_'+ch+'_SingleLepton_Run2016.root':
      rd = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_SingleLepton_Run2016.root')
      
      bdt_data_obs = rd.Get('h_scoreBDT_'+ch+'_SingleLepton_Run2016')
      bdt_data_obs.SetName('bdt_data_obs')

      keras_data_obs = rd.Get('h_scoreKeras_'+ch+'_SingleLepton_Run2016')
      keras_data_obs.SetName('keras_data_obs')

      target.cd()
      bdt_data_obs.Write()
      keras_data_obs.Write()
     
    elif scores == 'shape_'+ch+'_Top_Hct.root' and ch == 'Hct29':
      tch = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_Top_Hct.root')
      tbarch = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_AntiTop_Hct.root')

      bdt_sig = tch.Get('h_scoreBDT_'+ch+'_Top_Hct')
      bdt_sig.Scale(0.0631644530114)
      bdt_scale1 = 1625.4/bdt_sig.Integral()
      bdt_sig.Scale(bdt_scale1)
      bdt_tbarch = tbarch.Get('h_scoreBDT_'+ch+'_AntiTop_Hct')
      bdt_tbarch.Scale(0.063175201321)
      bdt_scale2 = 1639.1/bdt_tbarch.Integral()
      bdt_tbarch.Scale(bdt_scale2)
      bdt_sig.Add(bdt_sig, bdt_tbarch, 1.0, 1.0)
      bdt_sig.SetName('bdt_sig')

      keras_sig = tch.Get('h_scoreKeras_'+ch+'_Top_Hct')
      keras_sig.Scale(0.0631644530114)
      keras_scale1 = 1625.4/keras_sig.Integral()
      keras_sig.Scale(keras_scale1)
      keras_tbarch = tbarch.Get('h_scoreKeras_'+ch+'_AntiTop_Hct')
      keras_tbarch.Scale(0.063175201321)
      keras_scale2 = 1639.1/keras_tbarch.Integral()
      keras_tbarch.Scale(keras_scale2)
      keras_sig.Add(keras_sig, keras_tbarch, 1.0, 1.0)
      keras_sig.SetName('keras_sig')

      bdt_sig_gen = tch.Get('h_scoreBDTGen_'+ch+'_Top_Hct')
      bdt_sig_gen.Scale(0.0631644530114)
      bdt_sig_gen.Scale(bdt_scale1)
      bdt_tbarch_gen = tbarch.Get('h_scoreBDTGen_'+ch+'_AntiTop_Hct')
      bdt_tbarch_gen.Scale(0.063175201321)
      bdt_tbarch_gen.Scale(bdt_scale2)
      bdt_sig_gen.Add(bdt_sig_gen, bdt_tbarch_gen, 1.0, 1.0)
      bdt_sig_gen.SetName('bdt_sig_gen')

      keras_sig_gen = tch.Get('h_scoreKerasGen_'+ch+'_Top_Hct')
      keras_sig_gen.Scale(0.0631644530114)
      keras_sig_gen.Scale(keras_scale1)
      keras_tbarch_gen = tbarch.Get('h_scoreKerasGen_'+ch+'_AntiTop_Hct')
      keras_tbarch_gen.Scale(0.063175201321)
      keras_tbarch_gen.Scale(keras_scale2)
      keras_sig_gen.Add(keras_sig_gen, keras_tbarch_gen, 1.0, 1.0)
      keras_sig_gen.SetName('keras_sig_gen')

      target.cd()
      bdt_sig.Write()
      keras_sig.Write()
      bdt_sig_gen.Write()
      keras_sig_gen.Write()

    elif scores == 'shape_'+ch+'_Top_Hut.root' and ch == 'Hut30':
      tuh = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_Top_Hut.root')
      tbaruh = TFile.Open('/home/minerva1993/fcnc/analysis_jw/tmva/'+tmva_version+'/score_mva/'+ch+'/'+'shape_'+ch+'_AntiTop_Hut.root')

      bdt_sig = tuh.Get('h_scoreBDT_'+ch+'_Top_Hut')
      bdt_sig.Scale(0.0648001216909)
      bdt_scale1 = 1358/bdt_sig.Integral()
      bdt_sig.Scale(bdt_scale1)
      bdt_tbaruh = tbaruh.Get('h_scoreBDT_'+ch+'_AntiTop_Hut')
      bdt_tbaruh.Scale(0.0633035021123)
      bdt_scale2 = 1357.1/bdt_tbaruh.Integral()
      bdt_tbaruh.Scale(bdt_scale2)
      bdt_sig.Add(bdt_sig, bdt_tbaruh, 1.0, 1.0)
      bdt_sig.SetName('bdt_sig')

      keras_sig = tuh.Get('h_scoreKeras_'+ch+'_Top_Hut')
      keras_sig.Scale(0.0648001216909)
      keras_scale1 = 1358/keras_sig.Integral()
      keras_sig.Scale(keras_scale1)
      keras_tbaruh = tbaruh.Get('h_scoreKeras_'+ch+'_AntiTop_Hut')
      keras_tbaruh.Scale(0.0633035021123)
      keras_scale2 = 1357.1/keras_tbaruh.Integral()
      keras_tbaruh.Scale(keras_scale2)
      keras_sig.Add(keras_sig, keras_tbaruh, 1.0, 1.0)
      keras_sig.SetName('keras_sig')

      bdt_sig_gen = tuh.Get('h_scoreBDTGen_'+ch+'_Top_Hut')
      bdt_sig_gen.Scale(0.0648001216909)
      bdt_sig_gen.Scale(bdt_scale1)
      bdt_tbaruh_gen = tbaruh.Get('h_scoreBDTGen_'+ch+'_AntiTop_Hut')
      bdt_tbaruh_gen.Scale(0.0633035021123)
      bdt_tbaruh_gen.Scale(bdt_scale2)
      bdt_sig_gen.Add(bdt_sig_gen, bdt_tbaruh_gen, 1.0, 1.0)
      bdt_sig_gen.SetName('bdt_sig_gen')

      keras_sig_gen = tuh.Get('h_scoreKerasGen_'+ch+'_Top_Hut')
      keras_sig_gen.Scale(0.0648001216909)
      keras_sig_gen.Scale(keras_scale1)
      keras_tbaruh_gen = tbaruh.Get('h_scoreKerasGen_'+ch+'_AntiTop_Hut')
      keras_tbaruh_gen.Scale(0.0633035021123)
      keras_tbaruh_gen.Scale(keras_scale2)
      keras_sig_gen.Add(keras_sig_gen, keras_tbaruh_gen, 1.0, 1.0)
      keras_sig_gen.SetName('keras_sig_gen')

      target.cd()
      bdt_sig.Write()
      keras_sig.Write()
      bdt_sig_gen.Write()
      keras_sig_gen.Write()

    else: continue
    
  target.Close()
