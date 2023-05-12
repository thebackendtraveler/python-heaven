import nmap3

ip_devices = "192.168.137.0/24"

nmap = nmap3.NmapScanTechniques()
results = nmap.nmap_ping_scan(ip_devices)

print("Starting subnet scan")
print("{0}{1}{2}".format("Host".ljust(15), "MAC".center(30), "State".rjust(10)))
print("-"*60)

for host in results:

  if host != "stats" and host != "runtime":

        device_information = results[host]
        hostname = ""
        if device_information["macaddress"] != None:
            mac_address = device_information["macaddress"]["addr"]
        else:
            mac_address = "none"
        state = device_information["state"]["state"]

        print("{0}{1}{2}".format(
            host.ljust(15), mac_address.center(30), state.rjust(10)))
    else:
        if host == "stats":
            print("-"*60)
            print("The scan was completed with NMAP version {0}, and the command used was {1}".format(
                results[host]['version'], results[host]['args']))
            print("Completed the subnet scan")
