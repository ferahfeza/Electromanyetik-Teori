import numpy as np
from numpy import linalg as LA


P1 = [2,4,3]
P2 = [-1,5,6]

D = np.subtract(P2,P1)
print("D=",D[0],"ax",D[1],"ay",D[2],"az")

D_gen = LA.norm(D)
print(D_gen)

aD = D / D_gen
print(aD)

