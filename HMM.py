#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from hmmlearn import hmm

def HMM():

    #hmm_model = hmm.GaussianHMM(n_components=3, covariance_type="full")

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

def main():

    HMM()

if __name__ == "__main__":
  
    main() 
