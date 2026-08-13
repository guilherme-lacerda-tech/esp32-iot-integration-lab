// Generic ESP32 IoT lab sketch for public portfolio use.
// Uses fictional messages only.

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("BOOT ok");
  Serial.println("I2C device found at 0x40");
  Serial.println("RFID demo tag: DEMO-1234");
  Serial.println("CAN demo frame received");
  Serial.println("CELL modem ready");
}

void loop() {
  Serial.println("LAB heartbeat");
  delay(5000);
}
