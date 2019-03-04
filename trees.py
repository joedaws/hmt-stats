"""
trees.py -- 

This file contains Classes and methods for generating
a hidden markov tree as in [1]

Author: Joseph D Daws Jr
Last Modified: Mon Jan 8 2019

References:
    [1]: Bayesian Tree-structured Image Modeling Using
         Wavelet-domain Hidden Markov Models
         Romberg, Choi and Baraniuk
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def simpleHMTmat(j):
    """
    returns the transition matrix for level j
    using the universal paramters outlined in [1]

    I used the transition probabilities generated in the
    matlab code hmtmodel.m written by Choi
    """
    # set the transition matrix for level j
    if j < 3:
        # just the identity in this case
        Aj = np.array([[1,0],[0,1]])
    else:
        # define probability of small to small
        p00 = .8 + .2*(1-2.**(-j+4))
        # define probability of large to large
        p11 = .9 - .4*(1-2.**(-j+4))
        Aj = np.array([[p00,1-p11],[1-p00,p11]])
    return Aj

def trans_mat(pss=0.9,psl=0.1,pls=0.4,pll=0.6):
    """
    Creates a transition matrix P with the provided probs.

    INPUTS:
    pss -- probability form small to small
    psl -- probability form small to large
    pls -- probability form large to small
    pll -- probability form large to large

    OUTPUTS:
    P -- transition probability matrix
    """
    P = np.array([[pss,psl],[pls,pll]])
    return P

class Node:
    """
    Represents a node on a HMT with state 1
    stores its location in idx
    """
    def __init__(self,idx=np.array([0,0])):
        self.idx = idx

class sTree:
    def __init__(self,s,N):
        """
        INPUTS:
        s -- sparsity level
        N -- number of pixels in one dimension
             should be a power of 2
        """
        # set true sparsity level
        self.s = s
        # create list for nodes with state 1
        self.nodes = []
        # define max depth
        # first, ensure that N is a power of 2
        if N & (N-1) == 0:
            # then N is a power of 2
            self.max_depth = int(np.log(N)/np.log(2))
        else:
            # N is not a power of 2
            print("N is not a power of 2")
            print("Choose a power of 2 for N")
            
        # max realized depth
        self.max_realized_depth = 0
        # weighted l0 norm -- weighted sparsity
        self.norm = 0
    
    def add_node(self,p,l,k):
        """
        genereates a random node and stores it 
        in self.nodes list if it has state 1 also
        increments the norm of the growing hmt

        INPUTS:
        p -- vector of probabilities [ps,pl]
             ps = probability this node is small
             pl = probability this node is large
        l -- level index
        k -- index within level l
        """
        # draw from the probability distribution
        state = bernoulli.rvs(p[1],size=1)
        # add node if its state is 1
        if state == 1:
            # append the node to self.nodes
            n = Node(idx=np.array([l,k]))
            self.nodes.append(n)
            # increment the norm calculation
            self.norm += 2**l
        else:
            # no need to do anything
            return

    def grow_tree(self):
        """
        grows a tree by randomly drawing nodes and storing
        the ones with state 1

        INPUTS: 
        P0 -- initial transition matrix
        """

        # generate the root node
        cp = np.array([0.5,0.5]) # probability for root node
        self.add_node(cp,0,0) # add node

        # counter for level
        cl = 1 # current level
        # iterate over all levels
        while cl < self.max_depth:
            # update realized depth
            self.max_realized_depth = cl
            # get transition matrix for this level
            Pj = simpleHMTmat(cl)
            # update probabilities for nodes on this level
            cp = np.dot(Pj,cp)  
            #iterate over all possible nodes on level cl 
            for k in range(0,2**cl):
                # add nodes
                self.add_node(cp,cl,k)
                # check to see if we have reached s nodes
                if len(self.nodes) == self.s:
                    #print("Reached {0} nodes with index ({1},{2})\n"\
                    #        .format(self.s, cl, k))
                    return 
            # increment cl counter
            cl += 1

    def reset_tree(self):
        """
        zero out the current nodes 
        """
        # clear out nodes list
        self.nodes = []

        # reset the norm
        self.norm = 0

        return
