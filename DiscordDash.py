import sys, requests
import argparse
from Error.help import help_menu
from util.setting.set import set
from util.setting.reset import reset
from util.setting.install import install
from util.setting.is_valid import get_token 
from Tools.relationship.add_friend import add_friend
from Tools.relationship.relationship import gather_relationship


def main():
    if len(sys.argv) < 2:
        print("please give an argument, here's some help ")
        help_menu()
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
        #if sys.argv[1] and sys.argv[2] == '-r add':
            #get_token()
            #add_friend(user_id=sys.argv[3])
        
        if sys.argv[1] == '-r':
            get_token()
            gather_relationship()


    
if __name__ == "__main__":
    main()
