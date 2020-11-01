//#include <Servo.h>
//
//Servo servo1;  
//long num;     
//
//void setup()
//{
// servo1.attach(9);
//Serial.begin(9600); 
////Serial.print("Enter Position = ");
//}
//
//void loop() 
//{ 
//  if(Serial.available()>0)
//  { 
//  num= Serial.parseInt();   
//  Serial.print(num);  
//  Serial.println(" degrees");
//  Serial.print("Enter Position = ");
//  servo1.write(num);
//  Serial.end();
//  Serial.begin(9600);
//  }
//  
//}

#include <Servo.h>
Servo myservo; 
String inByte;
int pos;

void setup() {
 
  myservo.attach(9);
  myservo.write(90);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available())  // if data available in serial port
    { 
    inByte = Serial.readString(); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer 
    Serial.print(inByte);
    if(strstr(const_cast<char*>(inByte.c_str()),"L") != NULL){
      myservo.write(23);
      Serial.print(inByte);
      Serial.print("Locking\n");
    }else if(strstr(const_cast<char*>(inByte.c_str()),"U") != NULL){
      myservo.write(90);
      Serial.print("Unlocking\n");
    }
//    myservo.write(pos);     // move servo
//    Serial.print("Servo in position: ");  
//    Serial.println(inByte);
    }
}
