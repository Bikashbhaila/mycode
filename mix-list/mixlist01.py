#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display first item in the list
print("The first item in the list is (ip): " + my_list[0])
# display second item in the list
print("The first item in the list is (port): " + str(my_list[1]) )
# display third item in the list
print("The first item in the list is (state): " + my_list[2])

#display only the IP addresses on the screen
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
