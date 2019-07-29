import numpy as np 
import matplotlib.pyplot as plt 
import os
import handfulFunctions as hf

class mdrOutput:

    def __init__(self, nof=''):

        self.nameOfFile = nof

        fileLen = int(hf.fileLength(self.nameOfFile))
        self.arrayDischNum = np.zeros(fileLen, dtype=int)
        self.arrayDiagFreq = np.zeros(fileLen)
        self.arrayFreqShift = np.zeros(fileLen)
        self.arrayKapaSpec = np.zeros(fileLen)
        self.arrayRho = np.zeros(fileLen)
        self.arrayUncerRho = np.zeros(fileLen)
        self.arrayKapaPerp = np.zeros(fileLen)
        self.arrayUnKapaPe = np.zeros(fileLen)
        self.arrayMagField = np.zeros(fileLen)

        idx = 0

        with open(nof, 'r') as myFile:
            for line in myFile:
                fields = line.split()
                correctFields = [i for i in fields]
                self.arrayDischNum[idx] = int(correctFields[0])
                self.arrayDiagFreq[idx] = float(correctFields[1])
                self.arrayFreqShift[idx] = float(correctFields[4]) 
                self.arrayKapaSpec[idx] = float(correctFields[5])
                self.arrayRho[idx] = float(correctFields[10])
                self.arrayUncerRho[idx] = float(correctFields[11])
                self.arrayKapaPerp[idx] = float(correctFields[12])
                self.arrayUnKapaPe[idx] = float(correctFields[13])
                self.arrayMagField[idx] = float(correctFields[14])
                idx = idx + 1
        myFile.closed

    def dischInFile(self):
        return np.unique(self.arrayDischNum)

    def giveDiagFreq(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayDiagFreq[idx] if whichDisch!=0 else self.arrayDiagFreq

    def giveFreqShift(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayFreqShift[idx] if whichDisch!=0 else self.arrayFreqShift
    
    def giveMaxKapaSpectrum(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayKapaSpec[idx] if whichDisch!=0 else self.arrayKapaSpec

    def giveRho(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayRho[idx] if whichDisch!=0 else self.arrayRho

    def giveUncerRho(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayUncerRho[idx] if whichDisch!=0 else self.arrayUncerRho

    def giveKapaPerp(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayKapaPerp[idx] if whichDisch!=0 else self.arrayKapaPerp

    def giveUnKapaPe(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayUnKapaPe[idx] if whichDisch!=0 else self.arrayUnKapaPe

    def giveMagField(self, whichDisch=0):
        idx = np.where(self.arrayDischNum==whichDisch)
        return self.arrayMagField[idx] if whichDisch!=0 else self.arrayMagField