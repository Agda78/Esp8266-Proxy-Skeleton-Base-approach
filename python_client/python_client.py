# Communication management class
from client_proxy import ESP8266Proxy

# Service implementation management class (and related protocols)
from service_client import ServiceClient

# Board IP address
IP_BOARD = "192.168.1.101"

# Main execution of service implementation
if __name__ == "__main__":
    proxy = ESP8266Proxy(IP_BOARD)  # Modify with ESP8266 IP address
    client = ServiceClient(proxy)  # Service system implementation
    
    # Request the two available services and print the results
    print("Result of SERVICE_1:", client.request_service_1())
    print("Result of SERVICE_2:", client.request_service_2())
