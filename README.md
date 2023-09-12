# **DISCORD DASH**

### **Description**

**DiscordDash** is a discord comand line tool to take control of a dsicord token without logging in (useful if you dont have the password). It can help you in multiple situation as :
1. manage relationship of the user (add, delete, spam)
2. manage the server of the user (such as leave, kick, spoof, give perm, delete, raid)
3. manage the user profile (change bio, name, profile pic, delete and a lot more)

**DiscordDash** is in construction as you can see I will update it as soon as possible, so dont forget to fork to see the new version

---

### Depedencies

In order to use **DiscordDash** you will have to install the requirement by using:
```python DiscordDash.py -install```

You can also directly check the module to install in 
> requirement.json

---

### **Setup**

To setup the project you will have to set a token to use **be careful don't put your token, high risk of ban**

in order to set the token you just have to make a simple line 

```python DiscordDash.py -set```

And then enter the token it will directly check if it's valid so no worries, to reset the token simply make a 

```python DiscordDash.py -reset```

---

### **Documentation**

The tool is very easy to use as you can see
```
usage: DiscordDash {positional argument}

postional arguments:
    settings:
        -set : set a discord token to use 
        -reset : reset the discord token ot use
        -install : install all the dependencies
        -help : help menu
    Tools:
        Relationships:
            -r : get all the relationship ✅ 
            -r info {user_id} : get information about a specific user in relationships ⏳
            -r unadd {user_id} : unadd a friend ❌
            -r add {user_id} : add a user ⏳
            -r send {user_id} : send a message to a user ❌
        Server : 
            -s : get all the server 
            -s perm : get all the server where the victim have permission ❌
            -s delete {server_id} : delete a server ❌
            -s leave {server_id} : leave a server ❌
            -s spoof {server_id} {user_id} : spoof a user ❌
            -s kick {server_id} {user_id} : kick a user  ❌
        User:
            -u info : get victim info ⏳
            -u -b set : set a new bio ⏳
            -u -b : get victim bio ❌
            -u -st set : get user status ❌
            -u -st : get user status ❌
            -u -nuke : destroy token ❌
            -u seizure : enable seizure mode ❌
```

The project is still a newborn so we are working to finish it as faster as we can ! stay updated of the new feature 
The comand that are mark with a ❌ are not usable and will make the tool crash only use the ✅ one's

---
### Advertisement 

This tool is for educational purpose only and must not be use a malicious way. I decline all the responsablities about what you will do with 

---

### Don't forget

You can also check my latest project

1. [Spetsnaz]("https://github.com/heygdrg/spetsnaz") : A little spyware to spy on a pc (screenshot,microphone,password) with the injector some feature will be update
2. [Zehef]('https://github.com/heygdrg/Zehef') : a discord mass dm tool
3. [Pfizer]('https://github.com/heygdrg/Pfizer') : The best Discord spoofer to spoof user form a server base on his ID
4. [Spoofize]('https://github.com/heygdrg/Spoofize') : a mass leave tool

---















