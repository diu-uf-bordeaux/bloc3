---
layout: article
title: Architectures matérielles et robotique, systèmes et réseaux
---

- [Architecture des circuits](./archi)
- [Robotique et systèmes embarqués](./robot)
- [Systèmes d'exploitation](#)
- [Réseaux](https://moodle1.u-bordeaux.fr/course/view.php?id=4713)

## Suggestion de thématiques pour le projet

### Architecture des circuits
- Représentation binaire des entiers relatifs
- Notion de test et de branchement conditionnel
- Réalisation des boucles usuelles en assembleur (for, while, do-while)
- Manipulation des tableaux
- La pile et l'appel de fonctions
- L'unité arithmétique et logique d'un processeur
- Implémentation des registres dans un processeur
- ...

### Robotique et systèmes embarqués

#### SOCs

- Comparaison de différents types de SOCs
- Définition d'un cas d'usage et choix et justification du SOC adapté (exemple : choix du SOC pour un pilotage de capteur de son)
- Etude comparative de différents modèles de SOCs Arduino

#### Capteurs

- Captation d'une donnée numérique
- Captation d'une donnée analogique
- Fabrication et test d'un capteur
- Intégration d'un capteur, filtre de Kalman

#### Actuateurs

- Contrôle d'une LED
- Contrôle d'un servo moteur asservi à un capteur donné (exemple : fermeture d'un volet quand la nuit tombe)

#### Systèmes intégrés

- Création d'un dispositif multi-capteurs pour réaliser une fonction donnée (exemple : capteur de détection de son et de lumière, type système d'alarme)
- Création d'un robot mobile autonome
- Arbre de Noel à base de LEDs (clignotement)
- Détecteur d'ouverture de porte
- Système "fuyant" en présence de bruit/lumière

### Systèmes d'exploitation
- L'arborescence de fichier: parcourir, créer/détruire des répertoires/fichiers
- Les droits d'accès aux fichiers
- Les appels systèmes
- Partage des ressources:
  - Ordonnancement des processus (intérêt de mettre des processus en attente)
  - Partage de la mémoire
- La création de processus
- Mémoire virtuelle 

### Réseaux
- Fiabilisation des communications : code détecteur d'erreurs. Du bit de parité (simple et double) au CRC
- Fiabilisation des communications : du bit alterné au numéro de séquence TCP
- Internet décentralisé et le routage
- Paiement sécurisé sur Internet (HTTPS)
- Encapsulation des protocoles : exemple de HTTP
- Sous-réseaux IP
- IPv6
