# Dual Uplink AP Automation for ClearPass
This script auto updates endpoints database in ClearPass with Aruba AP secondary (ETH1) MAC-Address with data pulled from Aruba Activate.

```
 % python3 main.py
--- Starting ---
{'mac_address': '20:4C:03:7D:1B:AC', 'description': 'AP Eth1 MAC Address', 'status': 'Known'}
20:4C:03:7D:1B:AC Successfully Added to ClearPass
{'mac_address': '00:4E:35:C5:B4:89', 'description': 'AP Eth1 MAC Address', 'status': 'Known'}
00:4E:35:C5:B4:89 Successfully Added to ClearPass
--- Finished ---
```

Download the repo, make sure Python is installed.
Edit main.py and enter the credentials for Aruba Activate and Bearer token for ClearPass.
Then execute the script 'python3 main.py'

The script will first log into Aruba Activate and download the inventory of devices. Then parse the inventory for the mac-address of each device and add one hexadecimal to match the redundant hardware mac-address for each AP (ETH1). The script will then create a new Endpoints database entry for each new mac-address in ClearPass.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com
