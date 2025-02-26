# Service implementation class
class ServiceClient:
    def __init__(self, proxy):
        self.proxy = proxy

    # In this case, the board's result is directly requested from the Proxy,
    # which only returns the result received from the board
    def request_service_1(self):
        return self.proxy.send_request("SERVICE_1")

    def request_service_2(self):
        return self.proxy.send_request("SERVICE_2")
