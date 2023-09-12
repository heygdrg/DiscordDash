import requests 
from util.setting.defintion import getheaders, gettoken

payload = {'bio': "t"}
change= requests.patch('https://discord.com/api/v9/users/@me',
                       json = payload,
                        headers=getheaders(gettoken()))

print(change.json())