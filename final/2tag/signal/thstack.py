#sys.argv[1] == 0tag,1tag,2tag
#sys.arg[2] == old data,data1516,data151617
from ROOT import *
import sys
#execfile('AtlasStyle.py')
if sys.argv[2] == 'old':
    file1 = TFile('~/mypython/final/%s/data/data15.root'%sys.argv[1])
    file2 = TFile('~/mypython/final/%s/data/data16.root'%sys.argv[1])
    file3 = TFile('~/mypython/final/%s/sherpa/sherpa.root'%sys.argv[1])
elif sys.argv[2] == 'd1516':
    file1 = TFile('~/mypython/final/%s/data/data1516.root'%sys.argv[1])
    file3 = TFile('~/mypython/final/%s/sherpa/mc16aSherpa.root'%sys.argv[1])
elif sys.argv[2] =='d151617':
    file1 = TFile('~/mypython/final/%s/data/data1516.root'%sys.argv[1])
    file2 = TFile('~/mypython/final/%s/data/data17.root'%sys.argv[1])
    file3 = TFile('~/mypython/final/%s/sherpa/mc16aSherpaComb.root'%sys.argv[1])
    file4 = TFile('~/mypython/final/%s/sherpa/mc16dSherpa.root'%sys.argv[1])
elif sys.argv[2] == 'signal':
    file3 = TFile('~/mypython/final/2tag/signal/signal.root')

histlist = ['bb','bc','bj','cc','cj','jj']
myfile = TFile('thstack.root','RECREATE')
titles = ['Leading Jet p_{T} (GeV)','Subleading Jet p_{T} (GeV)','Leading Photon p_{T} (GeV)','Subleading Photon p_{T} (GeV)','Combined Jet Mass (GeV)','Combined Photon Mass (GeV)','Jet Eta','Jet Number (Number of Jets)','Combined Jet p_{T} (GeV)','Cosine yybb','Eta between yy and j1','Eta between yy and j2','Eta between j1 and j2','Eta between y1 and y2','Phi between yy and j1','Phi between yy and j2','Phi between j1 and j2','Phi between y1 and y2']
print_titles = ['Leading Jet pT (GeV)','Subleading Jet pT (GeV)','Leading Photon pT (GeV)','Subleading Photon pT (GeV)','Combined Jet Mass (GeV)','Combined Photon Mass (GeV)','Jet Eta','Jet Number (Number of Jets)','Combined Jet pT (GeV)','Cosine yybb','Eta between yy and j1','Eta between yy and j2','Eta between j1 and j2','Eta between y1 and y2','Phi between yy and j1','Phi between yy and j2','Phi between j1 and j2','Phi between y1 and y2']

for i in range(1,19):
    sherpas = []
    ths = THStack()#'THStack','%s %s' %(titles[i-1],sys.argv[1]))
    canvas = TCanvas('c1')
    uPad = TPad('uPad','uPad',0,0.3,1,1)
    dPad = TPad('dPad','dPad',0,0.05,1,0.3)
    #uPad.SetBottomMargin(.1)
    #uPad.SetBorderMode(0)
    #dPad.SetTopMargin(.00001)
    #dPad.SetBottomMargin(.25)
    #dPad.SetBorderMode(0)
    legend = TLegend(0.66,0.6,0.9,0.9)
    #legend = TLegend(0.6,0.6,0.9,0.9)
    #legend.SetTextSize(0.023)
    uPad.Draw()
    dPad.Draw()
    uPad.cd()
    if sys.argv[2] == 'old':
        h_d1 = file1.Get('Histogramdata;%i' %i)
        h_d2 = file2.Get('Histogramdata;%i' %i)
        h_data = h_d1 + h_d2
        h_dataomc = h_data.Clone('h_dataomc')
        SetOwnership(h_dataomc,True)
        legend.SetHeader('Rel 20.7 (%s)'%sys.argv[1])
        legend.AddEntry(h_data,'Data 2015-2016 (36.1 fb^{-1})')
    elif sys.argv[2] == 'd1516':
        h_data = file1.Get('Histogramdata;%i' %i)
        h_dataomc = h_data.Clone('h_dataomc')
        legend.SetHeader('Rel 21 (%s)'%sys.argv[1])
        legend.AddEntry(h_data,'Data 2015-2016 (36.1 fb^{-1})')
    elif sys.argv[2] == 'd151617':
        h_d1 = file1.Get('Histogramdata;%i' %i)
        h_d2 = file2.Get('Histogramdata;%i' %i)
        h_data = h_d1 + h_d2
        h_dataomc = h_data.Clone('h_dataomc')
        legend.SetHeader('Rel 21 (%s)'%sys.argv[1])
        legend.AddEntry(h_data,'Data 2015-2017 (79.8 fb^{-1})')
    elif sys.argv[2] == 'signal':
        h_data = TH1F('h','h',10,0,10)
        h_dataomc = h_data.Clone('h_dataomc')
        legend.SetHeader('Rel 21 (%s)'%sys.argv[1])
        legend.AddEntry(h_data,'Signal')
    h_data.SetMarkerStyle(kFullCircle)
    l = TLatex()
    lp = TLatex()
    l.SetNDC()
    lp.SetNDC()
    l.SetTextColor(1)
    lp.SetTextColor(1)
    #if i <= 5 or i == 9:
    #    h_data.Rebin(2)
    #    h_dataomc.Rebin(2)
    for j in range(6):
        if sys.argv[2] == 'd151617':
            h_shrpa1 = file3.Get('Histogram%s;%i' %(histlist[j],i))
            h_shrpa2 = file4.Get('Histogram%s;%i' %(histlist[j],i))
            h_sherpa = h_shrpa1 + h_shrpa2
        else:
            h_sherpa = file3.Get('Histogram%s;%i' %(histlist[j],i))

        sherpas.append(h_sherpa)
        if i <= 5 or i == 9:
            h_sherpa.Rebin(2)

        if histlist[j] == 'bb':
            h_sherpa.SetFillColor(kRed)
        elif histlist[j] == 'bc':
            h_sherpa.SetFillColor(kBlue)
        elif histlist[j] == 'bj':
            h_sherpa.SetFillColor(78)
        elif histlist[j] == 'cc':
            h_sherpa.SetFillColor(32)
        elif histlist[j] == 'cj':
            h_sherpa.SetFillColor(42)
        elif histlist[j] == 'jj':
            h_sherpa.SetFillColor(53)
        ths.Add(h_sherpa,'H')
    for k in range(6):
        legend.AddEntry(sherpas[5-k],'Sherpa yy+%s' %(histlist[5-k]))

    if i >= 10:
        themax = 1.6*max(h_data.GetMaximum(),ths.GetMaximum())
    else:
        themax = 1.25*max(h_data.GetMaximum(),ths.GetMaximum())
    ths.SetMaximum(themax)
    gStyle.SetOptStat(000000)
    ths.Draw('hist 0')
    h_data.Draw('EP same')

#ths.GetHistogram().GetXaxis().SetTitle('%s' %titles[i-1])
    ths.GetYaxis().SetTitle('Number of Events')
    legend.Draw()
    l.DrawLatex(0.71,0.55,'ATLAS')
    lp.DrawLatex(0.8,0.55,'Internal')
    #canvas.Write('THStack')#############
    #canvas.Print('THStack %s'%print_titles[i-1])##########
    #NEW CODE BEGIN
    dPad.cd()
#    ATLASLabel(0.56, 0.88, "Internal", 1)
    h_fullMC = ths.GetStack().Last()
    h_dataomc.Divide(h_fullMC)
    h_dataomc.SetMarkerStyle(20)
    h_dataomc.Draw("ep")
    h_dataomc.SetTitle("")
    tl = TLine(h_dataomc.GetXaxis().GetXmin(),1,h_dataomc.GetXaxis().GetXmax(),1)
    tl.SetLineWidth(1)
    tl.Draw()
    #      // Y axis ratio plot settings
    h_dataomc.GetYaxis().SetTitle(" Data/MC ")
    h_dataomc.GetYaxis().SetNdivisions(505)
    h_dataomc.GetYaxis().SetTitleSize(.1)
    h_dataomc.GetYaxis().SetTitleOffset(.5)
    h_dataomc.GetYaxis().SetLabelFont(43)
    h_dataomc.GetYaxis().SetLabelSize(15)
    #h_dataomc.GetYaxis().SetRangeUser(0.,2.)
  #  // X axis ratio plot settings
    #h_dataomc.GetXaxis().SetLabelSize(60)
    canvas.cd()
    xl = TLatex()
    xl.SetNDC()
    xl.SetTextColor(1)
    xl.SetTextSize(15)
    xl.SetTextFont(43)
    if i == 7 or i == 10:
        xl.DrawLatex(0.8,0.02,'%s'%titles[i-1])
    else:
        xl.DrawLatex(0.7,0.02,'%s'%titles[i-1])
    
    #h_dataomc.GetXaxis().SetTitle('%s'%titles[i-1])
    #h_dataomc.GetXaxis().SetTitleSize(.1)
    h_dataomc.GetXaxis().SetTitleOffset(1.2)
    h_dataomc.GetXaxis().SetLabelFont(43)
    h_dataomc.GetXaxis().SetLabelSize(15)
    canvas.Write('THStack')
    canvas.Print('DataoMC %s.pdf'%print_titles[i-1])
    canvas.Print('DataoMC %s.png'%print_titles[i-1])
