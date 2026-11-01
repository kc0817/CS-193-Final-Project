void setup() {
  Serial.begin(9600);
  delay(500);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int n = data.toInt();
    if (n > 0) {
      Serial.println("positive");
    }
    else if (n == 0) {
      Serial.println("zero");
    }
    else {
      Serial.println("negative");
    }
  }
}