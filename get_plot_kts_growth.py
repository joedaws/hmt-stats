#!/usr/bin/env python
# script to make plots comparing the growth
# of the various quantities of interest
import numpy as np
import matplotlib.pyplot as plt
# import bitree structure
from cal_kts import BiTree


# calculate \Theta^2s for fixed N
d = 12
N = 2**d
num = str(N)
# load data from file
svals = np.load('data/'+num+'_svals.npy')
theta2s = N*np.array(svals)

# calculate K_{\mathcal{T}}(s)
ksvals = []
# iterate over sparsity levels
for si in svals:
    # generate the value K(s)
    T = BiTree(s=si,depth=d)
    T.get_KTS()
    ksvals.append(T.KTS)

# load data from file
meanvals = np.load('data/'+num+'_means.npy')
p1std = np.load('data/'+num+'_p1std.npy')
m1std = np.load('data/'+num+'_m1std.npy')

# Make plot
fig = plt.figure()
ax = plt.gca()

# plot means
plt.plot(svals,meanvals,label='$\mathbb{E}[K(T_s)$]')
# plot sampling complexity values
plt.plot(svals,theta2s,label='$\Theta^2s$')
plt.plot(svals,ksvals,label='$K_{\mathcal{T}}(s)$')
# plot N
plt.plot(svals,N*np.ones((len(svals),)),label='$N=$'+num)

# set axis scale
ax.set_yscale('log')

# set legend
plt.legend(loc=4)

# set axis label
plt.xlabel('$s$--number of non-zero coefficients')
plt.title('Comparsion of Sampling Complexities for $N=2^{11}$')

# show the how plot
plt.show()
