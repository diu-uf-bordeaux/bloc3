---
layout: article
title: Système d'exploitation - StarWars
---

L'ensemble des exercices qui suivent reposent sur l'utilisation de l'arborescence de fichier inclue dans cette [archive](./starwars.tar.gz). Il est donc nécessaire de commencer par télécharger cette archive et de la décompresser dans votre répertoire de travail préféré.

L'arborescence est structurée comme suit:
  * un premier niveau de répertoires pour les régions de la galaxie,
  * un deuxième niveau de répertoires représentant chaque planète de cette région,
  * et enfin chacun des ces répertoires (planète) contient un ensemble de fichiers:
      * 1 fichier `Description` décrivant la planète
	  * 1 fichier pour chaque apparition de la planète dans un titre de la franchise
	  
Chaque fichier de _Description_ est du type:

~~~sh
> cat Colonies/Fondor/Description 
Type: Planète tellurique
Paysage: Déserts et terres en friche
Especes: Humains
Description:
Imperial manufacturing center with large shipyards. 
~~~

Tout autre fichier dans les répertoires de chaque planète ont un nom du type `XXXX-titre`, avec `XXXX` l'année de sortie du `titre`. Le contenu est un simple mot-clé décrivant le type de média du titre dans la liste ci-dessous:

~~~
Book
Comic
Film
Novella
Short story
Theme park
TV film
TV micro-series
TV series
Video game
VR game
~~~


## Utilisation de motifs

Entrainez-vous a lister les titres sortis sur une période de temps définie.

Par exemple, tous les titres des années 70s serait:

~~~
Bordure-Exterieure/Dantooine/1977-A_New_Hope
Bordure-Exterieure/Kessel/1977-Star_Wars
Bordure-Exterieure/Tatooine/1977-A_New_Hope
Bordure-Exterieure/Yavin/1977-Star_Wars
Bordure-Exterieure/Yavin-IV/1977-Star_Wars
Bordure-Mediane/Kashyyyk/1978-Star_Wars_Holiday_Special
Mondes-du-Noyau/Alderaan/1977-A_New_Hope
Mondes-du-Noyau/Corellia/1977-A_New_Hope
Zone-d_expansion/Mimban/1978-Star_Wars_Legends:_Splinter_of_the_Mind_s_Eye
~~~

## Travail sur les arguments et les tests dans les scripts

Lister les apparitions d'une planète en utiliant un script.

Ce script prendra deux arguments en paramètre. Une _région_ et une
_planete_ et retournera la liste des apparitions si la région existe, et
si la planète existe dans cette région.

On s'assurera de renvoyer:

 * `Region missing` si on passe aucun paramètre au script
 * `Planet missing` si on ne passe qu'un seul paramètre au script
 * `Region unknown` si la région n'existe pas
 * `Planet unknown` si la planète n'existe pas

Pour aller plus loin:

	* retourner le nombre de ces apparitions
	* limiter le listing uniquement à un type de media
	* ...
	
## Utilisation d'analyse de la taille des répertoires

Trouver la commande qui permet d'afficher la taille de chaque région de la galaxie.

Pour aller plus loin:

	* Trier les régions de la galaxie par taille
    * Afficher uniquement la région la plus grande (la plus petite)
	

