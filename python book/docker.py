from pysnmp.hlapi import *

# change the server to your docker ip address
SERVER = '10.0.0.126'
PORT = 161

errorIndication, errorStatus, errorIndex, varBinds = next(
    setCmd(SnmpEngine(),
           CommunityData("demo"),
           UdpTransportTarget((SERVER, PORT)),
           ContextData(),
           # In this case the object identity is set using a human readable format.
           # Note that the ObjectType declaration includes an ObjectIdentity as well
           # as the value to set to the MIB object to.
           ObjectType(ObjectIdentity("1.3.6.1.2.1.1.4.0"),
                      "Somewhere_else"))
)

if errorIndication:
    print("Error indication:  {}".format(errorIndication))
elif errorStatus:
    print("Error status:  {}\nError index:  {}\nOn object:  {}".format(errorStatus,
                                                                       errorIndex,
                                                                       varBinds[errorIndex - 1]))
else:
    for varBind in varBinds:
        # The same print() statement as in the previous example, but
        # written a bit more concisely.  The statement iterates through
        # all the values in varBind, calls prettyPrint() on each and then
        # joins the resulting values using " = "
        print(" = ".join([x.prettyPrint() for x in varBind]))