import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox,Frame
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from threading import Thread
import time
import socket
import subprocess
import calendar



global version
version = "4.0.0"


def user_login_4(a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0), c2=str(0), d2=str(0),
                 e2=str(0)):
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

            stringx=[]

            with open('DATA/Scanning/scanning.txt', 'r') as fh:
                all_lines = fh.readlines()
                for each in all_lines:
                    stringx.append(each.replace('\n',''))

            print(stringx)

            i=0


            datax=[]



            for string in stringx:

                i+=1

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


                datax.append([date_x,lot,gstin,serial])




            def selectItem(a):
                curItem = tree.focus()

                # print(tree.item(curItem)['values'])
                quantifiers = (tree.item(curItem)['values'])

                self.txtfld1.set("")
                self.txtfld2.delete(0, 'end')
                self.txtfld3.delete(0, 'end')
                self.txtfld5.delete(0,'end')


                self.txtfld1.set(str(quantifiers[1]))
                self.txtfld2.insert(0, str(quantifiers[2]))
                self.txtfld3.insert(0, str('0000'+str(quantifiers[3]))[-14:])
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

            def turn_button(x=0):
                self.txtfld1.destroy()
                self.txtfld1 = DateEntry(window, font=(
                "Helvetica", 10),
                                         state='readonly',
                                         date_pattern='y-mm-dd',
                                         anchor='center')
                self.txtfld1.place(x=270, y=150, width=260)

            self.lb1 = tk.Label(window,
                                text="EXP(YYYY-MM-DD)",
                                font=("Helvetica", 10),
                                bg='#EFEFEF')
            self.lb1.place(x=60, y=150)

            # self.txtfld1 = DateEntry(window,font=("Helvetica", 10),state='readonly',date_pattern='y-mm-dd',anchor='center')
            self.txtfld1 = ttk.Combobox(window,
                                        font=("Helvetica", 10), state='readonly')
            self.txtfld1.place(x=270, y=150, width=260)


            self.txtfld1.bind("<Button-1>", turn_button)

            self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
            self.lb2.place(x=60, y=190)

            self.txtfld2 = ttk.Entry(window,
                                     font=("Helvetica", 10))
            self.txtfld2.place(x=270, y=190, width=260)


            self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
            self.lb3.place(x=60, y=230)

            self.txtfld3 = ttk.Entry(window, text="Enter UID", font=("Helvetica", 10))
            self.txtfld3.place(x=270, y=230, width=260)


            self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
            # self.lb5.place(x=60, y=330)

            self.txtfld5 = ttk.Entry(window,
                                     font=("Helvetica", 10))
            # self.txtfld5.place(x=270, y=330, width=260)



            self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
            self.btn_back.place(x=10, y=290, width=130, height=40)

            self.btn_quit = ttk.Button(window, text="RESET", width=20, command=self.reset)
            self.btn_quit.place(x=160, y=290, width=130, height=40)

            self.btn_update = ttk.Button(window, text="UPDATE", width=20, command=self.validate)
            self.btn_update.place(x=310, y=290, width=130, height=40)

            self.btn_finish = ttk.Button(window, text="FINISH", width=20, command=self.validate)
            self.btn_finish.place(x=460, y=290, width=130, height=40)



            frame = Frame(window_user_login_4)
            frame.place(x=-1, y=344)

            # print(data)



            tree = ttk.Treeview(frame,
                                columns=(1, 2, 3, 4,5),
                                height=4, show="headings")
            tree.pack(side='left')
            tree.bind('<ButtonRelease-1>', selectItem)



            val = ["Sl No","Exp Date", "Bulk Lot", "GTIN", "Serial",]

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

            iter=0
            for valx in datax:
                print(valx)


                iter+=1



                flag=False


                if ((str(valx[0]) == "")):

                    flag=True


                if ((str(str(valx[1])) == "")):

                    flag=True



                if ((str(valx[2]) == "")):

                    flag=True


                if ((len(str(valx[2])) != 14)):

                    flag=True





                if ((str(valx[3]) == "")):

                    flag=True



                if flag == False:
                    tree.insert('', 'end', values=(str(iter),str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                tags=('oddx',))
                else:
                    tree.insert('', 'end', values=(str(iter),str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                tags=('evenx',))








            tree.tag_configure('oddx', background='#008001')
            tree.tag_configure('evenx', background='#FFFF00')





        def validate(self):



            if ((str(self.txtfld1.get()) != "")):

                a2 = (str(self.txtfld1.get()))

            else:

                messagebox.showwarning("Warning", "Missing Date Field")
                return (0)

            if ((str(self.txtfld2.get()) != "")):

                b2 = (str(self.txtfld2.get()))

            else:

                messagebox.showwarning("Warning", "Missing Bulk Lot Field")
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
                return (0)

            if ((str(self.txtfld5.get()) != "")):

                e2 = (str(self.txtfld5.get()))

            else:

                messagebox.showwarning("Warning", "Missing Batch Size Field")
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
    window_user_login_4.mainloop()



user_login_4()