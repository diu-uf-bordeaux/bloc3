int N = 0;

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  N += 1;
  Serial.print("N=");
  Serial.print(N);
  Serial.println(N);
  delay(10);
}


