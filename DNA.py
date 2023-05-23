import requests, json
from keys import URL, basic, token
# Module for DNA center
import dnacentersdk


GetToken_endpoint = "/dna/system/api/v1/auth/token"
netdev_endpoint= "/api/v1/network-device"
GetInt_endpoint= "/dna/intent/api/v1/interface/network-device/{device_ID}"
Devinfo_endpoint = "/dna/intent/api/v1/{device_ID}"

headers = {
    "Content-type" : "application/json",
    "Accept" : "application/json",
    #'Authorization' : f"Basic {basic}"
    "X-Auth-Token" : token 
}

# Requests auth token with basic
'''response = requests.post(f"{URL}{token_endpoint}", headers=headers, verify=False)
print(response.content)'''


# get network devices
response2 = requests.get(f"{URL}{GetInt_endpoint}", headers=headers, verify=False)
print (response2.content)



