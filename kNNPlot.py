# coding=utf-8

from numpy import *
from matplotlib import pyplot as plt
import kNN

datingDataMat, datingLables = kNN.datingFile2matrix('book_source/Ch02/datingTestSet2.txt')

fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(datingDataMat[:,0], datingDataMat[:, 1], 15.0 * array(datingLables), 15.0 * array(datingLables))

plt.xlabel('flying miles')
plt.ylabel('game time')

plt.show()
