#define IN1 2
#define IN2 3
const int SPEED = 250;
const int THRESHOLD = 20;

void setup() {
  Serial.begin(9600);

  //Set motor connections as outputs
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  // Stop motor
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void loop() {
  int photo1 = analogRead(A1);
  int photo2 = analogRead(A2);

  Serial.println("photo 1: ");
  Serial.println(photo1);
  Serial.println("photo 2: ");
  Serial.println(photo2);
  delay(2000);

  // recycling
  if (photo1 > THRESHOLD) {
    // Accelerate forward
    digitalWrite(IN1, LOW);
    for (int i = 0; i < SPEED; i++) {
      analogWrite(IN2, i);
      delay(20);
    }

    delay(500);

    // Decelerate forward
    for (int i = SPEED; i >= 0; i--) {
      analogWrite(IN2, i);
      delay(20);
    }

    delay(500);
  }

  // non-recycling
  if (photo2 > THRESHOLD) {  
    // Accelerate reverse
    digitalWrite(IN2, LOW);
    for (int i = 0; i < SPEED; i++) {
      analogWrite(IN1, i);
      delay(10);
    }

    delay(200);

    //Decelerate reverse
    for (int i = SPEED; i >= 0; i--) {
      analogWrite(IN1, i);
      delay(10);
    }

    delay(500);
  }
}
