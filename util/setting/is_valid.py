import json,requests

def getheaders(token):

    headers =     {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    }

    if token:
        headers.update({"Authorization": token})
        return headers
    
def validateToken(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        print('token succesfully check')
    else:
        print(f"Invalid Token.")

def get_token():
    try:
        with open('util/token.json', 'r') as file:
            data = json.load(file)
        if 'token' in data:
            token = data['token']
            validateToken(token)
        else:
            print("Token key not found in token.json file.")
    except FileNotFoundError:
        print("Error please login with a token")
        exit()
    except json.JSONDecodeError:
        print("Error decoding JSON in token.json file.")
