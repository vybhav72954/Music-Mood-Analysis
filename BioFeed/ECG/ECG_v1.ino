
void setup() {

Serial.begin(9600);
pinMode(10, INPUT); //  LO +
pinMode(11, INPUT); //  LO -
 
}
 
void loop() {
 
if((digitalRead(10) == 1)||(digitalRead(11) == 1)){
Serial.println('!');
}
else{
// analog input 0:
Serial.println(analogRead(A0));
}
//Wait
delay(1);
}
