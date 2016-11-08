# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


class ODE_1():
    
    def __init__(self, fonction, CI):
        self.f = fonction
        self.y_0 = CI

    def Euler(self, t, N) :
        t0 = 0
        h = (t-t0)/float(N)
        t = t0
        x = self.y_0[0]
        y = self.y_0[1]
        z = [x, y]
        temps = [t0]
        fonction1 = [x]
        fonction2 = [y]
        for i in range(N) :
            x = x + h*self.f(z)[0]
            y = y + h*self.f(z)[1]
            z = [x, y]
            t = t+h
            temps.append(t)
            fonction1.append(x)
            fonction2.append(y)
        #plt.plot(temps, fonction1)
        #plt.plot(temps, fonction2)
        plt.plot(fonction1, fonction2)
        plt.show()
    
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
 
if __name__ == '__main__':
    alpha = int(raw_input("Entrez alpha : "))
    beta = int(raw_input("Entrez beta : "))
    gamma = int(raw_input("Entrez gamma : "))
    delta = int(raw_input("Entrez delta : "))

    def f(x):
        global alpha, beta, gamma, delta
        return P_P(x, alpha, beta, gamma, delta)
    
    A = ODE_1(f, [5, 3])
    A.Euler(10, 10000)

#x = np.linspace(0, 5, 5)
#y = np.exp(x)
#plt.plot(x, y)
