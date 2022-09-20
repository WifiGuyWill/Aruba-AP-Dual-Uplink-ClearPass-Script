# Aruba script to auto update the endpoints database in ClearPass with Aruba AP secondary (ETH1) hardware info

```
 % python3 main.py
--- Starting ---
{'mac_address': '20:4C:03:7D:1B:CC', 'description': 'AP Eth1 MAC Address', 'status': 'Known'}
20:4C:03:8C:1A:AB Successfully Added to ClearPass
There was an error updating ClearPass
{'mac_address': '00:4E:35:C3:A5:19', 'description': 'AP Eth1 MAC Address', 'status': 'Known'}
00:4E:35:C6:A4:89 Successfully Added to ClearPass
There was an error updating ClearPass
--- Finished ---
```

Download the repo, make sure Python is installed.
Edit main.py and enter the credentials for Aruba Activate and Bearer tokenn for ClearPass.
Then execute the script 'python3 main.py'

The script will first log into Aruba Activate and download the inventory of devices. Then parse the inventory for the mac-address of each device and add one hexidecimal to match the redudant hardware mac-address for each AP (ETH1). The script will then create a new Endpoints database entry for each new mac-address in ClearPass.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com