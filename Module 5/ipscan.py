import nmap3
import argparse

parser = argparse.ArgumentParser(description='Network Scanning with Python and NMAP')
parser.add_argument('192.168.142.0/24', required=True, help="The network you want to scan example: 192.168.0.0/24")
args = parser.parse_args() #--subnet

ip_devices = args.subnet
nmap = nmap3.NmapScanTechniques()
results = nmap.nmap_ping_scan(ip_devices)

print("Starting the subnet scan")
print("{0}{1}{2}".format("Host".ljust(15), "MAC".center(
    30), "State".rjust(10)))
print("-"*80)

for host in results:
    if host != "stats" and host != "runtime" and host != "task_results":
        if results[host]["state"]["state"] != "down":
            device_information = results[host]
            hostname = ""
            if device_information["macaddress"] != None:
                mac_address = device_information["macaddress"]["addr"]
            else:
                mac_address = "None"
            state = device_information["state"]["state"]
            print("{0}{1}{2}".format(
                host.ljust(15), mac_address.center(30), state.rjust(10)))
    else:
        if host == "stats":
            print("-"*80)
            print("The scan was completed with NMAP version {0}, and the command used was {1}".format(results[host]['version'], results[host]['args']))
        elif host == "task_results":
            print("-"*80)
            print("Hosts in subnet {}".format(results[host][0]["extrainfo"]))
        else:
            print("The subnet scan was completed")
            