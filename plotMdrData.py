import numpy as np 
import matplotlib.pyplot as plt 
import readMdrData

class graphsMdrData:

    def __init__(self, nof=''):

        self.nameOfFile = nof
        self.myData = readMdrData.mdrOutput(nof)

        print('Visualization of MDR Data.')
        print('Finished reading file:', self.nameOfFile)
        print('Discharges in file:', self.myData.dischInFile())

    def profKapaPerp(self, whichDisch=[]):
        dischNum = list(self.myData.dischInFile()) if whichDisch == [] else whichDisch
        plt.figure(1)
        for idxDischarge in dischNum:
            r = self.myData.giveRho(idxDischarge)
            k = self.myData.giveKapaPerp(idxDischarge)
            plt.plot(r, k, 'o', label=str(idxDischarge))

        plt.grid(True)
        plt.legend(loc='best')
        plt.xlabel(r'$\rho$')
        plt.ylabel(r'$k_{}$'.format('\\perp'))
        plt.show()

        return

    def profMagField(self, whichDisch=[]):
        dischNum = list(self.myData.dischInFile()) if whichDisch == [] else whichDisch
        plt.figure(1)
        for idxDischarge in dischNum:
            r = self.myData.giveRho(idxDischarge)
            B = self.myData.giveMagField(idxDischarge)
            plt.plot(r, B, 'o', label=str(idxDischarge))

        plt.grid(True)
        plt.legend(loc='best')
        plt.xlabel(r'$\rho$')
        plt.ylabel(r'B')
        plt.show()

        return

    def spectrumKapaPerp(self, whichDisch=[]):
        dischNum = list(self.myData.dischInFile()) if whichDisch == [] else whichDisch
        plt.figure(3)
        for idxDischarge in dischNum:
            kapaPerp = self.myData.giveKapaPerp(idxDischarge)
            PowerFreq = self.myData.giveMaxKapaSpectrum(idxDischarge)
            plt.plot(np.log10(kapaPerp), 10.*np.log10(PowerFreq), 'o', label=str(idxDischarge))

        plt.grid(True)
        plt.legend(loc='best')
        plt.xlabel(r'$log \big ( k_{} \big ) $'.format('\\perp'))
        plt.ylabel(r'$10 \times log \big( S(k_{}) \big) $'.format('\\perp'))
        plt.show()

        return

    def profFreqShift(self, whichDisch=[]):
        dischNum = list(self.myData.dischInFile()) if whichDisch == [] else whichDisch
        plt.figure(4)
        for idxDischarge in dischNum:
            r = self.myData.giveRho(idxDischarge)
            fD = self.myData.giveFreqShift(idxDischarge)
            plt.plot(r, fD, 'o', label=str(idxDischarge))

        plt.grid(True)
        plt.legend(loc='best')
        plt.xlabel(r'$\rho$')
        plt.ylabel(r'$f_D$')
        plt.show()

        return