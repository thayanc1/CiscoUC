from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for reg in ucm.get_regions():
    print(reg.uuid)