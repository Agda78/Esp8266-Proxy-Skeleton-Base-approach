#include "RequestHandler.h"

// Practical service implementation
String handleRequest(String request) {
    if (request == "SERVICE_1") {
        return "Service_1_on_board";
    } else if (request == "SERVICE_2") {
        return "Service_2_on_board";
    }
    return "Comando sconosciuto";
}
