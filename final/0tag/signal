#sys.argv[1] == input
#sys.argv[2] == output
#sys.argv[3] == 0tag,1tag,2tag
#sys.argv[4] == only necessary for mc16a, specific "combined," to adjust weight
from ROOT import *
import sys
from math import *
file = TFile('/xdata/ebrost/tiny/%s'%sys.argv[1],'READ')
tree = file.Get('mini')
myfile = TFile('%s'%sys.argv[2],'RECREATE')
entries = tree.GetEntries() #/ 20
    
def MakeHists(name,title,nbin,low,high):
    hists = []
    histbb = TH1F(name+'bb',title+'bb',nbin,low,high)
    histbc = TH1F(name+'bc',title+'bc',nbin,low,high)
    histbj = TH1F(name+'bj',title+'bj',nbin,low,high)
    histcc = TH1F(name +'cc',title+'cc',nbin,low,high)
    histcj = TH1F(name+'cj',title+'cj',nbin,low,high)
    histjj = TH1F(name+'jj',title+'jj',nbin,low,high)
    histdata = TH1F(name+'data',title+'data',nbin,low,high)
    hists.append(histbb)
    hists.append(histbc)
    hists.append(histbj)
    hists.append(histcc)
    hists.append(histcj)
    hists.append(histjj)
    hists.append(histdata)
    return hists

hist_leadingjets = MakeHists('Histogram','Leading Jet pt', 40,0,200)
hist_subleadjets = MakeHists('Histogram','Subleading Jet pt', 20,0,100)
hist_leadingphs = MakeHists('Histogram','Leading Photon pt',40,0,200)
hist_subleadphs = MakeHists('Histogram','Subleading Photon pt',20,0,100)
hist_mjets = MakeHists('Histogram','Combined Jet Mass',18,70,160)
hist_mdiphs = MakeHists('Histogram','Combined Photon Mass',22,105,160)
hist_jeteta = MakeHists('Histogram','Jet Eta',10,-5,5)
hist_jetnum = MakeHists('Histogram','Jet Number',10,0,10)
hist_jetspt = MakeHists('Histogram','Combined Jet pt',40,0,200)
hist_cosyybb = MakeHists('Histogram','Cosine yybb',10,-1,1)
hist_yyj1Eta = MakeHists('Histogram','yyj1_Eta',16,-8,8)
hist_yyj2Eta = MakeHists('Histogram','yyj2_Eta',16,-8,8)
hist_b1b2Eta = MakeHists('Histogram','b1b2_Eta',16,-8,8)
hist_y1y2Eta = MakeHists('Histogram','y1y2_eta',16,-8,8)
hist_yyj1Phi = MakeHists('Histogram','yyj1_Phi',4,0,4)
hist_yyj2Phi = MakeHists('Histogram','yyj2_Phi',4,0,4)
hist_b1b2Phi = MakeHists('Histogram','b1b2_Phi',4,0,4)
hist_y1y2Phi = MakeHists('Histogram','y1y2_Phi',4,0,4)

def FillHist(hists,val,weight,jtype):
    if (jtype == 'data'):
        hists[6].Fill(val,weight)
    elif (jtype =='bb'):
        hists[0].Fill(val,weight)
    elif (jtype =='bc'):
        hists[1].Fill(val,weight)
    elif (jtype == 'bj'):
        hists[2].Fill(val,weight)
    elif (jtype == 'cc'):
        hists[3].Fill(val,weight)
    elif (jtype == 'cj'):
        hists[4].Fill(val,weight)
    elif (jtype == 'jj'):
        hists[5].Fill(val,weight)

for i in range(entries): #eventually will loop over entries
    tree.GetEntry(i)
    if tree.hgam_isPassed == 0:
        continue
    if tree.jet_n < 2:
        continue

    weight = None
    if sys.argv[1] == 'data15.root' or sys.argv[1] == 'data16.root' or sys.argv[1] == 'h021/data1516.root' or sys.argv[1] == 'h021/data17.root':
        weight = 1
    elif sys.argv[1] == 'sherpa_loose.root':
        weight = tree.hgam_weight * tree.yybb_low_weight * 0.005338
    elif sys.argv[1] == 'h021/Sherpa2_myy_90_175_mc16a.root':
        try:
            if sys.argv[4] == 'combined':
                weight = tree.hgam_weight * tree.yybb_low_weight * 0.0178421#data15-17
        except IndexError:#only use for data1516.root
            weight = tree.hgam_weight * tree.yybb_low_weight * 0.01786#data1516
    elif sys.argv[1] == 'h021/Sherpa2_myy_90_175_mc16d.root':
        weight = tree.hgam_weight * tree.yybb_low_weight * 0.017264#data15-17
        #try:
            #if sys.argv[3] == 'combined':
                #weight = 0.0094757
        #exept IndexError: #not used
         #   weight = 0.01728567


    highestjetpt = None
    secondjetpt = None
    highestjetEta = None
    secondjetEta = None
    highestphotonpt = None
    secondphotonpt = None
    highestphotonEta = None
    secondphotonEta = None
    two_photon_pass = None
    two_bjet_pass = None
    ph_vec1 = TLorentzVector()
    ph_vec2 = TLorentzVector()
    jet_vec1 = TLorentzVector()
    jet_vec2 = TLorentzVector()
    jet_vec_comb = TLorentzVector()
    ph_vec_comb = TLorentzVector()
    njets = None
    jet_tuple = ()
    jet1_tup = None
    jet2_tup = None
    label = ''
    njets = None
    phTruth1 = None
    phTruth2 = None
    jetlab1 = None
    jetlab2 = None
    jetphi1 = None
    jetphi2 = None
    jetpass1 = None
    jetpass2 = None

    for k in range(tree.photon_n): #photon selection
        if tree.photon_iso_Loose[k] == 1 and tree.photon_isTight[k] == 1:
            if tree.photon_pt[k] > highestphotonpt:
                if highestphotonpt > secondphotonpt:
                        secondphotonpt = highestphotonpt
                        secondphotonEta = highestphotonEta
                        ph_vec2 = ph_vec1
                highestphotonpt = tree.photon_pt[k]
                highestphotonEta = tree.photon_eta[k]
                ph_vec1.SetPtEtaPhiM(tree.photon_pt[k],tree.photon_eta[k],tree.photon_phi[k],0)   
            elif tree.photon_pt[k] > secondphotonpt:
                secondphotonpt = tree.photon_pt[k]
                secondphotonEta = tree.photon_eta[k]
                ph_vec2.SetPtEtaPhiM(tree.photon_pt[k],tree.photon_eta[k],tree.photon_phi[k],0)
    if ((highestphotonpt is not None) and (secondphotonpt is not None)):#checks for two photons
        ph_vec_comb = ph_vec1 + ph_vec2
        if (sys.argv[3] == '2tag') or (sys.argv[3] == '1tag'):
            if ((ph_vec_comb.M() >= 105) and (ph_vec_comb.M() <= 120)) or ((ph_vec_comb.M() >= 130) and (ph_vec_comb.M() <= 160)):
                two_photon_pass = True
        elif sys.argv[3] == '0tag':
            if (ph_vec_comb.M() >= 105) and (ph_vec_comb.M() <= 160):
                two_photon_pass = True

    for j in range(tree.jet_n): #jet selection        
        if abs(tree.jet_eta[j]) <= 2.5:
            if (((tree.jet_pt[j] > 40) and (tree.jet_pt[j] > highestjetpt))):
                    if highestjetpt > secondjetpt:
                        secondjetpt = highestjetpt
                        secondjetEta = highestjetEta
                        jetphi2 = jetphi1
                        jet_vec2 = jet_vec1
                        jetpass2 = jetpass1
                    highestjetpt = tree.jet_pt[j]
                    highestjetEta = tree.jet_eta[j]
                    jetphi1 = tree.jet_phi[j]
                    jet_vec1.SetPtEtaPhiM(tree.jet_pt[j],tree.jet_eta[j],tree.jet_phi[j],0)
                    jetpass1 = tree.jet_MV2c10_FixedCutBEff_70[j]
                    try:#corrects for the absence of jet_label in data
                        jet1_tup = str(tree.jet_label[j])
                    except:
                        continue
            elif ((tree.jet_pt[j] > 25) and (tree.jet_pt[j] > secondjetpt)):
                    secondjetpt = tree.jet_pt[j]
                    secondjetEta = tree.jet_eta[j]
                    jet_vec2.SetPtEtaPhiM(tree.jet_pt[j],tree.jet_eta[j],tree.jet_phi[j],0)
                    jetphi2 = tree.jet_phi[j]
                    jetpass2 = tree.jet_MV2c10_FixedCutBEff_70[j]
                    try:
                        jet2_tup = str(tree.jet_label[j])
                    except:
                        continue

    if (sys.argv[3] == '2tag' and jetpass1 == True and jetpass2 == True) or (sys.argv[3] =='1tag' and ((jetpass1 == True and jetpass2 == False) or (jetpass1 == False and jetpass2 == True))) or (sys.argv[3] == '0tag' and jetpass1 == False and jetpass2 == False):
            if ((highestjetpt is not None) and (secondjetpt is not None)):#checks for two jets
                njets = tree.jet_n
                jet_vec_minus = jet_vec1 - jet_vec2
                yyj1_dEta = ph_vec_comb.Eta() - jet_vec1.Eta() 
                yyj2_dEta = ph_vec_comb.Eta() - jet_vec2.Eta()  
                b1b2_dEta = jet_vec1.Eta() - jet_vec2.Eta() 
                y1y2_dEta = ph_vec1.Eta() - ph_vec2.Eta() 

                yyj1_dPhi = abs(ph_vec_comb.Phi() - jet_vec1.Phi()) 
                yyj2_dPhi = abs(ph_vec_comb.Phi() - jet_vec2.Phi()) 
                b1b2_dPhi = abs(jet_vec1.Phi() - jet_vec2.Phi()) 
                y1y2_dPhi = abs(ph_vec1.Phi() - ph_vec2.Phi()) 
                while yyj1_dPhi  > pi:
                    yyj1_dPhi -= pi
                while yyj2_dPhi > pi:
                    yyj2_dPhi -= pi
                while b1b2_dPhi > pi:
                    b1b2_dPhi -= pi
                while y1y2_dPhi > pi:
                    y1y2_dPhi -= pi

                jet_vec_comb = jet_vec1 + jet_vec2
            
                vZ = ph_vec1 + ph_vec2
                vH = ph_vec_comb + jet_vec_comb

                boost = -vH.BoostVector()
                vH.Boost(boost)
                vZ.Boost(boost)

                q = TLorentzVector()
                qbar = TLorentzVector()
                q.SetPxPyPzE(0,0,vH.M()/2,vH.M()/2)
                qbar.SetPxPyPzE(0,0,-vH.M()/2,vH.M()/2)

                try:##corrects any division by 0 error
                    cos_yybb = (q-qbar).Dot(vZ) / (vH.M() * vZ.P())
                except:
                    continue

                if ((jet_vec_comb.M() >= 85) and (jet_vec_comb.M() <= 140)):
                    two_bjet_pass = True
                    jet_tuple = jet_tuple + (jet1_tup,)
                    jet_tuple = jet_tuple + (jet2_tup,)
          
    if ((two_photon_pass == True) and (two_bjet_pass == True)): #Fill histograms
        if sys.argv[1] == 'data15.root' or sys.argv[1] == 'data16.root' or sys.argv[1] == 'h021/data1516.root' or sys.argv[1] == 'h021/data17.root':
            label = 'data'
        elif (jet_tuple == ('5','4') or jet_tuple == ('4','5')):
            label = 'bc'
        elif (jet_tuple == ('5','0') or jet_tuple == ('0','5')):
            label = 'bj'
        elif (jet_tuple == ('4','0') or jet_tuple == ('0','4')):
            label = 'cj'
        elif (jet_tuple == ('4','4')):
            label = 'cc'
        elif (jet_tuple == ('0','0')):
            label = 'jj'
        elif (jet_tuple == ('5','5')):
            label = 'bb'
    
        FillHist(hist_leadingjets,highestjetpt,weight,label)
        FillHist(hist_subleadjets,secondjetpt,weight,label)
        FillHist(hist_leadingphs,highestphotonpt,weight,label)
        FillHist(hist_subleadphs,secondphotonpt,weight,label)
        FillHist(hist_mjets,jet_vec_comb.M(),weight,label)
        FillHist(hist_mdiphs,ph_vec_comb.M(),weight,label)
        FillHist(hist_jeteta,highestjetEta,weight,label)
        FillHist(hist_jeteta,secondjetEta,weight,label)
        FillHist(hist_jetnum,njets,weight,label)
        FillHist(hist_jetspt,highestjetpt,weight,label)
        FillHist(hist_jetspt,secondjetpt,weight,label)
        FillHist(hist_cosyybb,cos_yybb,weight,label)
        FillHist(hist_yyj1Eta,yyj1_dEta,weight,label)
        FillHist(hist_yyj2Eta,yyj2_dEta,weight,label)
        FillHist(hist_b1b2Eta,b1b2_dEta,weight,label)
        FillHist(hist_y1y2Eta,y1y2_dEta,weight,label)
        FillHist(hist_yyj1Phi,yyj2_dPhi,weight,label)
        FillHist(hist_yyj2Phi,yyj2_dPhi,weight,label)
        FillHist(hist_b1b2Phi,b1b2_dPhi,weight,label)
        FillHist(hist_y1y2Phi,y1y2_dPhi,weight,label)
        print('filled %s. Entry %i out of %i.' %(label,i,entries))
        print(weight)
canvas = TCanvas('canvas','canvas',800,600)
canvas.cd()

for i in range(7):
    hist_leadingjets[i].Write()
    hist_subleadjets[i].Write()
    hist_leadingphs[i].Write()
    hist_subleadphs[i].Write()
    hist_mjets[i].Write()
    hist_mdiphs[i].Write()
    hist_jeteta[i].Write()
    hist_jetnum[i].Write()
    hist_jetspt[i].Write()
    hist_cosyybb[i].Write()
    hist_yyj1Eta[i].Write()
    hist_yyj2Eta[i].Write()
    hist_b1b2Eta[i].Write()
    hist_y1y2Eta[i].Write()
    hist_yyj1Phi[i].Write()
    hist_yyj2Phi[i].Write()
    hist_b1b2Phi[i].Write()
    hist_y1y2Phi[i].Write()
