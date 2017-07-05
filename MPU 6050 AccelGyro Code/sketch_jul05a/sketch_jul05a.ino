
#include <Wire.h>

long accelX, accelY, accelZ;
float gForceX, gForceY, gForceZ;

long gyroX, gyroY, gyroZ;
float rotX, rotY, rotZ;

void setup (){
  Serial.begin (9600);
  Wire.begin ();
  setupMPU();
}

void loop(){
  recordAccelRegisters();
  recordGyroRegisters();
  printData();
  delay (100);
}

void setupMPU (){
  Wire.beginTransmission (0b1101000);
  Wire.write (0x6B);
  Wire.write (0b00000000);
  Wire.endTransmission();
  Wire.beginTransmission (0b1101000);
  Wire.write (0x1b);
  Wire.write (0x00000000);
  Wire.endTransmission();
  Wire.beginTransmission(0b1101000);
  Wire.write(0x1c);
  Wire.write(0b00000000);
  Wire.endTransmission ();
}

void recordAccelRegisters(){
  Wire.beginTransmission(0b1101000);
  Wire.write(0x3B);
  Wire.endTransmission();
  Wire.requestFrom (0b1101000,6);
  while (Wire.available() <6);
  accelX = Wire.read()<<8|Wire.read();
  accelY = Wire.read()<<8|Wire.read();
  accelZ = Wire.read()<<8|Wire.read();
  processAccelData();
}

void processAccelData(){
  gForceX = accelX / 16384.0;
  gForceY = accelY / 16384.0;
  gForceZ = accelZ / 16384.0;
}

void recordGyroRegisters(){
    Wire.beginTransmission(0b1101000);
  Wire.write(0x43);
  Wire.endTransmission();
  Wire.requestFrom (0b1101000,6);
  while (Wire.available() <6);
  gyroX = Wire.read()<<8|Wire.read();
  gyroY = Wire.read()<<8|Wire.read();
  gyroZ = Wire.read()<<8|Wire.read();
  processGyroData();
}

void processGyroData(){
  rotX = gyroX / 131.0;
  rotY = gyroY / 131.0;
  rotZ = gyroZ / 131.0;
}

void printData(){
  Serial.print ("Gyro (deg)");
  Serial.print ("X=");
  Serial.print (rotX);
  Serial.print ("Y=");
  Serial.print (rotY);
  Serial.print ("Z=");
  Serial.print (rotZ);
  Serial.print ("Accel (g)");
  Serial.print ("X=");
  Serial.print (gForceX);
  Serial.print ("Y=");
  Serial.print (gForceY);
  Serial.print ("Z=");
  Serial.println (gForceZ);
  }

