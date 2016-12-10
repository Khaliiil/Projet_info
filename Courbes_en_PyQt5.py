#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Khalil MAHFOUDH

import sys
# Chargement des bibliothèques Qt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Code_khalil import *



    
class FenetreDessin(QWidget):

    def __init__(self, temps, proies, predateurs):
        QWidget.__init__(self)
        self.temps = temps
        self.proies = proies
        self.predateurs = predateurs

    def dessiner_courbe(self, qp):
        # Comment tracer les axes x, y (à revoir). Pb à résoudre : l'origine
        
        #initialisation des couleurs
        vert = QColor(0, 150, 80)
        bleu = QColor(0, 0, 200)
        noir = QColor(0, 0, 0)

        #initialisation des coefficients
        BAS = 500
        GAUCHE = 50
        COEFF_ABSCISSE = 50
        COEFF_ORDONNEE = 50

        #Lignes abscisse et ordonnées
        point_abscisse1 = QPoint(0, BAS)
        point_abscisse2 = QPoint(GAUCHE + self.temps[-1]*COEFF_ABSCISSE, BAS)
        point_ordonnee1 = QPoint(GAUCHE, BAS-(int(max(max(self.proies), max(self.predateurs)))+1)*COEFF_ORDONNEE)
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
        
                              
        for i in range(1, int(self.temps[-1])+2):#Axe des abscisses(numéros)
            qp.drawText(GAUCHE + i*COEFF_ABSCISSE, BAS+15, str(i))

        for i in range(1, int(max(max(self.proies), max(self.predateurs)))+2): #Axe des ordonnées(numéros)
            qp.drawText(GAUCHE - 10, BAS-i*COEFF_ORDONNEE, str(i))    
                    
        
        for i in range(len(self.temps)-1):#Courbes proies prédateur
            point1 = QPoint(GAUCHE + self.temps[i]*COEFF_ABSCISSE, BAS-self.proies[i]*COEFF_ORDONNEE)
            point2 = QPoint(GAUCHE + self.temps[i+1]*COEFF_ABSCISSE, BAS-self.proies[i+1]*COEFF_ORDONNEE)
            point3 = QPoint(GAUCHE + self.temps[i]*COEFF_ABSCISSE, BAS-self.predateurs[i]*COEFF_ORDONNEE)
            point4 = QPoint(GAUCHE + self.temps[i+1]*COEFF_ABSCISSE, BAS-self.predateurs[i+1]*COEFF_ORDONNEE)
            ligne = QLine(point1, point2)
            ligne2 = QLine(point3, point4)
            qp.setPen(bleu)
            qp.drawLine(ligne)
            qp.setPen(vert)
            qp.drawLine(ligne2)
        
    def paintEvent(self, event):
        """
        paintEvent est appelée chaque fois qu'il faut redessiner la fenêtre
        """
        qp = QPainter(self)
        self.dessiner_courbe(qp)

def signal():
    global i
    global fenetre

    
    i += 1000
    temps, proies, predateurs = A.Euler(25, i)
    fenetre = FenetreDessin(temps, proies, predateurs)
    fenetre.setGeometry(100, 100, 700, 600)
    fenetre.setWindowTitle("Modèle proie-prédateur")
    fenetre.show()
    print (i)
        
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    alpha = int(input("Entrez alpha : "))
    beta = int(input("Entrez beta : "))
    gamma = int(input("Entrez gamma : "))
    delta = int(input("Entrez delta : "))
    i = 1000
    def f(x):
        global alpha, beta, gamma, delta
        return P_P(x, alpha, beta, gamma, delta)
    
    A = ODE_1(f, [1, 1])
    #temps, proies, predateurs = A.Euler(10, 10000)
    #fenetre = FenetreDessin(temps, proies, predateurs)
    #fenetre.setWindowTitle("Modèle proie-prédateur")
    
    
    timer = QTimer()
    timer.timeout.connect(signal)
    timer.start(1000)
    

    app.exec()
