#!/usr/bin/env python3
#networkInventory.py
#Pamela Brauda
#Thursday, September 27, 2022
#Update routers and switches

#prompt constants
UPDATE = "\nWhich device would you like to update "
QUIT = "(enter x to quit)? "
NEW_IP = "What is the new IP address (111.111.111.111) "
SORRY = "Sorry, that is not a valid IP address\n"

#dictionaries
routers = {"router1":"10.10.10.1", "router2":"20.20.20.1", "router3":"30.30.30.1"}
switches = {"switch1":"10.10.10.2", "switch2":"10.10.10.3", "switch3":"10.10.10.4",
            "switch4":"10.10.10.5", "switch5":"20.20.20.2", "switch6":"20.20.20.3",
            "switch7":"30.30.30.2", "switch8":"30.30.30.3", "switch9":"30.30.30.4"}
updated = {}

#lists
invalidIPAddresses = []

#accumulator variables
##devicesUpdatedCount = 0
##invalidIPCount = 0

#flags and sentinels
quitNow = False
validIP = False

print("Network Equipment Inventory\n")
print("\tequipment name\tIP address")
for router, ipa in routers.items():
    print("\t" + router + "\t\t" + ipa)
for switch, ipa in switches.items():
    print("\t" + switch + "\t\t" + ipa)

while not quitNow:

    #prompt for device to update
    device = input(UPDATE + QUIT).lower()
    if device == 'x':
        quitNow = True
        break

    validIP = False
    #prompt for new IP address
    #validate IP address
    while not validIP:
        ipAddress = input(NEW_IP)
        octets = ipAddress.split('.')
        #print("octets", octets)
        for byte in octets:
            byte = int(byte)
            if byte < 0 or byte > 255:
##                invalidIPCount += 1
                invalidIPAddresses.append(ipAddress)
                print(SORRY)
                break
        else:
            validIP = True                

    #update device
    if 'r' in device:
        #modify the value associated with the key
        routers[device] = ipAddress 
        #print("routers", routers)
        
    else:
        switches[device] = ipAddress

##    devicesUpdatedCount += 1
    #add the device and ipAddress to the dictionary
    updated[device] = ipAddress

    print(device, "was updated; the new IP address is", ipAddress)
    #loop back to the beginning

#user finished updating devices
print("\nSummary:\n")
print()
print("Number of devices updated:", len(updated))
print("Updated equipment", updated)
print()
print("\nNumber of invalid addresses attempted:", len(invalidIPAddresses))
print("List of invalid addresses:", invalidIPAddresses)
print("\nThe updated router dictionary:\n", routers)
print("\nThe updated switches dictionary:\n", switches)

    



