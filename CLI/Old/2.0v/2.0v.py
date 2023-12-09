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


def close():
    sys.exit()


class updater:
    def __init__(self, root):
        root.title("PPX Updater")

        width = 662
        height = 765
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

        GLabel_772 = tk.Label(root)
        ft = tkFont.Font(family="Segoe UI", size=20)
        GLabel_772["font"] = ft
        GLabel_772["fg"] = "#333333"
        GLabel_772["justify"] = "center"
        GLabel_772["text"] = f"{username}, Welcome To PPX Updater"
        GLabel_772["relief"] = "flat"
        GLabel_772.place(x=150, y=10, width=400, height=200)

        GLabel_508 = tk.Label(root)
        ft = tkFont.Font(family="Segoe UI", size=28)
        GLabel_508["font"] = ft
        GLabel_508["fg"] = "#333333"
        GLabel_508["justify"] = "center"
        GLabel_508["text"] = "Select Your Package"
        GLabel_508.place(x=160, y=260, width=336, height=62)

        GButton_240 = tk.Button(root)
        GButton_240["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=10)
        GButton_240["font"] = ft
        GButton_240["fg"] = "#000000"
        GButton_240["justify"] = "center"
        GButton_240["text"] = "WhatsApp & FaceBook"
        GButton_240.place(x=220, y=430, width=190, height=79)
        GButton_240["command"] = self.GButton_240_command

        GButton_642 = tk.Button(root)
        GButton_642["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=28)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#000000"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "Defaults"
        GButton_642.place(x=220, y=520, width=190, height=72)
        GButton_642["command"] = self.GButton_642_command

        GButton_617 = tk.Button(root)
        GButton_617["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=10)
        GButton_617["font"] = ft
        GButton_617["fg"] = "#000000"
        GButton_617["justify"] = "center"
        GButton_617["text"] = "Exit"
        GButton_617.place(x=10, y=720, width=186, height=30)
        GButton_617["command"] = self.GButton_617_command

        GButton_349 = tk.Button(root)
        GButton_349["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Segoe UI", size=28)
        GButton_349["font"] = ft
        GButton_349["fg"] = "#000000"
        GButton_349["justify"] = "center"
        GButton_349["text"] = "Zoom"
        GButton_349.place(x=220, y=330, width=185, height=88)
        GButton_349["command"] = self.GButton_349_command

    @staticmethod
    def GButton_240_command():
        def update():
            def random_char(y):
                return "".join(random.choice(string.ascii_letters) for x in range(y))

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
    def GButton_642_command():
        def update():
            def random_char(y):
                return "".join(random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            print(f"Temp Folder Created Using The Name - {random_num}")

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/22e26fec003eba9a6a4bc8d11d2d171d.git"
            )  # default

            if os.path.exists(
                r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                os.remove(
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/22e26fec003eba9a6a4bc8d11d2d171d/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )
            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/22e26fec003eba9a6a4bc8d11d2d171d/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )

        update()

    @staticmethod
    def GButton_617_command():
        sys.exit()

    @staticmethod
    def GButton_349_command():
        def update():
            def random_char(y):
                return "".join(random.choice(string.ascii_letters) for x in range(y))

            random_num = random_char(10)
            print(f"Temp Folder Created Using The Name - {random_num}")

            main_dir = f"C:/Windows/Temp/{random_num}"
            os.mkdir(main_dir)
            print("Directory '% s' is built!" % main_dir)

            git.Git(main_dir).clone(
                "https://gist.github.com/0e0687d042c5ba6494d8d81c0051151f.git"
            )  # zoom

            if os.path.exists(
                r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
            ):
                os.remove(
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
                )
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/0e0687d042c5ba6494d8d81c0051151f/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )

            else:
                shutil.copy(
                    f"C:/Windows/Temp/{random_num}/0e0687d042c5ba6494d8d81c0051151f/A-Dev1412-SYS.ppx",
                    r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
                )

        update()


if __name__ == "__main__":
    root = tk.Tk()
    app = updater(root)
    root.mainloop()
