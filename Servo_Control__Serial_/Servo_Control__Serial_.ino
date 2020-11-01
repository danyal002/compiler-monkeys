#include <Servo.h>
Servo myservo;
String inByte;
int pos;

void setup()
{

  myservo.attach(9);
  myservo.write(90);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    inByte = Serial.readString();
    pos = inByte.toInt();
    Serial.print(inByte);
    if (strstr(const_cast<char *>(inByte.c_str()), "L") != NULL)
    {
      myservo.write(23);
      Serial.print(inByte);
      Serial.print("Locking\n");
    }
    else if (strstr(const_cast<char *>(inByte.c_str()), "U") != NULL)
    {
      myservo.write(90);
      Serial.print("Unlocking\n");
    }
  }
}
