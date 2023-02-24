#!/usr/bin/env python3
#switch.py
#A sub (child) class for a switch network device
#CIS3534C - Scripting for Network Professionals
#Module 7 - Object-oriented Programming

#necessary for inheritance
from networkdevice import NetworkDevice

class Switch(NetworkDevice):
    """ A generic switch """  
    
    counter = 0      #class variable to count how many switches are created

    def __init__(self, IPAddr, MACaddr, hostname, defaultGateway):
        #default protocol
        super().__init__(IPAddr, MACaddr)
        self.__hostname = self.validateHostname(hostname)
        self.__defaultGateway = super().validateIP(defaultGateway)
        Switch.counter += 1

    def getHostname(self):
        return self.__hostname

    def getDefaultGateway(self):
        return self.__defaultGateway

    #the host name can't be empty
    def validateHostname(self, hostname):
        if len(hostname) > 0:
            return hostname
        else:
            return "Switch Name Unknown"

    def setHostname(self, hostname):
        self.__hostname = self.validateHostname(hostname)
    
    def setDefaultGateway(self, protocol):
        self.__protocol = super().validateIP(DefaultGateway)

    def __str__(self):
        return super().__str__() + \
            f"\n    hostname: {self.__hostname}, default gateway {self.__defaultGateway}"

#unit test for this file only
def main():
    switch1 = Switch("192.168.1.99", "AA:BB:CC:DD:EE:FF", "switch1", "192.168.1.1")
    print("Your switch: ", switch1)
    print()
    switch2 = Switch("888.888.888.888", "AA:BB:CC:11:22:33", "", "192.168.1.1")
    print("Your switch: ", switch2)
    print()
    switch1.setHostname("WavyBlue")
    print("Your updated switch: ", switch1)
    print("You created", Switch.counter, "switches today!")


#top-level scope check
if __name__ == "__main__":
    main()
                    
