from ROOT import *
import sys
file1 = TFile('~/mypython/final/%s/data/data15.root'%sys.argv[1])
file2 = TFile('~/mypython/final/%s/data/data16.root'%sys.argv[1])
file3 = TFile('~/mypython/final/%s/sherpa/sherpa.root'%sys.argv[1])
histlist = ['bb','bc','bj','cc','cj','jj','data']
myfile = TFile('thstack.root','RECREATE')
titles = ['Leading Jet pt','Subleading Jet pt','Leading Photon pt','Subleading Photon pt','Combined Jet Mass','Combined Photon Mass','Jet Eta','Jet Number','Combined Jet pt','Cosine yybb','Eta between yy and j1','Eta between yy and j2','Eta between b1 and b2','Eta between y1 and y2','Phi between yy and j1','Phi between yy and j2','Phi between b1 and b2','Phi between y1 and y2']

for i in range(1,19):
    ths = THStack('THStack','%s' %(titles[i-1]))
    canvas = TCanvas('c','c',800,600)
    canvas.cd()
    legend = TLegend(0.5,0.5,0.9,0.9)
    legend.SetHeader('Legend Title','C')
    h_d15 = file1.Get('Histogramdata;%i' %i)
    h_d16 = file2.Get('Histogramdata;%i' %i)
    h_data = h_d15 + h_d16
    h_data.Rebin(2)
    h_data.SetMarkerStyle(kFullCircle)
    legend.AddEntry(h_data,'Data')
    for j in range(6):
        h_sherpa = file3.Get('Histogram%s;%i' %(histlist[j],i))
        h_sherpa.Rebin(2)
        #gStyle.SetErrorX(0)
        legend.AddEntry(h_sherpa,'Simulation %s' %histlist[j])
        if histlist[j] == 'bb':
            h_sherpa.SetFillColor(kRed) #gives bb histogram specific color
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
    ths.SetMaximum(50)
    ths.Draw()
    h_data.Draw('p0 same')
    ths.GetXaxis().SetTitle('%s' %titles[i-1])
    ths.GetYaxis().SetTitle('Number of Events')
    legend.Draw()
    canvas.Print('%s.pdf' %titles[i-1])
    canvas.Write('Histogram')#%s' %(histlist[j]))
