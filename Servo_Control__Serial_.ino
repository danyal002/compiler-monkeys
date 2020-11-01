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
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
    { 
    inByte = Serial.read(); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer        
    myservo.write(pos);     // move servo
    Serial.print("Servo in position: ");  
    Serial.println(inByte);
    }
}
