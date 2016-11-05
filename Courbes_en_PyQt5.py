#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Khalil MAHFOUDH

import sys
import random
# Chargement des bibliothèques Qt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def dessiner_grille(qp):

    # Comment tracer les axes x, y (à revoir). Pb à résoudre : l'origine
    """             
    point = QPoint(10, 10)
    point2 = QPoint(10, 400)
    point3 = QPoint(5, 395)
    point4 = QPoint(600, 395)
    ligne = QLine(point, point2) 
    ligne2 = QLine(point3, point4)
    qp.drawLine(ligne)
    qp.drawLine(ligne2)
    """
    #Traçage des données
    vert = QColor(0, 150, 80)
    bleu = QColor(0, 0, 200)
    
    for i in range(len(temps)-1):
        point1 = QPoint(temps[i]*50, 200-fonction1[i]*10)
        point2 = QPoint(temps[i+1]*50, 200-fonction1[i+1]*10)
        point3 = QPoint(temps[i]*50, 200-fonction2[i]*10)
        point4 = QPoint(temps[i+1]*50, 200-fonction2[i+1]*10)
        ligne = QLine(point1, point2)
        ligne2 = QLine(point3, point4)
        qp.setPen(bleu)
        qp.drawLine(ligne)
        qp.setPen(vert)
        qp.drawLine(ligne2)

    
class FenetreDessin(QWidget):


    def paintEvent(self, event):
        """
        paintEvent est appelée chaque fois qu'il faut redessiner la fenêtre
        """
        qp = QPainter(self)
        dessiner_grille(qp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    temps = [0, 0.05, 0.1, 0.15000000000000002, 0.2, 0.25, 0.3, 0.35, 0.39999999999999997, 0.44999999999999996, 0.49999999999999994, 0.5499999999999999, 0.6, 0.65, 0.7000000000000001, 0.7500000000000001, 0.8000000000000002, 0.8500000000000002, 0.9000000000000002, 0.9500000000000003, 1.0000000000000002, 1.0500000000000003, 1.1000000000000003, 1.1500000000000004, 1.2000000000000004, 1.2500000000000004, 1.3000000000000005, 1.3500000000000005, 1.4000000000000006, 1.4500000000000006, 1.5000000000000007, 1.5500000000000007, 1.6000000000000008, 1.6500000000000008, 1.7000000000000008, 1.7500000000000009, 1.800000000000001, 1.850000000000001, 1.900000000000001, 1.950000000000001, 2.000000000000001, 2.0500000000000007, 2.1000000000000005, 2.1500000000000004, 2.2, 2.25, 2.3, 2.3499999999999996, 2.3999999999999995, 2.4499999999999993, 2.499999999999999, 2.549999999999999, 2.5999999999999988, 2.6499999999999986, 2.6999999999999984, 2.7499999999999982, 2.799999999999998, 2.849999999999998, 2.8999999999999977, 2.9499999999999975, 2.9999999999999973, 3.049999999999997, 3.099999999999997, 3.149999999999997, 3.1999999999999966, 3.2499999999999964, 3.2999999999999963, 3.349999999999996, 3.399999999999996, 3.4499999999999957, 3.4999999999999956, 3.5499999999999954, 3.599999999999995, 3.649999999999995, 3.699999999999995, 3.7499999999999947, 3.7999999999999945, 3.8499999999999943, 3.899999999999994, 3.949999999999994, 3.999999999999994, 4.049999999999994, 4.099999999999993, 4.149999999999993, 4.199999999999993, 4.249999999999993, 4.299999999999993, 4.3499999999999925, 4.399999999999992, 4.449999999999992, 4.499999999999992, 4.549999999999992, 4.599999999999992, 4.6499999999999915, 4.699999999999991, 4.749999999999991, 4.799999999999991, 4.849999999999991, 4.899999999999991, 4.94999999999999, 4.99999999999999] 
    fonction1 = [5, 4.25, 3.54875, 2.949233046875, 2.472219750666958, 2.1128502466054297, 1.8533909771424504, 1.6735011878995398, 1.5554477693611957, 1.4856265962492046, 1.4543282513900542, 1.4549666049414836, 1.483302956453743, 1.5368280180747316, 1.6143141506891312, 1.7155053561495772, 1.8409073820728246, 1.9916466791721255, 2.169374617092824, 2.3761993026028025, 2.614631031562252, 2.8875289663811534, 3.198036175118043, 3.5494875632469145, 3.945269976788656, 4.3886048694451185, 4.8822097548412104, 5.427772671253635, 6.0251405009127685, 6.671072950740445, 7.357346458665813, 8.067912024596401, 8.774753282554645, 9.432174133510081, 9.969788083696338, 10.286206199751906, 10.249563163870397, 9.718342901502378, 8.601748086478551, 6.961964243262552, 5.089130870065465, 3.4043035159323782, 2.188078827530531, 1.4394226981994174, 1.0111005798895718, 0.7681695661581355, 0.6284080572866817, 0.5477819739668063, 0.5032001588918895, 0.4823443734766756, 0.47849824070447594, 0.48797779104548805, 0.5088310715338279, 0.5401598475110235, 0.5817555477055572, 0.6339003974425562, 0.6972593530470182, 0.7728244629206705, 0.861891232571476, 0.9660558398872358, 1.0872270020302608, 1.2276490313031898, 1.3899341676632049, 1.577103161120745, 1.7926335602250383, 2.0405153653018884, 2.3253136620817316, 2.652237527899875, 3.0272137853518424, 3.4569628390214846, 3.949071448339793, 4.512053094295158, 5.155379168578606, 5.889450876395292, 6.725457354543089, 7.675019946934141, 8.749435525521779, 9.958161632038564, 11.30584714412731, 12.78652735549258, 14.372221186786932, 15.990476158216167, 17.480755106683336, 18.51463170834151, 18.47580892878562, 16.397680001484105, 11.438075231154269, 4.770489384573732, 0.6892972522419791, 0.07289681888514266, 0.020310108347242284, 0.009133770774449282, 0.005380350584156944, 0.0037715872321267183, 0.002982094004211277, 0.0025719696662383357, 0.00236604220510793, 0.0022854017395986903, 0.0022916003877623244, 0.0023652821989337876, 0.0024970494482464004]
    fonction2 = [3, 3.15, 3.189375, 3.1174147265625, 2.953630907869646, 2.7280059596265027, 2.470598170928099, 2.205427754649618, 1.9488815020813322, 1.7106743709231509, 1.495610663886786, 1.3052439731879684, 1.1391494981648562, 0.9958047894554214, 0.8731628666127421, 0.7690082518616554, 0.681168490238919, 0.6076331972969465, 0.5466160898151174, 0.4965836253790663, 0.4562659835187385, 0.424661146772709, 0.401039985528309, 0.38495900749206463, 0.3762875664662997, 0.37525785510395765, 0.3825492065935041, 0.39942363868168185, 0.42793794645980143, 0.4712696698224606, 0.5342094532008184, 0.6238857639952967, 0.7507813840618457, 0.9300211779633566, 1.1826230272908127, 1.5356234700820919, 2.0182857589878207, 2.648955975664545, 3.406337905656228, 4.190093352618873, 4.810638686938334, 5.07260944187212, 4.921522661393548, 4.475652105845185, 3.9026394461960274, 3.319409607314258, 2.783021157748993, 2.313860572155633, 1.9144630133094753, 1.579738315272079, 1.3018895466145137, 1.0726592301739406, 0.8842990782233942, 0.7299372049551546, 0.6036639024301836, 0.5004903631535642, 0.416255342528812, 0.3475161705647498, 0.29144138634544736, 0.24571264786133876, 0.20843872520910112, 0.17808199068308592, 0.15339670171420045, 0.13337792721733077, 0.11721987930577386, 0.10428251792307203, 0.09406551834617752, 0.08618900642400033, 0.08038089100570713, 0.07647121987113273, 0.07439488416436355, 0.07420544297929255, 0.07610529931384703, 0.08050182318612996, 0.08810703520465256, 0.10011363355892791, 0.11850961357338367, 0.146652302014448, 0.1903412079700788, 0.2598713965029759, 0.3740397532171488, 0.568020905868122, 0.9085629623271254, 1.5209687020338623, 2.624783729530649, 4.524577116934199, 7.329290078823585, 10.055080628685706, 10.442447272957471, 8.713855328962543, 7.00284487985537, 5.609387330796736, 4.490071607540618, 3.5932651940023215, 2.8752897708582243, 2.3006605359058816, 1.8408242901802383, 1.4728772055423283, 1.1784700702402506, 0.942911085315697, 0.7544403807928213]
    fenetre = FenetreDessin()
    fenetre.show()
    app.exec()
