#credit to Tyler Burch (NIU) for this code
#https://gitlab.com/tjburch/bbyy_analysis/blob/master/backgroundComposition/plottingCode/AtlasStyle.py
from ROOT import *

def AtlasStyle():

    atlasStyle= TStyle("ATLAS","Atlas style")
    
    icol = 0

    atlasStyle.SetFrameBorderMode(icol)
    atlasStyle.SetCanvasBorderMode(icol)
    atlasStyle.SetPadBorderMode(icol)
    atlasStyle.SetPadColor(icol)
    atlasStyle.SetCanvasColor(icol)
    atlasStyle.SetStatColor(icol)

    atlasStyle.SetPaperSize(20,26)
    atlasStyle.SetPadTopMargin(0.05)
    atlasStyle.SetPadRightMargin(0.05)
    atlasStyle.SetPadBottomMargin(0.16)
    atlasStyle.SetPadLeftMargin(0.12)

    font=42
    tsize=0.05
    atlasStyle.SetTextFont(font)

    atlasStyle.SetTextSize(tsize)
    atlasStyle.SetLabelFont(font,"x")
    atlasStyle.SetTitleFont(font,"x")
    atlasStyle.SetLabelFont(font,"y")
    atlasStyle.SetTitleFont(font,"y")
    atlasStyle.SetLabelFont(font,"z")
    atlasStyle.SetTitleFont(font,"z")

    atlasStyle.SetLabelSize(tsize,"x")
    atlasStyle.SetTitleSize(tsize,"x")
    atlasStyle.SetLabelSize(tsize,"y")
    atlasStyle.SetTitleSize(tsize,"y")
    atlasStyle.SetLabelSize(tsize,"z")
    atlasStyle.SetTitleSize(tsize,"z")

    atlasStyle.SetLabelOffset(tsize/4,"x")
    atlasStyle.SetLabelOffset(tsize/4,"y")


    atlasStyle.SetMarkerStyle(20)
    atlasStyle.SetMarkerSize(1.2)
    atlasStyle.SetHistLineWidth(2)
    atlasStyle.SetLineStyleString(2,"[12 12]")

    atlasStyle.SetOptTitle(0)
    atlasStyle.SetOptStat(0)
    atlasStyle.SetOptFit(0)

    atlasStyle.SetPadTickX(1)
    atlasStyle.SetPadTickY(1)

    gROOT.SetStyle("Plain")

    gROOT.SetStyle("ATLAS")
    gROOT.ForceStyle()



def ATLASLabel(x, y, text, color):
  tsize=0.035
  tlx = TLatex()
  tlx.SetTextSize(tsize)
  tlx.SetNDC()
  tlx.SetTextFont(72)
  tlx.SetTextColor(color)
  delx = 0.1
     
  tlx.DrawLatex(x,y,"ATLAS")
  
  if (text):
      p = TLatex()
      p.SetNDC()
      p.SetTextSize(tsize)
      p.SetTextFont(42)
      p.SetTextColor(color)
      p.DrawLatex(x+delx,y,text)
  
def myLabel(x, y, color, text):    
    tsize=0.035
    tlx = TLatex()
    tlx.SetTextSize(tsize)
    tlx.SetNDC()
    tlx.SetTextColor(color)
    tlx.DrawLatex(x,y,text)

