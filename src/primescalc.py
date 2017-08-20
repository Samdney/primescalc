#!/usr/bin/python
#_____________________________________________________________________________
#
# This is a research program around the topic:
# "Prime numbers and how they can be calculated recursively."
#
# Based on the paper:
# "The recursively calculation of prime numbers"
# by Carolin Zöbelein
#
# Paper available on: https://github.com/Samdney/primescalc
#
# Author:   Carolin Zöbelein  <contact@carolin-zoebelein.de>   D4A7 35E8 D47F 801F 2CF6 2BA7 927A FD3C DE47 E13B 
# License:  see LICENSE file for information
#_____________________________________________________________________________


import numpy as np


def x_ij(x_i,x_j,mu=None):
    """
    Calculation of x_ij
    """
    if mu:
        x_ij = (2*x_i + 1)*x_j + x_i - mu
    else:
        x_ij = (2*x_i + 1)*x_j + x_i
    return x_ij

def y_ij(x_,x_j=None,mu=None):
    """
    Calculation of y_ij
    given by    x_i, x_j or x_ = x_ij
    """
    if x_j and mu:
        y_ij = 2*x_ij(x_,x_j,mu) + 1
    elif x_j and mu==None:
        y_ij = 2*x_ij(x_,x_j) + 1
    else:
        y_ij = 2*x_ + 1
    return y_ij


def x_j(eq,x_i1,x_i2,mu1,mu2):
    """
    Special solution for x_j's of the intersection of two equations
    """
    if eq==1:
        x_j1 = (1 + mu1 - mu2)*x_i2
        x_j = x_j1
    else:
        x_j2 = (1 + mu1 - mu2)*x_i1
        x_j = x_j2
    return x_j

def x_ij_int(x_i1,x_i2,mu1,mu2):
    """
    Special solution for x_ij of the intersection of two equations
    """
    x_i12 = x_ij(x_i1,x_i2)
    mu12 = -mu1*x_i1*(2*x_i2 + 1) + mu2*x_i2*(2*x_i1 + 1)

    x_ij_erg = x_i12 - mu12
    return x_ij_erg
    


def main():
    """
    Main entry point.    
    """
    initial_seed = 3

    #x_i = 1

    """Divisible numbers """
    #for x_j in range(1, 10):
    #    print(x_j,x_ij(x_i,x_j))

    #print("Hallo")

    """ NOT divisible numbers """
    #for x_i in range(1,6):
    #    for x_j in range(1,6):
    #        for mu in range(1,2*x_i + 1):
    #            print(x_i,x_j,mu,x_ij(x_i,x_j,mu))
    #        print("\n")
    #    print("\n") 

    """ Special solution for x_j's of the intersection of two equations"""
    x_i1 = 1
    x_i2 = 3
    #print("eq\tx_i1\tx_i2\tmu1\tmu2\t\tx_j")
    #for mu1 in range(1,2*x_i1 + 1):
    #    for mu2 in range(1,2*x_i2 + 1):
    #        x_j1 = x_j(1,x_i1,x_i2,mu1,mu2)
    #        x_j2 = x_j(2,x_i1,x_i2,mu1,mu2)

    #        print(1,"\t",x_i1,"\t",x_i2,"\t",mu1,"\t",mu2,"\t\t",x_j1)
    #        print(2,"\t",x_i1,"\t",x_i2,"\t",mu1,"\t",mu2,"\t\t",x_j2)
    #        print("\n")
    #    print("\n")
    
    """Special solution for x_ij of the intersection of two equations"""
    tmp = 2*x_i1*x_i2 + x_i1 + x_i2
    term = 2*tmp + 1
    print("x_i1\tx_i2\tmu1\t\mu2\tf\t\tx_ij")
    for mu1 in range(1,2*x_i1 + 1):
        for mu2 in range(1,2*x_i2 + 1):
            for f in range(0,5):
                x_ij = x_ij_int(x_i1,x_i2,mu1,mu2) + term*f

                print(x_i1,"\t",x_i2,"\t",mu1,"\t",mu2,"\t",f,"\t\t",x_ij)
            print("\n")
        print("\n")

main()
