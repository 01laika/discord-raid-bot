import urllib.parse
import requests
import time
import json
import rich
from rich.console import Console
console = Console()


console.print("""[red]
▄▄▄   ▄▄▄· ▪  ·▄▄▄▄      ▄▄▄▄▄            ▄▄▌      ▄▄▄▄·  ▄· ▄▌    ▄▄▌   ▄▄▄· ▪  ▄ •▄  ▄▄▄· 
▀▄ █·▐█ ▀█ ██ ██▪ ██     •██  ▪     ▪     ██•      ▐█ ▀█▪▐█▪██▌    ██•  ▐█ ▀█ ██ █▌▄▌▪▐█ ▀█ 
▐▀▀▄ ▄█▀▀█ ▐█·▐█· ▐█▌     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪      ▐█▀▀█▄▐█▌▐█▪    ██▪  ▄█▀▀█ ▐█·▐▀▀▄·▄█▀▀█ 
▐█•█▌▐█ ▪▐▌▐█▌██. ██      ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌    ██▄▪▐█ ▐█▀·.    ▐█▌▐▌▐█ ▪▐▌▐█▌▐█.█▌▐█ ▪▐▌
.▀  ▀ ▀  ▀ ▀▀▀▀▀▀▀▀•      ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀     ·▀▀▀▀   ▀ •     .▀▀▀  ▀  ▀ ▀▀▀·▀  ▀ ▀  ▀ 
""",justify="center")            
time.sleep(0.5)

def main():

    tokens = [ #put tokens in-between quoation marks seperated by a comma.
              "", 
              "",
              "x"
]

    start = console.input("[purple]\n(1) raid tool\n(2) leave servers\n(3) token checker\n\n[blue][>>>] Choice: ")

    if start == "1":
        server = console.input("[magenta]input server invite code => ")

        for each in tokens:
            token = {"authorization": each}
            invite = "https://discord.com/api/v8/invites/{}".format(server)
            r = requests.post(invite, headers=token)
            if r.status_code == 200:
                console.print("[purple]account joined succesfully")
            else:
                console.print("[red]error")
                
        autoverify = console.input("[magenta]auto-verify? (y) (n)\n").lower()
        if autoverify == "y":
            chnlid = console.input("[magenta]input channel ID where verification message is => ")
            msgid = console.input("[magenta]input message ID with reaction => ")
            verify = console.input("[magenta]input emoji to verify with => ")
            emoji = urllib.parse.quote_plus(verify)

            for each in tokens:
                token = {"authorization": each}
                time.sleep(0.3)
                r = requests.put("https://discord.com/api/v8/channels/{}/messages/{}/reactions/{}/%40me".format(chnlid, msgid, emoji), headers=token)
                if r.status_code == 204:
                    console.print("[purple]verified succesfully")
                else:
                    console.print("[red]error")
                
        channel = console.input("[magenta]input channel ID to spam => ")
        message = console.input("[magenta]input message to spam => ")
        times = int(console.input("[magenta]amount of times to spam => "))
        data = {"content": message}
        for x in range(times):
            for each in tokens:
                token = {"authorization": each}
                requests.post("https://discord.com/api/v8/channels/{}/messages".format(channel), json=data, headers=token)

    if start == "2":
        leave = console.input("[magenta]input server ID to leave => ")
        for each in tokens:
            token = {"authorization": each}
            requests.delete("https://discord.com/api/v8/users/@me/guilds/{}".format(leave), headers=token)
        time.sleep(0.5)

        
    if start == "3":
        for each in tokens:
            token = {"Authorization": each}
            
            valid = requests.get("https://discord.com/api/v8/users/@me/settings", headers=token)
            if valid.status_code == 200:
                console.print("[green]valid token passed\n{}\n".format(each))
            else: 
                console.print("[red]invalid token\n{}\n".format(each))
        time.sleep(0.5)
    main()

if __name__ == "__main__":
    main()
