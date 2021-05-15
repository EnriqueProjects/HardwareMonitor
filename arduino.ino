#include <LiquidCrystal.h>
LiquidCrystal ecran(12,11,5,4,3,2);

String informations;
bool ligne = 0;

void setup() {
  digitalWrite(8,HIGH);
  ecran.begin(16,2); 
  ecran.clear(); 
  Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char input = Serial.read();
        if(input == '/')
          decodInfos();
        else if (input == 'D')
          informations += (char)223;
        else
          informations += (String)input;
    }

}

void decodInfos(){
  ecran.print(informations);
  informations = "";
  ligne = !ligne;
  ecran.setCursor(0,ligne);
}
