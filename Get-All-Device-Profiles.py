from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for udp in ucm.get_device_profiles():
    print(udp.name)