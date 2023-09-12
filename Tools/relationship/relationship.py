import requests,json
import datetime
import sys

def used():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getheaders(token):

    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE2MTg4NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        'authorization' : token
    }

    if token:
        headers.update({"Authorization": token})
        return headers
    
    
def gettoken():
    global token
    token = ''
    try:
        with open(r'util\token.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    token = data.get('token')
    return token

def ID_info():
            friend = requests.get(f'https://discord.com/api/v9/users/{ID_list[int(selected_index) - 1]}',headers=getheaders(token)).json()
            print(f'[{used()}] User select {friend["username"]}')
            for element in friend:
                print(f"      {element} -> {friend[element]}")

def gather_relationship():
    global ID_list, selected_index

    ID_list = []
    token = gettoken()

    relationship = requests.get('https://discord.com/api/v9/users/@me/relationships',headers=getheaders(token)).json()
    
    for index, relation in enumerate(relationship, start=1):
        ID_list.append(relation['id'])
        if relation["user"]["global_name"] == 'None':
            username = relation["user"]["global_name"]
        else:
            username = relation["user"]["username"]
        print(f'[{used()}] [{index}] friend find -> {username}')
    
    while True:
        try: 
            selected_index = int(input(f"[{used()}] >>> ID : "))
            

            if 1 <= selected_index <= len(relationship):
                
                selected_relation = relationship[selected_index - 1]
                selected_username = selected_relation["user"]["username"]
                try:

                        ID_info()
                        print('Control + c to escape')
                        input('press Enter to continue')
                    
                except KeyboardInterrupt:
                    print('KEYBOARD INTERRUPT')
                    quit()
        
    
        except Exception as e :
            print(e)

gather_relationship()