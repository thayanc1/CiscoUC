from Login import cucm_username, cucm_password, cucm, version
from ciscoaxl import axl

ucm = axl(username=cucm_username,password=cucm_password,cucm=cucm,cucm_version=version)
user_id=input('Enter UserID: ')

user = ucm.get_user(user_id)
print(user)