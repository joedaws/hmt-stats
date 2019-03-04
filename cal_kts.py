"""
cal_kts.py

Author: Joseph D Daws Jr

This file contains classes and methods
for calculating the value of K_tree(s)
given a sparsity parameter s for the case of
binary trees
"""

class BiNode:
    def __init__(self,j=0,k=0):
        self.parent = None
        self.lchild = None
        self.rchild = None
        self.idx = (j,k)

class QuadNode:
    def __init__(self,j=0,k1=0,k2=0):
        self.parent = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.idx = (j,k1,k2)

class BiTree:
    def __init__(self,s,depth):
        # set sparsity level s
        self.s = s
        # list of nodes
        self.nodes = []
        # add the root node
        root = BiNode()
        self.nodes.append(root)
        # value of K_tree(s) we want to calculate
        self.KTS = 1 # value is 1 since we already added the root
        # set maximum depth
        self.max_depth = depth
    
    def get_KTS(self):
        """
        Calculate the value of KTS for the given s
        """
        # load root node
        nextnode = self.nodes[0]
        # add nodes while the number of nodes is less than s
        while len(self.nodes) < self.s:
            # add node
            nextnode = self.add_node(nextnode)
    
    def add_node(self,deep_one):
        """
        method for adding nodes to the tree given the input node
        
        INPUTS:
        deep_one -- node to add children to

        OUTPUTS:
        (newj,newk) -- tuple of indices of the next node to try 
                       to add children to
        """
        # check to see if we can add child to deep one
        if (deep_one.idx[0] == self.max_depth-1):
            # cannot add node here must move up
            return deep_one.parent

        elif (deep_one.lchild == None and deep_one.rchild == None):
            # add a left child
            childj = deep_one.idx[0]+1
            childk = 2*deep_one.idx[1]
            new_one = BiNode(j=childj,k=childk)
            new_one.parent = deep_one
            deep_one.lchild = new_one
            self.nodes.append(new_one)
            # increment KTS
            self.KTS += 2**childj
            # return the child node
            return new_one

        elif (deep_one.lchild != None and deep_one.rchild == None):
            # add a right child
            childj = deep_one.idx[0]+1
            childk = 2*deep_one.idx[1]+1
            new_one = BiNode(j=childj,k=childk)
            new_one.parent = deep_one
            deep_one.rchild = new_one
            self.nodes.append(new_one)
            # increment KTS
            self.KTS += 2**childj
            return new_one

        elif (deep_one.lchild != None and deep_one.rchild != None):
            # cannot add any children must move somewhere else
            return deep_one.parent

class QuadTree:
    def __init__(self,s,depth):
        # set sparsity level s
        self.s = s
        # list of nodes
        self.nodes = []
        # add the root node
        root = QuadNode()
        self.nodes.append(root)
        # value of K_tree(s) we want to calculate
        self.KTS = 1 # value is 1 since we already added the root
        # set maximum depth
        self.max_depth = depth
    
    def get_KTS(self):
        """
        Calculate the value of KTS for the given s
        """
        # load root node
        nextnode = self.nodes[0]
        # add nodes while the number of nodes is less than s
        while len(self.nodes) < self.s:
            # add node
            nextnode = self.add_node(nextnode)
    
    def add_node(self,deep_one):
        """
        method for adding nodes to the tree given the input node
        
        INPUTS:
        deep_one -- node to add children to

        OUTPUTS:
        (newj,newk) -- tuple of indices of the next node to try 
                       to add children to
        """
        # check to see if we can add child to deep one
        if (deep_one.idx[0] == self.max_depth-1):
            # cannot add node here must move up
            return deep_one.parent

        elif (deep_one.lchild == None and deep_one.rchild == None):
            # add a left child
            childj = deep_one.idx[0]+1
            childk = 2*deep_one.idx[1]
            new_one = BiNode(j=childj,k=childk)
            new_one.parent = deep_one
            deep_one.lchild = new_one
            self.nodes.append(new_one)
            # increment KTS
            self.KTS += 2**childj
            # return the child node
            return new_one

        elif (deep_one.lchild != None and deep_one.rchild == None):
            # add a right child
            childj = deep_one.idx[0]+1
            childk = 2*deep_one.idx[1]+1
            new_one = BiNode(j=childj,k=childk)
            new_one.parent = deep_one
            deep_one.rchild = new_one
            self.nodes.append(new_one)
            # increment KTS
            self.KTS += 2**childj
            return new_one

        elif (deep_one.lchild != None and deep_one.rchild != None):
            # cannot add any children must move somewhere else
            return deep_one.parent
