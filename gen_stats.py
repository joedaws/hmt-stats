#!/usr/bin/env python
# script to generate some statistics related to 
# the hidden markov tree model for wavelet coefficients

import numpy as np
from trees import sTree
import matplotlib.pyplot as plt
from scipy.stats import norm # for normal random variable

# iterate over different N which are powers of 2
for d in range(7,15):
    print(d)
    # number of basis functions
    bN = 2**d # size of an N sample signal
    # number of realizations
    sampN = 1000
    # list for values of s
    svals = []
    # lists for storing data
    meanvals = []
    plus1std = []
    minus1std = []

    # iterate over various sparsity levels
    for sle in range(int(0.02*bN),int(0.10*bN)):
        # instantiate a tree
        T = sTree(s=sle,N=bN)
        #print(sle)
        # generate samples and compute average
        vals = [] # list of values of the K(T) for generated T's
    
        # generate sampN trees
        for i in range(0,sampN):
            T.reset_tree()
            T.grow_tree()
            # save value
            vals.append(T.norm)
    
        # compute standard deviation
        stdval = np.std(vals)
        avg = sum(vals)/len(vals)
    
        # genereate histogram
        fig, ax = plt.subplots(1)
        plt.hist(vals,bins=30,alpha=0.6,color='b')
        plt.axvline(sum(vals)/len(vals), color='k', linestyle='dashed', linewidth=2)
        ax.set_xlabel('Weighted Sparsity')
        ax.set_yticklabels([])
        title = "Histogram of Weighted Sparsity: s = %3d, N = %4d" % (sle,bN)
        plt.title(title)
    
        # save histogram
        plt.savefig("plots/"+str(sle)+"_"+str(bN)+"_histo.png")
        # close figure
        plt.close(1)

        # save the data to appropriate arrays
        svals.append(sle)
        plus1std.append(avg + stdval)
        minus1std.append(max(avg - stdval,0))
        meanvals.append(avg)

    # save the generated data to be used for plotting later
    sstr = str(sle)
    bNstr = str(bN)
    np.save('data/'+bNstr+'_svals.npy',svals)
    np.save('data/'+bNstr+'_means.npy',meanvals)
    np.save('data/'+bNstr+'_p1std.npy',plus1std)
    np.save('data/'+bNstr+'_m1std.npy',minus1std)
