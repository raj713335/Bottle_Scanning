import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from threading import Thread
import time
import socket
import subprocess
import calendar



global version
version = "4.0.0"


def user_login_4():
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

            # with open('DATA/Scanning/data.txt', 'r') as fh:
            #     all_lines = fh.readlines()
            #     for each in all_lines:
            #         string = str(each)
            #
            # print(string)
            #
            # date_x = re.findall('17[0-9]{6}', string)
            # try:
            #     date_x = date_x[0]
            # except:
            #     date_x = ''
            # date_x = '20' + date_x[2:4] + '-' + date_x[
            #                                     4:6] + '-' + date_x[
            #                                                  6:8]
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
            #
            # # strings=string.split("")
            # #
            # # for string in strings:
            # #
            # #     print(string)
            # #
            # #     x1=string.find('17')
            # #     if x1!=-1 and date_x=='':
            # #         date_x=string[x1+2:x1+8]
            # #         date_x='20'+date_x[0:2]+'-'+date_x[2:4]+'-'+date_x[:]
            # #
            # #     # x2 = string.find('01')
            # #     # if x2!=-1:
            # #     #     gstin = string[x2 + 2:x2 + 16]
            # #
            # #     x3 = string.find('21')
            # #     if x3!=-1 and serial=='':
            # #         serial = string[x3 + 2:]
            # #
            # #     x4 = string.find('10')
            # #     if x4 != -1 and lot=='':
            # #         lot = string[x4 + 2:]
            # #
            # #     print(date_x,gstin,lot,serial)
            #
            # print(date_x, gstin, lot, serial)
            #
            # def turn_button(x=0):
            #
            #     self.txtfld1.destroy()
            #     self.txtfld1 = DateEntry(window, font=(
            #     "Helvetica", 10),
            #                              state='readonly',
            #                              date_pattern='y-mm-dd',
            #                              anchor='center')
            #     self.txtfld1.place(x=270, y=50, width=260)
            #
            # self.lb1 = tk.Label(window,
            #                     text="EXP(YYYY-MM-DD)",
            #                     font=("Helvetica", 10),
            #                     bg='white')
            # self.lb1.place(x=60, y=50)
            #
            # # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
            # self.txtfld1 = ttk.Combobox(window,
            #                             font=(
            #                             "Helvetica", 10),
            #                             state='readonly')
            # self.txtfld1.place(x=270, y=50, width=260)
            # self.txtfld1.set(date_x)
            #
            # self.txtfld1.bind("<Button-1>", turn_button)
            #
            # self.lb2 = tk.Label(window, text="Bulk Lot",
            #                     font=("Helvetica", 10),
            #                     bg='white')
            # self.lb2.place(x=60, y=100)
            #
            # self.txtfld2 = ttk.Entry(window,
            #                          font=("Helvetica", 10))
            # self.txtfld2.place(x=270, y=100, width=260)
            # self.txtfld2.insert(0, lot)
            #
            # self.lb3 = tk.Label(window, text="GTIN",
            #                     font=("Helvetica", 10),
            #                     bg='white')
            # self.lb3.place(x=60, y=150)
            #
            # self.txtfld3 = ttk.Entry(window,
            #                          text="Enter UID",
            #                          font=("Helvetica", 10))
            # self.txtfld3.place(x=270, y=150, width=260)
            # self.txtfld3.insert(0, gstin)
            #
            # self.lb4 = tk.Label(window,
            #                     text="Total Bottles",
            #                     font=("Helvetica", 10),
            #                     bg='white')
            # self.lb4.place(x=60, y=200)
            #
            # self.txtfld4 = ttk.Entry(window,
            #                          font=("Helvetica", 10))
            # self.txtfld4.place(x=270, y=200, width=260)
            #
            # self.lb5 = tk.Label(window, text="Batch Size",
            #                     font=("Helvetica", 10),
            #                     bg='white')
            # self.lb5.place(x=60, y=250)
            #
            # self.txtfld5 = ttk.Entry(window,
            #                          font=("Helvetica", 10))
            # self.txtfld5.place(x=270, y=250, width=260)
            # self.txtfld5.insert(0, serial)

            self.btn = ttk.Button(window, text="FINISH",
                                  width=20,command=self.validate
                                  )
            self.btn.place(x=60, y=330, width=200,
                           height=50)

            self.btn_quit = ttk.Button(window, text="NEXT",
                                       width=20,
                                       command=self.reset)
            self.btn_quit.place(x=330, y=330, width=200,
                                height=50)

        def validate(self):

            window_user_login_4.destroy()




            # if (str(self.txtfld1.get()) != "") and (
            #         str(self.txtfld2.get()) != "") and (
            #         str(self.txtfld3.get()) != "") \
            #         and (
            #         str(self.txtfld4.get()) != "") and (
            #         str(self.txtfld5.get()) != ""):
            #
            #     if len(str(self.txtfld3.get())) == 14:
            #
            #         window_user_login_4.destroy()
            #
            #         print("Hola")
            #
            #         # IF VALIDATION IS SUCCESFULL THEN IT OPENS USER EDIT WINDOW
            #         pass
            #
            #
            #     else:
            #         messagebox.showwarning("Warning",
            #                                "Missing Values")
            #
            #
            # else:
            #     messagebox.showwarning("Warning",
            #                            "Missing Values")

        def reset(self):

            self.txtfld1.delete(0, len(self.txtfld1.get()))
            self.txtfld1.insert(0, "")

            self.txtfld2.delete(0, len(self.txtfld2.get()))
            self.txtfld2.insert(0, "")

            self.txtfld3.delete(0, len(self.txtfld3.get()))
            self.txtfld3.insert(0, "")

            self.txtfld4.delete(0, len(self.txtfld4.get()))
            self.txtfld4.insert(0, "")

            self.txtfld5.delete(0, len(self.txtfld5.get()))
            self.txtfld5.insert(0, "")

    window_user_login_4 = tk.Tk()
    window_user_login_4.config(background='#EFEFEF')
    window_user_login_4.attributes('-alpha', 0.9)

    user_login_window = User_4(window_user_login_4)
    window_user_login_4.iconbitmap(
        default='DATA/IMAGES/icons/favicon.ico')
    window_user_login_4.title(
        'Scanning Page ' + version)
    window_user_login_4.geometry("600x450")
    window_user_login_4.mainloop()