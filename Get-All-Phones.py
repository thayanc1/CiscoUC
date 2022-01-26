from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for phone in ucm.get_phones():
    print(phone.name)