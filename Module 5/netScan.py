#!python3

import nmap3
import requests
import json

def getMacInfo(macaddress):
    
    try:
        url = "https://api.macaddress.io/v1"
        
        querystring = {"apiKey": "at_AM0jsCnRCJgTSSfvSoXdW7eipHDEQ",
                       "output": "json", "search": macaddress}
        
        headers = {'user-agent': 'vscode-restclient'}
        
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        
        #print(response.text)
        jResponse = json.loads(response.text)
        return (jResponse["vendorDetails"]["companyName"])
    except:
        return "None"
    
ip_devices = "192.168.142.0/24"
nmap = nmap3.NmapScanTechniques()
results = nmap.nmap_ping_scan(ip_devices)

print("Starting subnet scan")
print("{0}{1}{2}{3}".format("Host".ljust(15), "MAC".center(30), "Vendor".ljust(30), "State".rjust(10)))
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
            mVendor = getMacInfo(mac_address)
            print("{0}{1}{2}{3}".format(
                host.ljust(15), mac_address.center(30), mVendor.ljust(30), state.rjust(10)))
    else:
        if host == "stats":
            print("-"*80)
            print("the scan was completed with NMAP version {0}, and the command used was {1}".format(
                results[host]['version'], results[host]['args']))    
        elif host == "task_results":
            print("-"*80)
            print("Hosts in subnet {}".format(results[host][0]["extrainfo"]))
        else: 
            print("Completed the subnet scan")