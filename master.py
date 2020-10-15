import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox,Frame
from tkcalendar import  DateEntry
from PIL import Image, ImageTk
import cv2
import sys

# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
# from time import sleep     # Import the sleep function from the time module
#
#
# GPIO.setwarnings(False)    # Ignore warning for now
# GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)


# from gpiozero import LED
# led = LED(21)



already_scanned_data=[]
scanned_serial=[]

'''
REQUIREMENTS

'''


class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()



def main():



    def user_login_over_ride():

        for i in range(len(already_scanned_data)):
            already_scanned_data.pop()

        for i in range(len(scanned_serial)):
            scanned_serial.pop()

        class User_Login():



            def __init__(self, window):

                self.UID = []
                self.PWD = []



                with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        x, y = list(map(str, each.split(",")))
                        x = str(x).replace("\n", "")
                        y = str(y).replace("\n", "")
                        self.UID.append(x)
                        self.PWD.append(y)



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




                else:
                    messagebox.showerror("Error", "INVALID CREDENTIALS")

            def quit(self):
                window_user_login.destroy()
                exit(0)

        window_user_login = tk.Tk()
        # window_user_login.config(background='#EFEFEF')
        # window_user_login.attributes('-alpha', 0.97)

        user_login_window = User_Login(window_user_login)
        #window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login.title('Admin Login ' + '1')
        window_user_login.geometry("600x450")
        def exitx():
            exit(0)
        window_user_login.protocol('WM_DELETE_WINDOW', exitx)
        window_user_login.mainloop()




    def user_login_2(a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0),user_name=str(0)):
        class User_2():





            def __init__(self, window):

                self.windows=window

                with open('DATA/Scanning/data.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        string = str(each)

                if a1 == str(0):
                    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
                    string = string.replace(date_x[0], "")
                    try:
                        date_x = date_x[0]
                    except:
                        date_x = ''
                    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
                else:
                    date_x = a1

                if c1 == str(0):
                    gstin = re.findall('01[0-9]{14}', string)
                    string = string.replace(gstin[0], '')
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''
                else:
                    gstin = c1

                if b1 == str(0):
                    lot = re.findall('10[A-Za-z]{2}[0-9]*', string)
                    string = string.replace(lot[0], '')
                    try:
                        lot = str(lot[0]).replace('', "")
                        lot = lot.replace('10', '')
                    except:
                        lot = ''
                else:
                    lot = b1

                if d1 == str(0):
                    total = ""
                else:
                    total = d1

                if e1 == str(0):
                    serial = re.findall(r'21[0-9]*', string)
                    try:
                        serial = serial[0][2:-1]
                    except:
                        serial = ''
                else:
                    serial = e1


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


                self.lb5 = tk.Label(window, text="Serial Number", font=("Helvetica", 10), bg='#EFEFEF')
                self.txtfld5 = ttk.Entry(window,font=("Helvetica", 10))
                self.txtfld5.insert(0, serial)


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

                    messagebox.showwarning("Warning", "Missing Serial Number Field")
                    return (0)


                if ((str(self.txtfld4.get()) != "") ):

                    e1=(str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Missing Total Bottles Field")
                    return (0)


                if ((str(self.txtfld2.get()).isalnum())):

                    b1=(str(self.txtfld2.get()))

                else:

                    messagebox.showwarning("Warning", "Bulk Lot must be aplhanumeric and should not contain any special characters")
                    return (0)


                if ((str(self.txtfld3.get()).isalnum())):

                    c1=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "GTIN must be aplhanumeric and should not contain any special characters")
                    return (0)



                if ((str(self.txtfld5.get()).isalnum())):

                    e1=(str(self.txtfld5.get()))

                else:

                    messagebox.showwarning("Warning", "Serial Number must be aplhanumeric and should not contain any special characters")
                    return (0)


                if ((str(self.txtfld4.get()) != "0")):

                    d1=(str(self.txtfld4.get()))

                else:

                    messagebox.showwarning("Warning", "Total Bottle value cannot be 0")
                    return (0)






                try:

                    temp=int((self.txtfld4.get()))

                    d1=str(self.txtfld4.get())


                except:
                    messagebox.showwarning("Warning", "Total Bottle field must be numeric")
                    return (0)



                window_user_login_2.destroy()





                user_login_3(user_name=user_name,a1=a1, b1=b1, c1=c1,
                             d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                             e2=e2)




            def reset(self):

                def turn_button(x=0):

                    self.txtfld1.destroy()
                    self.txtfld1 = DateEntry(self.windows, font=("Helvetica", 10), state='readonly',
                                             date_pattern='y-mm-dd', anchor='center')
                    self.txtfld1.place(x=270, y=160, width=260)


                self.txtfld1.destroy()
                self.txtfld1 = ttk.Combobox(self.windows,font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=160, width=260)
                self.txtfld1.set("")
                self.txtfld1.bind("<Button-1>", turn_button)


                self.txtfld2.delete(0, len(self.txtfld2.get()))
                self.txtfld2.insert(0, "")

                self.txtfld3.delete(0, len(self.txtfld3.get()))
                self.txtfld3.insert(0, "")

                self.txtfld4.delete(0, len(self.txtfld4.get()))
                self.txtfld4.insert(0, "")

                self.txtfld5.delete(0, len(self.txtfld5.get()))
                self.txtfld5.insert(0, "")






        window_user_login_2 = tk.Tk()
        # window_user_login_2.config(background='#EFEFEF')
        # window_user_login_2.attributes('-alpha', 0.97)

        user_login_window = User_2(window_user_login_2)
        # window_user_login_2.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_2.title('Get Bulk Data ' + '2')
        window_user_login_2.geometry("600x450")
        def exitx():
            exit(0)
        window_user_login_2.protocol('WM_DELETE_WINDOW', exitx)
        window_user_login_2.mainloop()















    def user_login_3(user_name=str(0),a1=str(0),b1=str(0),c1=str(0),d1=str(0),e1=str(0),a2=str(0),b2=str(0),c2=str(0),d2=str(0),e2=str(0)):




        class User_3():

            def __init__(self, window):

                self.windows=window

                with open('DATA/Scanning/data.txt', 'r') as fh:
                    all_lines = fh.readlines()
                    for each in all_lines:
                        string = str(each)

                if a2 == str(0):
                    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
                    string = string.replace(date_x[0], "")
                    try:
                        date_x = date_x[0]
                    except:
                        date_x = ''
                    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
                else:
                    date_x = a2

                if c2 == str(0):
                    gstin = re.findall('01[0-9]{14}', string)
                    string = string.replace(gstin[0], '')
                    try:
                        gstin = gstin[0][2:]
                    except:
                        gstin = ''
                else:
                    gstin = c2

                if b2 == str(0):
                    lot = re.findall('10[A-Za-z]{2}[0-9]*', string)
                    string = string.replace(lot[0], '')
                    try:
                        lot = str(lot[0]).replace('', "")
                        lot = lot.replace('10', '')
                    except:
                        lot = ''
                else:
                    lot = b2

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


                self.txtfld4 = ttk.Entry(window,
                                         font=("Helvetica", 10))
                self.txtfld4.insert(0, d1)

                self.lb5 = tk.Label(window, text="Serial Number", font=("Helvetica", 10), bg='#EFEFEF')
                self.txtfld5 = ttk.Entry(window,
                                         font=("Helvetica", 10))
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


                if ((len(str(self.txtfld3.get())) == 14)):

                    c2=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "Wrong GSTIN Number Format")
                    return (0)




                if ((str(self.txtfld2.get()).isalnum())):

                    b2=(str(self.txtfld2.get()))

                else:

                    messagebox.showwarning("Warning", "Bulk Lot must be aplhanumeric and should not contain any special characters")
                    return (0)


                if ((str(self.txtfld3.get()).isalnum())):

                    c2=(str(self.txtfld3.get()))

                else:

                    messagebox.showwarning("Warning", "GTIN must be aplhanumeric and should not contain any special characters")
                    return (0)




                window_user_login_3.destroy()


                quiter(user_name=user_name,a1=a1, b1=b1, c1=c1,
                             d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                             e2=e2)


            def reset(self):

                def turn_button(x=0):

                    self.txtfld1.destroy()
                    self.txtfld1 = DateEntry(self.windows, font=("Helvetica", 10), state='readonly',
                                             date_pattern='y-mm-dd', anchor='center')
                    self.txtfld1.place(x=270, y=160, width=260)


                self.txtfld1.destroy()
                self.txtfld1 = ttk.Combobox(self.windows,font=("Helvetica", 10), state='readonly')
                self.txtfld1.place(x=270, y=160, width=260)
                self.txtfld1.set("")
                self.txtfld1.bind("<Button-1>", turn_button)


                self.txtfld2.delete(0, len(self.txtfld2.get()))
                self.txtfld2.insert(0, "")

                self.txtfld3.delete(0, len(self.txtfld3.get()))
                self.txtfld3.insert(0, "")




        window_user_login_3 = tk.Tk()
        # window_user_login_3.config(background='#EFEFEF')
        # window_user_login_3.attributes('-alpha', 0.97)

        user_login_window = User_3(window_user_login_3)
        #window_user_login_3.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_3.title('Get Repacking Data ' + '3.0.0')
        window_user_login_3.geometry("600x450")
        def exitx():
            exit(0)
        window_user_login_3.protocol('WM_DELETE_WINDOW', exitx)
        window_user_login_3.mainloop()




    def quiter(user_name=str(0),a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0), c2=str(0), d2=str(0),
                     e2=str(0),limit=str(0)):







        xml_data=[]

        stringx = []





        with open('DATA/Scanning/scanning.txt', 'r') as fh:
            all_lines = fh.readlines()
            for each in all_lines:
                stringx.append(each.replace('\n', ''))

        i = 0


        scanned_data = []

        for string in stringx:

            i += 1

            date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
            string = string.replace(date_x[0], "")
            try:
                date_x = date_x[0]
            except:
                date_x = ''
            date_x = '20' + date_x[2:4] + '-' + date_x[
                                                4:6] + '-' + date_x[
                                                             6:8]


            gstin = re.findall('01[0-9]{14}', string)
            string = string.replace(gstin[0], '')
            try:
                gstin = gstin[0][2:]
            except:
                gstin = ''

            lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
            string = string.replace(lot[0], '')
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

            scanned_data.append([date_x, gstin, lot, serial])












        if len(scanned_data)>len(already_scanned_data):
            value = False



            value = user_login_4(user_name=user_name, a1=a1, b1=b1, c1=c1,
                             d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                             e2=e2, id='NIL', limit='nil', scanned_data=str(0))



            if value == False:
                user_login_over_ride()

        else:
            user_login_4(user_name=user_name, a1=a1, b1=b1, c1=c1,
                         d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                         e2=e2, id='NIL', limit='end', scanned_data=scanned_data)




        user_login_4(user_name=user_name, a1=a1, b1=b1, c1=c1,
                     d1=d1, e1=e1, a2=a2, b2=b2, c2=c2, d2=d2,
                     e2=e2, id='NIL', limit='start', scanned_data=scanned_data)






    def user_login_4(user_name=str(0), a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0),
                     c2=str(0), d2=str(0),
                     e2=str(0), id=str(0), limit=str(0),scanned_data=str(0)):
        class User_4():

            def __init__(self, window):

                print(limit)



                stringx = already_scanned_data

                self.stringc = stringx
                self.windows = window

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

                self.txtfld00 = ttk.Combobox(window, font=("Helvetica", 20), justify='center')
                self.txtfld00.place(x=450, y=50, width=70)
                key_total_bottle=0

                for each in already_scanned_data:
                    #print(each)
                    if each!=False:
                        key_total_bottle+=1
                self.txtfld00.set(str(key_total_bottle))
                self.txtfld00.config(state='disabled')


                self.txtfld01 = ttk.Combobox(window, font=("Helvetica", 20), justify='center')
                self.txtfld01.place(x=525, y=50, width=70)
                self.txtfld01.set(d1)
                self.txtfld01.config(state='disabled')

                self.lb1 = tk.Label(window,
                                    text="EXP(YYYY-MM-DD)",
                                    font=("Helvetica", 10),
                                    bg='#EFEFEF')
                self.lb1.place(x=60, y=170)

                self.txtfld1 = ttk.Combobox(window,
                                            font=("Helvetica", 10))
                self.txtfld1.place(x=270, y=170, width=260)
                self.txtfld1.set(a1)
                self.txtfld1.config(state='disabled')

                self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2.place(x=60, y=210)

                self.txtfld2 = ttk.Combobox(window,
                                            font=("Helvetica", 10))
                self.txtfld2.place(x=270, y=210, width=260)
                self.txtfld2.set(b1)
                self.txtfld2.config(state='disabled')

                self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3.place(x=60, y=250)

                self.txtfld3 = ttk.Combobox(window, text="Enter UID", font=("Helvetica", 10))
                self.txtfld3.place(x=270, y=250, width=260)
                self.txtfld3.set(c1)
                self.txtfld3.config(state='disabled')

                self.lb5 = tk.Label(window, text="Serial Number", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb5.place(x=60, y=290)

                self.txtfld5 = ttk.Combobox(window,
                                            font=("Helvetica", 10))
                self.txtfld5.place(x=270, y=290, width=260)
                self.txtfld5.set(e1)
                self.txtfld5.config(state='disabled')

                self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                self.btn_back.place(x=10, y=400, width=180, height=40)

                self.btn_next = ttk.Button(window, text="NEXT", width=20)
                # self.btn_next.place(x=400, y=400, width=180, height=40)

                self.btn_quit = ttk.Button(window, text="DISPLAY", width=20, command=self.display)
                self.btn_quit.place(x=205, y=400, width=180, height=40)

                # print(already_scanned_data)
                # print(scanned_data)
                # print(len(already_scanned_data),len(scanned_data))
                #
                # if len(already_scanned_data)>len(scanned_data):
                #     self.btn_quit = ttk.Button(window, text="DISPLAY", width=20, command=self.display)
                #     self.btn_quit.place(x=205, y=400, width=180, height=40)
                #
                #     self.btn_back.place(x=3000, y=3000)
                #
                #     self.mannual_entry = ttk.Button(window, text="ADD NEW DATA", width=20,
                #                                     command=self.mannual_entry)
                #     self.mannual_entry.place(x=10, y=400, width=180, height=40)





                def task():


                    try:
                        if already_scanned_data[-1]==False:
                            flagx=True      #Earlier it was False
                        else:
                            flagx=True
                    except:
                        flagx=True





                    if flagx==True:
                        iterx = len(already_scanned_data)
                    else:
                        iterx = len(already_scanned_data)-1

                    if iterx>=len(scanned_data):
                        iterx=len(scanned_data)-1


                    date_xx = scanned_data[iterx][0]
                    lot_x = scanned_data[iterx][2]
                    gstin_x = scanned_data[iterx][1]
                    serial_x = scanned_data[iterx][3]





                    if flagx==True:

                        try:
                            if len(already_scanned_data)<len(scanned_data):
                                key_total_bottle = 0

                                for each in already_scanned_data:
                                    # print(each)
                                    if each != False:
                                        key_total_bottle += 1
                                self.txtfld00.set(str(key_total_bottle+1))
                        except:
                            return (0)
                        try:
                            self.txtfld1.set(date_xx)
                            self.txtfld2.set(lot_x)
                            self.txtfld3.set(gstin_x)
                            self.txtfld5.set(serial_x)
                        except:
                            pass

                        try:
                            self.btn_next.destroy()
                        except:
                            pass

                    else:
                        self.btn_next.destroy()
                        already_scanned_data.pop()
                        # try:
                        #     scanned_serial.pop()
                        # except:
                        #     pass

                    # GPIO.output(17, GPIO.LOW)

                    #led.off()





                    def validatex():

                        flag=True

                        #led.off()


                        if (str(self.txtfld5.get()) not in scanned_serial) or (len(scanned_data)==len(already_scanned_data)):

                            e3 = (str(self.txtfld5.get()))
                            self.txtfld5.config(state='disabled')


                        else:

                            #led.on()

                            #GPIO.output(17, GPIO.HIGH)  # Turn on

                            messagebox.showerror("Error", "Serial Number " + str(self.txtfld5.get()) +
                                                 " is duplicated. Please remove the duplicate bottle and restart the scanning" )


                            #sleep(1)  # Sleep for 1 second
                            #GPIO.output(17, GPIO.LOW)

                            #self.txtfld5.config(state='enabled')
                            already_scanned_data.append(False)
                            if len(already_scanned_data)<len(scanned_data):
                                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=task)
                                self.btn_next.place(x=400, y=400, width=180, height=40)


                            return (0)


                        if ((str(self.txtfld1.get()) == str(a1))):

                            a3 = (str(self.txtfld1.get()))
                            self.txtfld1.config(state='disabled')


                        else:

                            #led.on()

                            #GPIO.output(17, GPIO.HIGH)  # Turn on

                            messagebox.showerror("Error", "Date " + str(self.txtfld1.get()) +
                                                 " in serial number " + str(self.txtfld5.get()) +
                                                 " do not match with Bulk Date " + str(a1) +
                                                 " , Please change Date .")


                            #sleep(1)  # Sleep for 1 second
                            #GPIO.output(17, GPIO.LOW)

                            # window_user_login_4.destroy()
                            # user_login_over_ride()

                            #self.txtfld1.config(state='enabled')
                            # self.txtfld1.set('')
                            #self.txtfld1.set(str(self.txtfld1.get()))

                            #self.txtfld1.config(state='enabled')
                            self.txtfld1.bind('<Double-Button>')
                            already_scanned_data.append(False)
                            if len(already_scanned_data) < len(scanned_data):
                                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=task)
                                self.btn_next.place(x=400, y=400, width=180, height=40)
                            return (0)





                        if ((str(self.txtfld2.get()) == str(b1))):

                            b3 = (str(self.txtfld2.get()))
                            self.txtfld2.config(state='disabled')



                        else:

                            messagebox.showerror("Error", "Bulk Lot " + str(self.txtfld2.get()) +
                                                 " in serial number " + str(self.txtfld5.get()) +
                                                 " do not match with Bulk Lot " + str(b1) +
                                                 " , Please change Lot Number")

                            #self.txtfld2.config(state='enabled')
                            already_scanned_data.append(False)
                            if len(already_scanned_data) < len(scanned_data):
                                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=task)
                                self.btn_next.place(x=400, y=400, width=180, height=40)
                            return (0)

                        if ((str(self.txtfld3.get()) == str(c1))):

                            c3 = (str(self.txtfld3.get()))
                            self.txtfld3.config(state='disabled')

                        else:

                            #led.on()

                            #GPIO.output(17, GPIO.HIGH)  # Turn on

                            messagebox.showerror("Error", "GTIN " + str(self.txtfld3.get()) +
                                                 " in serial number " + str(self.txtfld5.get()) +
                                                 " do not match with Bulk Data GTIN " + str(c1) +
                                                 " , Please change GTIN Number")


                            #sleep(1)  # Sleep for 1 second
                            #GPIO.output(17, GPIO.LOW)

                            #self.txtfld3.config(state='enabled')
                            already_scanned_data.append(False)
                            if len(already_scanned_data) < len(scanned_data):
                                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=task)
                                self.btn_next.place(x=400, y=400, width=180, height=40)
                            return (0)

                        if ((str(self.txtfld5.get()).isalnum())):

                            e3 = (str(self.txtfld5.get()))
                            self.txtfld5.config(state='disabled')

                        else:

                            #led.on()

                            #GPIO.output(17, GPIO.HIGH)  # Turn on

                            messagebox.showwarning("Warning",
                                                   "Batch Number Number must be aplhanumeric and should not contain any special characters. Please change Batch Number")



                            #sleep(1)  # Sleep for 1 second
                            #GPIO.output(17, GPIO.LOW)

                            # self.txtfld5.config(state='enabled')
                            already_scanned_data.append(False)
                            if len(already_scanned_data) < len(scanned_data):
                                self.btn_next = ttk.Button(window, text="NEXT", width=20, command=task)
                                self.btn_next.place(x=400, y=400, width=180, height=40)
                            return (0)

                        if ((str(self.txtfld5.get()) != "")):

                            e3 = (str(self.txtfld5.get()))

                        else:

                            messagebox.showwarning("Warning", "Missing Serial Number Field")
                            window_user_login_4.destroy()
                            user_login_over_ride()

                        if flag==True:

                            if len(already_scanned_data)<len(scanned_data):
                                already_scanned_data.append([a3, b3, c3, e3])
                                scanned_serial.append(e3)

                            if len(already_scanned_data) < (len(scanned_data)):
                                window_user_login_4.after(2000, task)

                            else:
                                self.btn_quit = ttk.Button(window, text="DISPLAY", width=20, command=self.display)
                                self.btn_quit.place(x=205, y=400, width=180, height=40)

                                self.btn_back.place(x=3000,y=3000)

                                self.mannual_entry = ttk.Button(window, text="ADD NEW DATA", width=20, command=self.mannual_entry)
                                self.mannual_entry.place(x=10, y=400, width=180, height=40)

                                # self.btn_save = ttk.Button(self.windows, text="FINISH", width=20, command=finish)
                                # self.btn_save.place(x=400, y=400, width=180, height=40)




                                # self.btn_back.destroy()

                                def selectItem(a):
                                    curItem = tree.focus()

                                    quantifiers = (tree.item(curItem)['values'])

                                    self.txtfld1.set(str(quantifiers[1]))
                                    self.txtfld2.set(str(quantifiers[2]))
                                    self.txtfld3.set(str('0000' + str(quantifiers[3]))[-14:])
                                    self.txtfld5.set(str(quantifiers[4]))

                                frame = Frame(window_user_login_4)

                                tree = ttk.Treeview(frame,
                                                    columns=(1, 2, 3, 4, 5),
                                                    height=4, show="headings")
                                tree.pack(side='left')
                                tree.bind('<ButtonRelease-1>', selectItem)

                                val = ["Sl No", "Exp Date", "Bulk Lot", "GTIN", "Serial", ]

                                for i in range(1, len(val) + 1):
                                    tree.heading(i, text=val[i - 1])

                                for i in range(1, len(val) + 1):
                                    tree.column(i, width=116, anchor='center')

                                scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                                scroll.pack(side='right', fill='y')

                                tree.configure(yscrollcommand=scroll.set)

                                iter = 0
                                for valx in already_scanned_data:



                                    flag = False

                                    try:

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
                                            iter += 1

                                            tree.insert('', 'end',
                                                        values=(
                                                            str(iter), str(valx[0]), str(valx[1]), str(valx[2]),
                                                            str(valx[3])),
                                                        tags=('oddx',))
                                        else:
                                            tree.insert('', 'end',
                                                        values=(
                                                            str(iter), str(valx[0]), str(valx[1]), str(valx[2]),
                                                            str(valx[3])),
                                                        tags=('evenx',))

                                    except:
                                        pass

                                def finish():

                                    if str(self.txtfld01.get()) != str(len(tree.get_children())):
                                        glmb = tk.messagebox.askquestion('Warning',
                                                                         'Total Bottle Scanned: ' + str(
                                                                             len(tree.get_children()))
                                                                         + ' \nTotal Bottles Entered: ' + str(
                                                                             d1)
                                                                         + '\nTotal Bottles are not matching \nPlease Change the Total Bottles'
                                                                         ,
                                                                         icon='warning')
                                        if glmb=='no':
                                            return(0)


                                        if glmb == 'yes':

                                            glm = tk.messagebox.askquestion('Warning',
                                                                            'Are you sure you save the data to xml file ?',
                                                                            icon='warning')


                                            if glm == 'yes':

                                                try:
                                                    root.destroy()
                                                except:
                                                    pass

                                                def printtext():
                                                    updates_total_bottle = txtfld19.get()
                                                    root.destroy()
                                                    if str(updates_total_bottle) != str(len(tree.get_children())):
                                                        tk.messagebox.showerror('error',
                                                                                'Total Bottle Scanned ' + str(
                                                                                    len(tree.get_children()))
                                                                                + ' do not match with the Total Bottle in Bulk Data ' + str(
                                                                                    updates_total_bottle),
                                                                                icon='error')

                                                        return (0)
                                                    else:
                                                        def user_login_over_ride1():
                                                            class User_Login():

                                                                def __init__(self, window):

                                                                    self.UID = []
                                                                    self.PWD = []

                                                                    with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                                                        all_lines = fh.readlines()
                                                                        for each in all_lines:
                                                                            x, y = list(map(str, each.split(",")))

                                                                            x = str(x).replace("\n", "")
                                                                            y = str(y).replace("\n", "")
                                                                            self.UID.append(x)
                                                                            self.PWD.append(y)

                                                                    self.lbl = tk.Label(window, text="User",
                                                                                        font=("Helvetica", 20),
                                                                                        bg='#EFEFEF')
                                                                    # self.lbl.place(x=60, y=90)

                                                                    self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                                                             font=("Helvetica", 20))
                                                                    # self.txtfld1.place(x=220, y=90)
                                                                    self.txtfld1.insert(0, user_name)

                                                                    self.lb2 = tk.Label(window, text="Password",
                                                                                        font=("Helvetica", 20),
                                                                                        bg='#EFEFEF')
                                                                    self.lb2.place(x=60, y=90)

                                                                    self.txtfld2 = ttk.Entry(window,
                                                                                             text="Enter Password",
                                                                                             show="*",
                                                                                             font=("Helvetica", 20))
                                                                    self.txtfld2.place(x=220, y=90)

                                                                    self.btn = ttk.Button(window, text="SAVE", width=20,
                                                                                          command=self.validate)
                                                                    self.btn.place(x=60, y=220, width=200, height=50)

                                                                    self.btn_quit = ttk.Button(window, text="QUIT",
                                                                                               width=20,
                                                                                               command=self.quit)
                                                                    self.btn_quit.place(x=330, y=220, width=200,
                                                                                        height=50)

                                                                def validate(self):
                                                                    if (str(self.txtfld1.get()) in self.UID) and (
                                                                            str(self.txtfld2.get()) in self.PWD):

                                                                        user_id = str(self.txtfld1.get())

                                                                        window_user_login.destroy()

                                                                        data_xml = []
                                                                        xx = tree.get_children()

                                                                        for each in xx:
                                                                            vc = tree.item(each)['values']
                                                                            strx = '01' + (
                                                                                str('0000' + str(c1))[
                                                                                -14:]) + '21' + str(
                                                                                vc[4]) + '17' + str(a1[2:]).replace('-',
                                                                                                                    '') + '10' + b1
                                                                            data_xml.append(strx)

                                                                        def xml_creator():

                                                                            from datetime import datetime
                                                                            from xml.dom import minidom
                                                                            from xml.dom.minidom import \
                                                                                getDOMImplementation

                                                                            root = minidom.Document()
                                                                            root.standalone = 'No'

                                                                            iso_date = datetime.now().astimezone().isoformat()
                                                                            offset = iso_date[-6:]
                                                                            expire_date = a1
                                                                            bulk_lot_number = b1
                                                                            repackage_lot_number = b2
                                                                            strings = data_xml

                                                                            list_data = ''

                                                                            for each in strings:
                                                                                list_data += str(
                                                                                    '<epcis:epc>') + each + str(
                                                                                    '</epcis:epc>')

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
                                                  F                          <epcis:id>urn:epc:id:sgln:08662190003.0.0</epcis:id>
                                                                            </epcis:bizLocation>
                                                                            <epcis:extension><!--@Verify By ''' + str(
                                                                                user_id) + f'''-->
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

                                                                            xml_str = dom.toprettyxml(indent="  ",
                                                                                                      newl='',
                                                                                                      encoding='UTF-8')
                                                                            timestamp = int(datetime.now().timestamp())
                                                                            save_path_file = f"{b1}-{b2}-{timestamp}.xml"

                                                                            with open(save_path_file, "w") as f:
                                                                                f.write(xml_str.decode())

                                                                        xml_creator()
                                                                        messagebox.showwarning("Info",
                                                                                               "XML file Created Succesfully")
                                                                        for i in range(len(already_scanned_data)):
                                                                            already_scanned_data.pop()

                                                                        for i in range(len(scanned_serial)):
                                                                            scanned_serial.pop()


                                                                        window_user_login_4.destroy()
                                                                        user_login_over_ride()



                                                                    else:

                                                                        messagebox.showerror("Error",
                                                                                             "INVALID CREDENTIALS")

                                                                def quit(self):
                                                                    window_user_login.destroy()

                                                            window_user_login = tk.Tk()
                                                            # window_user_login.config(background='#EFEFEF')
                                                            # window_user_login.attributes('-alpha', 0.97)

                                                            user_login_window = User_Login(window_user_login)
                                                            # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                                                            window_user_login.title('Admin Login ')
                                                            window_user_login.geometry("600x350")
                                                            window_user_login.mainloop()

                                                        user_login_over_ride1()

                                                root = tk.Tk()

                                                root.title('Enter Total Bottle')

                                                lbl = tk.Label(root, text="Total Bottle", font=("Helvetica", 20),
                                                               bg='#EFEFEF')
                                                lbl.place(x=60, y=30)

                                                txtfld19 = tk.Entry(root, text="Total Bottle", font=("Helvetica", 20))
                                                txtfld19.place(x=220, y=30)

                                                b = ttk.Button(root, text='UPDATE', command=printtext)
                                                b.place(x=380, y=90, height=40, width=145)
                                                root.geometry("600x150")
                                                root.mainloop()





                                            else:
                                                return (0)

                                        else:
                                            def user_login_over_ride1():
                                                class User_Login():

                                                    def __init__(self, window):

                                                        self.UID = []
                                                        self.PWD = []

                                                        with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                                            all_lines = fh.readlines()
                                                            for each in all_lines:
                                                                x, y = list(map(str, each.split(",")))

                                                                x = str(x).replace("\n", "")
                                                                y = str(y).replace("\n", "")
                                                                self.UID.append(x)
                                                                self.PWD.append(y)

                                                        self.lbl = tk.Label(window, text="User", font=("Helvetica", 20),
                                                                            bg='#EFEFEF')
                                                        # self.lbl.place(x=60, y=90)

                                                        self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                                                 font=("Helvetica", 20))
                                                        # self.txtfld1.place(x=220, y=90)
                                                        self.txtfld1.insert(0, user_name)

                                                        self.lb2 = tk.Label(window, text="Password",
                                                                            font=("Helvetica", 20),
                                                                            bg='#EFEFEF')
                                                        self.lb2.place(x=60, y=90)

                                                        self.txtfld2 = ttk.Entry(window, text="Enter Password",
                                                                                 show="*",
                                                                                 font=("Helvetica", 20))
                                                        self.txtfld2.place(x=220, y=90)

                                                        self.btn = ttk.Button(window, text="SAVE", width=20,
                                                                              command=self.validate)
                                                        self.btn.place(x=60, y=220, width=200, height=50)

                                                        self.btn_quit = ttk.Button(window, text="QUIT", width=20,
                                                                                   command=self.quit)
                                                        self.btn_quit.place(x=330, y=220, width=200, height=50)

                                                    def validate(self):
                                                        if (str(self.txtfld1.get()) in self.UID) and (
                                                                str(self.txtfld2.get()) in self.PWD):

                                                            user_id = str(self.txtfld1.get())

                                                            window_user_login.destroy()

                                                            data_xml = []
                                                            xx = tree.get_children()

                                                            for each in xx:
                                                                vc = tree.item(each)['values']
                                                                strx = '01' + (
                                                                str('0000' + str(c1))[-14:]) + '21' + str(
                                                                    vc[4]) + '17' + str(a1[2:]).replace('-',
                                                                                                        '') + '10' + b1
                                                                data_xml.append(strx)

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
                                                                strings = data_xml

                                                                list_data = ''

                                                                for each in strings:
                                                                    list_data += str('<epcis:epc>') + each + str(
                                                                        '</epcis:epc>')

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
                                                                <epcis:extension><!--@Verify By ''' + str(
                                                                    user_id) + f'''-->
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

                                                                xml_str = dom.toprettyxml(indent="  ", newl='',
                                                                                          encoding='UTF-8')
                                                                timestamp = int(datetime.now().timestamp())
                                                                save_path_file = f"{b1}-{b2}-{timestamp}.xml"

                                                                with open(save_path_file, "w") as f:
                                                                    f.write(xml_str.decode())

                                                            xml_creator()
                                                            messagebox.showwarning("Info",
                                                                                   "XML file Created Succesfully")
                                                            for i in range(len(already_scanned_data)):
                                                                already_scanned_data.pop()

                                                            for i in range(len(scanned_serial)):
                                                                scanned_serial.pop()

                                                            window_user_login_4.destroy()
                                                            user_login_over_ride()



                                                        else:

                                                            messagebox.showerror("Error", "INVALID CREDENTIALS")

                                                    def quit(self):
                                                        window_user_login.destroy()

                                                window_user_login = tk.Tk()
                                                # window_user_login.config(background='#EFEFEF')
                                                # window_user_login.attributes('-alpha', 0.97)

                                                user_login_window = User_Login(window_user_login)
                                                # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                                                window_user_login.title('Admin Login ')
                                                window_user_login.geometry("600x350")
                                                window_user_login.mainloop()

                                            user_login_over_ride1()

                                self.btn_save = ttk.Button(self.windows, text="FINISH", width=20, command=finish)
                                self.btn_save.place(x=400, y=400, width=180, height=40)





                    validatex()


                if str(limit) == str('nil'):
                    self.btn_finish = ttk.Button(window, text="START  SCANNING", width=20, command=self.start)
                    self.btn_finish.place(x=-1, y=290, width=605, height=160)
                if limit == 'start':
                    if len(already_scanned_data) < (len(scanned_data)):
                        task()
                if limit == 'end':
                    print("kk")
                    if len(already_scanned_data) ==(len(scanned_data)):
                        try:
                            self.btn_next.destroy()
                            self.btn_finish.destroy()

                        except:
                            pass
                        task()

                    if len(already_scanned_data) >= len(scanned_data):

                        print(len(already_scanned_data) , len(scanned_data))

                        try:
                            self.btn_back.destroy()
                        except:
                            pass

                        # self.mannual_entry = ttk.Button(window, text="ADD NEW DATA", width=20,
                        #                                 command=self.mannual_entry)
                        # self.mannual_entry.place(x=10, y=400, width=180, height=40)

                        # self.btn_finish = ttk.Button(window, text="START  SCANNING", width=20, command=self.start)
                        # self.btn_finish.place(x=-1, y=290, width=605, height=160)

                        # self.btn_save = ttk.Button(self.windows, text="FINISH", width=20, command=finish)
                        # self.btn_save.place(x=400, y=400, width=180, height=40)














                stringx = already_scanned_data

                self.stringc = stringx
                self.windows = window





            def start(self):

                glmb = tk.messagebox.askquestion('Warning',
                                                 'Are you sure you want to start scanning ?',
                                                 icon='warning')
                if glmb == 'yes':
                    window_user_login_4.destroy()
                else:
                    pass

            def display(self):


                self.txtfld00.destroy()

                try:
                    self.lb0.destroy()
                    self.lb1.destroy()
                    self.txtfld1.destroy()
                    self.lb2.destroy()
                    self.txtfld2.destroy()
                    self.lb3.destroy()
                    self.txtfld3.destroy()
                    self.txtfld00.destroy()
                    self.mannual_entry.destroy()
                    #self.btn_quit.destroy()
                    self.btn_back.place(x=10, y=400, width=180, height=40)
                    self.btn_save.destroy()
                except:
                    pass




                datax = already_scanned_data

                def selectItem(a):
                    curItem = tree.focus()

                    quantifiers = (tree.item(curItem)['values'])

                frame = Frame(window_user_login_4)
                frame.place(x=-1, y=0)

                tree = ttk.Treeview(frame,
                                    columns=(1, 2, 3, 4, 5),
                                    height=17, show="headings")
                tree.pack(side='left')
                tree.bind('<ButtonRelease-1>', selectItem)

                val = ["Sl No", "Exp Date", "Bulk Lot", "GTIN", "Serial", ]

                for i in range(1, len(val) + 1):
                    tree.heading(i, text=val[i - 1])

                for i in range(1, len(val) + 1):
                    tree.column(i, width=116, anchor='center')

                scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                scroll.pack(side='right', fill='y')

                tree.configure(yscrollcommand=scroll.set)

                iter = 0
                for valx in datax:



                    flag = False

                    try:

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
                            iter += 1

                            tree.insert('', 'end',
                                        values=(
                                            str(iter), str(valx[0]), str(valx[1]), str(valx[2]),
                                            str(valx[3])),
                                        tags=('oddx',))


                        else:


                            tree.insert('', 'end',
                                        values=(
                                            str(iter), str(valx[0]), str(valx[1]), str(valx[2]),
                                            str(valx[3])),
                                        tags=('evenx',))

                    # tree.tag_configure('oddx', background='#008001')
                    # tree.tag_configure('evenx', background='#FFFF00')
                    except:
                        pass


                def delete():
                    glm = tk.messagebox.askquestion('Warning',
                                                    'Are you sure you want to Delete the item',
                                                    icon='warning')
                    if glm == 'yes':

                        def user_login_over_ride0():
                            class User_Login():

                                def __init__(self, window):

                                    self.UID = []
                                    self.PWD = []

                                    with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                        all_lines = fh.readlines()
                                        for each in all_lines:
                                            x, y = list(map(str, each.split(",")))
                                            x = str(x).replace("\n", "")
                                            y = str(y).replace("\n", "")
                                            self.UID.append(x)
                                            self.PWD.append(y)

                                    self.lbl = tk.Label(window, text="User", font=("Helvetica", 20),
                                                        bg='#EFEFEF')
                                    # self.lbl.place(x=60, y=90)

                                    self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                             font=("Helvetica", 20))
                                    # self.txtfld1.place(x=220, y=90)
                                    self.txtfld1.insert(0, user_name)

                                    self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20),
                                                        bg='#EFEFEF')
                                    self.lb2.place(x=60, y=90)

                                    self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*",
                                                             font=("Helvetica", 20))
                                    self.txtfld2.place(x=220, y=90)

                                    self.btn = ttk.Button(window, text="DELETE", width=20,
                                                          command=self.validate)
                                    self.btn.place(x=60, y=220, width=200, height=50)

                                    self.btn_quit = ttk.Button(window, text="QUIT", width=20,
                                                               command=self.quit)
                                    self.btn_quit.place(x=330, y=220, width=200, height=50)

                                def validate(self):
                                    if (str(self.txtfld1.get()) in self.UID) and (
                                            str(self.txtfld2.get()) in self.PWD):

                                        for selected_item in tree.selection():
                                            tree.delete(selected_item)

                                        window_user_login.destroy()





                                    else:

                                        messagebox.showerror("Error", "INVALID CREDENTIALS")

                                def quit(self):
                                    window_user_login.destroy()

                            window_user_login = tk.Tk()
                            # window_user_login.config(background='#EFEFEF')
                            # window_user_login.attributes('-alpha', 0.97)

                            user_login_window = User_Login(window_user_login)
                            # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                            window_user_login.title('Admin Login ')
                            window_user_login.geometry("600x350")
                            window_user_login.mainloop()

                        user_login_over_ride0()
                    else:
                        pass

                def finish():
                    if str(self.txtfld01.get()) != str(len(tree.get_children())):
                        glmb = tk.messagebox.askquestion('Warning',
                                                         'Total Bottle Scanned: ' + str(
                                                             len(tree.get_children()))
                                                         + ' \nTotal Bottles Entered: ' + str(
                                                             d1)
                                                         + '\nTotal Bottles are not matching \nPlease Change the Total Bottles'
                                                         ,
                                                         icon='warning')

                        if glmb == 'no':
                            return (0)


                        if glmb == 'yes':

                            glm = tk.messagebox.askquestion('Warning',
                                                            'Are you sure you save the data to xml file ?',
                                                            icon='warning')


                            if glm == 'yes':

                                try:
                                    root.destroy()
                                except:
                                    pass

                                def printtext():
                                    updates_total_bottle = txtfld19.get()
                                    root.destroy()
                                    if str(updates_total_bottle) != str(len(tree.get_children())):
                                        tk.messagebox.showerror('error',
                                                                'Total Bottle Scanned ' + str(
                                                                    len(tree.get_children()))
                                                                + ' do not match with the Total Bottle in Bulk Data ' + str(
                                                                    updates_total_bottle),
                                                                icon='error')

                                        return (0)
                                    else:
                                        def user_login_over_ride1():
                                            class User_Login():

                                                def __init__(self, window):

                                                    self.UID = []
                                                    self.PWD = []

                                                    with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                                        all_lines = fh.readlines()
                                                        for each in all_lines:
                                                            x, y = list(map(str, each.split(",")))

                                                            x = str(x).replace("\n", "")
                                                            y = str(y).replace("\n", "")
                                                            self.UID.append(x)
                                                            self.PWD.append(y)

                                                    self.lbl = tk.Label(window, text="User",
                                                                        font=("Helvetica", 20),
                                                                        bg='#EFEFEF')
                                                    # self.lbl.place(x=60, y=90)

                                                    self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                                             font=("Helvetica", 20))
                                                    # self.txtfld1.place(x=220, y=90)
                                                    self.txtfld1.insert(0, user_name)

                                                    self.lb2 = tk.Label(window, text="Password",
                                                                        font=("Helvetica", 20),
                                                                        bg='#EFEFEF')
                                                    self.lb2.place(x=60, y=90)

                                                    self.txtfld2 = ttk.Entry(window,
                                                                             text="Enter Password",
                                                                             show="*",
                                                                             font=("Helvetica", 20))
                                                    self.txtfld2.place(x=220, y=90)

                                                    self.btn = ttk.Button(window, text="SAVE", width=20,
                                                                          command=self.validate)
                                                    self.btn.place(x=60, y=220, width=200, height=50)

                                                    self.btn_quit = ttk.Button(window, text="QUIT",
                                                                               width=20,
                                                                               command=self.quit)
                                                    self.btn_quit.place(x=330, y=220, width=200,
                                                                        height=50)

                                                def validate(self):
                                                    if (str(self.txtfld1.get()) in self.UID) and (
                                                            str(self.txtfld2.get()) in self.PWD):

                                                        user_id = str(self.txtfld1.get())

                                                        window_user_login.destroy()

                                                        data_xml = []
                                                        xx = tree.get_children()

                                                        for each in xx:
                                                            vc = tree.item(each)['values']
                                                            strx = '01' + (
                                                                str('0000' + str(c1))[
                                                                -14:]) + '21' + str(
                                                                vc[4]) + '17' + str(a1[2:]).replace('-',
                                                                                                    '') + '10' + b1
                                                            data_xml.append(strx)

                                                        def xml_creator():

                                                            from datetime import datetime
                                                            from xml.dom import minidom
                                                            from xml.dom.minidom import \
                                                                getDOMImplementation

                                                            root = minidom.Document()
                                                            root.standalone = 'No'

                                                            iso_date = datetime.now().astimezone().isoformat()
                                                            offset = iso_date[-6:]
                                                            expire_date = a1
                                                            bulk_lot_number = b1
                                                            repackage_lot_number = b2
                                                            strings = data_xml

                                                            list_data = ''

                                                            for each in strings:
                                                                list_data += str(
                                                                    '<epcis:epc>') + each + str(
                                                                    '</epcis:epc>')

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
                                                            <epcis:extension><!--@Verify By ''' + str(
                                                                user_id) + f'''-->
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

                                                            xml_str = dom.toprettyxml(indent="  ",
                                                                                      newl='',
                                                                                      encoding='UTF-8')
                                                            timestamp = int(datetime.now().timestamp())
                                                            save_path_file = f"{b1}-{b2}-{timestamp}.xml"

                                                            with open(save_path_file, "w") as f:
                                                                f.write(xml_str.decode())

                                                        xml_creator()
                                                        messagebox.showwarning("Info",
                                                                               "XML file Created Succesfully")
                                                        for i in range(len(already_scanned_data)):
                                                            already_scanned_data.pop()

                                                        for i in range(len(scanned_serial)):
                                                            scanned_serial.pop()

                                                        #xml_creator()
                                                        window_user_login_4.destroy()
                                                        user_login_over_ride()



                                                    else:

                                                        messagebox.showerror("Error",
                                                                             "INVALID CREDENTIALS")

                                                def quit(self):
                                                    window_user_login.destroy()

                                            window_user_login = tk.Tk()
                                            # window_user_login.config(background='#EFEFEF')
                                            # window_user_login.attributes('-alpha', 0.97)

                                            user_login_window = User_Login(window_user_login)
                                            # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                                            window_user_login.title('Admin Login ')
                                            window_user_login.geometry("600x350")
                                            window_user_login.mainloop()

                                        user_login_over_ride1()

                                root = tk.Tk()

                                root.title('Enter Total Bottle')

                                lbl = tk.Label(root, text="Total Bottle", font=("Helvetica", 20),
                                               bg='#EFEFEF')
                                lbl.place(x=60, y=30)

                                txtfld19 = tk.Entry(root, text="Total Bottle", font=("Helvetica", 20))
                                txtfld19.place(x=220, y=30)

                                b = ttk.Button(root, text='UPDATE', command=printtext)
                                b.place(x=380, y=90, height=40, width=145)
                                root.geometry("600x150")
                                root.mainloop()





                            else:
                                return (0)

                        else:
                            def user_login_over_ride1():
                                class User_Login():

                                    def __init__(self, window):

                                        self.UID = []
                                        self.PWD = []

                                        with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                            all_lines = fh.readlines()
                                            for each in all_lines:
                                                x, y = list(map(str, each.split(",")))

                                                x = str(x).replace("\n", "")
                                                y = str(y).replace("\n", "")
                                                self.UID.append(x)
                                                self.PWD.append(y)

                                        self.lbl = tk.Label(window, text="User", font=("Helvetica", 20),
                                                            bg='#EFEFEF')
                                        # self.lbl.place(x=60, y=90)

                                        self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                                 font=("Helvetica", 20))
                                        # self.txtfld1.place(x=220, y=90)
                                        self.txtfld1.insert(0, user_name)

                                        self.lb2 = tk.Label(window, text="Password",
                                                            font=("Helvetica", 20),
                                                            bg='#EFEFEF')
                                        self.lb2.place(x=60, y=90)

                                        self.txtfld2 = ttk.Entry(window, text="Enter Password",
                                                                 show="*",
                                                                 font=("Helvetica", 20))
                                        self.txtfld2.place(x=220, y=90)

                                        self.btn = ttk.Button(window, text="SAVE", width=20,
                                                              command=self.validate)
                                        self.btn.place(x=60, y=220, width=200, height=50)

                                        self.btn_quit = ttk.Button(window, text="QUIT", width=20,
                                                                   command=self.quit)
                                        self.btn_quit.place(x=330, y=220, width=200, height=50)

                                    def validate(self):
                                        if (str(self.txtfld1.get()) in self.UID) and (
                                                str(self.txtfld2.get()) in self.PWD):

                                            user_id = str(self.txtfld1.get())

                                            window_user_login.destroy()

                                            data_xml = []
                                            xx = tree.get_children()

                                            for each in xx:
                                                vc = tree.item(each)['values']
                                                strx = '01' + (
                                                    str('0000' + str(c1))[-14:]) + '21' + str(
                                                    vc[4]) + '17' + str(a1[2:]).replace('-',
                                                                                        '') + '10' + b1
                                                data_xml.append(strx)

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
                                                strings = data_xml

                                                list_data = ''

                                                for each in strings:
                                                    list_data += str('<epcis:epc>') + each + str(
                                                        '</epcis:epc>')

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
                                                <epcis:extension><!--@Verify By ''' + str(
                                                    user_id) + f'''-->
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

                                                xml_str = dom.toprettyxml(indent="  ", newl='',
                                                                          encoding='UTF-8')
                                                timestamp = int(datetime.now().timestamp())
                                                save_path_file = f"{b1}-{b2}-{timestamp}.xml"

                                                with open(save_path_file, "w") as f:
                                                    f.write(xml_str.decode())

                                            xml_creator()
                                            window_user_login_4.destroy()
                                            user_login_over_ride()



                                        else:

                                            messagebox.showerror("Error", "INVALID CREDENTIALS")

                                    def quit(self):
                                        window_user_login.destroy()

                                window_user_login = tk.Tk()
                                # window_user_login.config(background='#EFEFEF')
                                # window_user_login.attributes('-alpha', 0.97)

                                user_login_window = User_Login(window_user_login)
                                # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                                window_user_login.title('Admin Login ')
                                window_user_login.geometry("600x350")
                                window_user_login.mainloop()

                            user_login_over_ride1()

                self.lbx = tk.Label(self.windows, text="* To delete multiple rows press ctrl and select the rows you want to delete and press delete button",
                                    font=("Helvetica", 10), bg='#EFEFEF')
                self.lbx.place(x=10,y=374)

                self.btn_quit = ttk.Button(self.windows, text="DELETE", width=20, command=delete)
                self.btn_quit.place(x=205, y=400, width=180, height=40)
                button1_ttp = CreateToolTip(self.btn_quit,
                                            'To delete multiple rows press ctrl and select the rows you want to delete and press delete button')

                self.btn_save = ttk.Button(self.windows, text="FINISH", width=20, command=finish)
                self.btn_save.place(x=400, y=400, width=180, height=40)



            def mannual_entry(self):

                value=True

                #print(scanned_data)





                while value==True:

                    glmb = tk.messagebox.askquestion('Warning',
                                                     'Are you sure you want to manually enter more serial number ? '
                                                     ,
                                                     icon='warning')

                    if glmb == 'no':
                        # window_user_login_4.destroy()
                        # quiter(user_name=user_name, a1=a1, b1=b1, c1=c1, d1=d1, e1=e1, a2=a2, b2=b2,
                        #        c2=c2, d2=d2, e2=e2, limit='mannual')
                        return (0)


                    if glmb == 'yes':

                        glm = 'yes'


                        if glm == 'yes':

                            try:
                                root.destroy()
                            except:
                                pass

                            def printtext():
                                updates_total_bottle = txtfld19.get()
                                root.destroy()
                                if str(updates_total_bottle) != str(updates_total_bottle):
                                    print(0)
                                    # tk.messagebox.showerror('error',
                                    #                         'Total Bottle Scanned ' + str(
                                    #                             len(tree.get_children()))
                                    #                         + ' do not match with the Total Bottle in Bulk Data ' + str(
                                    #                             updates_total_bottle),
                                    #                         icon='error')
                                    #
                                    # return (0)
                                else:
                                    def user_login_over_ride1():
                                        class User_Login():

                                            def __init__(self, window):

                                                self.UID = []
                                                self.PWD = []

                                                with open('DATA/PRIVATE/passkey.txt', 'r') as fh:
                                                    all_lines = fh.readlines()
                                                    for each in all_lines:
                                                        x, y = list(map(str, each.split(",")))

                                                        x = str(x).replace("\n", "")
                                                        y = str(y).replace("\n", "")
                                                        self.UID.append(x)
                                                        self.PWD.append(y)

                                                self.lbl = tk.Label(window, text="User",
                                                                    font=("Helvetica", 20),
                                                                    bg='#EFEFEF')
                                                # self.lbl.place(x=60, y=90)

                                                self.txtfld1 = ttk.Entry(window, text="Enter UID",
                                                                         font=("Helvetica", 20))
                                                # self.txtfld1.place(x=220, y=90)
                                                self.txtfld1.insert(0, user_name)

                                                self.lb2 = tk.Label(window, text="Password",
                                                                    font=("Helvetica", 20),
                                                                    bg='#EFEFEF')
                                                self.lb2.place(x=60, y=90)

                                                self.txtfld2 = ttk.Entry(window,
                                                                         text="Enter Password",
                                                                         show="*",
                                                                         font=("Helvetica", 20))
                                                self.txtfld2.place(x=220, y=90)

                                                self.btn = ttk.Button(window, text="ADD", width=20,
                                                                      command=self.validate)
                                                self.btn.place(x=60, y=220, width=200, height=50)

                                                self.btn_quit = ttk.Button(window, text="QUIT",
                                                                           width=20,
                                                                           command=self.quit)
                                                self.btn_quit.place(x=330, y=220, width=200,
                                                                    height=50)

                                            def validate(self):
                                                if (str(self.txtfld1.get()) in self.UID) and (
                                                        str(self.txtfld2.get()) in self.PWD):

                                                    user_id = str(self.txtfld1.get())

                                                    window_user_login.destroy()

                                                    already_scanned_data.append([a1,b1,c1,updates_total_bottle])



                                                    # data_xml = []
                                                    # xx = tree.get_children()
                                                    #
                                                    # for each in xx:
                                                    #     vc = tree.item(each)['values']
                                                    #     strx = '01' + (
                                                    #         str('0000' + str(c1))[
                                                    #         -14:]) + '21' + str(
                                                    #         vc[4]) + '17' + str(a1[2:]).replace('-',
                                                    #                                             '') + '10' + b1
                                                    #     data_xml.append(strx)


                                                    messagebox.showwarning("Info",
                                                                           "Serial Added Succesfully")





                                                    #xml_creator()
                                                    # window_user_login_4.destroy()
                                                    # user_login_over_ride()



                                                else:

                                                    messagebox.showerror("Error",
                                                                         "INVALID CREDENTIALS")

                                            def quit(self):
                                                window_user_login.destroy()

                                        window_user_login = tk.Tk()
                                        # window_user_login.config(background='#EFEFEF')
                                        # window_user_login.attributes('-alpha', 0.97)

                                        user_login_window = User_Login(window_user_login)
                                        # window_user_login.iconbitmap(default='DATA/IMAGES/icons/favicon.ico')
                                        window_user_login.title('Admin Login ')
                                        window_user_login.geometry("600x350")
                                        window_user_login.mainloop()

                                    user_login_over_ride1()

                            root = tk.Tk()

                            root.title('Enter Serial Number')

                            lbl = tk.Label(root, text="Serial ", font=("Helvetica", 20),
                                           bg='#EFEFEF')
                            lbl.place(x=60, y=30)

                            txtfld19 = tk.Entry(root, text="Serial", font=("Helvetica", 20))
                            txtfld19.place(x=220, y=30)

                            b = ttk.Button(root, text='ADD SERIAL', command=printtext)
                            b.place(x=380, y=90, height=40, width=145)
                            root.geometry("600x150")
                            root.mainloop()





                        else:
                            return (0)







            def back(self):

                MsgBox = tk.messagebox.askquestion('Warning',
                                                   'Going back to scanning Page .',
                                                   icon='warning')

                if MsgBox == 'yes':

                    window_user_login_4.destroy()
                    if already_scanned_data[-1] == False:
                        already_scanned_data.pop()

                    quiter(user_name=user_name, a1=a1, b1=b1, c1=c1, d1=d1, e1=e1, a2=a2, b2=b2,
                                 c2=c2, d2=d2, e2=e2,limit=limit)

                else:
                    pass

        window_user_login_4 = tk.Tk()
        # window_user_login_4.config(background='#EFEFEF')
        # window_user_login_4.attributes('-alpha', 0.97)

        user_login_window = User_4(window_user_login_4)
        # window_user_login_4.iconbitmap(
        #     default='DATA/IMAGES/icons/favicon.ico')
        window_user_login_4.title(
            'Scanning Page ' + '4')

        window_user_login_4.geometry("600x450")
        def exitx():
            exit(0)
        window_user_login_4.protocol('WM_DELETE_WINDOW', exitx)

        window_user_login_4.mainloop()

    user_login_over_ride()



if __name__ == '__main__':
    main()

