# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ODE_1():
    def __init__(self, f, CI):
        self.f = f
        self.y_0 = CI

    def Euler(self, t, N):
        """ Compute the Euler scheme for the current ordinary differential
    equation"""
        t0 = 0
        h = (t-t0)/float(N)
        liste_solutions = list()#Liste des solutions courrante. Cette liste contient toujours le même nombre d'élément que le systeme courrant.
        liste_finale = list()#Liste contenant les listes de solution approximées
        for i in self.y_0:
            liste_solutions.append(i)
            liste_finale.append([i])
        t = t0
        temps = [t0]
        for i in range(N):
            systeme = self.f(liste_solutions)
            for y in range(len(systeme)):
                liste_solutions[y] = liste_solutions[y] + h*systeme[y]
            t = t+h
            temps.append(t)
            for y in range(len(liste_finale)):
                liste_finale[y].append(liste_solutions[y])            
                
        return temps, liste_finale    

    def Runge_Kutta(self, t, N):
        """ Compute the Runge-Kutta 4 scheme for the current ordinary differential
    equation"""
        t0 = 0
        h = (t-t0)/float(N)
        liste_solutions = list()#Liste des solutions courrante. Cette liste contient toujours le même nombre d'élément que le systeme courrant.
        liste_finale = list()#Liste contenant les listes de solution approximées
        for i in self.y_0:
            liste_solutions.append(i)
            liste_finale.append([i])
        t = t0
        temps = [t0]
        for i in range(N):
            liste_k = [[], [], [], []]
            systeme = self.f(liste_solutions)
            for y in range(len(systeme)):
                liste_k[0].append(systeme[y])
                liste_solutions[y] = liste_finale[y][-1] + h*liste_k[0][y]/2

            systeme = self.f(liste_solutions)
            for y in range(len(systeme)):
                liste_k[1].append(systeme[y])
                liste_solutions[y] = liste_finale[y][-1] + h*liste_k[1][y]/2

            systeme = self.f(liste_solutions)
            for y in range(len(systeme)):
                liste_k[2].append(systeme[y]) 
                liste_solutions[y] = liste_finale[y][-1] + h*liste_k[2][y]
                
            systeme = self.f(liste_solutions)
            for y in range(len(systeme)):
                liste_k[3].append(systeme[y])
                liste_solutions[y] = liste_finale[y][-1] + (h/6)*(liste_k[0][y] + 2*liste_k[1][y] + 2*liste_k[2][y] + liste_k[3][y])

            t = t+h
            temps.append(t)
            for y in range(len(liste_finale)):
                liste_finale[y].append(liste_solutions[y])

        return temps, liste_finale

###############################################################################

class EvolutionSystem():
        
    def approx_Euler(self, f,  CI):
        """compute the approximations of the model via an Euler method"""
        approx = ODE_1(f, CI)
        temps = int(input("temps :"))
        iterations = int(input("itérations :"))
        resultats = approx.Euler(temps, iterations)
        
        return resultats

    def approx_Runge_Kutta(self, f, CI):
        approx = ODE_1(f, CI)
        temps = int(input("temps :"))
        iterations = int(input("itérations :"))
        resultats = approx.Runge_Kutta(temps, iterations)
        
        return resultats

    def show(self, f, CI):
        """Display the results of the approximation"""
        methode = input("Euler ou RK4 ? ")
        if methode == "Euler":
            resultats = self.approx_Euler(f, CI)
        elif methode == "RK4":
            resultats = self.approx_Runge_Kutta(f, CI)
        else:
            print ("Problème")

        app = QApplication(sys.argv)
        A = FenetreDessin(resultats)
        A.setGeometry(100, 100, 700, 600)
        A.show()
        app.exec()

###############################################################################

class FenetreDessin(QWidget):

    def __init__(self, resultats):#resulat doit être de longueur 2 et de type tuple
        QWidget.__init__(self)
        self.temps = resultats[0]
        self.effectifs = resultats[1]

    def dessiner_courbe(self, qp):
        # Comment tracer les axes x, y (à revoir). Pb à résoudre : l'origine
        
        #initialisation des couleurs
        vert = QColor(0, 150, 80)
        bleu = QColor(0, 0, 200)
        noir = QColor(0, 0, 0)

        #initialisation des coefficients
        BAS = 500
        GAUCHE = 50
        COEFF_ABSCISSE = 20
        COEFF_ORDONNEE = 20

        #Lignes abscisse et ordonnées
        point_abscisse1 = QPoint(0, BAS)
        point_abscisse2 = QPoint(GAUCHE + self.temps[-1]*COEFF_ABSCISSE, BAS)
        point_ordonnee1 = QPoint(GAUCHE, 0)
        point_ordonnee2 = QPoint(GAUCHE, BAS+GAUCHE)
        ligne_abscisse = QLine(point_abscisse1, point_abscisse2)
        ligne_ordonnee = QLine(point_ordonnee1, point_ordonnee2)
        qp.drawLine(ligne_abscisse)
        qp.drawLine(ligne_ordonnee)
        qp.drawText(GAUCHE - 10, BAS + 15, str(0))

        #Legendes
        rect_legende1 = QRect(GAUCHE + self.temps[int(len(self.temps)/2)]*COEFF_ABSCISSE, BAS + 50, 20, 20)
        qp.fillRect(rect_legende1, bleu)
        qp.setPen(bleu)
        qp.setFont(QFont("AnyStyle", 10))
        qp.drawText(GAUCHE + self.temps[int(len(self.temps)/2)]*COEFF_ABSCISSE + 60, BAS + 65, "Proies")
        rect_legende2 = QRect(GAUCHE + self.temps[int(len(self.temps)/2)]*COEFF_ABSCISSE, BAS + 75, 20, 20)
        qp.fillRect(rect_legende2, vert)
        qp.setFont(QFont("AnyStyle", 10))
        qp.drawText(GAUCHE + self.temps[int(len(self.temps)/2)]*COEFF_ABSCISSE + 60, BAS + 90, "Prédateurs")
        qp.setPen(noir)
                              
        for i in range(1, int(self.temps[-1])+2):#Axe des abscisses(numéros)
            qp.drawText(GAUCHE + i*COEFF_ABSCISSE, BAS+15, str(i))

        for i in range(1, 200): #Axe des ordonnées(numéros)
            qp.drawText(GAUCHE - 20, BAS-i*COEFF_ORDONNEE, str(i))    
                    
        
        for i in range(len(self.temps)-1):#Courbes especes
            for y in range(len(self.effectifs)):
                if self.effectifs[y][i]*COEFF_ORDONNEE > 2000:
                    break
                point1 = QPoint(GAUCHE + self.temps[i]*COEFF_ABSCISSE, BAS-self.effectifs[y][i]*COEFF_ORDONNEE)
                point2 = QPoint(GAUCHE + self.temps[i+1]*COEFF_ABSCISSE, BAS-self.effectifs[y][i+1]*COEFF_ORDONNEE)
                ligne = QLine(point1, point2)
                if y == 0:
                    qp.setPen(bleu)
                if y == 1:
                    qp.setPen(vert)
                if y == 2:
                    qp.setPen(noir)
                qp.drawLine(ligne)
            
        
    def paintEvent(self, event):
        """
        paintEvent est appelée chaque fois qu'il faut redessiner la fenêtre
        """
        qp = QPainter(self)
        self.dessiner_courbe(qp)
        
            
################################################################################

class ProiePredateur(EvolutionSystem):
    def __init__(self, alpha, beta, gamma, delta, zeta, mu):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.zeta = zeta
        self.mu = mu


    def systeme(self, x):
        """is the function that gives the differentiel system
        :return value: a list of length 2
        """
        liste = list()
        partie1 = self.alpha*x[0] - self.beta*x[0]*x[1]*x[2]
        partie2 = -self.gamma*x[1] + self.delta*x[0]*x[1]
        partie3 = -self.zeta*x[2] + self.mu*x[0]*x[2]
        liste.append(partie1)
        liste.append(partie2)
        liste.append(partie3)
        return liste




if __name__ == '__main__':

    A = ProiePredateur(2, 1 ,1 ,1, 1, 1)
    A.show(A.systeme, [1, 6, 5])




#class ProieMilieuPredateur(EvolutionSystem):
#    def __init__(self, ...):
#        pass
#
#    def f(self, x):
#        """is the function that gives the differentiel system"""
#        pass
