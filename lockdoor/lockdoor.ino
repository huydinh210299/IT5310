#include <Servo.h>

#include <SPI.h>
#include <MFRC522.h>

#define TURN_ON 0
#define TURN_OFF 1

Servo servo;

constexpr uint8_t RST_PIN = D3;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = D4;     // Configurable, see typical pin layout above
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522::MIFARE_Key key;
String tag;

String a;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  servo.attach(16); //D0
  servo.write(0);

  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522

  delay(2000);
}

void loop() {
  if (Serial.available()) {
    a = Serial.readString();
    Serial.print(a);
    a.trim();
    String command = a.substring(0);
    if (command == "lock") {
      servo.write(180);
      digitalWrite(LED_BUILTIN, TURN_ON);
    }
    if (command == "open") {
      servo.write(0);
      digitalWrite(LED_BUILTIN, TURN_OFF);
    }

  }

  if ( ! rfid.PICC_IsNewCardPresent())
    return;
  if (rfid.PICC_ReadCardSerial()) {
    for (byte i = 0; i < 4; i++) {
      tag += rfid.uid.uidByte[i];
    }
    Serial.print(tag);
    bool rs = tag == "220911633";
    if (tag == "220911633") {
      servo.write(0);
      digitalWrite(LED_BUILTIN, TURN_OFF);
    }
    if (tag == "13117114621") {
      servo.write(180);
      digitalWrite(LED_BUILTIN, TURN_ON);
    }
    tag = "";
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
  }
}
