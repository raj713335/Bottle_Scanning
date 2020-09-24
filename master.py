import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox,Frame
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

                    user_name=str(self.txtfld1.get())
                    window_user_login.destroy()

                    user_login_2(user_name=user_name)







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


    def user_login_2(a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0),user_name=str(0)):
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

                    lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
                    try:
                        lot = str(lot[0]).replace('', "")
                        lot = lot.replace('10', '')

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


                if str(d1)==str(0):
                    total=""
                else:
                    total=d1


                print("vvv"+d1)


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
                    self.txtfld1.place(x=270, y=160, width=260)

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
                self.lb1.place(x=60, y=160)

                # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=160, width=260)
                self.txtfld1.set(date_x)

                self.txtfld1.bind("<Button-1>", turn_button)

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=210)

                self.txtfld2 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld2.place(x=270, y=210, width=260)
                self.txtfld2.insert(0, lot)

                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=260)

                self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
                self.txtfld3.place(x=270, y=260, width=260)
                self.txtfld3.insert(0, gstin)

                self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4.place(x=60, y=310)


                self.txtfld4 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld4.place(x=270, y=310, width=260)
                self.txtfld4.insert(0, total)

                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
                #self.lb5.place(x=60, y=330)

                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                #self.txtfld5.place(x=270, y=330, width=260)
                self.txtfld5.insert(0, serial)

                # self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.validate)
                # self.btn_back.place(x=60, y=380, width=130, height=40)


                self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                self.btn_quit.place(x=60, y=380, width=160, height=40)

                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=self.validate)
                self.btn_next.place(x=370, y=380, width=160, height=40)

            def validate(self):

                if ((str(self.txtfld1.get()) != "")):

                    a1=(str(self.txtfld1.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    return (0)




                if ((str(self.txtfld2.get()) != "")):

                    b1=(str(self.txtfld2.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    return (0)


                if ((str(self.txtfld3.get()) != "")):

                    c1=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Missing GSTIN Number Field")
                    return (0)


                if ((len(str(self.txtfld3.get())) == 14)):

                    c1=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Wrong GSTIN Number Format")
                    return (0)





                if ((str(self.txtfld5.get()) != "") ):

                    e1=(str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    return (0)


                if ((str(self.txtfld4.get()) != "") ):

                    e1=(str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Total Bottles Field")
                    return (0)



                try:

                    print(1)
                    temp=int((self.txtfld4.get()))

                    d1=str(self.txtfld4.get())



                    print(3)




                except:
                    messagebox.showwarning("Warning", "Total Bottle field must be numeric")
                    return (0)



                window_user_login_2.destroy()



                # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW

                user_login_3(user_name=user_name,a1=a1, b1=b1, c1=c1,
                             d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
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















    def user_login_3(user_name=str(0),a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0)):

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
                    date_x = a2

                if b2 == str(0):

                    lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
                    try:
                        lot = str(lot[0]).replace('', "")
                        lot = lot.replace('10', '')
                    except:
                        lot = ''
                else:
                    lot = b2

                if c2 == str(0):
                    gstin = re.findall('01[0-9]{14}', string)
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''
                else:
                    gstin = c2

                if d2 == str(0):
                    total = ""
                else:
                    total = d2

                if e2 == str(0):
                    serial = re.findall(r'21[0-9]*', string)
                    try:
                        serial = serial[0][2:-1]
                    except:
                        serial = ''
                else:
                    serial = e2

                print(date_x, gstin, lot, serial)

                def turn_button(x=0):

                    self.txtfld1.destroy()
                    self.txtfld1 = DateEntry(window, font=("Helvetica", 10),
                                             state='readonly',
                                             date_pattern='y-mm-dd',
                                             anchor='center')
                    self.txtfld1.place(x=270, y=160, width=260)

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
                self.lb1.place(x=60, y=160)

                # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=160, width=260)
                self.txtfld1.set(date_x)

                self.txtfld1.bind("<Button-1>", turn_button)

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=210)

                self.txtfld2 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld2.place(x=270, y=210, width=260)
                self.txtfld2.insert(0, lot)

                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=260)

                self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
                self.txtfld3.place(x=270, y=260, width=260)
                self.txtfld3.insert(0, gstin)

                self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4.place(x=60, y=310)

                self.txtfld4 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld4.place(x=270, y=310, width=260)
                self.txtfld4.insert(0, total)

                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
                #self.lb5.place(x=60, y=330)

                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                #self.txtfld5.place(x=270, y=330, width=260)
                self.txtfld5.insert(0, serial)

                self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                self.btn_back.place(x=60, y=380, width=130, height=40)

                self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                self.btn_quit.place(x=232, y=380, width=130, height=40)

                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=self.validate)
                self.btn_next.place(x=400, y=380, width=130, height=40)


            def back(self):
                a2 = (str(self.txtfld1.get()))
                b2 = (str(self.txtfld2.get()))
                c2 = (str(self.txtfld3.get()))
                d2 = (str(self.txtfld4.get()))
                e2 = (str(self.txtfld5.get()))


                window_user_login_3.destroy()



                user_login_2(user_name=user_name,a1=a1,b1=b1,c1=c1,d1=d1,e1=e1,a2=a2,b2=b2,
                             c2=c2,d2=d2,e2=e2)



            def validate(self):

                if ((str(self.txtfld1.get()) != "")):

                    a2=(str(self.txtfld1.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    return (0)




                if ((str(self.txtfld2.get()) != "")):

                    b2=(str(self.txtfld2.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    return (0)


                if ((str(self.txtfld3.get()) != "")):

                    c2=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Missing GSTIN Number Field")
                    return (0)


                if (    (len(str(self.txtfld3.get())) == 14)):

                    c2=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Wrong GSTIN Number")
                    return (0)





                if ((str(self.txtfld5.get()) != "") ):

                    e2=(str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    return (0)



                if ((str(self.txtfld4.get()) != "") ):

                    d2=(str(self.txtfld4.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Total Bottle Field")
                    return (0)


                try:
                    temp=int((self.txtfld4.get()))
                    d2 = (str(self.txtfld4.get()))






                except:
                    messagebox.showwarning("Warning", "Total Bottle field must be numeric")
                    return(0)




                if (d1==d2):

                    a2=(str(self.txtfld1.get()))

                else:

                    messagebox.showwarning("Warning", "Total Bottle value in Bulk Data and Repacking Data are not Same")
                    return (0)

                window_user_login_3.destroy()

                # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW

                quiter(user_name=user_name,a1=a1, b1=b1, c1=c1,
                             d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
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





        window_user_login_3 = tk.Tk()
        window_user_login_3.config(background='#EFEFEF')
        window_user_login_3.attributes('-alpha', 0.97)

        user_login_window = User_3(window_user_login_3)
        window_user_login_3.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_3.title('Get Repacking Data ' + '3.0.0')
        window_user_login_3.geometry("600x450")
        window_user_login_3.mainloop()





    # def user_login_4(a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0)):
    #     class User_4():
    #
    #         def __init__(self, window):
    #
    #             # class CustomDateEntry(DateEntry):
    #             #
    #             #     def _select(self, event=None):
    #             #         date = self._calendar.selection_get()
    #             #         if date is not None:
    #             #             self._set_text(date.strftime('%Y-%m-%d'))
    #             #             self.event_generate('<<DateEntrySelected>>')
    #             #         self._top_cal.withdraw()
    #             #         if 'readonly' not in self.state():
    #             #             self.focus_set()
    #
    #             with open('DATA/Scanning/data.txt', 'r') as fh:
    #                 all_lines = fh.readlines()
    #                 for each in all_lines:
    #                     string = str(each)
    #
    #             print(string)
    #
    #             date_x = re.findall('17[0-9]{6}', string)
    #             try:
    #                 date_x = date_x[0]
    #             except:
    #                 date_x = ''
    #             date_x = '20' + date_x[2:4] + '-' + date_x[
    #                                                 4:6] + '-' + date_x[
    #                                                              6:8]
    #
    #             gstin = re.findall('01[0-9]{14}', string)
    #             try:
    #                 gstin = gstin[0][2:]
    #             except:
    #                 gstin = ''
    #
    #             lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
    #             try:
    #                 lot = str(lot[0]).replace('', "")
    #                 lot = lot.replace('10', '')
    #             except:
    #                 lot = ''
    #
    #             serial = re.findall(r'21[0-9]*', string)
    #             try:
    #                 serial = serial[0][2:-1]
    #             except:
    #                 serial = ''
    #
    #             #
    #             # # strings=string.split("")
    #             # #
    #             # # for string in strings:
    #             # #
    #             # #     print(string)
    #             # #
    #             # #     x1=string.find('17')
    #             # #     if x1!=-1 and date_x=='':
    #             # #         date_x=string[x1+2:x1+8]
    #             # #         date_x='20'+date_x[0:2]+'-'+date_x[2:4]+'-'+date_x[:]
    #             # #
    #             # #     # x2 = string.find('01')
    #             # #     # if x2!=-1:
    #             # #     #     gstin = string[x2 + 2:x2 + 16]
    #             # #
    #             # #     x3 = string.find('21')
    #             # #     if x3!=-1 and serial=='':
    #             # #         serial = string[x3 + 2:]
    #             # #
    #             # #     x4 = string.find('10')
    #             # #     if x4 != -1 and lot=='':
    #             # #         lot = string[x4 + 2:]
    #             # #
    #             # #     print(date_x,gstin,lot,serial)
    #             #
    #             # print(date_x, gstin, lot, serial)
    #             #
    #             # def turn_button(x=0):
    #             #
    #             #     self.txtfld1.destroy()
    #             #     self.txtfld1 = DateEntry(window, font=(
    #             #     "Helvetica", 10),
    #             #                              state='readonly',
    #             #                              date_pattern='y-mm-dd',
    #             #                              anchor='center')
    #             #     self.txtfld1.place(x=270, y=50, width=260)
    #             #
    #             # self.lb1 = tk.Label(window,
    #             #                     text="EXP(YYYY-MM-DD)",
    #             #                     font=("Helvetica", 10),
    #             #                     bg='white')
    #             # self.lb1.place(x=60, y=50)
    #             #
    #             # # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
    #             # self.txtfld1 = ttk.Combobox(window,
    #             #                             font=(
    #             #                             "Helvetica", 10),
    #             #                             state='readonly')
    #             # self.txtfld1.place(x=270, y=50, width=260)
    #             # self.txtfld1.set(date_x)
    #             #
    #             # self.txtfld1.bind("<Button-1>", turn_button)
    #             #
    #             # self.lb2 = tk.Label(window, text="Bulk Lot",
    #             #                     font=("Helvetica", 10),
    #             #                     bg='white')
    #             # self.lb2.place(x=60, y=100)
    #             #
    #             # self.txtfld2 = ttk.Entry(window,
    #             #                          font=("Helvetica", 10))
    #             # self.txtfld2.place(x=270, y=100, width=260)
    #             # self.txtfld2.insert(0, lot)
    #             #
    #             # self.lb3 = tk.Label(window, text="GTIN",
    #             #                     font=("Helvetica", 10),
    #             #                     bg='white')
    #             # self.lb3.place(x=60, y=150)
    #             #
    #             # self.txtfld3 = ttk.Entry(window,
    #             #                          text="Enter UID",
    #             #                          font=("Helvetica", 10))
    #             # self.txtfld3.place(x=270, y=150, width=260)
    #             # self.txtfld3.insert(0, gstin)
    #             #
    #             # self.lb4 = tk.Label(window,
    #             #                     text="Total Bottles",
    #             #                     font=("Helvetica", 10),
    #             #                     bg='white')
    #             # self.lb4.place(x=60, y=200)
    #             #
    #             # self.txtfld4 = ttk.Entry(window,
    #             #                          font=("Helvetica", 10))
    #             # self.txtfld4.place(x=270, y=200, width=260)
    #             #
    #             # self.lb5 = tk.Label(window, text="Batch Size",
    #             #                     font=("Helvetica", 10),
    #             #                     bg='white')
    #             # self.lb5.place(x=60, y=250)
    #             #
    #             # self.txtfld5 = ttk.Entry(window,
    #             #                          font=("Helvetica", 10))
    #             # self.txtfld5.place(x=270, y=250, width=260)
    #             # self.txtfld5.insert(0, serial)
    #
    #             def turn_button(x=0):
    #
    #                 self.txtfld1.destroy()
    #                 self.txtfld1 = DateEntry(window, font=("Helvetica", 10),
    #                                          state='readonly',
    #                                          date_pattern='y-mm-dd',
    #                                          anchor='center')
    #                 self.txtfld1.place(x=270, y=160, width=260)
    #
    #             load = cv2.imread('DATA/IMAGES/bottle.png', 1)
    #             cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
    #             load = Image.fromarray(cv2imagex1)
    #             load = load.resize((int(100), int(110)), Image.ANTIALIAS)
    #             render = ImageTk.PhotoImage(load)
    #             img = tk.Label(image=render)
    #             img.image = render
    #             img.place(x=80, y=10)
    #
    #             self.lb0 = tk.Label(window, text="Scanning Page", font=("Helvetica", 25, 'bold'), bg='#EFEFEF')
    #             self.lb0.place(x=230, y=50)
    #
    #             self.lb1 = tk.Label(window, text="EXP(YYYY-MM-DD)", font=("Helvetica", 10), bg='#EFEFEF')
    #             self.lb1.place(x=60, y=160)
    #
    #             # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
    #             self.txtfld1 = ttk.Combobox(window,
    #                                         font=("Helvetica", 10), state='readonly')
    #             self.txtfld1.place(x=270, y=160, width=260)
    #             #self.txtfld1.set(date_x)
    #
    #             self.txtfld1.bind("<Button-1>", turn_button)
    #
    #             self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
    #             self.lb2.place(x=60, y=210)
    #
    #             self.txtfld2 = ttk.Entry(window,
    #                                      font=("Helvetica", 10))
    #             self.txtfld2.place(x=270, y=210, width=260)
    #             #self.txtfld2.insert(0, lot)
    #
    #             self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
    #             self.lb3.place(x=60, y=260)
    #
    #             self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
    #             self.txtfld3.place(x=270, y=260, width=260)
    #             #self.txtfld3.insert(0, gstin)
    #
    #             self.lb4 = tk.Label(window, text="Total Bottles", font=("Helvetica", 10), bg='#EFEFEF')
    #             self.lb4.place(x=60, y=310)
    #
    #             self.txtfld4 = ttk.Entry(window,
    #                                      font=("Helvetica", 10))
    #             self.txtfld4.place(x=270, y=310, width=260)
    #
    #             self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
    #             #self.lb5.place(x=60, y=330)
    #
    #             self.txtfld5 = ttk.Entry(window,
    #                                      font=("Helvetica", 10))
    #             #self.txtfld5.place(x=270, y=330, width=260)
    #             #self.txtfld5.insert(0, serial)
    #
    #             self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
    #             self.btn_back.place(x=60, y=380, width=130, height=40)
    #
    #             self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
    #             self.btn_quit.place(x=232, y=380, width=130, height=40)
    #
    #             self.btn_next = ttk.Button(window, text="NEXT", width=20, command=self.validate)
    #             self.btn_next.place(x=400, y=380, width=130, height=40)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #         def validate(self):
    #
    #             if ((str(self.txtfld1.get()) != "")):
    #
    #                 a2=(str(self.txtfld1.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Missing Date Field")
    #                 return (0)
    #
    #
    #
    #
    #             if ((str(self.txtfld2.get()) != "")):
    #
    #                 b2=(str(self.txtfld2.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Missing Bulk Lot Field")
    #                 return (0)
    #
    #
    #             if ((str(self.txtfld3.get()) != "")):
    #
    #                 c2=(str(self.txtfld3.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Missing GSTIN Number Field")
    #                 return (0)
    #
    #
    #             if (    (len(str(self.txtfld3.get())) == 14)):
    #
    #                 c2=(str(self.txtfld3.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Wrong GSTIN Number")
    #                 return (0)
    #
    #
    #
    #
    #
    #             if ((str(self.txtfld5.get()) != "") ):
    #
    #                 e2=(str(self.txtfld5.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Missing Batch Size Field")
    #                 return (0)
    #
    #
    #
    #             if ((str(self.txtfld4.get()) != "") ):
    #
    #                 d2=(str(self.txtfld4.get()))
    #
    #             else:
    #
    #                 messagebox.showwarning("Warning", "Missing Total Bottle Field")
    #                 return (0)
    #
    #
    #             try:
    #                 temp=int((self.txtfld4.get()))
    #                 d2 = (str(self.txtfld4.get()))
    #
    #
    #
    #
    #
    #
    #             except:
    #                 messagebox.showwarning("Warning", "Total Bottle field must be numeric")
    #                 return(0)
    #
    #
    #             window_user_login_4.destroy()
    #
    #             # if (str(self.txtfld1.get()) != "") and (
    #             #         str(self.txtfld2.get()) != "") and (
    #             #         str(self.txtfld3.get()) != "") \
    #             #         and (
    #             #         str(self.txtfld4.get()) != "") and (
    #             #         str(self.txtfld5.get()) != ""):
    #             #
    #             #     if len(str(self.txtfld3.get())) == 14:
    #             #
    #             #         window_user_login_4.destroy()
    #             #
    #             #         print("Hola")
    #             #
    #             #         # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW
    #             #         pass
    #             #
    #             #
    #             #     else:
    #             #         messagebox.showwarning("Warning",
    #             #                                "Missing Values")
    #             #
    #             #
    #             # else:
    #             #     messagebox.showwarning("Warning",
    #             #                            "Missing Values")
    #
    #         def back(self):
    #
    #             MsgBox = tk.messagebox.askquestion('Warning',
    #                                                'All Progress will be lost',
    #                                                icon='warning')
    #
    #             if MsgBox=='yes':
    #
    #
    #                 window_user_login_4.destroy()
    #
    #                 user_login_3(a1=a1,b1=b1,c1=c1,d1=d1,e1=e1,a2=a2,b2=b2,
    #                              c2=c2,d2=d2,e2=e2)
    #
    #             else:
    #                 pass
    #
    #
    #
    #
    #
    #         def reset(self):
    #
    #             # self.txtfld1.delete(0, len(self.txtfld1.get()))
    #             # self.txtfld1.insert(0, "")
    #
    #             self.txtfld1.set("")
    #
    #             self.txtfld2.delete(0, len(self.txtfld2.get()))
    #             self.txtfld2.insert(0, "")
    #
    #             self.txtfld3.delete(0, len(self.txtfld3.get()))
    #             self.txtfld3.insert(0, "")
    #
    #             self.txtfld4.delete(0, len(self.txtfld4.get()))
    #             self.txtfld4.insert(0, "")
    #
    #             self.txtfld5.delete(0, len(self.txtfld5.get()))
    #             self.txtfld5.insert(0, "")
    #
    #     window_user_login_4 = tk.Tk()
    #     window_user_login_4.config(background='#EFEFEF')
    #     window_user_login_4.attributes('-alpha', 0.97)
    #
    #     user_login_window = User_4(window_user_login_4)
    #     window_user_login_4.iconbitmap(
    #         default='DATA/IMAGES/icons/favicon.ico')
    #     window_user_login_4.title(
    #         'Scanning Page ' + '4.0.0')
    #     window_user_login_4.geometry("600x450")
    #     window_user_login_4.mainloop()
    #
    #

    def quiter(user_name=str(0),a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0), c2=str(0), d2=str(0),
                     e2=str(0)):
        xml_data=[]

        stringx = []



        with open('DATA/Scanning/scanning.txt', 'r') as fh:
            all_lines = fh.readlines()
            for each in all_lines:
                stringx.append(each.replace('\n', ''))

        print(stringx)

        user_login_4(a1=a1, b1=b1, c1=c1,
                     d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                     e2=e2, date_xx=a2, gstin_x=c2, lot_x=b2, serial_x=e2, id='NIL', limit='nil')




        i = 0

        sl_dub=[]

        for string in stringx:

            i += 1

            date_x = re.findall('17[0-9]{6}', string)
            try:
                date_x = date_x[0]
            except:
                date_x = ''
            date_x = '20' + date_x[2:4] + '-' + date_x[
                                                4:6] + '-' + date_x[
                                                             6:8]

            gstin = re.findall('01[0-9]{14}', string)
            try:
                gstin = gstin[0][2:]
            except:
                gstin = ''

            lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
            try:
                lot = str(lot[0]).replace('', "")
                lot = lot.replace('10', '')
            except:
                lot = ''

            serial = re.findall(r'21[0-9]*', string)
            try:
                serial = serial[0][2:-1]
            except:
                serial = ''


            if serial not in sl_dub:

                xm=user_login_4(a1=a1, b1=b1, c1=c1,
                         d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                         e2=e2,date_xx=date_x,gstin_x=gstin,lot_x=lot,serial_x=serial,id=i,limit=3000)

                print("88",xm)

                if xm==True:
                    string=string.replace('\x1d','')
                    xml_data.append(string)

                sl_dub.append(serial)

        def xml_creator():

            from datetime import datetime
            from xml.dom import minidom
            from xml.dom.minidom import getDOMImplementation

            root = minidom.Document()
            root.standalone = 'No'

            iso_date = datetime.now().astimezone().isoformat()
            offset = iso_date[-6:]
            expire_date = a1
            bulk_lot_number = b1
            repackage_lot_number = b2
            strings = xml_data

            print(xml_data)

            list_data = ''

            for each in strings:
                list_data += str('<epcis:epc>') + each + str('</epcis:epc>')

            stringlx = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <epcis:EPCISDocument xmlns:epcis="urn:epcglobal:epcis:xsd:1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creationDate="{iso_date}" schemaVersion="1">
            <epcis:EPCISBody>
            <epcis:EventList>
            <epcis:ObjectEvent>
            <epcis:eventTime>{iso_date}</epcis:eventTime>
            <epcis:eventTimeZoneOffset>{offset}</epcis:eventTimeZoneOffset>
            <epcis:epcList>''' + str(list_data) + f'''
            </epcis:epcList>
            <epcis:action>ADD</epcis:action>
            <epcis:bizStep>urn:epcglobal:cbv:bizstep:commissioning</epcis:bizStep>
            <epcis:disposition>urn:epcglobal:cbv:disp:active</epcis:disposition>
            <epcis:readPoint>
            <epcis:id>urn:systechcitadel.com:device:sgln:101</epcis:id>
            </epcis:readPoint>
            <epcis:bizLocation>
            <epcis:id>urn:epc:id:sgln:08662190003.0.0</epcis:id>
            </epcis:bizLocation>
            <epcis:extension><!--@Verify By '''+user_name+f'''-->
            <epcis:field name="Lot Number (Bulk)" value="{bulk_lot_number}"/>
            <epcis:field name="Expiration Date" value="{expire_date}"/>
            <epcis:field name="Lot Number (Repackaged)" value="{repackage_lot_number}"/>
            </epcis:extension>
            </epcis:ObjectEvent>
            </epcis:EventList>
            </epcis:EPCISBody>
            </epcis:EPCISDocument>
            '''

            dom = minidom.parseString(stringlx)

            xml_str = dom.toprettyxml(indent="  ", newl='', encoding='UTF-8')
            timestamp = int(datetime.now().timestamp())
            save_path_file = f"{b1}-{b2}-{timestamp}.xml"

            with open(save_path_file, "w") as f:
                f.write(xml_str.decode())

        xml_creator()

        user_login_over_ride()




    def user_login_4(a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0), c2=str(0), d2=str(0),
                     e2=str(0),date_xx=str(0),gstin_x=str(0),lot_x=str(0),serial_x=str(0),id=str(0),limit=str(0)):

        validatex=True

        class User_4():




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

                stringx = []

                with open('DATA/Scanning/scanning.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        stringx.append(each.replace('\n', ''))

                print(stringx)

                # if limit=='nil':
                #
                #     if d2 != len(stringx):
                #
                #         MsgBox = tk.messagebox.askquestion('Warning',
                #                                            'Total Bottle in repacking data ' + str(
                #                                                d2) + ' do not match with the available data '
                #                                            + str(len(stringx)) + ' still want to proceed ?',
                #                                            icon='warning')
                #
                #         if MsgBox == 'yes':
                #             window_user_login_4.destroy()
                #
                #         else:
                #             user_login_3(a1=a1, b1=b1, c1=c1,
                #                          d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                #                          e2=e2)

                i = 0

                datax = []

                for string in stringx:

                    i += 1

                    date_x = re.findall('17[0-9]{6}', string)
                    try:
                        date_x = date_x[0]
                    except:
                        date_x = ''
                    date_x = '20' + date_x[2:4] + '-' + date_x[
                                                        4:6] + '-' + date_x[
                                                                     6:8]

                    gstin = re.findall('01[0-9]{14}', string)
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''

                    lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
                    try:
                        lot = str(lot[0]).replace('', "")
                        lot = lot.replace('10', '')
                    except:
                        lot = ''

                    serial = re.findall(r'21[0-9]*', string)
                    try:
                        serial = serial[0][2:-1]
                    except:
                        serial = ''

                    datax.append([date_x, lot, gstin, serial])

                def selectItem(a):
                    curItem = tree.focus()

                    # print(tree.item(curItem)['values'])
                    quantifiers = (tree.item(curItem)['values'])

                    self.txtfld1.set("")
                    self.txtfld2.delete(0, 'end')
                    self.txtfld3.delete(0, 'end')
                    self.txtfld5.delete(0, 'end')

                    self.txtfld1.set(str(quantifiers[1]))
                    self.txtfld2.insert(0, str(quantifiers[2]))
                    self.txtfld3.insert(0, str('0000' + str(quantifiers[3]))[-14:])
                    self.txtfld5.insert(0, str(quantifiers[4]))

                    # print(quantifiers)

                    print(quantifiers)

                load = cv2.imread('DATA/IMAGES/bottle.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(100), int(110)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=80, y=10)

                self.lb0 = tk.Label(window, text="Scanning Page", font=("Helvetica", 25, 'bold'), bg='#EFEFEF')
                self.lb0.place(x=200, y=50)

                self.txtfld00 = ttk.Entry(window, font=("Helvetica", 25), justify='center')
                self.txtfld00.place(x=450, y=50, width=70)
                self.txtfld00.insert(0, id)

                self.txtfld01 = ttk.Entry(window, font=("Helvetica", 25), justify='center')
                self.txtfld01.place(x=525, y=50, width=70)
                self.txtfld01.insert(0, d2)

                # def turn_button(x=0):
                #     self.txtfld1.destroy()
                #     self.txtfld1 = DateEntry(window, font=(
                #         "Helvetica", 10),
                #                              state='readonly',
                #                              date_pattern='y-mm-dd',
                #                              anchor='center')
                #     self.txtfld1.place(x=270, y=150, width=260)

                self.lb1 = tk.Label(window,
                                    text="EXP(YYYY-MM-DD)",
                                    font=("Helvetica", 10),
                                    bg='#EFEFEF')
                self.lb1.place(x=60, y=150)

                # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=150, width=260)
                self.txtfld1.set(date_xx)
                self.txtfld1.config(state='disabled')

                # self.txtfld1.bind("<Button-1>", turn_button)

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=190)

                self.txtfld2 = ttk.Combobox(window,
                                         font=("Helvetica", 10),state='readonly')
                self.txtfld2.place(x=270, y=190, width=260)
                self.txtfld2.set(lot_x)
                self.txtfld2.config(state='disabled')


                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=230)

                self.txtfld3 = ttk.Combobox(window, text="Enter UID", font=("Helvetica", 10),state='readonly')
                self.txtfld3.place(x=270, y=230, width=260)
                self.txtfld3.set(gstin_x)
                self.txtfld3.config(state='disabled')

                self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
                # self.lb5.place(x=60, y=330)

                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                # self.txtfld5.place(x=270, y=330, width=260)
                self.txtfld5.insert(0,serial_x)

                if str(limit)==str('end'):
                    self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                    self.btn_back.place(x=10, y=290, width=180, height=40)

                    self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                    self.btn_quit.place(x=205, y=290, width=180, height=40)

                    self.btn_update = ttk.Button(window, text="DELETE", width=20, command=self.delete)
                    self.btn_update.place(x=400, y=290, width=180, height=40)

                if str(limit) == str('nil'):
                    self.btn_finish = ttk.Button(window, text="START  SCANNING", width=20, command=self.start)
                    self.btn_finish.place(x=-1, y=290, width=605, height=160)


                # self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                # self.btn_back.place(x=10, y=290, width=130, height=40)
                #
                # self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
                # self.btn_quit.place(x=160, y=290, width=130, height=40)
                #
                # self.btn_update = ttk.Button(window, text="DELETE", width=20, command=self.delete)
                # self.btn_update.place(x=310, y=290, width=130, height=40)
                #
                # self.btn_finish = ttk.Button(window, text="FINISH", width=20)
                # self.btn_finish.place(x=460, y=290, width=130, height=40)

                if limit=='end':

                    frame = Frame(window_user_login_4)
                    frame.place(x=-1, y=344)

                    # print(data)

                    tree = ttk.Treeview(frame,
                                        columns=(1, 2, 3, 4, 5),
                                        height=4, show="headings")
                    tree.pack(side='left')
                    tree.bind('<ButtonRelease-1>', selectItem)

                    val = ["Sl No", "Exp Date", "Bulk Lot", "GTIN", "Serial", ]

                    for i in range(1, len(val) + 1):
                        tree.heading(i, text=val[i - 1])

                    # tree.heading(2, text="Column 2")
                    # tree.heading(3, text="Column 3")

                    for i in range(1, len(val) + 1):
                        tree.column(i, width=116, anchor='center')

                    # tree.column(2, width=100)
                    # tree.column(3, width=100)

                    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                    scroll.pack(side='right', fill='y')

                    """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
                    scrollx.pack(side='bottom', fill='x')"""

                    tree.configure(yscrollcommand=scroll.set)

                    iter = 0
                    for valx in datax:
                        print(valx)

                        iter += 1

                        flag = False

                        if ((str(valx[0]) == "")):
                            flag = True

                        if ((str(str(valx[1])) == "")):
                            flag = True

                        if ((str(valx[2]) == "")):
                            flag = True

                        if ((len(str(valx[2])) != 14)):
                            flag = True

                        if ((str(valx[3]) == "")):
                            flag = True

                        if flag == False:
                            tree.insert('', 'end',
                                        values=(str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                        tags=('oddx',))
                        else:
                            tree.insert('', 'end',
                                        values=(str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                        tags=('evenx',))

                    tree.tag_configure('oddx', background='#008001')
                    tree.tag_configure('evenx', background='#FFFF00')



                if ((str(self.txtfld1.get()) != "")):

                    a2 = (str(self.txtfld1.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    validatex=False


                if ((str(self.txtfld2.get()) != "")):

                    b2 = (str(self.txtfld2.get()))


                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    validatex = False


                if ((str(self.txtfld3.get()) != "")):

                    c2 = (str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Missing GSTIN Number Field")


                if ((len(str(self.txtfld3.get())) == 14)):

                    c2 = (str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Wrong GSTIN Number")
                    validatex = False


                if ((str(self.txtfld5.get()) != "")):

                    e2 = (str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    validatex = False


            def delete(self):

                mfx=tk.messagebox.askquestion('Warning',
                                          'Are you sure you want to delete the item with serial no '+str(self.txtfld5.get()),
                                          icon='warning')

                if mfx==True:

                    validatex=False
                else:
                    pass

            def start(self):

                window_user_login_4.destroy()


            def validate(self):

                if ((str(self.txtfld1.get()) != "")):

                    a2 = (str(self.txtfld1.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Date Field")
                    validatex=False
                    return (0)

                if ((str(self.txtfld2.get()) != "")):

                    b2 = (str(self.txtfld2.get()))


                else:

                    messagebox.showwarning("Warning", "Missing Bulk Lot Field")
                    validatex = False
                    return (0)

                if ((str(self.txtfld3.get()) != "")):

                    c2 = (str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Missing GSTIN Number Field")
                    return (0)

                if ((len(str(self.txtfld3.get())) == 14)):

                    c2 = (str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Wrong GSTIN Number")
                    validatex = False
                    return (0)

                if ((str(self.txtfld5.get()) != "")):

                    e2 = (str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Batch Size Field")
                    validatex = False
                    return (0)

                window_user_login_4.destroy()





            def back(self):

                MsgBox = tk.messagebox.askquestion('Warning',
                                                   'All Progress will be lost',
                                                   icon='warning')

                if MsgBox == 'yes':

                    window_user_login_4.destroy()

                    user_login_3(a1=a1, b1=b1, c1=c1, d1=d1, e1=e1, a2=a2, b2=b2,
                                 c2=c2, d2=d2, e2=e2)

                else:
                    pass

            def reset(self):

                # self.txtfld1.delete(0, len(self.txtfld1.get()))
                # self.txtfld1.insert(0, "")

                self.txtfld1.set("")

                self.txtfld2.delete(0, len(self.txtfld2.get()))
                self.txtfld2.insert(0, "")

                self.txtfld3.delete(0, len(self.txtfld3.get()))
                self.txtfld3.insert(0, "")

                self.txtfld5.delete(0, len(self.txtfld5.get()))
                self.txtfld5.insert(0, "")





        window_user_login_4 = tk.Tk()
        window_user_login_4.config(background='#EFEFEF')
        window_user_login_4.attributes('-alpha', 0.97)

        user_login_window = User_4(window_user_login_4)
        window_user_login_4.iconbitmap(
            default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_4.title(
            'Scanning Page ' + '4.0.0')

        window_user_login_4.geometry("600x450")

        if limit!='nil':
            window_user_login_4.after(int(limit), lambda: window_user_login_4.destroy())
        window_user_login_4.mainloop()

        return (validatex)










    user_login_over_ride()











if __name__ == '__main__':
    main()

