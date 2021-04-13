# -*- coding: utf-8 -*-



"""
###################################
Created on Fri Apr 10 09:24:17 2020
@author: SAV-MR
###################################
"""

"""
import time
from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, textvariable=var,anchor="center", relief=RAISED, fg="white", bg="black", padx="3", pady="3", width="35",height="5",font="Castellar 25")
var.set("Welcome to 'Def Control' JEOL Script")
label.pack()
#root.mainloop()
#root.geometry(newGeometry="TOP")
root.mainloop()
time.sleep(0.5)
root.quit()
#root.destroy()
"""


import sys
import time
from PyQt4 import  QtGui, uic
#from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyJEM import TEM3
#from PyJEM import TEM3

MDS=TEM3.MDS3()
eos = TEM3.EOS3()
BB=TEM3.Def3()
lens=TEM3.Lens3()
HV = TEM3.HT3()
A=lens.GetCL3
#A=45000 #FOR TEST


CLA1=BB.GetCLA1()
IS1=BB.GetIS1()
print(CLA1)
print(IS1)
#CLA1=[32000 ,32000]  #FOR TEST
#IS1=[34000 ,34000]   #FOR TEST
CLA1X=CLA1[0]
print("x:",CLA1X)
CLA1Y=CLA1[1]
print ("y:",CLA1Y)
IS1X=IS1[0]
IS1Y=IS1[1]
print (IS1X,IS1Y,CLA1X,CLA1Y)


qtCreatorFile =  "Def Control.ui" # Enter Graphic ui file name here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Deflector Control")
        
        """
        arrows        
        """
        self.plus.clicked.connect(self.up)
        self.moins.clicked.connect(self.down)
        #QtGui.QToolButton.clicked.connect
        
        """
        ------------------------------
        #combo boxes get change value
        ------------------------------
        """
        self.comboBox1.currentIndexChanged.connect(self.Spot)
        self.comboBox2.currentIndexChanged.connect(self.Alpha)
        """
        -----------------------------
        #radioButtons select detect
        -----------------------------
        """
        func=eos.GetMagValue()
        
        unit=func[1]
        print(unit)
        u2=func[2]
        print(u2)
        func=str(func[0])
        print(func)
        self.Func.setText(u2)
        
        self.radioButtonGUNS.clicked.connect(self.GUNS)
        self.radioButtonGUNT.clicked.connect(self.GUNT)
        self.radioButtonSPOTA.clicked.connect(self.SPOTA)
        self.radioButtonBS.clicked.connect(self.BS)
        self.radioButtonBT.clicked.connect(self.BT)
        self.radioButtonCLS.clicked.connect(self.CLS)
        self.radioButtonOLS.clicked.connect(self.OLS)
        self.radioButtonIS1.clicked.connect(self.IS1)
        self.radioButtonIS2.clicked.connect(self.IS2)
        self.radioButtonILS.clicked.connect(self.ILS)
        self.radioButtonPLA.clicked.connect(self.PLA)
        self.radioButtonCOMPS.clicked.connect(self.CLCOMPS)
        self.radioButtonCOMPT.clicked.connect(self.CLCOMPT)
        self.radioButtonCOMPA.clicked.connect(self.CLCOMPA)
        """
        ------------------------------
        # PushButtons Functions
        ------------------------------
        """
        self.Mag.clicked.connect(self.MAG)
        self.Diff.clicked.connect(self.Dif)
        self.Lmag.clicked.connect(self.LMag)
        """
        -----------------------------
        #CL3 slider change value detect
        -----------------------------
        """
        self.horizontalSlider.sliderMoved.connect(self.Bright)
        self.horizontalSlider.valueChanged.connect(self.Bright)
        
        CL3=lens.GetCL3()
        time.sleep(1)
        CL3=lens.GetCL3()
        time.sleep(1)
        CL3=lens.GetCL3()
        time.sleep(1)
        print("CL3=",CL3)
        #CL3=[45000]  #FOR TEST
        #CL3=CL3[0]
        CL3=int(CL3)
        print(type(CL3))
        print("cl3:",CL3)
        self.CL3value.setText(str(hex(CL3)).upper()[2:])
        
        
        A=lens.GetCL3()
        #A=45000  #for test
        #type(A)
        print(A)
        #self.horizontalSlider.sliderPosition(A)
        #self.horizontalSlider.setSliderPosition(A)
        C=self.horizontalSlider.sliderPosition()
        #print (type(C))
        #print(C)
        R=C
        print(R)
        self.CL3value.setText(str(hex(R)).upper()[2:])        
        
        
        """
        ---------------------------------
        #self.horizontalSlider.setCursor(32000)  #for test
        ---------------------------------
        """
        #self.horizontalSlider.setTickPosition(2)
        self.horizontalSlider.setSliderPosition(CL3)
        
        #self.dial1.sliderMoved.connect(self.x)
        #self.dial2.sliderMoved.connect(self.y)
        
        """
        ---------------------------------
        #cHECK BOX COARSE FINE  
        ---------------------------------
        """
        self.Coarse.clicked.connect(self.Step) 
        self.CF.clicked.connect(self.Step)
        
        
        self.ScrollBar1.sliderMoved.connect(self.x)
        self.ScrollBar1.valueChanged.connect(self.x)
        self.ScrollBar2.sliderMoved.connect(self.y)
        self.ScrollBar2.valueChanged.connect(self.y)
        """
        ----------------------------
        #Get values from Microscope 
        ----------------------------
        """
        Gun1=BB.GetGunA1()
        Gun2=BB.GetGunA2()
        Spot=BB.GetSpotA()
        CLStig=BB.GetCLs()
        Cla1=BB.GetCLA1()
        Cla2=BB.GetCLA2()
        Ols=BB.GetOLs()
        Is1=BB.GetIS1()
        Is2=BB.GetIS2()
        Ils=BB.GetILs()
        Pla=BB.GetPLA()
        ClacompS=BB.GetShifBal()
        ClacompT=BB.GetTiltBal()
        ClacompA=BB.GetAngBal()
        
        AL=eos.GetAlpha()
        time.sleep(1)
        AL=eos.GetAlpha()
        time.sleep(1)
        AL=eos.GetAlpha()
        time.sleep(1)
        print("AL=",AL)
        self.comboBox2.setCurrentIndex(AL)
        #QtGui.QComboBox.setCurrentIndex
        SP=eos.GetSpotSize()
        time.sleep(1)
        SP=eos.GetSpotSize()
        time.sleep(1)
        SP=eos.GetSpotSize()
        time.sleep(1)
        print("SP=",SP)
        self.comboBox1.setCurrentIndex(SP)
        """
        ------------------------------------
        #Set values for testing offline only
        ------------------------------------
        
        ""Gun1=[30000 ,34000] #FOR TEST
        Gun2=[33000 ,33100]  #FOR TEST
        Spot=[32700 ,32730]  #FOR TEST
        Cla1=[32020 ,32000]  #FOR TEST
        Cla2=[32050 ,38000]  #FOR TEST
        Spot=[31010 ,31000]  #FOR TEST
        CLStig=[32501 ,32500]  #FOR TEST
        Ols=[32801 ,32810]  #FOR TEST
        Is1=[34000 ,34001]   #FOR TEST
        Is2=[32768 ,32767]  #FOR TEST
        Ils=[36768 ,40767]  #FOR TEST
        Pla=[32766 ,32757]  #FOR TEST
        ClacompS=[32766 ,32757]  #FOR TEST
        ClacompT=[22501 ,22550] #FOR TEST
        ClacompA=[32866 ,32877]  #FOR TEST
        """
        """
        %%%%%%%%%%%%%%%%%%%%%%%%
        #Get indivudually X & Y
        %%%%%%%%%%%%%%%%%%%%%%%%
        """
        GUN1X=int(str(Gun1[0]))
        GUN1Y=int(str(Gun1[1]))
        GUN2X=int(str(Gun2[0]))
        GUN2Y=int(str(Gun2[1]))
        CLSX=int(str(CLStig[0]))
        CLSY=int(str(CLStig[1]))
        CLA1X=int(str(Cla1[0]))
        CLA1Y=int(str(Cla1[1]))
        CLA2X=int(str(Cla2[0]))
        CLA2Y=int(str(Cla2[1]))
        SPOTX=int(str(Spot[0]))
        SPOTY=int(str(Spot[1]))
        CLSX=int(str(CLStig[0]))
        CLSY=int(str(CLStig[1]))
        OLSX=int(str(Ols[0]))
        OLSY=int(str(Ols[1]))
        IS1X=int(str(Is1[0]))
        IS1Y=int(str(Is1[1]))
        IS2X=int(str(Is2[0]))
        IS2Y=int(str(Is2[1]))
        ILSX=int(str(Ils[0]))        
        ILSY=int(str(Ils[1]))
        PLAX=int(str(Pla[0]))
        PLAY=int(str(Pla[1]))
        CLACSX=int(str(ClacompS[0]))
        CLACSY=int(str(ClacompS[1]))
        CLACTX=int(str(ClacompT[0]))
        CLACTY=int(str(ClacompT[1]))
        CLACAX=int(str(ClacompA[0]))
        CLACAY=int(str(ClacompA[1]))
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #Writes values in Text Boxes in Hex value
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.GUN1X.setText(str(hex(GUN1X)).upper()[2:])
        self.GUN1Y.setText(str(hex(GUN1Y)).upper()[2:])
        self.GUN2X.setText(str(hex(GUN2X)).upper()[2:])
        self.GUN2Y.setText(str(hex(GUN2Y)).upper()[2:])
        
        self.xvalue.setText(str(hex(CLA1X)).upper()[2:])
        self.yvalue.setText(str(hex(CLA1Y)).upper()[2:])
        
        self.BSX.setText(str(hex(CLA1X)).upper()[2:])
        self.BSY.setText(str(hex(CLA1Y)).upper()[2:])
        self.BTX.setText(str(hex(CLA2X)).upper()[2:])
        self.BTY.setText(str(hex(CLA2Y)).upper()[2:])
        
        self.SPOTX.setText(str(hex(SPOTX)).upper()[2:])
        self.SPOTY.setText(str(hex(SPOTY)).upper()[2:])
        
        self.CLSX.setText(str(hex(CLSX)).upper()[2:])
        self.CLSY.setText(str(hex(CLSY)).upper()[2:])       
        
        self.OLSX.setText(str(hex(OLSX)).upper()[2:])
        self.OLSY.setText(str(hex(OLSY)).upper()[2:]) 
        
        self.IS1X.setText(str(hex(IS1X)).upper()[2:])
        self.IS1Y.setText(str(hex(IS1Y)).upper()[2:]) 
        self.IS2X.setText(str(hex(IS2X)).upper()[2:])
        self.IS2Y.setText(str(hex(IS2Y)).upper()[2:]) 
        
        self.ILSX.setText(str(hex(ILSX)).upper()[2:])
        self.ILSY.setText(str(hex(ILSY)).upper()[2:]) 
        
        self.PLAX.setText(str(hex(PLAX)).upper()[2:])
        self.PLAY.setText(str(hex(PLAY)).upper()[2:]) 
        
        self.CLSHIFTX.setText(str(hex(CLACSX)).upper()[2:]) 
        self.CLSHIFTY.setText(str(hex(CLACSY)).upper()[2:]) 
        self.CLTILTX.setText(str(hex(CLACTX)).upper()[2:]) 
        self.CLTILTY.setText(str(hex(CLACTY)).upper()[2:]) 
        self.CLANGLEX.setText(str(hex(CLACAX)).upper()[2:]) 
        self.CLANGLEY.setText(str(hex(CLACAY)).upper()[2:]) 
        
        """
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #Set Scrollbar to CLA1 values (default for start)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        #self.ScrollBar1.setSliderPosition(CLA1X)
        #self.ScrollBar2.setSliderPosition(CLA1Y)
        print(type(CLA1X))
        #print (IS1X,IS1Y,CLA1X,CLA1Y)
        self.textEdit.setText("Beam Shift")
        #QtGui.QSpinBox.setValue()
        
    """
    wwwwwwwwwwwwwwwwwwwwwwwww
    Coarse / Fine Step detect
    wwwwwwwwwwwwwwwwwwwwwwwww
    """    
    
    def up(self):
        print("up")
        eos.UpSelector()
        func=eos.GetMagValue()
        unit=func[1]
        u2=func[2]
        print(u2)
        self.Func.setText(u2)
        
        #QtGui.QSpinBox.UpDownArrows()
        
            
    def down(self):
        print("down")
        eos.DownSelector()
        func=eos.GetMagValue()
        unit=func[1]
        u2=func[2]
        self.Func.setText(u2)
        
    def Step(self):
        #Check Button
        if (self.Coarse.isChecked()==True):
            self.ScrollBar1.setSingleStep(20)
            self.ScrollBar1.setPageStep(100)
            self.ScrollBar2.setSingleStep(20)
            self.ScrollBar2.setPageStep(100)
        if (self.Coarse.isChecked()==False):
            self.ScrollBar1.setSingleStep(1)
            self.ScrollBar1.setPageStep(16)
            self.ScrollBar2.setSingleStep(1)
            self.ScrollBar2.setPageStep(16)
            
        #Tool Button
        if (self.CF.isChecked()==True):
            self.label_8.setText("Coarse")
            self.ScrollBar1.setSingleStep(20)
            self.ScrollBar1.setPageStep(100)
            self.ScrollBar2.setSingleStep(20)
            self.ScrollBar2.setPageStep(100)
            print("Coarse")
        if (self.CF.isChecked()==False):
            self.label_8.setText("Fine")
            self.ScrollBar1.setSingleStep(1)
            self.ScrollBar1.setPageStep(16)
            self.ScrollBar2.setSingleStep(1)
            self.ScrollBar2.setPageStep(16)
            print("Fine")
            
        
                
                
        
        """
    # Control of Sliders for Def x and Def Y    
        ____________________________________
        """
        
    def x(self):
        
        GUNS=self.radioButtonGUNS.isChecked()
        GUNT=self.radioButtonGUNT.isChecked()
        SPOTA=self.radioButtonSPOTA.isChecked()
        BS=self.radioButtonBS.isChecked()
        BT=self.radioButtonBT.isChecked()
        CLS=self.radioButtonCLS.isChecked()
        Ols=self.radioButtonOLS.isChecked()
        IS1=self.radioButtonIS1.isChecked()
        IS2=self.radioButtonIS2.isChecked()
        ILS=self.radioButtonILS.isChecked()
        PLA=self.radioButtonPLA.isChecked()
        CLCS=self.radioButtonCOMPS.isChecked()
        CLCT=self.radioButtonCOMPT.isChecked()
        CLCA=self.radioButtonCOMPA.isChecked()
        
        #D=self.dial1.SliderOrientationChange.
        #print(D)
        
        if (GUNS==True):
            self.tabWidget.setCurrentIndex(0)
            GUN1=BB.GetGunA1()
            GUN1X=int(str(GUN1[0]))
            GUN1Y=int(str(GUN1[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("Gun Shift")
            print(GUN1X)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.GUN1X.setText(str(hex(R)).upper()[2:])
            BB.SetCLA1(R,GUN1Y)
            
        if (GUNT==True):
            self.tabWidget.setCurrentIndex(0)
            GUN2=BB.GetGunA2()
            GUN2X=int(str(GUN2[0]))
            GUN2Y=int(str(GUN2[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("Gun Tilt")
            print(GUN2X)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.GUN2X.setText(str(hex(R)).upper()[2:])
            BB.SetGunA2(R,GUN2Y)
            
        if (SPOTA==True):
            self.tabWidget.setCurrentIndex(0)
            SPOT=BB.GetSpotA()
            SPOTX=int(str(SPOT[0]))
            SPOTY=int(str(SPOT[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("Spot Align")
            print(SPOTX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.SPOTX.setText(str(hex(R)).upper()[2:])
            BB.SetSpotA(R,SPOTY)  #see if SetSpotA available online
            """
            D=BB.spa.bit_length()
            E=BB.spa.conjugate()
            F=BB.spa.to_bytes(4,"big")
            """
            #print(D,"  ",E,"  ",F)
            
        if(CLS==True):
            self.tabWidget.setCurrentIndex(0)
            CLS=BB.GetCLs()
            CLSX=int(str(CLS[0]))
            CLSY=int(str(CLS[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("Cond Stig")
            print(CLSX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.CLSX.setText(str(hex(R)).upper()[2:])        
            BB.SetCLs(R,CLSY)
            
        if (BS==True):
            self.tabWidget.setCurrentIndex(0)
            CLA1=BB.GetCLA1()
            #CLA1=[32000 ,32000]  #FOR TEST
            CLA1X=CLA1[0]
            CLA1Y=CLA1[1]
            CLA1X=int(CLA1X)
            CLA1Y=int(CLA1Y)
            #A=self.dial1.sliderPosition()
            A=self.ScrollBar1.sliderPosition()
            print(A)
            self.textEdit.setText("Beam Shift")
            print(CLA1X)
            R=A
            print(A,R)
            value=hex(R)
            value=str(value)
            value=value[2:]
            value=value.upper()
            print(value)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.BSX.setText(str(hex(R)).upper()[2:])
            BB.SetCLA1(R,CLA1Y)
            
        if (BT==True):
            self.tabWidget.setCurrentIndex(0)
            CLA2=BB.GetCLA2()
            CLA2X=int(str(CLA2[0]))
            CLA2Y=int(str(CLA2[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("Beam Tilt")
            print(CLA2X)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.BTX.setText(str(hex(R)).upper()[2:])
            BB.SetCLA2(R,CLA2Y)
            
            
        if (Ols==True):
            self.tabWidget.setCurrentIndex(1)
            Ols=BB.GetOLs()
            OLSX=int(str(Ols[0]))
            OLSY=int(str(Ols[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("OL STIG")
            print(OLSX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.OLSX.setText(str(hex(R)).upper()[2:])
            BB.SetOLs(R,OLSY)
            
        if (IS1==True):
            self.tabWidget.setCurrentIndex(1)
            IS1=BB.GetIS1()
            #IS1=[34000 ,34000]  #FOR TEST
            IS1X=IS1[0]
            IS1Y=IS1[1]
            IS1X=int(IS1X)
            IS1Y=int(IS1Y)
            #B=self.dial1.sliderPosition()
            B=self.ScrollBar1.sliderPosition()
            print(B)
            #print ("def:",Image)
            self.textEdit.setText("Image Shift 1")
            print(IS1X)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.IS1X.setText(str(hex(R)).upper()[2:])
            BB.SetIS1(R,IS1Y)
            
        if (IS2==True):
            self.tabWidget.setCurrentIndex(1)
            IS2=BB.GetIS2()
            #IS2=[34000 ,34000]  #FOR TEST
            IS2X=IS2[0]
            IS2Y=IS2[1]
            IS2X=int(IS2X)
            IS2Y=int(IS2Y)
            #B=self.dial1.sliderPosition()
            B=self.ScrollBar1.sliderPosition()
            print(B)
            #print ("def:",Image)
            self.textEdit.setText("Image Shift 2")
            print(IS2X)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.IS2X.setText(str(hex(R)).upper()[2:])
            BB.SetIS2(R,IS2Y)
            
        if (ILS==True):
            self.tabWidget.setCurrentIndex(1)
            ILS=BB.GetILs()
            ILSX=int(str(ILS[0]))
            ILSY=int(str(ILS[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("IL STIG")
            print(ILSX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.ILSX.setText(str(hex(R)).upper()[2:])
            BB.SetILs(R,ILSY)
            
        if (PLA==True):
            self.tabWidget.setCurrentIndex(1)
            PLA=BB.GetPLA()
            PLAX=int(str(PLA[0]))
            PLAY=int(str(PLA[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("PL Align")
            print(PLAX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.PLAX.setText(str(hex(R)).upper()[2:])
            BB.SetPLA(R,PLAY)
        
        if (CLCS==True):
            self.tabWidget.setCurrentIndex(2)
            clcs=BB.GetShifBal()
            clcsX=int(str(clcs[0]))
            clcsY=int(str(clcs[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP SHIFT")
            print(clcsX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.CLSHIFTX.setText(str(hex(R)).upper()[2:])
            BB.SetShifBal(R,clcsY)
            
        if (CLCT==True):
            self.tabWidget.setCurrentIndex(2)
            clct=BB.GetTiltBal()
            clctX=int(str(clct[0]))
            clctY=int(str(clct[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP TILT")
            print(clctX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.CLTILTX.setText(str(hex(R)).upper()[2:])
            BB.SetTiltBal(R,clctY)
            
        if (CLCA==True):
            self.tabWidget.setCurrentIndex(2)
            clca=BB.GetAngBal()
            clcaX=int(str(clca[0]))
            clcaY=int(str(clca[1]))
            B=self.ScrollBar1.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP ANGLE")
            print(clcaX)
            R=B
            print(B,R)
            self.xvalue.setText(str(hex(R)).upper()[2:])
            self.CLANGLEX.setText(str(hex(R)).upper()[2:])
            BB.SetAngBal(R,clcaY)
            
        
            
        
            
        
        
    def y(self):
        GUNS=self.radioButtonGUNS.isChecked()
        GUNT=self.radioButtonGUNT.isChecked()
        SPOTA=self.radioButtonSPOTA.isChecked()
        BS=self.radioButtonBS.isChecked()
        BT=self.radioButtonBT.isChecked()
        CLS=self.radioButtonCLS.isChecked()
        Ols=self.radioButtonOLS.isChecked()
        IS1=self.radioButtonIS1.isChecked()
        IS2=self.radioButtonIS2.isChecked()
        ILS=self.radioButtonILS.isChecked()
        PLA=self.radioButtonPLA.isChecked()
        CLCS=self.radioButtonCOMPS.isChecked()
        CLCT=self.radioButtonCOMPT.isChecked()
        CLCA=self.radioButtonCOMPA.isChecked()
        
        if(GUNS==True):
            GUN1=BB.GetGunA1()
            GUN1X=int(str(GUN1[0]))
            GUN1Y=int(str(GUN1[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("Gun Shift")
            print(GUN1Y)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.GUN1Y.setText(str(hex(R)).upper()[2:])
            BB.SetGunA1(GUN1X,R)
            
        if(GUNT==True):
            GUN2=BB.GetGunA2()
            GUN2X=int(str(GUN2[0]))
            GUN2Y=int(str(GUN2[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("Gun Tilt")
            print(GUN2Y)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.GUN2Y.setText(str(hex(R)).upper()[2:])
            BB.SetGunA2(GUN2X,R)
            
        if(SPOTA==True):
            SPOT=BB.GetSpotA()
            SPOTX=int(str(SPOT[0]))
            SPOTY=int(str(SPOT[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("Spot Align")
            print(SPOTY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.SPOTY.setText(str(hex(R)).upper()[2:])    
            BB.SetSpotA(SPOTX,R)  # See if SetSpotA available online
            
        if(CLS==True):
            CLS=BB.GetCLs()
            CLSX=int(str(CLS[0]))
            CLSY=int(str(CLS[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("Cond Stig")
            print(CLSY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.CLSY.setText(str(hex(R)).upper()[2:])  
            BB.SetCLs(CLSX,R)
        
            
        
        if (BS==True):
            CLA1=BB.GetCLA1()
            #CLA1=[32000 ,32000]  #FOR TEST
            CLA1X=CLA1[0]
            CLA1Y=CLA1[1]
            CLA1X=int(CLA1X)
            CLA1Y=int(CLA1Y)
            #A=self.dial2.sliderPosition()
            A=self.ScrollBar2.sliderPosition()
            #print("def:",Beam)
            print(CLA1Y,A)
            self.textEdit.setText("Beam Shift")
            #print(CLA1Y)
            R=A
            print(A,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.BSY.setText(str(hex(R)).upper()[2:])
            BB.SetCLA1(CLA1X,R)
            
        if (BT==True):
            CLA2=BB.GetCLA2()
            CLA2X=int(str(CLA2[0]))
            CLA2Y=int(str(CLA2[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("Beam Tilt")
            print(CLA2Y)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.BTY.setText(str(hex(R)).upper()[2:])  
            BB.SetCLA2(CLA2X,R)
            
            
        if (Ols==True):
            Ols=BB.GetOLs()
            OLSX=int(str(Ols[0]))
            OLSY=int(str(Ols[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("OL STIG")
            print(OLSY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.OLSY.setText(str(hex(R)).upper()[2:])
            BB.SetOLs(OLSX,R)
            
        if (IS1==True):
            IS1=BB.GetIS1()
            #IS1=[34000 ,34000]  #FOR TEST
            IS1X=IS1[0]
            IS1Y=IS1[1]
            IS1X=int(IS1X)
            IS1Y=int(IS1Y)
            #print ("def:",Image)    
            #B=self.dial2.sliderPosition()
            B=self.ScrollBar2.sliderPosition()
            print(IS1Y,B)
            self.textEdit.setText("Image Shift 1")
            #print(IS1Y)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.IS1Y.setText(str(hex(R)).upper()[2:])
            BB.SetIS1(IS1X,R)
            
        if (IS2==True):
            IS2=BB.GetIS2()
            #IS1=[34000 ,34000]  #FOR TEST
            IS2X=IS2[0]
            IS2Y=IS2[1]
            IS2X=int(IS2X)
            IS2Y=int(IS2Y)
            #print ("def:",Image)    
            #B=self.dial2.sliderPosition()
            B=self.ScrollBar2.sliderPosition()
            print(IS2Y,B)
            self.textEdit.setText("Image Shift 2")
            #print(IS1Y)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.IS2Y.setText(str(hex(R)).upper()[2:])
            BB.SetIS2(IS2X,R)
            
        if (ILS==True):
            ILS=BB.GetILs()
            ILSX=int(str(ILS[0]))
            ILSY=int(str(ILS[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("IL STIG")
            print(ILSY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.ILSY.setText(str(hex(R)).upper()[2:])
            BB.SetILs(ILSX,R)
            
        if (PLA==True):
            PLA=BB.GetPLA()
            PLAX=int(str(PLA[0]))
            PLAY=int(str(PLA[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("PL Align")
            print(PLAY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.PLAY.setText(str(hex(R)).upper()[2:])
            BB.SetPLA(PLAX,R)
            
        if (CLCS==True):
            clcs=BB.GetShifBal()
            clcsX=int(str(clcs[0]))
            clcsY=int(str(clcs[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP SHIFT")
            print(clcsY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.CLSHIFTY.setText(str(hex(R)).upper()[2:])
            BB.SetShifBal(clcsX,R)
            
        if (CLCT==True):
            clct=BB.GetTiltBal()
            clctX=int(str(clct[0]))
            clctY=int(str(clct[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP TILT")
            print(clctY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.CLTILTY.setText(str(hex(R)).upper()[2:])
            BB.SetTiltBal(clctX,R)
            
        if (CLCA==True):
            clca=BB.GetAngBal()
            clcaX=int(str(clca[0]))
            clcaY=int(str(clca[1]))
            B=self.ScrollBar2.sliderPosition()
            print(B)
            self.textEdit.setText("CL COMP ANGLE")
            print(clcaY)
            R=B
            print(B,R)
            self.yvalue.setText(str(hex(R)).upper()[2:])
            self.CLANGLEY.setText(str(hex(R)).upper()[2:])
            BB.SetAngBal(clcaX,R)
        
            
            
            
    """        
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # fucntions for brigthness slider  
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """
    def Bright(self):
        A=lens.GetCL3()
        #A=45000  #for test
        #type(A)
        print(A)
        #self.horizontalSlider.sliderPosition(A)
        #self.horizontalSlider.setSliderPosition(A)
        C=self.horizontalSlider.sliderPosition()
        #print (type(C))
        #print(C)
        R=C
        print(R)
        self.CL3value.setText(str(hex(R)).upper()[2:])
        lens.SetCL3(R)
        
        
        
    
    """    
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # fucntions for Spot size and Alpha select   
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """
    def Spot(self):
        SP = self.comboBox1.currentText()
        #print(SP)
        #self.results_window2.setText(str(SP))
        SP=int(SP)
        SP=SP-1
        eos.SelectSpotSize(SP)
        print("Spot:",SP+1)
        
    def Alpha(self):
        AL = self.comboBox2.currentText()
        #print(AL)
        AL=int(AL)
        AL=AL-1
        eos.SetAlphaSelector(AL)
        print("Alpha:",AL+1)
        
    """    
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #Functions for radiobuttons defs select
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """    
    def GUNS(self,GUNS):
        GUNS=self.radioButtonGUNS.isChecked()
        print ("def:",GUNS)
        self.textEdit.setText("Gun Shift")
        GUN1=BB.GetGunA1()
        #GUN1=[28000 ,23000]  #FOR TEST
        GUN1X=GUN1[0]
        GUN1Y=GUN1[1]
        self.ScrollBar1.setSliderPosition(GUN1X)
        self.ScrollBar2.setSliderPosition(GUN1Y)
        self.GUN1X.setText(str(hex(GUN1X)).upper()[2:])
        self.GUN1Y.setText(str(hex(GUN1Y)).upper()[2:])
        self.xvalue.setText(str(hex(GUN1X)).upper()[2:])
        self.yvalue.setText(str(hex(GUN1Y)).upper()[2:])
        
    def GUNT(self,GUNT):
        GUNT=self.radioButtonGUNT.isChecked()
        print ("def:",GUNT)
        self.textEdit.setText("Gun Tilt")
        GUN2=BB.GetGunA2()
        #GUN2=[38000 ,28000]  #FOR TEST
        GUN2X=GUN2[0]
        GUN2Y=GUN2[1]
        self.ScrollBar1.setSliderPosition(GUN2X)
        self.ScrollBar2.setSliderPosition(GUN2Y)
        self.GUN2X.setText(str(hex(GUN2X)).upper()[2:])
        self.GUN2Y.setText(str(hex(GUN2Y)).upper()[2:])
        self.xvalue.setText(str(hex(GUN2X)).upper()[2:])
        self.yvalue.setText(str(hex(GUN2Y)).upper()[2:])
        
    def SPOTA(self,SPOTA):
        SPOTA=self.radioButtonSPOTA.isChecked()
        print ("def:",SPOTA)
        self.textEdit.setText("Spot Align")
        SPOTA=BB.GetSpotA()
        #SPOTA=[38000 ,28000]  #FOR TEST
        SPOTAX=SPOTA[0]
        SPOTAY=SPOTA[1]
        self.ScrollBar1.setSliderPosition(SPOTAX)
        self.ScrollBar2.setSliderPosition(SPOTAY)
        self.SPOTX.setText(str(hex(SPOTAX)).upper()[2:])
        self.SPOTY.setText(str(hex(SPOTAY)).upper()[2:])
        self.xvalue.setText(str(hex(SPOTAX)).upper()[2:])
        self.yvalue.setText(str(hex(SPOTAY)).upper()[2:])
        
    def CLS(self,CLS):
        CLS=self.radioButtonCLS.isChecked()
        print ("def:",CLS)
        self.textEdit.setText("Cond Stig")
        CLS=BB.GetCLs()
        #CLS=[30800 ,20080]  #FOR TEST
        CLSX=CLS[0]
        CLSY=CLS[1]
        self.ScrollBar1.setSliderPosition(CLSX)
        self.ScrollBar2.setSliderPosition(CLSY)
        self.CLSX.setText(str(hex(CLSX)).upper()[2:])
        self.CLSY.setText(str(hex(CLSY)).upper()[2:])
        self.xvalue.setText(str(hex(CLSX)).upper()[2:])
        self.yvalue.setText(str(hex(CLSY)).upper()[2:])
        
    def BS(self,Beam):
        Beam=self.radioButtonBS.isChecked()
        print ("def:",Beam)
        self.textEdit.setText("Beam Shift")
        CLA1=BB.GetCLA1()
        #CLA1=[32000 ,32000]  #FOR TEST
        CLA1X=CLA1[0]
        CLA1Y=CLA1[1]
        self.ScrollBar1.setSliderPosition(CLA1X)
        self.ScrollBar2.setSliderPosition(CLA1Y)
        self.BSX.setText(str(hex(CLA1X)).upper()[2:])
        self.BSY.setText(str(hex(CLA1Y)).upper()[2:])
        self.xvalue.setText(str(hex(CLA1X)).upper()[2:])
        self.yvalue.setText(str(hex(CLA1Y)).upper()[2:])
        
    def BT(self,BT):
        BT=self.radioButtonBT.isChecked()
        print ("def:",BT)
        self.textEdit.setText("Beam Tilt")
        CLA2=BB.GetCLA2()
        #CLA2=[31000 ,39000]  #FOR TEST
        CLA2X=CLA2[0]
        CLA2Y=CLA2[1]
        self.ScrollBar1.setSliderPosition(CLA2X)
        self.ScrollBar2.setSliderPosition(CLA2Y)
        self.BTX.setText(str(hex(CLA2X)).upper()[2:])
        self.BTY.setText(str(hex(CLA2Y)).upper()[2:])
        self.xvalue.setText(str(hex(CLA2X)).upper()[2:])
        self.yvalue.setText(str(hex(CLA2Y)).upper()[2:])
        
    def IS1(self,Image1):
        Image1=self.radioButtonIS1.isChecked()
        print ("def:",Image1)
        self.textEdit.setText("Image Shift 1")
        IS1=BB.GetIS1()
        #IS1=[34000 ,34000]   #FOR TEST
        IS1X=int(str(IS1[0]))
        IS1Y=int(str(IS1[1]))
        self.ScrollBar1.setSliderPosition(IS1X)
        self.ScrollBar2.setSliderPosition(IS1Y)
        self.IS1X.setText(str(hex(IS1X)).upper()[2:])
        self.IS1Y.setText(str(hex(IS1Y)).upper()[2:])
        self.xvalue.setText(str(hex(IS1X)).upper()[2:])
        self.yvalue.setText(str(hex(IS1Y)).upper()[2:])
        
    def IS2(self,Image2):
        Image2=self.radioButtonIS2.isChecked()
        print ("def:",Image2)
        self.textEdit.setText("Image Shift 2")
        IS2=BB.GetIS2()
        #IS2=[36000 ,54000]   #FOR TEST
        IS2X=int(str(IS2[0]))
        IS2Y=int(str(IS2[1]))
        self.ScrollBar1.setSliderPosition(IS2X)
        self.ScrollBar2.setSliderPosition(IS2Y)
        self.IS2X.setText(str(hex(IS2X)).upper()[2:])
        self.IS2Y.setText(str(hex(IS2Y)).upper()[2:])
        self.xvalue.setText(str(hex(IS2X)).upper()[2:])
        self.yvalue.setText(str(hex(IS2Y)).upper()[2:])
        
    def OLS(self,OLS):
        OLS=self.radioButtonOLS.isChecked()
        print ("def:",OLS)
        self.textEdit.setText("OL STIG")
        OLS=BB.GetOLs()
        #OLS=[38000 ,54000]   #FOR TEST
        OLSX=int(str(OLS[0]))
        OLSY=int(str(OLS[1]))
        self.ScrollBar1.setSliderPosition(OLSX)
        self.ScrollBar2.setSliderPosition(OLSY)
        self.OLSX.setText(str(hex(OLSX)).upper()[2:])
        self.OLSY.setText(str(hex(OLSY)).upper()[2:])
        self.xvalue.setText(str(hex(OLSX)).upper()[2:])
        self.yvalue.setText(str(hex(OLSY)).upper()[2:])
        
    def ILS(self,ILS):
        OLS=self.radioButtonILS.isChecked()
        print ("def:",OLS)
        self.textEdit.setText("IL STIG")
        ILS=BB.GetILs()
        #ILS=[38000 ,54000]   #FOR TEST
        ILSX=int(str(ILS[0]))
        ILSY=int(str(ILS[1]))
        self.ScrollBar1.setSliderPosition(ILSX)
        self.ScrollBar2.setSliderPosition(ILSY)
        self.ILSX.setText(str(hex(ILSX)).upper()[2:])
        self.ILSY.setText(str(hex(ILSY)).upper()[2:])
        self.xvalue.setText(str(hex(ILSX)).upper()[2:])
        self.yvalue.setText(str(hex(ILSY)).upper()[2:])
        
    def PLA(self,PLA):
        PLA=self.radioButtonPLA.isChecked()
        print ("def:",PLA)
        self.textEdit.setText("PL Align")
        PLA=BB.GetPLA()
        #PLA=[33000 ,31000]   #FOR TEST
        PLAX=int(str(PLA[0]))
        PLAY=int(str(PLA[1]))
        self.ScrollBar1.setSliderPosition(PLAX)
        self.ScrollBar2.setSliderPosition(PLAY)
        self.PLAX.setText(str(hex(PLAX)).upper()[2:])
        self.PLAY.setText(str(hex(PLAY)).upper()[2:])
        self.xvalue.setText(str(hex(PLAX)).upper()[2:])
        self.yvalue.setText(str(hex(PLAY)).upper()[2:])
        
        
        
    def CLCOMPS(self,CLCS):
        CLCS=self.radioButtonCOMPS.isChecked()
        print ("def:",CLCS)
        self.textEdit.setText("CL COMP SHIFT")
        CLCS=BB.GetShifBal()
        #CLCS=[35000 ,39000]   #FOR TEST
        CLCSX=int(str(CLCS[0]))
        CLCSY=int(str(CLCS[1]))
        self.ScrollBar1.setSliderPosition(CLCSX)
        self.ScrollBar2.setSliderPosition(CLCSY)
        self.CLSHIFTX.setText(str(hex(CLCSX)).upper()[2:])
        self.CLSHIFTY.setText(str(hex(CLCSY)).upper()[2:])
        self.xvalue.setText(str(hex(CLCSX)).upper()[2:])
        self.yvalue.setText(str(hex(CLCSY)).upper()[2:])
        
    
    def CLCOMPT(self,CLCT):
        CLCT=self.radioButtonCOMPT.isChecked()
        print ("def:",CLCT)
        self.textEdit.setText("CL COMP TILT")
        CLCT=BB.GetTiltBal()
        #CLCT=[43000 ,47000]   #FOR TEST
        CLCTX=int(str(CLCT[0]))
        CLCTY=int(str(CLCT[1]))
        self.ScrollBar1.setSliderPosition(CLCTX)
        self.ScrollBar2.setSliderPosition(CLCTY)
        self.CLTILTX.setText(str(hex(CLCTX)).upper()[2:])
        self.CLTILTY.setText(str(hex(CLCTY)).upper()[2:])
        self.xvalue.setText(str(hex(CLCTX)).upper()[2:])
        self.yvalue.setText(str(hex(CLCTY)).upper()[2:])
        
    
    def CLCOMPA(self,CLCA):
        CLCA=self.radioButtonCOMPA.isChecked()
        print ("def:",CLCA)
        self.textEdit.setText("CL COMP ANGLE")
        CLCA=BB.GetAngBal()
        #see if GetAngleBal enabled online
        #CLCA=[31000 ,32000]   #FOR TEST
        CLCAX=int(str(CLCA[0]))
        CLCAY=int(str(CLCA[1]))
        self.ScrollBar1.setSliderPosition(CLCAX)
        self.ScrollBar2.setSliderPosition(CLCAY)
        self.CLANGLEX.setText(str(hex(CLCAX)).upper()[2:])
        self.CLANGLEY.setText(str(hex(CLCAY)).upper()[2:])
        self.xvalue.setText(str(hex(CLCAX)).upper()[2:])
        self.yvalue.setText(str(hex(CLCAY)).upper()[2:])
    """    
    *******************************************
    # Functions Mode Select by PushButtons 
    *******************************************
    """       
    def MAG(self):
        eos.SelectFunctionMode(0)
        print("ok Mag Mode")
        func=eos.GetMagValue()
        unit=func[1]
        u2=func[2]
        print(u2)
        self.Func.setText(u2)
        
        
    def Dif(self):
        eos.SelectFunctionMode(4)
        print("ok Diff Mode")
        func=eos.GetMagValue()
        unit=func[1]
        u2=func[2]
        print(u2)
        self.Func.setText(u2)
        
    def LMag(self):
        eos.SelectFunctionMode(2)
        print("ok Low Mag Mode")
        func=eos.GetMagValue()
        unit=func[1]
        u2=func[2]
        print(u2)
        func=str(func[0])
        self.Func.setText(u2)
    


app = QtGui.QApplication(sys.argv)
window = MyApp()
window.move(620,500)
window.show()
sys.exit(app.exec_())