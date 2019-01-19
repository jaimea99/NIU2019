from ROOT import *
import itertools
file = TFile('/xdata/ebrost/tiny/MGPy8_hh_yybb_plus_lambda04.root','READ')
tree = file.Get('mini')
#myfile = TFile('loosejetcut.root','RECREATE')
entries = tree.GetEntries()
hist_jeteta = TH1F('Histogram','Jet Eta',20,-5,5)
hist_jetpt = TH1F('Histogram', 'Jet pt', 200, 0 ,300)
hist_mbb = TH1F('Histogram','Combined Jet Mass', 350, 0,700)
hist_mdiphoton = TH1F('Histogram','Combined Photon Mass', 80,100,180)
hist_leadingjetpt = TH1F('Histogram', 'Leading Jet pt', 200,0,400)
hist_subleadjetpt = TH1F('Histogram', 'Subleading Jet pt', 200, 0 ,200)
hist_leadingphEt = TH1F('hist','Leading Photon pt', 400,0,400)
hist_subleadphEt = TH1F('hist','Subleading Photon pt',400,0,400)
hist_jetnumber = TH1F('hist', 'number of jets', 10,0,10)
hist_leadingjetpt2tag = TH1F('hist','2b leading jet pt',200,0,400)
hist_leadingjetpt1tag1c = TH1F('hsit','1tag1c',200,0,400)
hist_leadingjetpt1tag1o = TH1F('hist','1tag1o',200,0,400)
hist_leadingjetpt1c1o = TH1F('hist','1c1o',200,0,400)
hist_leadingjetpt2o = TH1F('hist','2o',200,0,400)

for i in range(500000): #eventually will loop over entries
    tree.GetEntry(i)
    highestjetpt = 0
    secondjetpt = 0
    highestjetEta = 0
    secondjetEta = 0
    highestphotonpt = 0
    secondphotonpt = 0
    highestphotonEta = 0
    secondphotonEta = 0
    two_photon_pass = False
    two_bjet_pass = False
    ph_vec1 = TLorentzVector()
    ph_vec2 = TLorentzVector()
    jet_vec1 = TLorentzVector()
    jet_vec2 = TLorentzVector()
    jet_vec_comb = TLorentzVector()
    ph_vec_comb = TLorentzVector()
    njets = 0
    firstjetlabel = 0
    secondjetlabel = 0
    jet_tuple = ()

    for k in range(tree.photon_n): #photon selection
        if tree.photon_topoEtcone40[k] < (.05*tree.photon_pt[k]) and tree.photon_ptcone20[k] < (0.065*tree.photon_pt[k]):
            if abs(tree.photon_eta[k]) < 2.37 and (abs(tree.photon_eta[k]) > 1.52 or abs(tree.photon_eta[k]) < 1.37):
                if tree.photon_pt[k] / tree.m_yy > 0.35 and tree.photon_pt[k] > highestphotonpt:
                    highestphotonpt = tree.photon_pt[k]
                    highestphotonEta = tree.photon_eta[k]
                    ph_vec1.SetPtEtaPhiM(tree.photon_pt[k],tree.photon_eta[k],tree.photon_phi[k],0)
                elif tree.photon_pt[k] / tree.m_yy > 0.25 and tree.photon_pt[k] > secondphotonpt:
                    secondphotonpt = tree.photon_pt[k]
                    secondphotonEta = tree.photon_eta[k]
                    ph_vec2.SetPtEtaPhiM(tree.photon_pt[k],tree.photon_eta[k],tree.photon_phi[k],0)
    if highestphotonpt > 0 and secondphotonpt > 0:#checks for two photons
        ph_vec_comb = ph_vec1 + ph_vec2
        if ph_vec_comb.M() >= 105 and ph_vec_comb.M() <= 160:
            two_photon_pass = True

    for j in range(tree.jet_n): #jet selection
        if abs(tree.jet_eta[j]) <= 2.5:
            if tree.jet_pt[j] > 40 and tree.jet_pt[j] > highestjetpt:
                if tree.jet_MV2c10_FixedCutBEff_77[j] == True:#checks if jet is btagged at 77% efficiency level
                    highestjetpt = tree.jet_pt[j]
                    highestjetEta = tree.jet_eta[j]
                    jet_vec1.SetPtEtaPhiM(tree.jet_pt[j],tree.jet_eta[j],tree.jet_phi[j],0)
                    firstjetlabel = tree.jet_label[j]
            elif tree.jet_pt[j] > 25 and tree.jet_pt[j] > secondjetpt:
                if tree.jet_MV2c10_FixedCutBEff_77[j] == True:#checks if btagged at 77% efficiency
                    secondjetpt = tree.jet_pt[j]
                    secondjetEta = tree.jet_eta[j]
                    jet_vec2.SetPtEtaPhiM(tree.jet_pt[j],tree.jet_eta[j],tree.jet_phi[j],0)
                    secondjetlabel = tree.jet_label[j]
    if highestjetpt > 0 and secondjetpt > 0:#checks for two jets
        njets = tree.jet_n
        jet_vec_comb = jet_vec1 + jet_vec2
        if jet_vec_comb.M() >= 85 and jet_vec_comb.M() <= 140:
            two_bjet_pass = True
            jet_tuple = jet_tuple + (str(firstjetlabel),)
            jet_tuple = jet_tuple + (str(secondjetlabel),)

    if two_photon_pass == True and two_bjet_pass == True: #Fill histograms
        if jet_tuple == ('5','5'):
            hist_leadingjetpt2tag.Fill(highestjetpt)
        for set in itertools.combinations('54',2):
            if set == jet_tuple:
                hist_leadingjetpt1tag1c.Fill(highestjetpt)
            else:
                continue
        for set in itertools.combinations('50',2):
            if set == jet_tuple:
                hist_leadingjetpt1tag1o.Fill(highestjetpt)
            else:
                continue
        for set in itertools.combinations('40',2):
            if set == jet_tuple:
                hist_leadingjetpt1c1o.Fill(highestjetpt)
            else:
                continue
        if jet_tuple == ('0','0'):
            hist_leadingjetpt2o.Fill(highestjetpt)


        #hist_jetnumber.Fill(njets)   
        #hist_jeteta.Fill(highestjetEta)
        #hist_jeteta.Fill(secondjetEta)
        #hist_jetpt.Fill(highestjetpt)
        #hist_jetpt.Fill(secondjetpt)
        #hist_mbb.Fill( jet_vec_comb.M() )
        #hist_mdiphoton.Fill(ph_vec_comb.M())
        #hist_leadingphEt.Fill(abs(highestphotonpt))
        #hist_subleadphEt.Fill(abs(secondphotonpt))
        #hist_leadingjetpt.Fill(highestjetpt)
        #hist_subleadjetpt.Fill(secondjetpt)
        
canvas = TCanvas('canvas','canvas',800,600)
canvas.cd()

hist_jeteta.SetXTitle('Eta value for Jets')
hist_jetpt.SetXTitle('Jet pt (GeV)')
hist_mbb.SetXTitle('Di-jet Mass (GeV)')
hist_mdiphoton.SetXTitle('Di-photon Mass (GeV)')
hist_leadingjetpt.SetXTitle('Leading Jet pt (GeV)')
hist_subleadjetpt.SetXTitle('Subleading Jet pt (GeV)')
hist_leadingphEt.SetXTitle('Leading Photon Transverse Energy (GeV)')
hist_subleadphEt.SetXTitle('Subleading Photon Energy (GeV)')
hist_jetnumber.SetXTitle('Number of Jets')
hist_jeteta.SetYTitle('Number of Events')
hist_jetpt.SetYTitle('Number of Events')
hist_mbb.SetYTitle('Number of Events')
hist_mdiphoton.SetYTitle('Number of Events')
hist_leadingjetpt.SetYTitle('Number of Events')
hist_subleadjetpt.SetYTitle('Number of Events')
hist_leadingphEt.SetYTitle('Number of Events')
hist_subleadphEt.SetYTitle('Number of Events')
hist_jetnumber.SetYTitle('Number of Events')

hist_leadingjetpt2tag.Draw()
canvas.Print('2tagleadingpt.pdf')
hist_leadingjetpt1tag1c.Draw()
canvas.Print('1tag1cpt.pdf')
hist_leadingjetpt1tag1o.Draw()
canvas.Print('1tag1opt.pdf')
hist_leadingjetpt1c1o.Draw()
canvas.Print('1c1opt.pdf')
hist_leadingjetpt2o.Draw()
canvas.Print('2opt.pdf')

#hist_jeteta.Draw('hist')
#canvas.Print('jeteta.pdf')
#hist_jeteta.Write()
#hist_jetpt.Draw()
#canvas.Print('Jetpt.pdf')
#hist_jetpt.Write()
#hist_mbb.Draw()
#canvas.Print('mbb.pdf')
#hist_jetpt.Write()
#hist_mdiphoton.Draw()
#canvas.Print('diphotonm.pdf')
#hist_mdiphoton.Write()
#hist_leadingjetpt.Draw()
#canvas.Print('leadjetpt.pdf')
#hist_leadingjetpt.Write()
#hist_subleadjetpt.Draw()
#canvas.Print('subleadjetpt.pdf')
#hist_subleadjetpt.Write()
#hist_leadingphEt.Draw()
#canvas.Print('leadphEt.pdf')
#hist_leadingphEt.Write()
#hist_subleadphEt.Draw()
#canvas.Print('subleadphEt.pdf')
#hist_subleadphEt.Write()
#hist_jetnumber.Draw()
#canvas.Print('jetnum.pdf')
#hist_jetnumber.Write()
