# From Login.py module get the Login Credential
from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

for user in ucm.get_users():
    # Print the First Name and Last Name of the User List
    print(user.firstName, user.lastName)