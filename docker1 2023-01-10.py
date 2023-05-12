from pysnmp.hlapi import *

# change the server to your docker ip address
SERVER = '10.0.0.126'
PORT = 161

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           # Uses the credentials "public"
           CommunityData("demo"),
           # Connects using IPv4 to port 161
           UdpTransportTarget((SERVER, PORT)),
           # Creates a default instance of ContextData
           ContextData(),
           # Requests details on a single OID
           ObjectType(ObjectIdentity("1.3.6.1.2.1.1.4.0")))
)

if errorIndication:
    print("Error indication:  {}".format(errorIndication))
elif errorStatus:
    print("Error status:  {}\nError index:  {}\nOn object:  {}".format(errorStatus,
                                                                       errorIndex,
                                                                       varBinds[errorIndex - 1]))
else:
    for varBind in varBinds:
        # varBind[0] contains the OID and varBind[1] contains the value.
        print("{} = {}".format(varBind[0], varBind[1]))
        # Displaying the same OID and value, but with prettyPrint
        print("{} = {}".format(
            varBind[0].prettyPrint(), varBind[1].prettyPrint()))