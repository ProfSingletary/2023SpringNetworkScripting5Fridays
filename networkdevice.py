#!/usr/bin/env python3
#networkdevice.py
#A super (parent) class for generic network devices
#CIS3534C - Scripting for Network Professionals
#Module 7 - Object-oriented Programming

class NetworkDevice:
    """A generic device that can be connected to a network"""

    def __init__(self, IPaddr, MACaddr):
        self.__IPaddr = self.validateIP(IPaddr) #assures a valid IP address
        self.__MACaddr = MACaddr #read only

    def setIPaddr(self, IPaddr):
        """Update the IP address after validation"""
        self.__IPaddr = validateIP(IPaddr)

    def getIPaddr(self):
        return self.__IPaddr

    def getMACaddr(self):
        return self.__MACaddr

    #this method lets you print(objName)
    def __str__(self): #creates a string version of the object
        return f"IP address {self.__IPaddr}; MAC address {self.__MACaddr}"

    #from our solution to Module 5/6, without user interaction
    def validateIP(self, ipAddr):
        """validates the IP address has no alpha characters and
           digits are between 0 and 255"""
        octets = ipAddr.split('.')
        #print("octets", octets)
        for byte in octets:
            if byte.isalpha():
                print("Invalid input - no letters or characters")
                return "0.0.0.0"    #provides a default IP address
            byte = int(byte)
            if byte < 0 or byte > 255:
                print("Sorry,", ipAddr, "is not a valid IP address, defaulting to zeros")
                return "0.0.0.0"    #provides a default IP address
        else:
            #validIP = True
            return ipAddr
                

#unit test for this file only
def main():
    nd1 = NetworkDevice("192.168.1.1", "AA:BB:CC:DD:EE:FF")
    print("Your network device: ", nd1)
    print()
    nd2 = NetworkDevice("555.555.555.555", "AA:BB:CC:11:22:33")
    print("Your network device: ", nd2)


#top-level scope check
if __name__ == "__main__":
    main()
        
