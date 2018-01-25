import matplotlib.pyplot as plt

decisionNode = dict(boxstyle='sawtooth', fc='0.8')
leafNode = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstype="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
  createPlot.ax1.annotate(nodeText, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes franction', va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)

  def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    reatePlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'
    .....
