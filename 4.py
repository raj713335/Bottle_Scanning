import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox,Frame
from tkcalendar import  DateEntry
from PIL import Image, ImageTk
import cv2
import sys




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

scanned_data=[['2021-08-31', '00307815988012', 'FX000563', '914093071883001'], ['2021-08-31', '00307815988012', 'FX000563', '914093071883002'], ['2021-08-31', '00307815988012', 'FX000563', '914093071883003'], ['2021-08-31', '00307815988012', 'FX000563', '914093071883004'], ['2021-08-31', '00307815988012', 'FX000563', '914093071883005'], ['2021-08-31', '00307815988012', 'FX000563', '914093071883006']]




already_scanned_data=[]


def user_login_4(user_name=str(0), a1=str(0), b1=str(0), c1=str(0), d1=str(0), e1=str(0), a2=str(0), b2=str(0),
                 c2=str(0), d2=str(0),
                 e2=str(0), id=str(0), limit=str(0)):
    class User_4():

        def __init__(self, window):



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
            if id == 'NIL':
                self.txtfld00.set('0')
                self.txtfld00.config(state='disabled')
            else:
                self.txtfld00.set(id)
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
                                        font=("Helvetica", 10), state='readonly')
            self.txtfld1.place(x=270, y=170, width=260)
            self.txtfld1.set(a1)
            self.txtfld1.config(state='disabled')

            self.lb2 = tk.Label(window, text="Bulk Lot", font=("Helvetica", 10), bg='#EFEFEF')
            self.lb2.place(x=60, y=210)

            self.txtfld2 = ttk.Combobox(window,
                                        font=("Helvetica", 10), state='readonly')
            self.txtfld2.place(x=270, y=210, width=260)
            self.txtfld2.set(b1)
            self.txtfld2.config(state='disabled')

            self.lb3 = tk.Label(window, text="GTIN", font=("Helvetica", 10), bg='#EFEFEF')
            self.lb3.place(x=60, y=250)

            self.txtfld3 = ttk.Combobox(window, text="Enter UID", font=("Helvetica", 10), state='readonly')
            self.txtfld3.place(x=270, y=250, width=260)
            self.txtfld3.set(c1)
            self.txtfld3.config(state='disabled')

            self.lb5 = tk.Label(window, text="Batch Size", font=("Helvetica", 10), bg='#EFEFEF')
            self.lb5.place(x=60, y=290)

            self.txtfld5 = ttk.Combobox(window,
                                        font=("Helvetica", 10))
            self.txtfld5.place(x=270, y=290, width=260)
            self.txtfld5.set(e1)
            self.txtfld5.config(state='disabled')

            self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
            self.btn_back.place(x=10, y=400, width=180, height=40)





            def task():




                iterx=len(already_scanned_data)

                date_xx = scanned_data[iterx][0]
                lot_x = scanned_data[iterx][2]
                gstin_x = scanned_data[iterx][1]
                serial_x = scanned_data[iterx][3]

                print(date_xx, lot_x, gstin_x, serial_x)

                self.txtfld1.set(date_xx)
                self.txtfld2.set(lot_x)
                self.txtfld3.set(gstin_x)
                self.txtfld5.set(serial_x)

                def validatex():

                    if ((str(self.txtfld1.get()) == str(a1))):

                        a3 = (str(self.txtfld1.get()))

                    else:

                        messagebox.showerror("Error", "Date " + str(self.txtfld1.get()) +
                                             " in serial number " + str(self.txtfld5.get()) +
                                             " do not match with Bulk Date " + str(a1) +
                                             " , returning back to Admin page.")

                        window_user_login_4.destroy()
                        user_login_over_ride()

                    if ((str(self.txtfld2.get()) == str(b1))):

                        b3 = (str(self.txtfld2.get()))


                    else:

                        messagebox.showerror("Error", "Bulk Lot " + str(self.txtfld2.get()) +
                                             " in serial number " + str(self.txtfld5.get()) +
                                             " do not match with Bulk Lot " + str(b1) +
                                             " , returning back to Admin page.")

                        window_user_login_4.destroy()
                        user_login_over_ride()

                    if ((str(self.txtfld3.get()) == str(c1))):

                        c3 = (str(self.txtfld3.get()))

                    else:

                        messagebox.showerror("Error", "GTIN " + str(self.txtfld3.get()) +
                                             " in serial number " + str(self.txtfld5.get()) +
                                             " do not match with Bulk Data GTIN " + str(c1) +
                                             " , returning back to Admin page.")

                        window_user_login_4.destroy()
                        user_login_over_ride()

                    if ((str(self.txtfld5.get()).isalnum())):

                        e3 = (str(self.txtfld5.get()))

                    else:

                        messagebox.showwarning("Warning",
                                               "Batch Number Number must be aplhanumeric and should not contain any special characters")

                        window_user_login_4.destroy()
                        user_login_over_ride()

                    if ((str(self.txtfld5.get()) != "")):

                        e3 = (str(self.txtfld5.get()))

                    else:

                        messagebox.showwarning("Warning", "Missing Batch Size Field")
                        window_user_login_4.destroy()
                        user_login_over_ride()

                    already_scanned_data.append([a3,b3,c3,e3])
                    if len(already_scanned_data) < (len(scanned_data)):
                        window_user_login_4.after(2000, task)
                    else:
                        limit='end'
                        print(limit)

                        if str(limit) == str('end'):

                            self.btn_back.destroy()

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
                            for valx in stringx:

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
                                                values=(
                                                str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                                tags=('oddx',))
                                else:
                                    tree.insert('', 'end',
                                                values=(
                                                str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                                tags=('evenx',))

                            def finish():

                                glm = tk.messagebox.askquestion('Warning',
                                                                'Are you sure you save the data to xml file ?',
                                                                icon='warning')
                                if glm == 'yes':

                                    if str(self.txtfld01.get()) != str(len(tree.get_children())):
                                        glmb = tk.messagebox.askquestion('Warning',
                                                                         'Total Bottle Scanned ' + str(
                                                                             len(tree.get_children()))
                                                                         + ' do not match with the Total Bottle in Bulk Data ' + str(
                                                                             d1)
                                                                         + '. Do you want to update the Total Bottle in Bulk Data to '
                                                                         + str(len(tree.get_children())) + ' ?',
                                                                         icon='warning')
                                        if glmb == 'yes':

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

                                                                self.txtfld2 = ttk.Entry(window, text="Enter Password",
                                                                                         show="*",
                                                                                         font=("Helvetica", 20))
                                                                self.txtfld2.place(x=220, y=90)

                                                                self.btn = ttk.Button(window, text="SAVE", width=20,
                                                                                      command=self.validate)
                                                                self.btn.place(x=60, y=220, width=200, height=50)

                                                                self.btn_quit = ttk.Button(window, text="QUIT",
                                                                                           width=20,
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

                                                    self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20),
                                                                        bg='#EFEFEF')
                                                    self.lb2.place(x=60, y=90)

                                                    self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*",
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
                                                            strx = '01' + (str('0000' + str(c1))[-14:]) + '21' + str(
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
                                                            <epcis:extension><!--@Verify By ''' + str(user_id) + f'''-->
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

                            self.btn_save = ttk.Button(window, text="FINISH", width=20, command=finish)
                            self.btn_save.place(x=400, y=400, width=180, height=40)

                            self.btn_back = ttk.Button(window, text="BACK", width=20, command=self.back)
                            self.btn_back.place(x=10, y=400, width=180, height=40)

                            self.btn_quit = ttk.Button(window, text="DISPLAY", width=20, command=self.display)
                            self.btn_quit.place(x=205, y=400, width=180, height=40)



                        if limit == 'end':

                            datax = scanned_data

                            def selectItem(a):
                                curItem = tree.focus()

                                quantifiers = (tree.item(curItem)['values'])

                            frame = Frame(window_user_login_4)
                            frame.place(x=-1, y=0)

                            tree = ttk.Treeview(frame,
                                                columns=(1, 2, 3, 4, 5),
                                                height=18, show="headings")
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
                                                values=(
                                                str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                                tags=('oddx',))
                                else:
                                    tree.insert('', 'end',
                                                values=(
                                                str(iter), str(valx[0]), str(valx[1]), str(valx[2]), str(valx[3])),
                                                tags=('evenx',))

                            # tree.tag_configure('oddx', background='#008001')
                            # tree.tag_configure('evenx', background='#FFFF00')

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

                                glm = tk.messagebox.askquestion('Warning',
                                                                'Are you sure you save the data to xml file ?',
                                                                icon='warning')
                                if glm == 'yes':

                                    if str(self.txtfld01.get()) != str(len(tree.get_children())):
                                        glmb = tk.messagebox.askquestion('Warning',
                                                                         'Total Bottle Scanned ' + str(
                                                                             len(tree.get_children()))
                                                                         + ' do not match with the Total Bottle in Bulk Data ' + str(
                                                                             d1)
                                                                         + '. Do you want to update the Total Bottle in Bulk Data to '
                                                                         + str(len(tree.get_children())) + ' ?',
                                                                         icon='warning')
                                        if glmb == 'yes':

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

                                                                self.txtfld2 = ttk.Entry(window, text="Enter Password",
                                                                                         show="*",
                                                                                         font=("Helvetica", 20))
                                                                self.txtfld2.place(x=220, y=90)

                                                                self.btn = ttk.Button(window, text="SAVE", width=20,
                                                                                      command=self.validate)
                                                                self.btn.place(x=60, y=220, width=200, height=50)

                                                                self.btn_quit = ttk.Button(window, text="QUIT",
                                                                                           width=20,
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

                                                    self.lb2 = tk.Label(window, text="Password", font=("Helvetica", 20),
                                                                        bg='#EFEFEF')
                                                    self.lb2.place(x=60, y=90)

                                                    self.txtfld2 = ttk.Entry(window, text="Enter Password", show="*",
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
                                                            strx = '01' + (str('0000' + str(c1))[-14:]) + '21' + str(
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
                                                            <epcis:extension><!--@Verify By ''' + str(user_id) + f'''-->
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

                            self.btn_quit = ttk.Button(self.windows, text="DELETE", width=20, command=delete)
                            self.btn_quit.place(x=205, y=400, width=180, height=40)
                            button1_ttp = CreateToolTip(self.btn_quit,
                                                        'To delete multiple rows press ctrl and select the rows you want to delete and press delete button')

                            self.btn_save = ttk.Button(self.windows, text="FINISH", width=20, command=finish)
                            self.btn_save.place(x=400, y=400, width=180, height=40)


                validatex()

            if limit == 'start':
                if len(already_scanned_data)<(len(scanned_data)):
                    task()


            if str(limit) == str('nil'):
                self.btn_finish = ttk.Button(window, text="START  SCANNING", width=20, command=self.start)
                self.btn_finish.place(x=-1, y=290, width=605, height=160)



            stringx = scanned_data



            self.stringc = stringx
            self.windows = window











        def start(self):

            glmb = tk.messagebox.askquestion('Warning',
                                             'Are you sure you want to start scanning ?',
                                             icon='warning')
            if glmb == 'yes':
                window_user_login_4.destroy()
            else:
                exit(0)

        def display(self):
            self.lb0.destroy()
            self.lb1.destroy()
            self.txtfld1.destroy()
            self.lb2.destroy()
            self.txtfld2.destroy()
            self.lb3.destroy()
            self.txtfld3.destroy()
            self.txtfld00.destroy()
            self.btn_quit.destroy()
            self.btn_back.place(x=10, y=400, width=180, height=40)
            self.btn_save.destroy()



        def back(self):

            MsgBox = tk.messagebox.askquestion('Warning',
                                               'All Progress will be lost',
                                               icon='warning')

            if MsgBox == 'yes':

                window_user_login_4.destroy()

                user_login_3(user_name=user_name, a1=a1, b1=b1, c1=c1, d1=d1, e1=e1, a2=a2, b2=b2,
                             c2=c2, d2=d2, e2=e2)

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
    window_user_login_4.mainloop()



user_login_4(user_name=str(0), a1=str('2021-08-31'), b1=str('FX000563'), c1=str('00307815988012'), d1=str(0), e1=str('914093071883001'), a2=str(0), b2=str(0),
                 c2=str(0), d2=str(0),
                 e2=str(0), id=str(0), limit=str('nil'))

