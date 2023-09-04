import json
def set(token):
    try:
        token = token
    except ValueError:
        print("Error : please try again")
        quit()
    try:
        with open('token.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data['token'] = token

    with open('util/token.json', 'w') as file:
        json.dump(data, file)

    print(f"Token succesfully set !")
