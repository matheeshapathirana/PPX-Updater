import os
import random
import shutil
import string
from tkinter import *

import git


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
    )

    shutil.move(
        f"C:/Windows/Temp/{random_num}/0e0687d042c5ba6494d8d81c0051151f/A-Dev1412-SYS.ppx",
        r"C:\Program Files (x86)\A-Developer1412\HTTP Proxy Injector\AppData\Profiles",
    )


def create_account():
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

    update_button = Button(
        window, font=("Segoe UI", 20, "bold"), text="Update", command=update()
    )
    update_button.place(relx=0.37, rely=0.5)

    window.mainloop()


create_account()
