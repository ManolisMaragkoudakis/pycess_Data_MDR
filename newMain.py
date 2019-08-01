import plotMdrData

myGraphs = plotMdrData.graphsMdrData('newHigh.dat')
discharge = []
#myGraphs.profKapaPerp()
#myGraphs.profMagField()
myGraphs.profKapaPerp()
myGraphs.profFreqShift()
myGraphs.profVelocity()
myGraphs.profElectricField()