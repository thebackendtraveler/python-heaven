from pysnmp.hlapi import *
count = 0
# change the server to your docker ip address
SERVER = '10.0.0.126'
PORT = 161
for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public'),
                          UdpTransportTarget((SERVER, PORT)),
                          ContextData(),
                          # Starts the walk from 1.3.6
                          ObjectType(ObjectIdentity("1.3.6"))):

    if errorIndication:
        print("Error indication:  {}".format(errorIndication))
        # The loop is stopped on any form of error
        break
    elif errorStatus:
        print("Error status:  {}\nError index:  {}\nOn object:  {}".format(errorStatus,
                                                                           errorIndex,
                                                                           varBinds[errorIndex - 1]))
        # The loop is stopped on any form of error
        break
    else:
        for varBind in varBinds:
            print("{} = {}".format(varBind[0], varBind[1]))
        # Only displays the first 20 OIDs
        count += 1
        if count > 19:
            break