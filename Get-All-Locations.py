#
# Script created by Thaya Nagarajah
#

# From Login.py module get the Login Credential
from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for loc in ucm.get_locations():
    print(loc.name)
