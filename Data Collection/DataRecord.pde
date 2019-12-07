//Data Recording Code

//Achille Hebert III

import processing.serial.*;
//Variable Declaration
PrintWriter output;
int dir = 0;
Serial udSerial;
String val;
int i = 0;

int trial = 11;
String ID = "Rocket";

void setup() {
  udSerial = new Serial(this, "COM9", 250000);  //enter directory from tools in ard. IDE into 2nd argument
  output = createWriter (str(year()) + "_" + str(month()) + "_" + str(day()) + "_" + str(hour()) + "_" + str(minute()) + "_" + str(second()) + "_" + ID + "_" + " VoltageData.csv");
  size(300, 200);
  background(60);
  text(ID, 100, 100);
}

  void draw() {
    
    while (udSerial.available() > 0) {
      String SenVal = udSerial.readStringUntil('\n');;
      
      if (SenVal != null) {
        output.print(SenVal);
        background(60);
        text(SenVal, 100, 100, 1000,1000);
        i=i+1;        
        
      }
    }
    //currently diabled since we don't want to end data collection prematurely
    //if (i>10000){
    //  output.flush();
    //  output.close();
    //  exit();
    //}
  }
  void keyPressed(){
      output.flush();
      output.close();
      exit();
  }
