import getpass
import os
import random
import shutil
import string
import sys
import tkinter as tk
import tkinter.font as tkFont

import git

username = getpass.getuser()


class App:

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

    @staticmethod
    def GButton_60_command():

        def update():

            def random_char(y):
                return "".join(
                    random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            print(f"Temp Folder Created Using The Name - {random_num}")

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/2f4e1cd64005f983ce1823585948c8ff.git"
            )  # whatsapp

            if os.path.exists(
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                os.remove(
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/2f4e1cd64005f983ce1823585948c8ff/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/2f4e1cd64005f983ce1823585948c8ff/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )

        update()

    @staticmethod
    def GButton_304_command():
        print("command")

    @staticmethod
    def GButton_383_command():
        print("command")

    @staticmethod
    def GButton_820_command():
        print("command")

    @staticmethod
    def GButton_567_command():
        print("command")

    @staticmethod
    def GButton_155_command():
        print("command")

    @staticmethod
    def GButton_970_command():
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
