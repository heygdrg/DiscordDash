import sys, requests
from Error.help import help_menu
from util.setting.set import set
from util.setting.reset import reset
from util.setting.install import install
from util.setting.is_valid import get_token

def main():
    if len(sys.argv) < 2:
        print("Veuillez fournir un mot en argument.")
    else:
        if sys.argv[1] == '-help':
            help_menu()
        
        if sys.argv[1] == '-set':
            set(token=input('enter the token : '))
        
        if sys.argv[1] == '-install':
            install()

        if sys.argv[1] == '-reset':
            get_token()
            reset()
        

if __name__ == "__main__":
    main()
