# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def Euler(F, t0, tf, y0, n) :
    t = t0
    y = y0
    h = (tf-t0)/float(n)
    temps = [t0]
    solution = [y0]
    for i in range(n) :
        y = y + h*F(t, y)
        t = t+h
        temps.append(t)
        solution.append(y)
    plt.plot(temps, solution)
    return solution
    
def F(t, y):# Codage de l'équation différentielle y'(t) = -3y(t)
    y = -3*y
    return y
    
    
Euler(F, 0, 5, 1, 1000)


 
