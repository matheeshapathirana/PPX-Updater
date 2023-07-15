import os
import random
import shutil
import string
import urllib
from tkinter import *

import git


def error():
    window = Tk()

    window.geometry("380x100")
    window.title("You Need An Internet Connection For This")
    progname = Label(
        window,
        font=("Segoe UI", 15, "bold", "underline"),
        text="You Need An Internet Connection For This",
        fg="black",
    )
    progname.grid(row=3, column=3, padx=50, pady=30)


def connect(host="http://google.com"):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if connect():

    def random_char(y):
        return "".join(random.choice(string.ascii_letters) for x in range(y))

    random_num = random_char(20)
    main_dir = f"C:/Windows/Temp/{random_num}"
    os.mkdir(main_dir)
else:
    error()


def done():
    window = Tk()

    window.geometry("380x100")
    window.title("File updated successfully!")
    progname = Label(
        window,
        font=("Segoe UI", 15, "bold", "underline"),
        text="File updated successfully!",
        fg="black",
    )
    progname.grid(row=3, column=3, padx=50, pady=30)


def update():

    def random_char(y):
        return "".join(random.choice(string.ascii_letters) for x in range(y))

    random_num = random_char(10)
    main_dir = f"C:/Windows/Temp/{random_num}"
    os.mkdir(main_dir)
    git.Git(main_dir).clone(
        "https://gist.github.com/22e26fec003eba9a6a4bc8d11d2d171d.git")

    os.remove(
        r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles\A-Dev1412-SYS.ppx"
    )

    shutil.move(
        f"C:/Windows/Temp/{random_num}/22e26fec003eba9a6a4bc8d11d2d171d/A-Dev1412-SYS.ppx",
        r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
    )


def updater():
    window = Tk()

    window.geometry("500x500")
    window.title("PPX Updater")
    progname = Label(
        window,
        font=("Segoe UI", 15, "bold", "underline"),
        text="Click the update button to update the Rules",
        fg="black",
    )
    progname.grid(row=1, column=3, padx=50, pady=30)

    prog = Label(
        window,
        font=("Segoe UI", 15, "bold", "underline"),
        text="Click the update button to update the Rules",
        fg="black",
    )
    prog.grid(row=1, column=3, padx=50, pady=30)

    update_button = Button(
        window,
        font=("Segoe UI", 20, "bold"),
        text="Restore To Default",
        command=update(),
    )
    update_button.place(relx=0.27, rely=0.5)

    window.mainloop()


updater()

# network connetion checkr, fix the done def
