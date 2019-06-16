// Ceci est un commentaire (commence par //), ne sera pas interprété
// Comme ce qui commence par "#" en Python

// Dans cet exemple, on suppose qu'on a branché 3 LEDs sur les broches 7 8 et 9
// et un bouton sur la broche 10
// On allume à tour de rôle chacune des LEDs, en passant à la suivante lorsque
// le bouton est appuyé

// On déclare un entier (int) "N" global (accessible dans toutes les
// fonctions)
int N;

// Un tableau de 3 éléments initialisé avec 7, 8 et 9
int leds[3] = {7, 8, 9};

// La broche du bouton est la 10
int bouton = 10;

// Fonction "setup", qui sera appellée une fois au début
void setup(){
  // Ouverture de la communication série
  Serial.begin(115200);

  // Initialisation de variables
  N = 0;

  // Cette boucle sera executée pour k=0, k=1 et k=2 (boucle "for")
  for (int k=0; k<3; k++) {
    // On met les broches correspondantes à celles du tableau "leds" en
    // sortie
    pinMode(leds[k], OUTPUT);
  }

  // Le bouton est mis en entrée, avec la résistance "Pull-Up" interne
  // Dans ce cas, l'autre côté du bouton (qui est connecté quand on appuie dessus)
  // devra être branché à la masse
  pinMode(bouton, INPUT);
  digitalWrite(bouton, HIGH);
}

// Fonction "loop" (boucle), qui sera appellée en boucle
void loop(){
  N = N+1;
  Serial.println("Boucle!");

  // On décide ici quelle LED sera allumée
  // Avec l'opérateur modulo, on aura donc 0, 1, 2, 0, 1, 2 etc.
  int ledAllumee = N%3;

  // Affichera par exemple:
  // Itération 123, la led #0 sera allumée[retour à la ligne]
  Serial.print("Itération: ");
  Serial.print(N);
  Serial.print(" la LED #");
  Serial.print(ledAllumee);
  Serial.print(" sera allumée");
  Serial.println();
  
  // Encore une fois, pour k de 0 à 2 inclu
  for (int k=0; k<3; k++) {
    if (k == ledAllumee) { // Si k est le numéro de la LED allumée, on
      // la met à "HIGH"
      digitalWrite(leds[k], HIGH);
    } else { // Sinon à "LOW"
      digitalWrite(leds[k], LOW);
    }
  }

  // Tant que le bouton n'est pas appuyé, on attend
  while (digitalRead(bouton) == HIGH) {
    delay(10); // Attend 10 ms
  }

  // Maintenant, on attend que le bouton soit relâché
  while (digitalRead(bouton) == LOW) {
    delay(10); // Attend 10 ms
  }
}
