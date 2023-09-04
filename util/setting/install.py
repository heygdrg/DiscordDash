import json

def install():
    with open('util/requierement.json', 'r') as file:
        data = json.load(file)

    for module_name in data['modules']:
        try:
            exec(f'import {module_name}')
            print(f"Module {module_name} import succesfully.")
        except ImportError:
            print(f"Error while installing module {module_name}.")
