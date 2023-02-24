#!/usr/bin/env python3
#router.py
#A sub (child) class for a router network device
#CIS3534C - Scripting for Network Professionals
#Module 7 - Object-oriented Programming

#necessary for inheritance
from networkdevice import NetworkDevice

class Router(NetworkDevice):
    """ A generic router """
   
    
    counter = 0      #class variable to count how many routers are created

    def __init__(self, IPAddr, MACaddr, hostname, protocol="RIPV2"):
        #default protocol
        super().__init__(IPAddr, MACaddr)
        self.__hostname = self.validateHostname(hostname)
        self.__protocol = self.validateProtocol(protocol)
        Router.counter += 1

    def getHostname(self):
        return self.__hostname

    def getProtocol(self):
        return self.__protocol

    #the host name can't be empty
    def validateHostname(self, hostname):
        if len(hostname) > 0:
            return hostname
        else:
            return "Router Name Unknown"

    def setHostname(self, hostname):
        self.__hostname = self.validateHostname(hostname)

    #
    def validateProtocol(self, protocol):
        VALID_PROTOCOLS = ["EIGRP", "OSPF", "RIP", "BGP", "RIPV2"]
        if protocol.upper() in VALID_PROTOCOLS:
            return protocol
        else:
            return "OSPF"

    def setProtocol(self, protocol):
        self.__protocol = self.validateProtocol(protocol)

    def __str__(self):
        return super().__str__() + \
            f"\n    hostname: {self.__hostname}, routing protocol {self.__protocol}"

#unit test for this file only
def main():
    router1 = Router("192.168.1.1", "AA:BB:CC:DD:EE:FF", "router1", "ABCDE")
    print("Your router: ", router1)
    print()
    router2 = Router("555.555.555.555", "AA:BB:CC:11:22:33", "", "EIGRP")
    print("Your router: ", router2)
    print()
    router1.setHostname("BlueWave")
    print("Your updated router: ", router1)
    print("You created", Router.counter, "routers today!")


#top-level scope check
if __name__ == "__main__":
    main()
                    
