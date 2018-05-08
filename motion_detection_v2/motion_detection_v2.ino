/* Author: Jake Johnson
 * Date Created: May 7, 2018
 * This code puts arduino to sleep and wakes the arduino up if the interrupt pin (2) is triggered HIGH by the PIR sensor
 * Derived from: https://playground.arduino.cc/Learning/ArduinoSleepCode
 * Derived from: https://www.arduino.cc/reference/en/language/functions/digital-io/digitalwrite
 */

#include <avr/sleep.h>

int wakePin = 2;                 // pin used for waking up
int interruptGPIOPin = 13;        // pin used to interrupt the RaspberryPi
int sleepStatus = 0;             // variable to store a request for sleep
int count = 0;                   // counter

void wakeUpNow()        // here the interrupt is handled after wakeup
{
  
  // Serial.println("I'm awake! What do you want?!!");
  // execute code here after wake-up before returning to the loop() function
  // timers and code using timers (serial.print and more...) will not work here.
  // we don't really need to execute any special functions here, since we
  // just want the thing to wake up

}

void setup()
{
  pinMode(wakePin, INPUT);
  pinMode(interruptGPIOPin, OUTPUT);

  Serial.begin(9600);

  attachInterrupt(0, wakeUpNow, HIGH); // use interrupt 0 (pin 2) and run function
                                      // wakeUpNow when pin 2 gets HIGH 
}

void sleepNow()         // here we put the arduino to sleep
{
    digitalWrite(interruptGPIOPin, LOW);
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);   // sleep mode is set here

    sleep_enable();          // enables the sleep bit in the mcucr register
                             // so sleep is possible. just a safety pin 

    attachInterrupt(0,wakeUpNow, HIGH); // use interrupt 0 (pin 2) and run function
                                       // wakeUpNow when pin 2 gets HIGH 

    sleep_mode();            // here the device is actually put to sleep
                             // THE PROGRAM CONTINUES FROM HERE AFTER WAKING UP

    sleep_disable();         // first thing after waking from sleep:
                             // disable sleep...
    detachInterrupt(0);      // disables interrupt 0 on pin 2 so the 
                             // wakeUpNow code will not be executed 
                             // during normal running time.
}

void loop()
{
  // display information about the counter
  Serial.print("Awake for ");
  Serial.print(count);
  Serial.println("sec");
  count++;
  delay(1000);                           // waits for a second
  
  digitalWrite(interruptGPIOPin, HIGH);


  // check if it should go to sleep because of time
  if (count >= 5) {
      Serial.println("Timer: Entering Sleep mode");
      delay(100);     // this delay is needed, the sleep 
                      //function will provoke a Serial error otherwise!!
      count = 0;
      sleepNow();     // sleep function called here
  }
}

