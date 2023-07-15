import tkinter as tk
import tkinter.font as tkFont


class App:

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
        GLabel_327["text"] = "Update Date - "
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

    @staticmethod
    def GButton_674_command():
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
