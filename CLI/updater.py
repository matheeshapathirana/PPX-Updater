import os
import random
import string
import tkinter as tk
import tkinter.font as tkFont

import git


def version_check():

    def random_char(y):
        return "".join(random.choice(string.ascii_letters) for x in range(y))

    random_num = random_char(10)
    print(f"Temp Folder Created Using The Name - {random_num}")

    main_dir = f"C:/Windows/Temp/{random_num}"
    os.mkdir(main_dir)
    print("Directory '% s' is built!" % main_dir)

    git.Git(main_dir).clone(
        "https://gist.github.com/182c5338c9bb5fe62081bbc590cd70de.git"
    )  # version
    a = open(
        "D:/OneDrive - adithya/Programming/Python/PPX updater GUI Version/cur_version.txt"
    )
    cur_version_check = a.read()
    f = open(
        f"C:/Windows/Temp/{random_num}/182c5338c9bb5fe62081bbc590cd70de/version.txt",
        "r",
    )
    check = f.read()
    if check > cur_version_check:

        class App:

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

            @staticmethod
            def GButton_439_command():
                print("command")

            @staticmethod
            def GButton_368_command():
                root.destroy()

        if __name__ == "__main__":
            root = tk.Tk()
            app = App(root)
            root.mainloop()
    else:

        class no_updates:

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

            @staticmethod
            def GButton_284_command():
                root.destroy()

        if __name__ == "__main__":
            root = tk.Tk()
            app = no_updates(root)
            root.mainloop()


version_check()
