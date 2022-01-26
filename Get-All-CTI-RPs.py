#
# Script created by Thaya Nagarajah
#

# From Login.py module get the Login Credential
from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for cti in ucm.get_cti_route_points():
    print(cti.name)
