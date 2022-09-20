#!/usr/bin/python3
#(c) 2022 Will Smith

import requests
activate_username = "username"
activate_password = "password"
clearpass_hostname = "clearpass.hostname.com"
clearpass_bearer_token = "fb686e72f35276f4559b976b65441383e168d9e1"

def activate_login():
    session = requests.Session()
    logon_url = "https://activate.arubanetworks.com/LOGIN"
    payload= ("credential_0=" + activate_username + "&credential_1=" + activate_password)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        session.post(logon_url, headers=headers, data=payload)
        return session
    except:
        print("Error Logging into Activate")
        return

def activate_inventory(session):
    f = open("ap_mac_eth0.txt", "w")
    inventory_url = "https://activate.arubanetworks.com/api/ext/inventory.json?action=query"
    try:
        response = session.post(inventory_url)
        response_data = response.json()
        devices = response_data['devices']
        for ap in devices:
            ap_type = ap['additionalData']['partCategory']
            if ap_type == "UAP" or ap_type == "IAP" or ap_type == "RAP" or ap_type == "AP" or ap_type == "CAP":
                for mac in devices:
                    f.write(mac['mac'] + "\n")
                return
    except:
        print("Error with Activate inventory query")

def ap_mac_address_opperation():
    try:
        ap_mac = open("ap_mac_eth1.txt", "w")
        with open('ap_mac_eth0.txt') as f:
            for line in f:
                ap_mac_line = line.strip()
                ap_mac_address = ap_mac_line.replace(":", "")
                ap_mac_eth1 = ("{:012X}".format(int(ap_mac_address, 16) + 1))
                ap_mac.write(':'.join(ap_mac_eth1[i]+ap_mac_eth1[i+1] for i in range(0, len(ap_mac_eth1), 2)) + "\n")
        return
    except:
        print("Error with mac address opperation")

def clearpass_endpointdb_update():
    try:
        with open("ap_mac_eth1.txt") as ap_mac:
            for mac in ap_mac:
                ap_mac_line = mac.strip()
                clearpass_url = ("https://" + clearpass_hostname + "/api/endpoint")
                headers = {"accept": "application/json", "Authorization": "Bearer " + clearpass_bearer_token, "content-type": "application/json"}
                payload = {"mac_address": ap_mac_line, "description": "AP Eth1 MAC Address", "status": "Known"}
                response = requests.post(clearpass_url, json=payload, headers=headers)
                print(payload)
                if response.status_code == 201:
                    print(ap_mac_line + " Successfully Added to ClearPass")
                elif response.status_code == 422:
                    print(ap_mac_line + " Already Added to ClearPass...Skipping")
                else:
                    print("There was an error updating ClearPass")
        return
    except:
        print("Error writing to ClearPass")

if __name__ == "__main__":
    print("--- Starting ---")
    session = activate_login()
    activate_inventory(session)
    ap_mac_address_opperation()
    clearpass_endpointdb_update()
    print("--- Finished ---")
