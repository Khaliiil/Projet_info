# -*- coding: utf-8 -*-


class ODE_1():
    
    def __init__(self, systeme, CI):
        self.f = systeme
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
            systeme = self.f(z)
            x = x + h*systeme[0]
            y = y + h*systeme[1]
            z = [x, y]
            t = t+h
            temps.append(t)
            fonction1.append(x)
            fonction2.append(y)
        return fonction1, fonction2, fonction2 

    def Runge_Kutta(t, N):
        pass

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
    alpha = 3
    beta = 2
    gamma = 4
    delta = 1

    def f(x):
        global alpha, beta, gamma, delta
        return P_P(x, alpha, beta, gamma, delta)

    A = ODE_1(f, [5, 3])
    A.Euler(10, 100000)
#A = ODE_1(P_P, [5, 3])

########################################################################
#def F(x, y):
#    y = -3*y
#    return y

#x = np.linspace(0, 5, 5)
#y = np.exp(x)
#plt.plot(x, y)
 
