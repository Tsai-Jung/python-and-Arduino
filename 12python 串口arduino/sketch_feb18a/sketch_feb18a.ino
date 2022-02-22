#include <Servo.h>

Servo myservo;  // 定义Servo对象来控制
int pos = 0;    // 角度存储变量
char var;
void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // 控制线连接数字9
  myservo.write(100);
}
void loop() {
  while(Serial.available()>0)
  {
    var=Serial.read();
    if(var == '0'){
      myservo.write(170); }
    if(var== '1'){
      myservo.write(30);}
    if(var== '2'){
      myservo.write(100);}
  }
}
