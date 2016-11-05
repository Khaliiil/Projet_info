# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as plt


class ODE_1():
    
    def __init__(self, fonction, CI):
        self.f = fonction
        self.y_0 = CI

    def Euler(self, t, N) :
        
        alpha = int(raw_input("Entrez alpha : "))
        beta = int(raw_input("Entrez beta : "))
        gamma = int(raw_input("Entrez gamma : "))
        delta = int(raw_input("Entrez delta : "))
        t0 = 0
        h = (t-t0)/float(N)
        t = t0
        y = self.y_0[1]
        x = self.y_0[0]
        z = [x, y]
        temps = [t0]
        fonction1 = [x]
        fonction2 = [y]
        for i in range(N) :
            x = x + h*self.f(z, alpha, beta, gamma, delta)[0]
            y = y + h*self.f(z, alpha, beta, gamma, delta)[1]
            z = [x, y]
            t = t+h
            temps.append(t)
            fonction1.append(x)
            fonction2.append(y)
        plt.plot(temps, fonction1)
        plt.plot(temps, fonction2)
    
    def Runge_Kutta(t, N):
        pass
    

    
def F(x, y):
    y = -3*y
    return y
    
#Nous allons ici tenter de définir la fonction qui représente notre sys. différentiel avec des valeurs prises au hasard pour les coeffs

# x est une liste
def P_P(x, alpha, beta, gamma, delta):
    liste = list()
    partie1 = alpha*x[0] - beta*x[0]*x[1]
    partie2 = -gamma*x[1] + delta*x[0]*x[1]
    liste.append(partie1)
    liste.append(partie2)
    return liste
 
   
    
A = ODE_1(P_P, [5, 3])
A.Euler(10, 100000)

#x = np.linspace(0, 5, 5)
#y = np.exp(x)
#plt.plot(x, y)
