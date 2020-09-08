import icoshift
import scipy as sp
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

wine = loadmat('../data/WineData.mat')

X = wine['X']
ppm = wine['ppm'][0]
ppm_ints = wine['ppm_ints'][0]
wine_ints = wine['wine_ints'][0]

# plt.figure()
for i in range(X.shape[0]):
    plt.plot(ppm, X[i,:])
# plt.show()
print(X.shape, ppm.shape)

# plt.figure()
for i in range(X.shape[0]):
    plt.plot(ppm[7151:7550], X[i,7151:7550])
# plt.show()

lacInter = list(range(7551,7751))
options = np.array([2,1,0])

print("iCOshift 1: aligns the whole spectra according to a reference signal selected (Ethanol CH3 resonance)")

xCS, ints, ind, target = icoshift.icoshift('average', X, lacInter,  'f')


for i in range(X.shape[0]):
    plt.plot(ppm[7151:7550], xCS[i,7151:7550])
# plt.show()

print("iCOshift 2: splits the dataset in 50 regular intervals and aligns each of them separately")

xCS, ints, ind, target = icoshift.icoshift('average', X, 50, 'f')



print("iCOshift 3: splits the dataset in regular intervals 800 points wide and search for the best "
      "allowed shift for each of them separately")

xCS, ints, ind, target = icoshift.icoshift('average', X, '800', 'b')




print("iCOshift 4: splits the dataset in pre-defined intervals (on the basis of the user's knowledge) "
      "and aligns each of them")

xCS, ints, ind, target = icoshift.icoshift('average', X, wine_ints.tolist(), 'f')



print("iCOshift 4a: Like the previous example but using an intermediate coshift step")

xCS, ints, ind, target = icoshift.icoshift('max', X, wine_ints.tolist(), 'f', coshift_preprocessing=True)



print("iCOshift 4b: Like the previous example but using also missing values (NaN) in the last setp")

xCS, ints, ind, target = icoshift.icoshift('max', X, wine_ints.tolist(), 'f', coshift_preprocessing=True, fill_with_previous=False)

