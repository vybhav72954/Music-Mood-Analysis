import processing.serial.*;
 
Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph
float height_old = 0;
float height_new = 0;
float inByte = 0;
int BPM = 0;
int beat_old = 0;
float[] beats = new float[500];  // Used to calculate average BPM
int beatIndex;
float threshold = 620.0;  //Threshold
boolean belowThreshold = true;
PFont font;
 
 
void setup () {
  // window size:
  size(1000, 400);        
 
  // List all the available serial ports
  println(Serial.list());
  //Port
  myPort = new Serial(this, Serial.list()[4], 9600);
  // Wait for newline
  myPort.bufferUntil('\n');
  //Background color
  background(0xff);
  //TODO FONT
  font = createFont("Ariel", 12, true);
}
 
 
void draw () {
     //Map and draw the line //Error yha aate h
     inByte = map(inByte, 0, 1023, 0, height);
     height_new = height - inByte; 
     line(xPos - 1, height_old, xPos, height_new);
     height_old = height_new;
    
      // back to the beginning
      if (xPos >= width) {
        xPos = 0;
        background(0xff);
      } 
      else {
        // Incremnet
        xPos++;
      }
      
      //  \BPM 
      if (millis() % 128 == 0){
        fill(0xFF);
        rect(0, 0, 200, 20);
        fill(0x00);
        text("BPM: " + inByte, 15, 10);
      }
}
 
 
void serialEvent (Serial myPort) 
{
  // ASCII
  String inString = myPort.readStringUntil('\n');
 
  if (inString != null) 
  {
    // no whitespace:
    inString = trim(inString);
 
    // Dead Graph, no LED :|
    if (inString.equals("!")) 
    { 
      stroke(0, 0, 0xff); //Set stroke to blue ( R, G, B)
      inByte = 512;  // Flat Line
    }
    //Wokrin
    else 
    {
      stroke(0xff, 0, 0); //Set stroke to red ( R, G, B)
      inByte = float(inString); 
      
      // BPM calculation
      if (inByte > threshold && belowThreshold == true)
      {
        calculateBPM();
        belowThreshold = false;
      }
      else if(inByte < threshold)
      {
        belowThreshold = true;
      }
    }
  }
}
  
void calculateBPM () 
{  
  int beat_new = millis();    // new beat per millisecond
  int diff = beat_new - beat_old;    // find the time between the last two beats
  float currentBPM = 60000 / diff;    // convert to beats per minute
  beats[beatIndex] = currentBPM;  // store to array to convert the average
  float total = 0.0;
  for (int i = 0; i < 500; i++){
    total += beats[i];
  }
  BPM = int(total / 500);
  beat_old = beat_new;
  beatIndex = (beatIndex + 1) % 500;  // cycle through the array instead of using FIFO queue
  }
