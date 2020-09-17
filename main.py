import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
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

                self.UID = []
                self.PWD = []


                with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        x,y=list(map(str,each.split(",")))
                        print(x,y)
                        x=str(x).replace("\n","")
                        y = str(y).replace("\n", "")
                        self.UID.append(x)
                        self.PWD.append(y)


                # Static user Name and Password
                # self.UID = ["John_Deere_Admin"]
                # self.PWD = ["1234"]

                print(self.UID)
                print(self.PWD)

                self.lbl = tk.Label(window, text="User", font=("Helvetica", 20), bg='white')
                self.lbl.place(x=60, y=90)

                self.txtfld1 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 20))
                self.txtfld1.place(x=220, y=90)

                self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20), bg='white')
                self.lb2.place(x=60, y=220)

                self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*", font=("Helvetica", 20))
                self.txtfld2.place(x=220, y=220)

                self.btn = ttk.Button(window, text="LOGIN", width=20, command=self.validate)
                self.btn.place(x=60, y=330, width=200, height=50)

                self.btn_quit = ttk.Button(window, text="QUIT",width=20, command=self.quit)
                self.btn_quit.place(x=330, y=330,width=200, height=50)

            def validate(self):
                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):
                    window_user_login.destroy()


                    def user_login_2():
                        class User_2():

                            def __init__(self, window):

                                # class CustomDateEntry(DateEntry):
                                #
                                #     def _select(self, event=None):
                                #         date = self._calendar.selection_get()
                                #         if date is not None:
                                #             self._set_text(date.strftime('%Y-%m-%d'))
                                #             self.event_generate('<<DateEntrySelected>>')
                                #         self._top_cal.withdraw()
                                #         if 'readonly' not in self.state():
                                #             self.focus_set()

                                with open('DATA/Scanning/data.txt', 'r') as fh:
                                    all_lines = fh.readlines()
                                    for each in all_lines:
                                        string=str(each)
                                        
                                print(string)

                                date_x=''

                                # date_x=re.findall('^17[0-9]{6}',string)
                                # try:
                                #     date_x=date_x[0]
                                # except:
                                #     date_x=''
                                # date_x='20'+'-'+date_x[2:4]+'-'+date_x[4:6]+'-'+date_x[6:8]
                                gstin=re.findall('^01[0-9]{14}',string)
                                try:
                                    gstin=gstin[0][2:]
                                except:
                                    gstin=''
                                lot=''
                                serial=''

                                print(date_x,gstin)

                                strings=string.split("")

                                for string in strings:

                                    print(string)

                                    x1=string.find('17')
                                    if x1!=-1 and date_x=='':
                                        date_x=string[x1+2:x1+8]
                                        date_x='20'+date_x[0:2]+'-'+date_x[2:4]+'-'+date_x[:]

                                    # x2 = string.find('01')
                                    # if x2!=-1:
                                    #     gstin = string[x2 + 2:x2 + 16]

                                    x3 = string.find('21')
                                    if x3!=-1 and serial=='':
                                        serial = string[x3 + 2:]

                                    x4 = string.find('10')
                                    if x4 != -1 and lot=='':
                                        lot = string[x4 + 2:]

                                    print(date_x,gstin,lot,serial)

                                print(date_x, gstin, lot, serial)

                                self.lb1 = tk.Label(window, text="EXP(YYYY-MM-DD)",font=("Helvetica", 10), bg='white')
                                self.lb1.place(x=60, y=50)


                                self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                                self.txtfld1.place(x=270, y=50,width=260)
                                #self.txtfld1.setvar(date_x)



                                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='white')
                                self.lb2.place(x=60, y=100)

                                self.txtfld2 = ttk.Entry(window,
                                                         font=("Helvetica", 10))
                                self.txtfld2.place(x=270, y=100,width=260)
                                self.txtfld2.insert(0, lot)


                                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='white')
                                self.lb3.place(x=60, y=150)

                                self.txtfld3 = ttk.Entry(window,text="Enter UID", font=("Helvetica", 10))
                                self.txtfld3.place(x=270, y=150,width=260)
                                self.txtfld3.insert(0, gstin)

                                self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='white')
                                self.lb4.place(x=60, y=200)

                                self.txtfld4 = ttk.Entry(window,
                                                         font=("Helvetica", 10))
                                self.txtfld4.place(x=270, y=200,width=260)



                                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='white')
                                self.lb5.place(x=60, y=250)

                                self.txtfld5 = ttk.Entry(window,
                                                         font=("Helvetica", 10))
                                self.txtfld5.place(x=270, y=250,width=260)
                                self.txtfld5.insert(0, serial)



                                self.btn = ttk.Button(window, text="NEXT", width=20, command=self.validate)
                                self.btn.place(x=60, y=330, width=200, height=50)

                                self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                                self.btn_quit.place(x=330, y=330, width=200, height=50)

                            def validate(self):
                                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):
                                    window_user_login.destroy()

                                    print("Hola")

                                    # IF VALIDATION IS SUCCESFUL THEN IT OPENS USER EDIT WINDOW
                                    pass


                                else:
                                    messagebox.showerror("Error", "INVALID CREDENTIALS")

                            def reset(self):
                                self.txtfld1.delete(0,len(self.txtfld1.get()))
                                self.txtfld1.insert(0, "")

                                self.txtfld2.delete(0,len(self.txtfld2.get()))
                                self.txtfld2.insert(0, "")

                                self.txtfld3.delete(0,len(self.txtfld3.get()))
                                self.txtfld3.insert(0, "")

                                self.txtfld4.delete(0,len(self.txtfld4.get()))
                                self.txtfld4.insert(0, "")

                                self.txtfld5.delete(0,len(self.txtfld5.get()))
                                self.txtfld5.insert(0, "")



                        window_user_login_2 = tk.Tk()
                        window_user_login_2.config(background='white')
                        window_user_login_2.attributes('-alpha', 0.9)

                        user_login_window = User_2(window_user_login_2)
                        window_user_login_2.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                        window_user_login_2.title('Get Bulk Data ' + version)
                        window_user_login_2.geometry("600x450")
                        window_user_login_2.mainloop()

                    user_login_2()

















                    print("Hola")

                    # IF VALIDATION IS SUCCESFUL THEN IT OPENS USER EDIT WINDOW



                else:
                    messagebox.showerror("Error", "INVALID CREDENTIALS")















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

