// Declarar el puerto Serial2 para UART
#include <HardwareSerial.h>

HardwareSerial mySerial(2);  // Usamos Serial2 para la comunicación UART

// String inputString = "";      // Variable para almacenar datos recibidos
String inputString = "";
bool stringComplete = false;  // Bandera para saber si la cadena está completa

void setup() {
  Serial.begin(115200);                        // Iniciar comunicación por el puerto Serial estándar
  mySerial.begin(115200, SERIAL_8N1, 16, 17);  // Serial2 (TX: GPIO17, RX: GPIO16)

  Serial.println("Iniciando comunicación con AS7265x...");

  // Enviar un comando de ejemplo al AS7265x

  mySerial.println("ATLED0=0"); // Comando para encender la Luz de STAT del sensor
  delay(100);
  mySerial.println("ATLED1=1");  // Comando para encender un LED del sensor
  mySerial.println("ATLED3=1");  // Comando para encender un Luz Near Infra Red
  mySerial.println("ATLED5=1");  // Comando para encender un Luz Ultra Violeta

  delay(100);
  mySerial.println("ATCDATA");  // Comando para pedir datos espectrales
}

void loop() {
  // Si se ha recibido una cadena completa
  if (stringComplete) {
    // Serial.println("Datos recibidos desde AS7265x:");
    Serial.println(inputString);  // Imprime los datos recibidos
    inputString = "";             // Limpia la cadena
    stringComplete = false;       // Reinicia la bandera

    delay(500);                   // Espera 1 segundo antes de pedir nuevos datos
    mySerial.println("ATCDATA");  // Solicita nuevamente datos al AS7265x
  }

  // Mientras haya datos disponibles en el puerto UART
  while (mySerial.available()) {
    char inChar = (char)mySerial.read();  // Lee cada byte
    inputString += inChar;                // Añádelo a la cadena

    // Si se detecta un salto de línea, la cadena está completa
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}