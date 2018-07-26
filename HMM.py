#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np
from hmmlearn import hmm

def HMM():

    #hmm_model = hmm.GaussianHMM(n_components=3, covariance_type="full")

    a = np.array([[0.6, 0.6, 0.6],
                  [0.4, 0.4, 0.4],
                  [0.7, 0.7, 0.3]], dtype=np.float64)

    b = np.array([[0.6, 0.4, 0.4],
                  [0.5, 0.5, 0.5],
                  [0.5, 0.5, 1.0]], dtype=np.float64)

    g = np.zeros((3,3))
    bunki = np.zeros((3,3))
    route = np.zeros((3,3))
    g[0,0]= 1.0
  
    bunki[0,:] = 1
    bunki[:,0] = 3

    for j in range(1,3):
        g[j,0] = g[j-1,0] * a[j,0] * b[j,0]
    for i in range(1,3):
        g[0,i] = g[0,i-1] * a[0,i] * b[0,i]

    for y in range(1,3):
        for x in range(1,3):
            number = np.array([0]*2, dtype=np.float64)

            if y<3:
                number[0] = g[y,x-1] * a[y,x-1] * b[y,x-1]
            if x<3:
                number[1] = g[y-1,x] * a[y-1,x] * b[y-1,x]
            
            num_max = number.max()
          
            if num_max == number[0]:
                bunki[y,x] = 1
            if num_max == number[1]:
                bunki[y,x] = 3
      
            g[y,x] = num_max

    y, x = 2, 2
    route[y,x] = 1
  
    while True:
        if bunki[y,x] == 1:
            route[y,x-1] = 1
            x-=1
        if bunki[y,x] == 3:
            route[y-1,x] = 1
            y-=1
        if x<=0 and y<=0:
            break


    print(g)
    print(route)
    print(bunki)


    """
    a_11 = 0.6
    a_12 = 0.4
    a_22 = 0.7
    a_2e = 0.3

    b_1R = 0.6
    b_1B = 0.4
    b_2R = 0.5
    b_2B = 0.5
    
    alpha_1 = a_11 * b_1R * a_11 * b_1B * a_11 * b_1B * a_12 * b_2B * a_2e
    alpha_2 = a_11 * b_1R * a_12 * b_2B * a_22 * b_2B * a_22 * b_2B * a_2e
    alpha_3 = a_11 * b_1R * a_11 * b_1B * a_22 * b_2B * a_22 * b_2B * a_2e

    print(alpha_1)
    print(alpha_2)
    print(alpha_3)

    E = max(alpha_1, alpha_2)
    E = max(E, alpha_3)

    print(E)
    """

def main():

    HMM()

if __name__ == "__main__":
  
    main() 
