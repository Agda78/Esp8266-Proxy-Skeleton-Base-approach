# Esp8266 Proxy-Skeleton base approach

This project consists of two fundamental components:

## 1. `python_client`
The `python_client` implements a proxy client structure using sockets. It is responsible for managing communication between the client and the `arduino_server`.

## 2. `arduino_server`
The `arduino_server` contains the sketch that implements the service, handling socket communication with the client.

Both components work together to establish a seamless client-server interaction over sockets.
