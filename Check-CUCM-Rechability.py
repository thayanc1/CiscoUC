import requests
import urllib3
from getpass import getpass

# From Login.py module get the Login Credential
from Login import cucm_username, cucm_password, cucm, version

# Define disablement of HTTPS Insecure Request error message.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL to hit for request against axl
baseurl = 'https://'

# Define user input required for script; pub ip, username, pw.
username = cucm_username
password = cucm_password
ccmip = cucm
version = version

# Here's where we verify reachability of the AXL interface for DB dip.
try:
    reachabilitycheck = requests.get(baseurl + ccmip + '/axl', auth=(username, password), verify=False)
    if reachabilitycheck.status_code != 200:
        print('AXL Interface at ' + baseurl + ccmip + '/axl/ is not available, or some other error. '
                                                      'Please verify CCM AXL Service Status.')
        print(reachabilitycheck.status_code)
        print('Contact script dev to create exception or handle response code.')
        exit()
    elif reachabilitycheck.status_code == 200:
        print()
        print('AXL Interface is working and accepting requests.')
except requests.exceptions.ConnectionError:
    print('Connection error occurred. Unable to get HTTP Response from CUCM AXL Interface. Check connectivity.')
except requests.exceptions.Timeout:
    print('Connection timed out to UCM AXL Interface.')
except Exception as m:
    print(m)
