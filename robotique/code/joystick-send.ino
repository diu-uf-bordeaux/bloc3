void setup()
{
  Serial.begin(115200);
}

void loop()
{
  Serial.print(analogRead(A4));
  Serial.print(" ");
  Serial.print(analogRead(A5));
  Serial.print(" ");
}
