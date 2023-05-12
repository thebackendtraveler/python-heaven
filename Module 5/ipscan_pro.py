import nmap3
import json

#The function to scan the network
def scan_network(ip_devices):
    nmap = nmap3.NmapScanTechniques()
    results = nmap.nmap_ping_scan(ip_devices)
    csv_result = ""
    
    print("Starting subnet scan")
    print("{0}{1}{2}".format("Host".ljust(15), "MAC".center(30), "State".rjust(10)))
    print("-"*80)
    csv_result = "host, mac, state\n"
    
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
                csv_result = csv_result + ("{0}{1}{2}\n".format(host, mac_address, state))
            else:
                if host == "stats":
                    print("-"*80)
                    print("The scan ws completed with NMAP version {0}, and the command used was {1}".format(
                        results[host]['version'], [results][host]['args']))
                elif host == "task_results":
                    print("-"*80)
                    print("Hosts in subnet {}".format(results[host][0]["extrainfo"]))
                else:
                    print("The subnet scan was completed..")
    return csv_result

#The function to scan a device on the network
def scan_device(device):
    csv_result = "protocol, port_number, name, state\n"
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(device)
    for port in results [device]['ports']:
        csv_results = csv_results + "{0}{1}{2}{3}\n".format(port['protocol'], port['portid'], port['service']['name'], port['state'])
    return csv_result

#The function to save the result of the scan to a file
def save_to_file(contents):
    try:
        filename = input("What is the filename to be used?: ")
        if filename[-4:] != ".csv":
            filename = filename + ".csv"
        if contents == "":
            print("Nothing to save, please do a scan first...")
            return
        file = open(filename, "w")
        file.write(contents)
        file.close()
        print("File [{}] save was completed successfully.".format(filename))
        
    except Exception as e:
        print("An error occurred while trying to save the file...")
        print(e)
        
#The function for the main menu
def main_menu():
    choice = 0
    results = ""
    while choice != 4:
        print("1. Scan a network")
        print("2. Scan a device for open ports")
        print("3. Save results to a csv file")
        print("4. Exit the application")
        choice = int(input("Please select an option: "))
        
        if choice == 1:
            network = input("What network do you want to scan?: ")
            results = scan_network(network)
        
        if choice == 2:
            device = input("What device do you want to scan for default open ports?: ")
            results = scan_device(device)
        
        if choice == 3:
            save_to_file(results)
            
main_menu()