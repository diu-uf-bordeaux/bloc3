#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
  lcd.init();
  Serial.begin(115200);
}

void loop()
{
  lcd.backlight();
  String str = Serial.readStringUntil('\n');
  if (str != "") {
   lcd.clear();
   lcd.setCursor(0, 0);
   lcd.print(str);
  }
}
