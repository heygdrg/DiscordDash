def help_menu():
    menu = """
usage: DiscordDash {token} {positional argument}

postional arguments:
    settings:
        -set : set a discord token to use 
        -reset : reset the discord token ot use
        -install : install all the dependencies
        -help : help menu
    Tools:
        Relationships:
            -r : get all the relationship
            -r {user_id} : get information about a specific user in relationships
            -r unadd {user_id} : unadd a friend
            -r add {user_id} : add a user
            -r send {user_id} : send a message to a user
        Server : 
            -s : get all the server
            -s perm : get all the server where the victim have permission
            -s delete {server_id} : delete a server 
            -s leave {server_id} : leave a server
            -s spoof {server_id} {user_id} : spoof a user
            -s kick {server_id} {user_id} : kick a user
        User:
            -u info : get victim info
            -u -b set : set a new bio
            -u -b : get victim bio
            -u -st set : get user status
            -u -st : get user status
            -u -nuke : destroy token
            -u seizure : enable seizure mode"""
    print(menu)