import os
import tkinter as tk
import tkinter.ttk as ttk
from datetime import date, datetime
from threading import Thread
import time
import socket
import subprocess
import calendar


global version
version="1.0.0"


def main():
    regwindowx = tk.Tk()
    screen_widthx = regwindowx.winfo_screenwidth()
    # screen_heightx = regwindowx.winfo_screenheight()
    regwindowx.destroy()

    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        # The image must be stored to Tk or it will be garbage collected.
        rootx.image = tk.PhotoImage(file='DATA/IMAGES/LOADING/loading.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+270+5")
        # root.lift()
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(1000, lambda: labelx.destroy())
        rootx.after(1000, lambda: rootx.destroy())  # Destroy the widget after 1 seconds
        labelx.mainloop()


    for i in range(0,3):
        loading()


    def user_login_over_ride():
        class User_Login():

            def __init__(self, window):

                # Static user Name and Password
                self.UID = ["John_Deere_Admin"]
                self.PWD = ["1234"]

                self.lbl = tk.Label(window, text="User", font=("Helvetica", 30, 'bold'), bg='white')
                self.lbl.place(x=60, y=70)

                self.txtfld1 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 30, 'bold'))
                self.txtfld1.place(x=220, y=70)

                self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 30, 'bold'), bg='white')
                self.lb2.place(x=60, y=200)

                self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*", font=("Helvetica", 30, 'bold'))
                self.txtfld2.place(x=220, y=200)

                self.btn = ttk.Button(window, text="LOGIN", width=20, command=self.validate)
                self.btn.place(x=435, y=300, width=230, height=50)

                self.btn_quit = ttk.Button(window, text="QUIT", command=self.quit)
                self.btn_quit.place(x=675, y=-1)

            def validate(self):
                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):
                    window_user_login.destroy()

                    # IF VALIDATION IS SUCCESFUL THEN IT OPENS USER EDIT WINDOW
                    pass















            def quit(self):
                window_user_login.destroy()

        window_user_login = tk.Tk()
        window_user_login.config(background='white')
        window_user_login.attributes('-alpha', 0.9)

        user_login_window = User_Login(window_user_login)
        window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login.title('Admin Login ' + version)
        window_user_login.geometry("600x450")
        window_user_login.mainloop()

    user_login_over_ride()














if __name__ == '__main__':
    main()

