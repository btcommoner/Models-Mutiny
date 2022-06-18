#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:26:46 2022

@author: btcommoner
"""

from matplotlib import pyplot as plt
import numpy as np

dt = np.array([
          [18, .4],
          [19, .5],
          [20, .6],
          [21, .6],
          [22, .6],
          [23, .6],
          [24, .6],
          [25, .7],
          [26, .7],
          [27, .7],
          [28, .7],
          [29, .8],
          [30, .8],
          [32, .95],
          [35, 1.0],
          [38, .8],
          [40, .7],
          [42, .6],
          [46, .4]
])

X = dt[:, 0]
y = dt[:, 1]

theta = np.polyfit(X, y, 4)

def smv_simps(X): 
    return theta[4]+ theta[3]* pow(X,1) + theta[2]* pow(X,2) + theta[1] * pow(X, 3) + theta[0] * pow(X, 4)

smv_simps_plot = theta[4]+ theta[3]* pow(X,1) + theta[2]* pow(X,2) + theta[1] * pow(X, 3) + theta[0] * pow(X, 4) 

dt2 = np.array([
          [18, .62],
          [19, .62],
          [20, .70],
          [21, .72],
          [22, .75],
          [23, .78],
          [24, .80],
          [25, .822],
          [26, .84],
          [27, .86],
          [28, .875],
          [29, .89],
          [30, .90],
          [32, .913],
          [35, .909],
          [38, .905],
          [40, .905],
          [42, .900],
          [46, .895]
])

X2 = dt2[:, 0]
y2 = dt2[:, 1]

omega = np.polyfit(X2, y2, 4)

marriage_success_plot_M = omega[4]+ omega[3]* pow(X2,1) + omega[2]* pow(X2,2) + omega[1] * pow(X2, 3) + omega[0] * pow(X2, 4) 

def marriage_success_M(X2):
    return omega[4]+ omega[3]* pow(X2,1) + omega[2]* pow(X2,2) + omega[1] * pow(X2, 3) + omega[0] * pow(X2, 4) 

dt3 = np.array([
          [18, .05],
          [19, .05],
          [20, .07],
          [21, .10],
          [22, .10],
          [23, .14],
          [24, .15],
          [25, .18],
          [26, .21],
          [27, .23],
          [28, .35],
          [29, .35],
          [30, .40],
          [32, .40],
          [35, .55],
          [38, .60],
          [40, .65],
          [42, .75],
          [46, .75]
])

X3 = dt3[:, 0]
y3 = dt3[:, 1]

sigma = np.polyfit(X3, y3, 4)

def gold_diggers(X3):
   return sigma[4]+ sigma[3]* pow(X3,1) + sigma[2]* pow(X3,2) + sigma[1] * pow(X3, 3) + sigma[0] * pow(X3, 4) 

gold_diggers_plot = sigma[4]+ sigma[3]* pow(X3,1) + sigma[2]* pow(X3,2) + sigma[1] * pow(X3, 3) + sigma[0] * pow(X3, 4) 

dt_w = np.array([
          [18, 7.5],
          [19, 8],
          [20, 9],
          [21, 10],
          [22, 10],
          [23, 9],
          [24, 8.5],
          [25, 7],
          [26, 6.5],
          [27, 5.5],
          [28, 5],
          [29, 4.5],
          [30, 4],
          [32, 3.5],
          [34, 2.5],
          [38, 1.5],
          [40, 1],
          [42, .5],
          [46, .25]
])

X4 = dt_w[:, 0]
y4 = dt_w[:, 1]/10.0

orange = np.polyfit(X4, y4, 4)

smv_hoes_plot = orange[4]+ orange[3]* pow(X4,1) + orange[2]* pow(X4,2) + orange[1] * pow(X4, 3) + orange[0] * pow(X4, 4) 

def smv_hoes(X): 
    return orange[4]+ orange[3]* pow(X,1) + orange[2]* pow(X,2) + orange[1] * pow(X, 3) + orange[0] * pow(X, 4) 


dt2 = np.array([
          [18, .68],
          [19, .68],
          [20, .68],
          [21, .72],
          [22, .75],
          [23, .78],
          [24, .80],
          [25, .822],
          [26, .84],
          [27, .86],
          [28, .875],
          [29, .89],
          [30, .90],
          [32, .913],
          [34, .905],
          [38, .905],
          [40, .905],
          [42, .900],
          [46, .895]
])

X5 = dt2[:, 0]
y5 = dt2[:, 1]

phi = np.polyfit(X5, y5, 4)

marriage_success_plot_W = phi[4]+ phi[3]* pow(X5,1) + phi[2]* pow(X5,2) + phi[1] * pow(X5, 3) + phi[0] * pow(X5, 4)

def marriage_success_W(X5):
    return phi[4]+ phi[3]* pow(X5,1) + phi[2]* pow(X5,2) + phi[1] * pow(X5, 3) + phi[0] * pow(X5, 4)

#SIMULATION
smv_weight = 5.0
marriage_success_weight = 5.0
gold_digger_weight = 1.0

solution_plot_M = smv_weight*smv_simps_plot + marriage_success_weight*marriage_success_plot_M - gold_digger_weight*gold_diggers_plot
solution_plot_W = smv_weight*smv_hoes_plot +marriage_success_weight*marriage_success_plot_W

def solution_M(X):
    return smv_simps(X) + marriage_success_weight * marriage_success_M(X) - gold_digger_weight*gold_diggers(X)

def solution_W(X):
    return smv_weight* smv_hoes(X) +marriage_success_weight * marriage_success_W(X)

def find_maxM():
    curr_maxM = 0
    curr_xM = 0 
    for n in range(18,50):
        y = solution_M(n)
        if (curr_maxM < y): 
            curr_maxM = y
            curr_xM = n
    return curr_xM

def find_maxW():
    curr_maxW = 0
    curr_xW = 0 
    for n in range(18,50):
        z = solution_W(n)
        if (curr_maxW < z): 
            curr_maxW = z
            curr_xW = n
    return curr_xW

optimal_age_M = find_maxM()
optimal_age_W = find_maxW()

print("The optimal marriage age for men is ", optimal_age_M)
print("The optimal marriage age for women is ", optimal_age_W)

#PLOTS
#Sexual Market Value (Will Stay the Same Every Time)
plt.plot(X, smv_simps_plot, 'b', color = "blue")
plt.plot(X4, smv_hoes_plot, 'b', color = "pink")
plt.title('Sexual Marketplace Value')
plt.xlabel('Age')
plt.ylabel('Attractiveness')
plt.show()

#Value of Marriage (Will Change with Weight Changes)
plt.title("Value of Marriage")
plt.plot(X4, solution_plot_W, 'pink')
plt.plot(X, solution_plot_M, 'blue') # plotting t, a separately 
plt.xlabel('Age')
plt.show()
