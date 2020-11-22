#include "GyverEncoder.h"
#include <PID_v1.h>
#include "SevenSegmentTM1637.h"
#include "SevenSegmentExtended.h"
#include "SevenSegmentFun.h"
#include <EEPROM.h>

// Hot gun pinout
#define heater 11
#define fan 5
#define sensor 10
#define temp_sensor A1

//Display
const byte PIN_CLK = 3;   // define CLK pin (any digital pin)
const byte PIN_DIO = 2;   // define DIO pin (any digital pin)
SevenSegmentFun    display(PIN_CLK, PIN_DIO);

// Encoder pinout
#define btn 8
#define pin_1 7
#define pin_2 6
Encoder enc1(pin_1, pin_2, btn);

//Define Variables we'll be connecting to
double set_temp = 200, heater_temp, heater_pwm;

//Temperatures
//set_temp=200;
int set_temp_min = 150;
int set_temp_max = 480;

int set_air_speed_min = 20;
int set_air_speed_max = 100;
int set_air_speed = 100;

//Specify the links and initial tuning parameters
double Kp=0.5, Ki=1.0 , Kd=3.0;
PID myPID(&heater_temp, &heater_pwm, &set_temp, Kp, Ki, Kd, DIRECT);

// Timer settings
unsigned long previousMillis = 0;        // will store last time LED was updated
unsigned long display_previousMillis = 0;
unsigned long holder_previousMillis = 0;

// constants won't change:
const long interval = 200;  
int holder_interval = 4000;  
int display_interval = 1000;
int counter;
bool on_off_state=true;
bool air_or_temp_control=true;
bool force_on_off_state = true;
void setup_ports(){
  pinMode(heater, OUTPUT);
  pinMode(fan, OUTPUT);
  pinMode(sensor, INPUT_PULLUP);
  //TCCR0B = TCCR0B & B11111000 | B00000010; // for PWM frequency of 7812.50 Hz
  digitalWrite(fan, HIGH);
}

void setup_print(){
  Serial.println("Set_temp,Real_Temp,Heater_PWM,Fan_Set");
}


void read_values_from_eeprom(){
  set_air_speed = EEPROM.read(0);
  set_temp = EEPROM.read(1)*2;
  
  //Serial.print("Air_speed: ");
  //Serial.println(set_air_speed);
  //Serial.print("Set_temp: ");
  //Serial.println(set_temp);
}

void setup() {
  enc1.setType(TYPE2);
  myPID.SetMode(AUTOMATIC);
  display.begin();            // initializes the display
  display.setBacklight(100);  // set the brightness to 100 %
  delay(1000);                // wait 1000 ms
  setup_ports();
  Serial.begin(9600);
  //setup_print();
  read_values_from_eeprom();
  holder_interval = 0; 
  //while(1);
}

void check_holder(){
  unsigned long currentMillis = millis();

  if (currentMillis - holder_previousMillis >= holder_interval) {
    holder_interval = 4000; 
    // save the last time you blinked the LED
    holder_previousMillis = currentMillis;
    if(digitalRead(sensor)){
       //Serial.println("Piced up from the holder");
        if(force_on_off_state){
          on_off_state = true;
        }else{
          on_off_state = false;
        }
    }else{
      //Serial.println("Placed to the holder");
      on_off_state = false;
    }
  }
}

void pid_correction(){
  heater_temp = analogRead(temp_sensor);
  if(on_off_state){
    int fan_speed = map(set_air_speed,0,100,0,255);
    analogWrite(fan, fan_speed);
    myPID.Compute();
    analogWrite(heater, heater_pwm);
  }else{
    digitalWrite(heater, 0);
    if(heater_temp >= 180){
      digitalWrite(fan, HIGH);
      delay(100);
    }else{
      digitalWrite(fan, LOW);
    }
  }
}

void data_display(){
  unsigned long currentMillis = millis();
  if (currentMillis - display_previousMillis >= display_interval) {
    // save the last time you blinked the LED
    display_previousMillis = currentMillis;
    display_interval = 300;
    
    if(on_off_state){
      if(heater_temp <= set_temp_max){
        display.printNumber(heater_temp);
      }else{
        display.clear();
        display.print("ERR");
      }
    }else{
      display.clear();
      display.print("OFF");
    }
    
  }
  
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void handle_data_transmit(){
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
  previousMillis = currentMillis;
  Serial.print(set_temp);
  Serial.print(",");
  Serial.print(heater_temp);
  Serial.print(",");
  Serial.print(set_air_speed);
  Serial.print(",");
  Serial.println(on_off_state);

  while(Serial.available()) {
    String incoming_data= Serial.readString();
    String _set_temp, _set_speed, _set_on_off;
    int soft_set_temp, soft_set_speed, soft_set_on_off;
    _set_temp = getValue(incoming_data,',',0);
    _set_speed = getValue(incoming_data,',',1);
    _set_on_off = getValue(incoming_data,',',2);
    soft_set_temp=_set_temp.toInt();
    soft_set_speed=_set_speed.toInt();
    soft_set_on_off=_set_on_off.toInt(); 
    
    if( set_temp_min <= soft_set_temp && soft_set_temp <= set_temp_max){
      //Serial.println(soft_set_temp);
      set_temp = soft_set_temp;
    }else{
      //Serial.println("Set_temp_error");
    }

    if( set_air_speed_min <= soft_set_speed && soft_set_speed <= set_air_speed_max){
      //Serial.println(set_air_speed);
      set_air_speed = soft_set_speed;
    }else{
      //Serial.println("Set_air_speed_error");
    }

    if(soft_set_on_off == 1){
      //Serial.println("Turn on");
      force_on_off_state = true;
    }else{
      force_on_off_state = false;
      //Serial.println("Turn off");
    }
    
  }

}

}

void handle_encoder(){
  enc1.tick();
  if(air_or_temp_control){
    if (enc1.isRight() && set_temp <= set_temp_max){
      set_temp +=10;
      display_interval = 2000;
      EEPROM.write(1, set_temp/2);
      display.clear();
      char b[5];
      String str;
      str="t" + String(set_temp);
      str.toCharArray(b,5); 
      display.print(b);
    }
    
    if (enc1.isLeft() && set_temp >= set_temp_min){
      display_interval = 2000;
      set_temp -=10;
      EEPROM.write(1, set_temp/2);
      display.clear();
      char b[5];
      String str;
      str="t" + String(set_temp);
      str.toCharArray(b,5); 
      display.print(b);
    }
  }else{
    if (enc1.isRight() && set_air_speed < set_air_speed_max){
      set_air_speed +=10;
      display_interval = 2000;
      EEPROM.write(0, set_air_speed);
      display.clear();
      char b[5];
      String str;
      str="A" + String(set_air_speed);
      str.toCharArray(b,5); 
      display.print(b);
    }
    
    if (enc1.isLeft() && set_air_speed > set_air_speed_min){
      display_interval = 2000;
      set_air_speed -=10;
      EEPROM.write(0, set_air_speed);
      display.clear();
      char b[5];
      String str;
      str="A" + String(set_air_speed);
      str.toCharArray(b,5); 
      display.print(b);
    }
  }
  
  if (enc1.isDouble()){
    display_interval = 2000;
    force_on_off_state=!force_on_off_state;
    display.clear();
    if(force_on_off_state){
      display.print("ON");
    }else{
      display.print("OFF");
    }
  }

  if (enc1.isSingle()){
    air_or_temp_control =!air_or_temp_control;
    display_interval = 2000;
    display.clear();
    if(air_or_temp_control){
      display.print("Temp");
    }else{
      display.print("Air");
    }
  }

  /*
    if (enc1.isRight()) Serial.println("Right");         // если был поворот
  if (enc1.isLeft()) Serial.println("Left");
  
  if (enc1.isRightH()) Serial.println("Right holded"); // если было удержание + поворот
  if (enc1.isLeftH()) Serial.println("Left holded");
  
  //if (enc1.isPress()) Serial.println("Press");         // нажатие на кнопку (+ дебаунс)
  //if (enc1.isRelease()) Serial.println("Release");     // то же самое, что isClick
  
  if (enc1.isClick()) Serial.println("Click");         // одиночный клик
  if (enc1.isSingle()) Serial.println("Single");       // одиночный клик (с таймаутом для двойного)
  if (enc1.isDouble()) Serial.println("Double");       // двойной клик
  
  
  if (enc1.isHolded()) Serial.println("Holded");       // если была удержана и энк не поворачивался*/
}

void loop() {  
  pid_correction();
  handle_encoder();
  check_holder();
  data_display();
  handle_data_transmit();
}
