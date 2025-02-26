#include <ESP8266WiFi.h>
#include "RequestHandler.h"


// Setting of information for WiFi connection
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// Setup of listener socket port
SOCKET_PORT=80;
WiFiServer server(SOCKET_PORT);

void setup() {
    // Setting of the serial comunication for debugging
    Serial.begin(115200);
    
    // WiFi connection
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connection loading...");
    }
    Serial.println("Connected at the Network");

    // Print on the serial of the IP
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    server.begin();
}

void loop() {
    // Listener socket
    WiFiClient client = server.available();
    if (client) {
        // Management of new arriving request
        String request = client.readStringUntil('\n');
        Serial.println("Richiesta ricevuta: " + request);

        // Implementation and call of requested service
        String response = handleRequest(request);

        // Print of the response and continue
        client.println(response);

        // End the socket comunication
        client.stop();
    }
}
