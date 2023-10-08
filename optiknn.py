#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:26:23 2022

@author: enzobergamini
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import neighbors, metrics

def graph():
    data = pd.read_excel("BDD/bdd.xlsx")
    x=data[data.columns[:-1]].values
    y=data['masque']
    
    Y=[k for k in range(101)]
    
    Xb=[0 for i in range(101)]
    Xp=[0 for i in range(101)]
    
    for i in range(len(x)):
        Xb[int(x[i][1])]=Xb[int(x[i][1])]+1
        Xp[int(x[i][0])]=Xp[int(x[i][0])]+1
    
    fig, axes = plt.subplots(ncols=2) 
    axes[0].bar(Y,Xb)
    axes[0].set_xlabel("pixels de teinte bleu (% de l'image)")
    axes[0].set_ylabel("nombre d'images sur 2114")
    
    Xp[0]=0
    Xp[1]=0
    
    axes[1].bar(Y,Xp)
    axes[1].set_xlabel("pixels de teinte peau (% de l'image)")
    
    
    plt.savefig("001.png",dpi=500)
    plt.show()
    
def graph2():
    data = pd.read_excel("BDD/bdd3.xlsx")
    x=data[data.columns[:-1]].values
    y=data['masque']
    
    Y=[k for k in range(101)]
    
    Xtot=[0 for i in range(101)]
    Xteinte=[0 for i in range(101)]
    Xgris=[0 for i in range(101)]

    
    for i in range(len(x)):
        Xtot[int((x[i][0]/360)*100)]=Xtot[int((x[i][0]/360)*100)]+1 
        Xteinte[int((x[i][1]/360)*100)]=Xteinte[int((x[i][1]/360)*100)]+1
        Xgris[int((x[i][2]/360)*100)]=Xgris[int((x[i][2]/360)*100)]+1
    
    fig, axes = plt.subplots(ncols=3) 
    axes[0].bar(Y,Xtot)
    axes[0].set_ylabel("nombre d'images sur 693")
    
    
    
    axes[1].bar(Y,Xteinte)
    
    axes[2].bar(Y,Xgris)
    
    
    plt.savefig("002.png",dpi=500)
    plt.show()
  
def opti2():
    data = pd.read_excel("BDD/bdd3.xlsx")
    x=data[data.columns[:-1]].values
    y=data['masque']
    y_class=np.where(y==0,0,1)
        
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y_class, test_size=0.3)
    
    # Fixer les valeurs des hyperparamètres à tester
    param_grid = {'n_neighbors':[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]}
    
    # Choisir un score à optimiser, ici l'accuracy (proportion de prédictions correctes)
    score = 'accuracy'
    
    # Créer un classifieur kNN avec recherche d'hyperparamètre par validation croisée
    clf = model_selection.GridSearchCV(neighbors.KNeighborsClassifier(), param_grid, cv=5, scoring=score)
    
    clf.fit(x_train, y_train)
    
    # Afficher le(s) hyperparamètre(s) optimaux
    print("Meilleur(s) hyperparamètre(s) sur le jeu d'entraînement:")
    print(clf.best_params_)
    
    # Afficher les performances correspondantes
    print("Résultats de la validation croisée :")
    for mean, std, params in zip(
            clf.cv_results_['mean_test_score'], # score moyen
            clf.cv_results_['std_test_score'],  # écart-type du score
            clf.cv_results_['params']           # valeur de l'hyperparamètre
        ):
    
        print("{} = {:.3f} (+/-{:.03f}) for {}".format(
            score,
            mean,
            std*2,
            params
        ) )
    return list(clf.best_params_.values())[0]
        
def opti1():
    data = pd.read_excel("BDD/bdd.xlsx")
    x=data[data.columns[:-1]].values
    y=data['masque']
    y_class=np.where(y==0,0,1)
        
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y_class, test_size=0.3)
    
    # Fixer les valeurs des hyperparamètres à tester
    param_grid = {'n_neighbors':[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]}
    
    # Choisir un score à optimiser, ici l'accuracy (proportion de prédictions correctes)
    score = 'accuracy'
    
    # Créer un classifieur kNN avec recherche d'hyperparamètre par validation croisée
    clf = model_selection.GridSearchCV(neighbors.KNeighborsClassifier(), param_grid, cv=5, scoring=score)
    
    clf.fit(x_train, y_train)
    
    # Afficher le(s) hyperparamètre(s) optimaux
    print("Meilleur(s) hyperparamètre(s) sur le jeu d'entraînement:")
    print(clf.best_params_)
    
    # Afficher les performances correspondantes
    print("Résultats de la validation croisée :")
    for mean, std, params in zip(
            clf.cv_results_['mean_test_score'], # score moyen
            clf.cv_results_['std_test_score'],  # écart-type du score
            clf.cv_results_['params']           # valeur de l'hyperparamètre
        ):
    
        print("{} = {:.3f} (+/-{:.03f}) for {}".format(
            score,
            mean,
            std*2,
            params
        ) )
    return list(clf.best_params_.values())[0]

def choix1(n): 
    L=[0 for i in range(22)]
    for i in range(n):
        L[opti1()]+=1
    m=max(L)
    for i in range(len(L)):
        if L[i]==m:
            return i,L
        