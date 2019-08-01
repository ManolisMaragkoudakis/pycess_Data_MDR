import numpy as np 
import matplotlib.pyplot as plt 
import readMdrData

nameOfFile = 'newHigh.dat'

myData = readMdrData.mdrOutput(nameOfFile)
discharge = 48425

print(myData.giveMaxKapaSpectrum(discharge))
print(myData.giveFreqShift(discharge))
'''
r8 = myData.giveRho(discharge)
kapaPerp8 = myData.giveKapaPerp(discharge)

r7 = myData.giveRho(discharge-1)
kapaPerp7 = myData.giveKapaPerp(discharge-1)

r6 = myData.giveRho(discharge-2)
kapaPerp6 = myData.giveKapaPerp(discharge-2)

r5 = myData.giveRho(discharge-3)
kapaPerp5 = myData.giveKapaPerp(discharge-3)

r4 = myData.giveRho(discharge-4)
kapaPerp4 = myData.giveKapaPerp(discharge-4)

plt.figure(1)
plt.plot(r8, kapaPerp8, 'o')
plt.plot(r7, kapaPerp7, 'o')
plt.plot(r6, kapaPerp6, 'o')
plt.plot(r5, kapaPerp5, 'o')
plt.plot(r4, kapaPerp4, 'o')
plt.grid(True)
plt.xlabel(r'$\rho$')
plt.ylabel(r'$k_{}$'.format('\\perp'))
plt.show()
'''