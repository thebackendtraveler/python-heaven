import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("10.0.0.138")

print(results)