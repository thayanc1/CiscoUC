# From Login.py module get the Login Credential
from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)

# Get the UserID for the query
user_id=input('Enter UserID: ')
user = ucm.get_user(user_id)

# Print the list of Associated Devices for the User
print(user.associatedDevices)