#define DIRX 9
#define STEPX 10
#define DIRY 5
#define STEPY 6
#define DIRZ 2
#define STEPZ 3
int i, a, choise;
void setup() {
  pinMode(DIRX, OUTPUT);
  pinMode(STEPX, OUTPUT);
  pinMode(DIRY, OUTPUT);
  pinMode(STEPY, OUTPUT);
  pinMode(DIRZ, OUTPUT);
  pinMode(STEPZ, OUTPUT);
  Serial.begin(9600);
}
void moveDrill(char axis,int direction, int steps, int delayReal){
  int step;
  int directionD;
  if(axis=='x'){
      step=STEPX;
      directionD=DIRX;
  }
  if(axis=='y'){
      step=STEPY;
      directionD=DIRY;
  }
  if(axis=='z'){
     int step=STEPZ;
     int directionD=DIRZ;
  }
  if(direction==1){
     digitalWrite(directionD,HIGH);
  }
  if(direction==0){
    digitalWrite(directionD,LOW);
  }
  for(int i = 0; i < steps; i++){
    //Serial.println("You have eye cancer");
        digitalWrite(step, LOW);
        delay(delayReal);
        digitalWrite(step, HIGH);
        delay(delayReal);
  }
  digitalWrite(step,LOW);
  digitalWrite(direction,LOW);
  
}
void loop(){
  if(Serial.available() > 0){
    char axis=Serial.readStringUntil('%')[0];
    int direction=Serial.readStringUntil('%').toInt();
    int steps=Serial.readStringUntil('%').toInt();
    int delay=Serial.readStringUntil('%').toInt();
    /*
    Serial.println(axis);
    Serial.println(direction);
    Serial.println(steps);
    Serial.println(delay);
    */
    moveDrill(axis,direction,steps,delay);
  }
}

