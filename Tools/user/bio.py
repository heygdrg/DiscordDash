import requests 
from util.setting.defintion import getheaders, gettoken

payload = {'bio': "t"}
bio = requests.get('https://discord.com/api/v9/users/@me',
                        headers=getheaders(gettoken()))

print(bio.json())