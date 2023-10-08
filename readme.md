# Face mask detector

## Description

Ce projet à été réalisé dans le cadre du TIPE (Travail d'Initiative Personnelle Encadré) de la classe préparatoire MPSI du lycée Robespierre d'Arras. Il a pour but de détecter si une personne porte un masque ou non à partir d'une image.

## Ancrage du sujet au thèmes de l’année

Le masque chirurgical est un outil primordial pour prévenir la crise sanitaire actuelle, or si il n’est pas porté ou mal porté dans les lieux publics, il perd son utilité. Pouvoir vérifier que tout le monde porte correctement son masque permet donc la prévention d’une avancée de l ‘épidémie.

## Motivation du choix de l’étude

Le traitement d’image et plus précisément la détection d’objet fera,selon moi, partie de notre futur et fait déjà partie de notre présent. Faire un sujet sur ce thème m’intéressait donc grandement. De plus, la crise sanitaire actuelle m’a donné l’idée de faire un sujet sur la détection de masque.

## Description du projet 

L’objectif de ce projet est de pouvoir détecter si une personne porte un masque ou non à partir d’une image. Pour cela, nous allons utiliser la méthode knn (k-nearest neighbors) qui est une méthode d’apprentissage supervisé. Cette méthode consiste à comparer la nouvelle image à classifier avec les images de la base de données et de lui attribuer la classe de l’image la plus proche. Pour cela, nous allons devoir constituer une base de données d’images de personnes portant un masque et d’autres n’en portant pas. 

### Préparation de la base de données

Comme le nombre d'image de personnes portant un masque est limité, nous allons utiliser un algorithme qui permet de prendre des images de personnes ne portant pas de masque et de leur ajouter un masque. Nous allons ensuite utiliser un algorithme de détection de visage pour ne garder que le visage de la personne.