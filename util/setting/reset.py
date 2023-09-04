import json
import os

def reset():
    try:
        if os.path.exists('util/token.json'):
            with open('util/token.json', 'r') as file:
                data = json.load(file)
                
            if 'token' in data:
                current_token = data['token']
                print(f"The current token is: {current_token}")
                
                confirm = input("Do you want to change the token? (Yes/No): ").strip().lower()
                
                if confirm == 'yes':
                    os.remove('util/token.json')
                    print("The token has been deleted.")
                else:
                    print("The token was not modified.")
        else:
            print("The token.json file does not exist.")
    
    except FileNotFoundError:
        print("The token.json file was not found.")
    except json.JSONDecodeError:
        print("The token.json file contains invalid JSON format.")

