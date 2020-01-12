#include "HX711.h"
#include <Adafruit_NeoPixel.h>
#define BUTTON_PIN   2

// HX711.DOUT	- pin #A1
// HX711.PD_SCK	- pin #A0

HX711 scale(A1, A0);
Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 3, NEO_GRB + NEO_KHZ800);

void setup() 
{
  Serial.begin(38400); 
  // Setup du bouton
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  strip.begin();
  strip.clear();
  strip.show(); // Initialize all pixels to 'off'

  // Setup du capteur de poids
  scale.set_scale(2280.f);               
  scale.tare();
}


// Variables globales
float f_pesee_old;
float f_pesee;
int i;
bool b_newState_old;
bool b_newState;

void loop() 
{
  b_newState_old=false;
  f_pesee_old=0;

  // Lecture du poids par le capteur
  f_pesee=-scale.get_units(10);

  // Action uniquement si la pesée est pertinente
  if (abs(f_pesee) > 0.2)
  {
    // Boucle tant que la pesée n'est pas terminée
    while (abs(f_pesee_old-f_pesee)>0.2)
    {
      f_pesee_old=f_pesee;
      delay(1000);
      f_pesee=-scale.get_units(10);
    }
    // Envoi de la mesure
    Serial.println(f_pesee);
    // Boucle pour le bouton
    for (i=0;i<10;i++)
    {
      b_newState = digitalRead(BUTTON_PIN);
      if (b_newState) break;
      delay(500);
    }

    // Envoi d'une chaine de caractère en fonction de la valeur du bouton
    if (b_newState)
    {
      Serial.println("oui");
      delay(3000);
    }
    else
    {
      Serial.println("non");
    }
  }
  scale.tare();
  delay(2000);
}


