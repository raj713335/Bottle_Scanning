import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import cv2
from datetime import date, datetime
from threading import Thread
import time
import socket
import subprocess
import calendar


global version
version = "1.0.0"



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

    for i in range(0, 3):
        loading()

    def user_login_over_ride():
        class User_Login():

            def __init__(self, window):

                self.UID = []
                self.PWD = []

                with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        x, y = list(map(str, each.split(",")))
                        print(x, y)
                        x = str(x).replace("\n", "")
                        y = str(y).replace("\n", "")
                        self.UID.append(x)
                        self.PWD.append(y)

                # Static user Name and Password
                # self.UID = ["John_Deere_Admin"]
                # self.PWD = ["1234"]

                print(self.UID)
                print(self.PWD)

                self.lbl = tk.Label(window, text="User", font=("Helvetica", 20), bg='#EFEFEF')
                self.lbl.place(x=60, y=90)

                self.txtfld1 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 20))
                self.txtfld1.place(x=220, y=90)

                self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20), bg='#EFEFEF')
                self.lb2.place(x=60, y=220)

                self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*", font=("Helvetica", 20))
                self.txtfld2.place(x=220, y=220)

                self.btn = ttk.Button(window, text="LOGIN", width=20, command=self.validate)
                self.btn.place(x=60, y=330, width=200, height=50)

                self.btn_quit = ttk.Button(window, text="QUIT", width=20, command=self.quit)
                self.btn_quit.place(x=330, y=330, width=200, height=50)

            def validate(self):
                if (str(self.txtfld1.get()) in self.UID) and (str(self.txtfld2.get()) in self.PWD):
                    window_user_login.destroy()

                    user_login_2()







                    # IF VALIDATION IS SUCCESFUL THEN IT OPENS USER EDIT WINDOW



                else:
                    messagebox.showerror("Error", "INVALID CREDENTIALS")

            def quit(self):
                window_user_login.destroy()

        window_user_login = tk.Tk()
        window_user_login.config(background='#EFEFEF')
        window_user_login.attributes('-alpha', 0.97)

        user_login_window = User_Login(window_user_login)
        window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login.title('Admin Login ' + version)
        window_user_login.geometry("600x450")
        window_user_login.mainloop()





    # version = "2.0.0"


    def user_login_2(a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0)):
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
                        string = str(each)

                print(string)

                if a1==str(0):
                    date_x = re.findall('17[0-9]{6}', string)
                    try:
                        date_x = date_x[0]
                    except:
                        date_x = ''
                    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
                else:
                    date_x=a1



                if b1==str(0):
                    lot = re.findall(r'10[0-9A-Za-z]*', string)
                    try:
                        lot = lot[0][3:-1]
                    except:
                        lot = ''
                else:
                    lot=b1


                if c1==str(0):
                    gstin = re.findall('01[0-9]{14}', string)
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''
                else:
                    gstin=c1


                if d1==str(0):
                    total=""
                else:
                    total=d1


                if e1==str(0):
                    serial = re.findall(r'21[0-9]*', string)
                    try:
                        serial = serial[0][2:-1]
                    except:
                        serial = ''
                else:
                    serial=e1

                # strings=string.split("")
                #
                # for string in strings:
                #
                #     print(string)
                #
                #     x1=string.find('17')
                #     if x1!=-1 and date_x=='':
                #         date_x=string[x1+2:x1+8]
                #         date_x='20'+date_x[0:2]+'-'+date_x[2:4]+'-'+date_x[:]
                #
                #     # x2 = string.find('01')
                #     # if x2!=-1:
                #     #     gstin = string[x2 + 2:x2 + 16]
                #
                #     x3 = string.find('21')
                #     if x3!=-1 and serial=='':
                #         serial = string[x3 + 2:]
                #
                #     x4 = string.find('10')
                #     if x4 != -1 and lot=='':
                #         lot = string[x4 + 2:]
                #
                #     print(date_x,gstin,lot,serial)

                print(date_x, gstin, lot, serial)

                def turn_button(x=0):

                    self.txtfld1.destroy()
                    self.txtfld1 = DateEntry(window, font=("Helvetica", 10), state='readonly',
                                             date_pattern='y-mm-dd', anchor='center')
                    self.txtfld1.place(x=270, y=130, width=260)

                load = cv2.imread('DATA/IMAGES/bottle.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(100), int(110)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=80, y=10)

                self.lb0 = tk.Label(window, text="Bulk Details", font=("Helvetica", 30,'bold'), bg='#EFEFEF')
                self.lb0.place(x=200, y=50)

                self.lb1 = tk.Label(window, text="EXP(YYYY-MM-DD)", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb1.place(x=60, y=130)

                # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=130, width=260)
                self.txtfld1.set(date_x)

                self.txtfld1.bind("<Button-1>", turn_button)

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=180)

                self.txtfld2 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld2.place(x=270, y=180, width=260)
                self.txtfld2.insert(0, lot)

                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=230)

                self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
                self.txtfld3.place(x=270, y=230, width=260)
                self.txtfld3.insert(0, gstin)

                self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4.place(x=60, y=280)


                self.txtfld4 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld4.place(x=270, y=280, width=260)
                self.txtfld4.insert(0, total)

                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb5.place(x=60, y=330)

                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld5.place(x=270, y=330, width=260)
                self.txtfld5.insert(0, serial)

                # self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.validate)
                # self.btn_back.place(x=60, y=380, width=130, height=40)


                self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                self.btn_quit.place(x=232, y=380, width=130, height=40)

                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=self.validate)
                self.btn_next.place(x=400, y=380, width=130, height=40)

            def validate(self):

                if ((str(self.txtfld1.get()) != "")):

                    a=0

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    return (0)




                if ((str(self.txtfld2.get()) != "")):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    return (0)


                if ((str(self.txtfld3.get()) != "")
                         and
                        (len(str(self.txtfld3.get())) == 14)):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Wrong/Missing GSTIN Number")
                    return (0)





                if ((str(self.txtfld5.get()) != "") ):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    return (0)



                try:

                    print(1)
                    temp=int((self.txtfld4.get()))



                    print(3)




                except:
                    messagebox.showwarning("Warning", "Wrong/Missing Total Bottle")
                    return (0)



                window_user_login_2.destroy()



                # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW

                user_login_3(a1=(str(self.txtfld1.get())), b1=(str(self.txtfld2.get())), c1=(str(self.txtfld3.get())),
                             d1=(str(self.txtfld4.get())), e1=(str(self.txtfld5.get())), a2=a2, b2=b2, c2=c2, d2=d2,
                             e2=e2)




            def reset(self):


                # self.txtfld1.delete(0, len(self.txtfld1.get()))
                # self.txtfld1.insert(0, "")

                self.txtfld1.set("")


                self.txtfld2.delete(0, len(self.txtfld2.get()))
                self.txtfld2.insert(0, "")

                self.txtfld3.delete(0, len(self.txtfld3.get()))
                self.txtfld3.insert(0, "")

                self.txtfld4.delete(0, len(self.txtfld4.get()))
                self.txtfld4.insert(0, "")

                self.txtfld5.delete(0, len(self.txtfld5.get()))
                self.txtfld5.insert(0, "")






        window_user_login_2 = tk.Tk()
        window_user_login_2.config(background='#EFEFEF')
        window_user_login_2.attributes('-alpha', 0.97)

        user_login_window = User_2(window_user_login_2)
        window_user_login_2.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_2.title('Get Bulk Data ' + '2.0.0')
        window_user_login_2.geometry("600x450")
        window_user_login_2.mainloop()




    # version = "3.0.0"

    def user_login_3(a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0)):

        print(4)


        class User_3():

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
                        string = str(each)

                print(string)

                # date_x = re.findall('17[0-9]{6}', string)
                # try:
                #     date_x = date_x[0]
                # except:
                #     date_x = ''
                # date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
                #
                # gstin = re.findall('01[0-9]{14}', string)
                # try:
                #     gstin = gstin[0][2:]
                # except:
                #     gstin = ''
                #
                # lot = re.findall(r'10[0-9A-Za-z]*', string)
                # try:
                #     lot = lot[0][3:-1]
                # except:
                #     lot = ''
                #
                # serial = re.findall(r'21[0-9]*', string)
                # try:
                #     serial = serial[0][2:-1]
                # except:
                #     serial = ''

                # strings=string.split("")
                #
                # for string in strings:
                #
                #     print(string)
                #
                #     x1=string.find('17')
                #     if x1!=-1 and date_x=='':
                #         date_x=string[x1+2:x1+8]
                #         date_x='20'+date_x[0:2]+'-'+date_x[2:4]+'-'+date_x[:]
                #
                #     # x2 = string.find('01')
                #     # if x2!=-1:
                #     #     gstin = string[x2 + 2:x2 + 16]
                #
                #     x3 = string.find('21')
                #     if x3!=-1 and serial=='':
                #         serial = string[x3 + 2:]
                #
                #     x4 = string.find('10')
                #     if x4 != -1 and lot=='':
                #         lot = string[x4 + 2:]
                #
                #     print(date_x,gstin,lot,serial)

                if a2 == str(0):
                    date_x = re.findall('17[0-9]{6}', string)
                    try:
                        date_x = date_x[0]
                    except:
                        date_x = ''
                    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
                else:
                    date_x = a1

                if b2 == str(0):
                    lot = re.findall(r'10[0-9A-Za-z]*', string)
                    try:
                        lot = lot[0][3:-1]
                    except:
                        lot = ''
                else:
                    lot = b1

                if c2 == str(0):
                    gstin = re.findall('01[0-9]{14}', string)
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''
                else:
                    gstin = c1

                if d2 == str(0):
                    total = ""
                else:
                    total = d1

                if e2 == str(0):
                    serial = re.findall(r'21[0-9]*', string)
                    try:
                        serial = serial[0][2:-1]
                    except:
                        serial = ''
                else:
                    serial = e1

                print(date_x, gstin, lot, serial)

                def turn_button(x=0):

                    self.txtfld1.destroy()
                    self.txtfld1 = DateEntry(window, font=("Helvetica", 10),
                                             state='readonly',
                                             date_pattern='y-mm-dd',
                                             anchor='center')
                    self.txtfld1.place(x=270, y=130, width=260)

                load = cv2.imread('DATA/IMAGES/bottle.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(100), int(110)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=80, y=10)

                self.lb0 = tk.Label(window, text="Repacking Details", font=("Helvetica", 25, 'bold'), bg='#EFEFEF')
                self.lb0.place(x=200, y=50)

                self.lb1 = tk.Label(window, text="EXP(YYYY-MM-DD)", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb1.place(x=60, y=130)

                # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=130, width=260)
                self.txtfld1.set(date_x)

                self.txtfld1.bind("<Button-1>", turn_button)

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=180)

                self.txtfld2 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld2.place(x=270, y=180, width=260)
                self.txtfld2.insert(0, lot)

                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=230)

                self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
                self.txtfld3.place(x=270, y=230, width=260)
                self.txtfld3.insert(0, gstin)

                self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4.place(x=60, y=280)

                self.txtfld4 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld4.place(x=270, y=280, width=260)
                self.txtfld4.insert(0, total)

                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb5.place(x=60, y=330)

                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld5.place(x=270, y=330, width=260)
                self.txtfld5.insert(0, serial)

                self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                self.btn_back.place(x=60, y=380, width=130, height=40)

                self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                self.btn_quit.place(x=232, y=380, width=130, height=40)

                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=self.validate)
                self.btn_next.place(x=400, y=380, width=130, height=40)


            def back(self):


                window_user_login_3.destroy()

                user_login_2(a1=a1,b1=b1,c1=c1,d1=d1,e1=e1,a2=(str(self.txtfld1.get())),b2=(str(self.txtfld2.get())),
                             c2=(str(self.txtfld3.get())),d2=(str(self.txtfld4.get())),e2=(str(self.txtfld5.get())))



            def validate(self):

                if ((str(self.txtfld1.get()) != "")):

                    a=0

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    return (0)




                if ((str(self.txtfld2.get()) != "")):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    return (0)


                if ((str(self.txtfld3.get()) != "")
                         and
                        (len(str(self.txtfld3.get())) == 14)):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Wrong/Missing GSTIN Number")
                    return (0)





                if ((str(self.txtfld5.get()) != "") ):

                    a = 0

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    return (0)



                try:
                    temp=int((self.txtfld4.get()))

                    window_user_login_3.destroy()



                    # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW

                    #user_login_4()




                except:
                    messagebox.showwarning("Warning", "Wrong/Missing Total Bottle")


            def reset(self):

                # self.txtfld1.delete(0, len(self.txtfld1.get()))
                # self.txtfld1.insert(0, "")

                self.txtfld1.set("")

                self.txtfld2.delete(0, len(self.txtfld2.get()))
                self.txtfld2.insert(0, "")

                self.txtfld3.delete(0, len(self.txtfld3.get()))
                self.txtfld3.insert(0, "")

                self.txtfld4.delete(0, len(self.txtfld4.get()))
                self.txtfld4.insert(0, "")

                self.txtfld5.delete(0, len(self.txtfld5.get()))
                self.txtfld5.insert(0, "")

        window_user_login_3 = tk.Tk()
        window_user_login_3.config(background='#EFEFEF')
        window_user_login_3.attributes('-alpha', 0.97)

        user_login_window = User_3(window_user_login_3)
        window_user_login_3.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_3.title('Get Repacking Data ' + version)
        window_user_login_3.geometry("600x450")
        window_user_login_3.mainloop()

    user_login_over_ride()











if __name__ == '__main__':
    main()
