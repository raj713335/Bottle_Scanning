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

                class App:
                    def __init__(self):

                        def selectItem(a):
                            curItem = tree.focus()
                            # print(tree.item(curItem)['values'])
                            quantifiers = (tree.item(curItem)['values'])



                            def user_modify_station():
                                # CLASS FOR ADDING STATION
                                class User_Modify_station():

                                    def __init__(self, window):
                                        load = cv2.imread('Images/background.png', 1)
                                        cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                                        load = Image.fromarray(cv2imagex1)
                                        load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                                        render = ImageTk.PhotoImage(load)
                                        img = tk.Label(image=render)
                                        img.image = render
                                        img.place(x=0, y=140)

                                        # LABEL AND TEXT BOX TO ENTER DETAILS OF ALL ELEMENTS OF A STATION
                                        self.lb_title = Label(window, text="Características Chaves",
                                                              font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9',
                                                              fg='#34943a')
                                        self.lb_title.place(x=400, y=150)

                                        self.lb1 = Label(window, text="#KC",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                                        self.lb1.place(x=5, y=142)

                                        self.txtfld1 = ttk.Combobox(window, text="#KC",
                                                                    font=("Ariel", 10))
                                        self.txtfld1.place(x=60, y=140)

                                        self.txtfld1.set(quantifiers[0])

                                        self.txtfld1.config(state=DISABLED)

                                        self.lb2 = Label(window, text="Part Number",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb2.place(x=80, y=230)

                                        self.txtfld2 = ttk.Combobox(window, text="Part Number",
                                                                    font=("Ariel", 10), values=Part_Number)
                                        self.txtfld2.place(x=210, y=230)

                                        self.txtfld2.set(quantifiers[1])

                                        self.lb3 = Label(window, text="Rev.",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb3.place(x=420, y=230)

                                        self.txtfld3 = ttk.Combobox(window, text="Rev.",
                                                                    font=("Ariel", 10), values=Rev)
                                        self.txtfld3.place(x=550, y=230)

                                        self.txtfld3.set(quantifiers[2])

                                        self.lb4 = Label(window, text="Centro de Traball",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb4.place(x=760, y=230)

                                        self.txtfld4 = ttk.Combobox(window, text="Centro de Traball",
                                                                    font=("Ariel", 10), values=Centro_de_Trabalho)
                                        self.txtfld4.place(x=890, y=230)

                                        self.txtfld4.set(quantifiers[4])

                                        self.lb5 = Label(window, text="KC Similar",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb5.place(x=760, y=310)

                                        self.txtfld5 = ttk.Combobox(window, text="KC Similar", state="readonly",
                                                                    font=("Ariel", 10), values=KC_Similar)
                                        self.txtfld5.place(x=890, y=310)

                                        self.txtfld5.set(quantifiers[3])
                                        self.txtfld5.configure(state=DISABLED)

                                        self.lb6 = Label(window, text="Processo",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb6.place(x=420, y=270)

                                        self.txtfld6 = ttk.Combobox(window,
                                                                    text="Processo",
                                                                    font=("Ariel", 10), values=Processo)
                                        self.txtfld6.place(x=550, y=270)

                                        self.txtfld6.set(quantifiers[5])

                                        self.lb7 = Label(window, text="Descrição",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb7.place(x=760, y=270)

                                        self.txtfld7 = ttk.Combobox(window,

                                                                    text="Descrição",
                                                                    font=("Ariel", 10), values=Descrição)
                                        self.txtfld7.place(x=890, y=270)

                                        self.txtfld7.set(quantifiers[6])

                                        self.lb8 = Label(window, text="Especificação",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb8.place(x=80, y=310)

                                        self.txtfld8 = ttk.Combobox(window, text="Especificação",
                                                                    font=("Ariel", 10), values=Especificação)
                                        self.txtfld8.place(x=210, y=310)

                                        self.txtfld8.set(quantifiers[7])

                                        self.lb9 = Label(window, text="Tolerância",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                         anchor='e')
                                        self.lb9.place(x=420, y=310)

                                        self.txtfld9 = ttk.Combobox(window,

                                                                    text="Tolerância",
                                                                    font=("Ariel", 10), values=Tolerância)
                                        self.txtfld9.place(x=550, y=310)

                                        self.txtfld9.set(quantifiers[8])

                                        self.lb10 = Label(window, text="Unidade",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb10.place(x=80, y=270)

                                        self.txtfld10 = ttk.Combobox(window, text="Unidade",
                                                                     font=("Ariel", 10), values=Unidade)
                                        self.txtfld10.place(x=210, y=270)

                                        self.txtfld10.set(quantifiers[9])

                                        self.lb11 = Label(window, text="Tipo de caract.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb11.place(x=80, y=350)

                                        self.txtfld11 = ttk.Combobox(window,
                                                                     text="Tipo de caract.",
                                                                     font=("Ariel", 10), values=Tipo_de_caract)
                                        self.txtfld11.place(x=210, y=350)

                                        self.txtfld11.set(quantifiers[10])

                                        self.lb12 = Label(window, text="Tipo de dados",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb12.place(x=420, y=350)

                                        self.txtfld12 = ttk.Combobox(window, text="Tipo de dados",
                                                                     font=("Ariel", 10), values=Tipo_de_dados)
                                        self.txtfld12.place(x=550, y=350)

                                        self.txtfld12.set(quantifiers[11])

                                        self.lb13 = Label(window, text="Local de Medição",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb13.place(x=760, y=350)

                                        self.txtfld13 = ttk.Combobox(window,
                                                                     text="Local de Medição",
                                                                     font=("Ariel", 10), values=Local_de_Medição)
                                        self.txtfld13.place(x=890, y=350)

                                        self.txtfld13.set(quantifiers[12])

                                        self.lb14 = Label(window, text="Resp. Qualidade",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb14.place(x=80, y=390)

                                        self.txtfld14 = ttk.Combobox(window, text="Resp. Qualidade",
                                                                     font=("Ariel", 10), values=Resp_Qualidade)
                                        self.txtfld14.place(x=210, y=390)

                                        self.txtfld14.set(quantifiers[13])

                                        self.lb15 = Label(window, text="Resp. Manufatura",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb15.place(x=420, y=390)

                                        self.txtfld15 = ttk.Combobox(window,
                                                                     text="Resp. Manufatura",
                                                                     font=("Ariel", 10), values=Resp_Manufatura)
                                        self.txtfld15.place(x=550, y=390)

                                        self.txtfld15.set(quantifiers[14])

                                        self.lb16 = Label(window, text="Produto",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb16.place(x=760, y=390)

                                        self.txtfld16 = ttk.Combobox(window, text="Produto",
                                                                     font=("Ariel", 10), values=Produto)
                                        self.txtfld16.place(x=890, y=390)
                                        self.txtfld16.set(quantifiers[15])

                                        self.lb17 = Label(window, text="Projeto / ECM",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb17.place(x=80, y=430)

                                        self.txtfld17 = ttk.Combobox(window,
                                                                     text="Projeto / ECM",
                                                                     font=("Ariel", 10), values=Projeto_ECM)
                                        self.txtfld17.place(x=210, y=430)
                                        self.txtfld17.set(quantifiers[16])

                                        self.lb18 = Label(window, text="Data de Impl.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb18.place(x=420, y=430)

                                        self.txtfld18 = ttk.Combobox(window, text="Data de Impl.",
                                                                     font=("Ariel", 10), values=Data_de_Impl)
                                        self.txtfld18.place(x=550, y=430)
                                        self.txtfld18.set(quantifiers[17])

                                        self.lb19 = Label(window, text="Status",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb19.place(x=760, y=430)

                                        self.txtfld19 = ttk.Combobox(window, state="readonly",
                                                                     text="Status",
                                                                     font=("Ariel", 10), values=Status)
                                        self.txtfld19.place(x=890, y=430)

                                        self.txtfld19.set(quantifiers[18])

                                        image_loader(image_pathx=quantifiers[1])

                                        # RR CODES FOR BOXES

                                        self.lb20 = Label(window, text="Estudo RR",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb20.place(x=80, y=480)

                                        self.txtfld20 = ttk.Combobox(window,
                                                                     text="Estudo RR",
                                                                     font=("Ariel", 10), values=Estudo_rr)
                                        self.txtfld20.place(x=210, y=480)
                                        self.txtfld20.set(quantifiers[20])
                                        self.txtfld20.configure(state=DISABLED)

                                        self.lb21 = Label(window, text="R&R Solicitado",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb21.place(x=420, y=480)

                                        self.txtfld21 = ttk.Combobox(window, text="R&R Solicitado", state="readonly",
                                                                     font=("Ariel", 10), values=list(
                                                ["Sim", "Não"]))
                                        self.txtfld21.place(x=550, y=480)
                                        self.txtfld21.set(quantifiers[19])
                                        # self.txtfld21.configure(state=DISABLED)

                                        self.lb22 = Label(window, text="Resultado",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb22.place(x=760, y=480)

                                        self.txtfld22 = ttk.Combobox(window,
                                                                     text="Resultado", state="readonly",
                                                                     font=("Ariel", 10), values=Resultado)
                                        self.txtfld22.place(x=890, y=480)

                                        self.txtfld22.set(quantifiers[21])
                                        self.txtfld22.configure(state=DISABLED)

                                        # TABLE FOR CAPABILITY

                                        self.lb30 = Label(window, text="Estudo CAP",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb30.place(x=80, y=520)

                                        self.txtfld30 = ttk.Combobox(window,
                                                                     text="Estudo CAP",
                                                                     font=("Ariel", 10), values=Estudo_cap)
                                        self.txtfld30.place(x=210, y=520)
                                        self.txtfld30.set(quantifiers[22])
                                        self.txtfld30.configure(state=DISABLED)

                                        self.lb31 = Label(window, text="CP",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb31.place(x=420, y=520)

                                        self.txtfld31 = ttk.Combobox(window, text="CP",
                                                                     font=("Ariel", 10), values=Cp)
                                        self.txtfld31.place(x=550, y=520)
                                        self.txtfld31.set(quantifiers[23])
                                        self.txtfld31.configure(state=DISABLED)

                                        self.lb32 = Label(window, text="CPK",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb32.place(x=760, y=520)

                                        self.txtfld32 = ttk.Combobox(window,
                                                                     text="CPK", state="readonly",
                                                                     font=("Ariel", 10), values=Cpk)
                                        self.txtfld32.place(x=890, y=520)

                                        self.txtfld32.set(quantifiers[24])
                                        self.txtfld32.configure(state=DISABLED)

                                        self.lb33 = Label(window, text="PPM",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb33.place(x=80, y=550)

                                        self.txtfld33 = ttk.Combobox(window,
                                                                     text="PPM",
                                                                     font=("Ariel", 10), values=PPM)
                                        self.txtfld33.place(x=210, y=550)
                                        self.txtfld33.set(quantifiers[25])
                                        self.txtfld33.configure(state=DISABLED)

                                        self.lb34 = Label(window, text="Data",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb34.place(x=420, y=550)

                                        self.txtfld34 = ttk.Combobox(window, text="Data",
                                                                     font=("Ariel", 10), values=Data)
                                        self.txtfld34.place(x=550, y=550)
                                        self.txtfld34.set(quantifiers[26])
                                        self.txtfld34.configure(state=DISABLED)

                                        self.lb35 = Label(window, text="Link",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14,
                                                          anchor='e')
                                        self.lb35.place(x=760, y=550)

                                        self.txtfld35 = ttk.Combobox(window,
                                                                     text="Link", state="readonly",
                                                                     font=("Ariel", 10))
                                        self.txtfld35.place(x=890, y=550)

                                        self.txtfld35.set("")
                                        self.txtfld35.configure(state=DISABLED)

                                        def visitrandr():
                                            RR_ID = self.txtfld20.get()
                                            # print(RR_ID)

                                            if RR_ID != "":
                                                # print(RR_ID)
                                                RandR(kc_id=str(self.txtfld1.get()), rr_id=str(self.txtfld20.get()))
                                            else:
                                                RandR(kc_id=str(self.txtfld1.get()), rr_id=0)

                                        def visitcabs():
                                            CABS_ID = self.txtfld30.get()
                                            # print(CABS_ID)

                                            try:
                                                yes_no = str(self.txtfld21.get())
                                                if yes_no == "Não":
                                                    openCapFormat(quantifiers[-1])
                                                else:
                                                    approve = str(self.txtfld22.get())
                                                    if approve == "Aprovado":
                                                        openCapFormat(quantifiers[-1])
                                                    else:
                                                        tk.messagebox.showerror("CREATE RR STUDY",
                                                                                "RR STUDY NOT APPROVED")



                                            except:
                                                pass

                                            # if CABS_ID!="":
                                            #     #print(CABS_ID)
                                            #     cabs(CABS_ID)
                                            # else:
                                            #     tk.messagebox.showerror("CREATE RR STUDY", "RR STUDY NOT CREATED")

                                        def visitcabs2():
                                            try:
                                                CABS_ID = self.txtfld30.get()
                                                cabs(CABS_ID)
                                            except:
                                                cabs_next(quantifiers[0])

                                        self.btn6 = ttk.Button(user_add, text="R&R", style='my.TButton', width=20,
                                                               command=visitrandr)
                                        self.btn6.place(x=460, y=70, width=230, height=70)

                                        self.btn7 = ttk.Button(user_add, text="CAPABILITY", style='my.TButton',
                                                               width=20, command=visitcabs2)
                                        self.btn7.place(x=690, y=70, width=230, height=70)

                                        # self.btn77 = ttk.Button(user_add, text="DELETE", width=20)
                                        # self.btn77.place(x=700, y=700, width=30, height=23)

                                        def excel_sheets():
                                            KC = self.txtfld1.get()
                                            Part_number = self.txtfld2.get()
                                            Rev = self.txtfld3.get()
                                            Centro = self.txtfld4.get()
                                            Kc_Similar = self.txtfld5.get()
                                            Processo = self.txtfld6.get()
                                            Descri = self.txtfld7.get()
                                            Expec = self.txtfld8.get()
                                            Tolerancia = self.txtfld9.get()
                                            Uniade = self.txtfld10.get()
                                            Tipoc = self.txtfld11.get()
                                            Tipod = self.txtfld12.get()
                                            local = self.txtfld13.get()
                                            respq = self.txtfld14.get()
                                            respm = self.txtfld15.get()
                                            produdo = self.txtfld16.get()
                                            proj = self.txtfld17.get()
                                            data = self.txtfld18.get()
                                            status = self.txtfld19.get()

                                            if Tipod == str("Variável"):
                                                if status == str("Máquina"):
                                                    # open F-CQ-311-01-04
                                                    print(Tipod, status)

                                                else:
                                                    # F-CQ-311-01-02
                                                    print(Tipod, status)
                                            if Tipod == str("Atributo"):
                                                # F-CQ-311-01-05
                                                print(Tipod)

                                            if self.txtfld30 != "":
                                                openCapFormat(quantifiers[-1])

                                        def kc_similar():
                                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                                       "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKCmaster] 
                                                        WHERE [Espec#]='""" + str(
                                                self.txtfld8.get()).strip() + """' AND [Tol#]='""" + str(
                                                self.txtfld9.get().strip()) + """'"""

                                            cursor_SQL.execute(query)

                                            # print(query)

                                            kc_similar = ["Não"]

                                            for row in cursor_SQL:
                                                # print(row)
                                                kc_similar.append(row[0])

                                            conn_SQL.close()

                                            kc_similar = set(kc_similar)
                                            # print(kc_similar)

                                            self.txtfld5 = ttk.Combobox(window, text="KC Similar", state="readonly",
                                                                        font=("Ariel", 10), values=list(kc_similar))
                                            self.txtfld5.place(x=890, y=310)

                                        def submit():

                                            MsgBox = tk.messagebox.askquestion('UPDATE KC DATA',
                                                                               'Are you sure you want to update KC DATA Number ' + str(
                                                                                   self.txtfld1.get()),
                                                                               icon='warning')

                                            if MsgBox == 'yes':
                                                KC_dd = self.txtfld1.get()
                                                Part_number = self.txtfld2.get()
                                                Rev = self.txtfld3.get()
                                                Centro = self.txtfld4.get()
                                                Kc_Similar = self.txtfld5.get()
                                                Processo = self.txtfld6.get()
                                                Descri = self.txtfld7.get()
                                                Expec = self.txtfld8.get()
                                                Tolerancia = self.txtfld9.get()
                                                Uniade = self.txtfld10.get()
                                                Tipoc = self.txtfld11.get()
                                                Tipod = self.txtfld12.get()
                                                local = self.txtfld13.get()
                                                respq = self.txtfld14.get()
                                                respm = self.txtfld15.get()
                                                produdo = self.txtfld16.get()
                                                proj = self.txtfld17.get()
                                                data = self.txtfld18.get()
                                                status = self.txtfld19.get()
                                                rr_no = self.txtfld20.get()
                                                yes_no = self.txtfld21.get()
                                                rr_approve = self.txtfld22.get()

                                                cap_no = self.txtfld22.get()
                                                cpx = self.txtfld22.get()
                                                cpkx = self.txtfld22.get()
                                                ppmx = self.txtfld22.get()
                                                datax = self.txtfld22.get()

                                                if ((str(self.txtfld1.get())).strip() != "" and
                                                        (str(self.txtfld2.get())).strip() != "" and
                                                        (str(self.txtfld3.get())).strip() != "" and
                                                        (str(self.txtfld4.get())).strip() != "" and
                                                        (str(self.txtfld5.get())).strip() != "" and
                                                        (str(self.txtfld6.get())).strip() != "" and
                                                        (str(self.txtfld7.get())).strip() != "" and
                                                        (str(self.txtfld8.get())).strip() != "" and (
                                                                str(self.txtfld9.get())).strip() != "" and (
                                                                str(self.txtfld10.get())).strip() != "" and (
                                                                str(self.txtfld11.get())).strip() != ""
                                                        and (str(self.txtfld12.get())).strip() != ""
                                                        and (str(self.txtfld13.get())).strip() != ""
                                                        and (str(self.txtfld14.get())).strip() != ""
                                                        and (str(self.txtfld15.get())).strip() != ""
                                                        and (str(self.txtfld16.get())).strip() != ""
                                                        and (str(self.txtfld17.get())).strip() != ""
                                                        and (str(self.txtfld18.get())).strip() != ""
                                                        and (str(self.txtfld19.get())).strip() != ""
                                                ):

                                                    try:

                                                        conn_SQL = pymssql.connect(
                                                            "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                            "jdaat",
                                                            "jdaat2012", "PU_FA_Testing")
                                                        cursor_SQL = conn_SQL.cursor()

                                                        query = """UPDATE [PU_FA_Testing].[dbo].[KC] 
                SET [# KC] ='""" + str(KC_dd) + """',
                    [Part Number] ='""" + str(Part_number) + """', 
                    [Rev#] ='""" + str(Rev) + """',
                    [KC Similar]= '""" + str(Kc_Similar) + """', 
                    [Centro de Trabalho]='""" + str(Centro) + """', 
                    [Processo] ='""" + str(Processo) + """',
                    [Descrição] ='""" + str(Descri) + """', 
                    [Especificação]= '""" + str(Expec) + """',
                    [Tolerância] ='""" + str(Tolerancia) + """',
                    [Unidade]='""" + str(Uniade) + """',
                    [Tipo de caract#] ='""" + str(Tipoc) + """',
                    [Tipo de dados] ='""" + str(Tipod) + """',
                    [Local de Medição] ='""" + str(local) + """',
                    [Resp# Qualidade] ='""" + str(respq) + """', 
                    [Resp# Manufatura]='""" + str(respm) + """',
                    [Produto]='""" + str(produdo) + """',
                    [Projeto / ECM]= '""" + str(proj) + """',
                    [Data de Impl#] ='""" + str(data) + """',
                    [Status] ='""" + str(status) + """',


                    [R&R Solicitado]='""" + str(yes_no) + """',
                    [# Estudo]='""" + str(rr_no) + """',
                    [Resultado]='""" + str(rr_approve) + """',

                    [# Estudo1]='""" + str(cap_no) + """',
                    [Cp]='""" + str(cpx) + """',
                    [Cpk]='""" + str(cpkx) + """',
                    [PPM]='""" + str(ppmx) + """',
                    [Data]='""" + str(datax) + """'
                    WHERE [# KC] ='""" + str(KC_dd) + """'

                                            """

                                                        print(query)

                                                        cursor_SQL.execute(query)
                                                        conn_SQL.commit()
                                                        cursor_SQL.close()

                                                        # tk.messagebox.showerror("", "WRONG VALUES")

                                                        messagebox.showinfo("Information", "Updated Sucessfully")

                                                        master()

                                                    except:

                                                        messagebox.showerror("Error", "Error")


                                                else:

                                                    messagebox.showwarning("Warning", "Enter Values")


                                            else:
                                                tk.messagebox.showinfo('Information',
                                                                       'You will now return to the KC Master screen')

                                        self.btn_kc_sim_check = ttk.Button(window, text="", command=kc_similar)
                                        self.btn_kc_sim_check.place(x=1060, y=310, width=25, height=23)

                                        def kc_delete():

                                            MsgBox = tk.messagebox.askquestion('DELETE KC ',
                                                                               'Are you sure you want to delete KC NUMBER ' + str(
                                                                                   self.txtfld1.get()),
                                                                               icon='warning')

                                            if MsgBox == 'yes':

                                                conn_SQL = pymssql.connect(
                                                    "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                    "jdaat",
                                                    "jdaat2012", "PU_FA_Testing")
                                                cursor_SQL = conn_SQL.cursor()
                                                query = """DELETE FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC]='""" + str(
                                                    self.txtfld1.get()) + """'"""

                                                print(query)

                                                cursor_SQL.execute(query)

                                                conn_SQL.commit()

                                                conn_SQL.close()

                                                tk.messagebox.showinfo('SUCESS',
                                                                       'DELETED SUCCESFULLY')
                                                master()


                                            else:
                                                tk.messagebox.showinfo('MESSAGE',
                                                                       'You will now return to the master screen')

                                        self.btn_kc_sim_check = ttk.Button(window, text="DELETE", command=kc_delete)
                                        self.btn_kc_sim_check.place(x=1100, y=140, width=50, height=23)
                                        #
                                        # self.btn_rr_check = ttk.Button(window, text="", command=kc_rr)
                                        # self.btn_rr_check.place(x=380, y=480, width=25, height=23)

                                        kc_similar()

                                        # self.btn_cap_check = ttk.Button(window, text="", command=kc_cap)
                                        # self.btn_cap_check.place(x=380, y=520, width=25, height=23)

                                        def next_step_insert():

                                            conn_SQL = pymssql.connect(
                                                "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                "jdaat",
                                                "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """SELECT *  FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL ORDER BY [# KC] DESC"""

                                            cursor_SQL.execute(query)

                                            data = []

                                            for row in cursor_SQL:
                                                # print(row)
                                                data.append([*row])

                                            kc_no = max(
                                                list(map(int, set([data[x][0][3:] for x in range(0, len(data))]))))
                                            kc_no = str("KC_") + ((str("00000") + str(int(kc_no) + 1))[-5:])

                                            self.lb1 = Label(window, text="#KC",
                                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                                            self.lb1.place(x=5, y=140)

                                            self.txtfld1 = ttk.Combobox(window, text="#KC",
                                                                        font=("Ariel", 10))
                                            self.txtfld1.place(x=60, y=140)
                                            self.txtfld1.set(kc_no)
                                            self.txtfld1.config(state=DISABLED)

                                            time.sleep(1)

                                            MsgBox = tk.messagebox.askquestion('INSERT VALUES',
                                                                               'Are you sure you want to insert data to Master List With KC ID ' + str(
                                                                                   self.txtfld1.get()),
                                                                               icon='warning')
                                            if MsgBox == 'yes':

                                                KC_dd = self.txtfld1.get()
                                                Part_number = self.txtfld2.get()
                                                Rev = self.txtfld3.get()
                                                Centro = self.txtfld4.get()
                                                Kc_Similar = self.txtfld5.get()
                                                Processo = self.txtfld6.get()
                                                Descri = self.txtfld7.get()
                                                Expec = self.txtfld8.get()
                                                Tolerancia = self.txtfld9.get()
                                                Uniade = self.txtfld10.get()
                                                Tipoc = self.txtfld11.get()
                                                Tipod = self.txtfld12.get()
                                                local = self.txtfld13.get()
                                                respq = self.txtfld14.get()
                                                respm = self.txtfld15.get()
                                                produdo = self.txtfld16.get()
                                                proj = self.txtfld17.get()
                                                data = self.txtfld18.get()
                                                status = self.txtfld19.get()

                                                yes_no = self.txtfld21.get()

                                                # print(local,Descri)

                                                if ((str(self.txtfld1.get())).strip() != "" and
                                                        (str(self.txtfld2.get())).strip() != "" and
                                                        (str(self.txtfld3.get())).strip() != "" and
                                                        (str(self.txtfld4.get())).strip() != "" and
                                                        (str(self.txtfld5.get())).strip() != "" and
                                                        (str(self.txtfld6.get())).strip() != "" and
                                                        (str(self.txtfld7.get())).strip() != "" and
                                                        (str(self.txtfld8.get())).strip() != "" and (
                                                                str(self.txtfld9.get())).strip() != "" and (
                                                                str(self.txtfld10.get())).strip() != "" and (
                                                                str(self.txtfld11.get())).strip() != ""
                                                        and (str(self.txtfld12.get())).strip() != ""
                                                        and (str(self.txtfld13.get())).strip() != ""
                                                        and (str(self.txtfld14.get())).strip() != ""
                                                        and (str(self.txtfld15.get())).strip() != ""
                                                        and (str(self.txtfld16.get())).strip() != ""
                                                        and (str(self.txtfld17.get())).strip() != ""
                                                        and (str(self.txtfld18.get())).strip() != ""
                                                        and (str(self.txtfld19.get())).strip() != ""
                                                        and (str(self.txtfld21.get())).strip() != ""
                                                ):

                                                    try:

                                                        conn_SQL = pymssql.connect(
                                                            "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                            "jdaat",
                                                            "jdaat2012", "PU_FA_Testing")
                                                        cursor_SQL = conn_SQL.cursor()

                                                        query = """INSERT INTO [PU_FA_Testing].[dbo].[KC] VALUES(
                                                                                            '""" + str(KC_dd) + """',
                                                                                                                         '""" + str(
                                                            Part_number) + """', 
                                                                                                                         '""" + str(
                                                            Rev) + """',
                                                                                                                        '""" + str(
                                                            Kc_Similar) + """', 
                                                                                                                        '""" + str(
                                                            Centro) + """', 
                                                                                                                        '""" + str(
                                                            Processo) + """',
                                                                                                                        '""" + str(
                                                            Descri) + """', 
                                                                                                                        '""" + str(
                                                            Expec) + """',
                                                                                                                        '""" + str(
                                                            Tolerancia) + """',
                                                                                                                   '""" + str(
                                                            Uniade) + """',
                                                                                                                    '""" + str(
                                                            Tipoc) + """',
                                                                                                                   '""" + str(
                                                            Tipod) + """',
                                                                                                                  '""" + str(
                                                            local) + """',
                                                                                                                 '""" + str(
                                                            respq) + """', 
                                                                                                              '""" + str(
                                                            respm) + """',
                                                                                                               '""" + str(
                                                            produdo) + """',
                                                                                                            '""" + str(
                                                            proj) + """',
                                                                                                            '""" + str(
                                                            data) + """',
                                                                                                            '""" + str(
                                                            status) + """','','','""" + str(yes_no) + """','','','','','','','','','','','','','',(SELECT GETDATE())
                                                                                                            )

                                                                                                                        """

                                                        cursor_SQL.execute(query)
                                                        conn_SQL.commit()
                                                        cursor_SQL.close()

                                                        # tk.messagebox.showerror("", "WRONG VALUES")

                                                        messagebox.showinfo("Information", "Added Sucessfully")

                                                        # print(local)

                                                        if Descri == "Torque" or local == "Lab. CMM" or (
                                                                self.txtfld21.get() == "Não"):
                                                            master()
                                                        else:
                                                            RandR(kc_id=str(self.txtfld1.get()), rr_id=0)




                                                    except:

                                                        messagebox.showerror("Error", "Error")


                                                else:

                                                    messagebox.showwarning("Warning", "Enter Values")


                                            else:
                                                tk.messagebox.showinfo('MESSAGE',
                                                                       'You will now return to the master screen')

                                        self.btn_submit = ttk.Button(window, text="INSERT NEW",
                                                                     command=next_step_insert)
                                        self.btn_submit.place(x=550, y=580, width=165, height=40)

                                        self.btn_new_study = ttk.Button(window, text="NEW STUDY", command=visitcabs)
                                        self.btn_new_study.place(x=210, y=580, width=165, height=40)

                                        self.btn_submit = ttk.Button(window, text="UPDATE", command=submit)
                                        self.btn_submit.place(x=890, y=580, width=165, height=40)

                                User_Modify_station(user_add)

                            user_modify_station()

                        frame = Frame(user_add)
                        frame.place(x=0, y=650)

                        # print(data)

                        tree = ttk.Treeview(frame, columns=(
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                            26,
                            27), height=17, show="headings")

                        tree.pack(side='left')
                        tree.bind('<ButtonRelease-1>', selectItem)

                        if id_master != 0:
                            selectItem(a=id_master)

                        val = ["# KC", "Part Number", "Rev.", "KC Similar", "Centro de Trabalho",
                               "Processo", "Descrição", "Especificação",
                               "Tolerância", "Unidade", "Tipo de caract.", "Tipo de dados", "Local de Medição",
                               "Resp. Qualidade", "Resp. Manufatura", "Produto", "Projeto / ECM",
                               "Data de Impl.", "Status", "R&R Solicitado", "# Estudo", "Resultado", "# Estudo", "Cp",
                               "Cpk", "PPM", "Data"]

                        for i in range(1, len(val) + 1):
                            tree.heading(i, text=val[i - 1])

                        # tree.heading(2, text="Column 2")
                        # tree.heading(3, text="Column 3")

                        for i in range(1, len(val)):
                            tree.column(i, width=70, anchor='center')

                        tree.column(27, width=80, anchor='center')

                        # tree.column(2, width=100)
                        # tree.column(3, width=100)

                        scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
                        scroll.pack(side='right', fill='y')

                        """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
                        scrollx.pack(side='bottom', fill='x')"""

                        tree.configure(yscrollcommand=scroll.set)

                        iterx = 0
                        for valx in data:
                            tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                           , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                           , valx[10], valx[11], valx[12], valx[13], valx[14]
                                                           , valx[15], valx[16], valx[17], valx[18], valx[21], valx[22],
                                                           valx[23],
                                                           valx[25], valx[26]
                                                           , valx[27], valx[28], valx[29]),
                                        tags=(str(valx[18]),))

                            iterx += 1

                        tree.tag_configure('EPDP', background='#FFF9CC')
                        tree.tag_configure('Máquina', background='#99CCFF')
                        tree.tag_configure('OFP', background='#99CCFF')
                        tree.tag_configure('Eliminada', background='#FF9999')
                        tree.tag_configure('Passivo', background='#D9D9D9')
                        tree.tag_configure('Obsoleto', background='#A6A6A6')

                        conn_SQL.close()

                        def command(x=0):
                            destroy = x

                            var0 = ""
                            var1 = ""
                            var2 = ""
                            var3 = ""
                            var4 = ""
                            var5 = ""
                            var6 = ""
                            var7 = ""
                            var8 = ""
                            var9 = ""
                            var10 = ""
                            var11 = ""
                            var12 = ""
                            var13 = ""
                            var14 = ""
                            var15 = ""
                            var16 = ""
                            var17 = ""
                            var18 = ""
                            var19 = ""
                            var20 = ""
                            var21 = ""
                            var22 = ""
                            var23 = ""
                            var24 = ""
                            var25 = ""
                            var26 = ""

                            # "# KC", "Part Number", "Rev.", "KC Similar", "Centro de Trabalho",
                            # "Processo", "Descrição", "Especificação",
                            # "Tolerância", "Unidade", "Tipo de caract.", "Tipo de dados", "Local de Medição",
                            # "Resp. Qualidade", "Resp. Manufatura", "Produto", "Projeto / ECM",
                            # "Data de Impl.", "Status", "R&R Solicitado", "# Estudo", "Resultado", "# Estudo", "Cp", "Cpk", "PPM", "Data"

                            if (self.tkvar0.get()) != '# KC':
                                var0 = self.tkvar0.get()
                            if (self.tkvar1.get()) != 'Part Number':
                                var1 = self.tkvar1.get()
                            if (self.tkvar2.get()) != 'Rev.':
                                var2 = self.tkvar2.get()
                            if (self.tkvar3.get()) != 'KC Similar':
                                var3 = self.tkvar3.get()
                            if (self.tkvar4.get()) != 'Centro de Trabalho':
                                var4 = self.tkvar4.get()
                            if (self.tkvar5.get()) != 'Processo':
                                var5 = self.tkvar5.get()
                            if (self.tkvar6.get()) != 'Descrição':
                                var6 = self.tkvar6.get()
                            if (self.tkvar7.get()) != 'Especificação':
                                var7 = self.tkvar7.get()
                            if (self.tkvar8.get()) != 'Tolerância':
                                var8 = self.tkvar7.get()
                            if (self.tkvar9.get()) != 'Unidade':
                                var9 = self.tkvar9.get()
                            if (self.tkvar10.get()) != 'Tipo de caract.':
                                var10 = self.tkvar10.get()
                            if (self.tkvar11.get()) != 'Tipo de dados':
                                var11 = self.tkvar11.get()
                            if (self.tkvar12.get()) != 'Local de Medição':
                                var12 = self.tkvar12.get()
                            if (self.tkvar13.get()) != 'Resp. Qualidade':
                                var13 = self.tkvar13.get()
                            if (self.tkvar14.get()) != 'Resp. Manufatura':
                                var14 = self.tkvar14.get()
                            if (self.tkvar15.get()) != 'Produto':
                                var15 = self.tkvar15.get()
                            if (self.tkvar16.get()) != 'Projeto / ECM':
                                var16 = self.tkvar16.get()
                            if (self.tkvar17.get()) != 'Data de Impl.':
                                var17 = self.tkvar17.get()
                            if (self.tkvar18.get()) != 'Status':
                                var18 = self.tkvar18.get()
                            if (self.tkvar19.get()) != 'R&R Solicitado':
                                var19 = self.tkvar19.get()
                            if (self.tkvar20.get()) != '# Estudo':
                                var20 = self.tkvar20.get()
                            if (self.tkvar21.get()) != 'Resultado':
                                var21 = self.tkvar21.get()
                            if (self.tkvar22.get()) != '# Estudo':
                                var22 = self.tkvar22.get()
                            if (self.tkvar23.get()) != 'Cp':
                                var23 = self.tkvar23.get()
                            if (self.tkvar24.get()) != 'Cpk':
                                var24 = self.tkvar24.get()
                            if (self.tkvar25.get()) != 'PPM':
                                var25 = self.tkvar25.get()
                            # if (self.tkvar26.get())!='Data':
                            #     var26=self.tkvar26.get()

                            # print(var0,var1,var2,var3,var4,var5,var6)

                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                       "jdaat2012", "PU_FA_Testing")
                            cursor_SQL = conn_SQL.cursor()

                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] LIKE '%""" + str(var0) + """%' 
                                        AND ([Part Number] LIKE '%""" + str(var1) + """%' OR [Part Number] is NULL) 
                                        AND ([Rev#] LIKE '%""" + str(var2) + """%' OR [Rev#] is NULL) AND
                                        ([KC Similar] LIKE '%""" + str(var3) + """%'  OR [KC Similar] is NULL) AND 
                                                            ([Centro de Trabalho] LIKE '%""" + str(var4) + """%' OR [Centro de Trabalho] is NULL) AND 
                                        ([Processo] LIKE '%""" + str(var5) + """%'  OR [Processo] is NULL) AND 
                                                            ([Descrição] LIKE '%""" + str(var6) + """%'  OR [Descrição] is NULL) AND 
                                                            ([Especificação] LIKE '%""" + str(var7) + """%'  OR [Especificação] is NULL) AND 
                                                            ([Tolerância] LIKE '%""" + str(var8) + """%' OR [Tolerância] is NULL) AND 
                                                            ([Unidade] LIKE '%""" + str(var9) + """%' OR [Unidade] is NULL) AND 
                                                            ([Tipo de caract#] LIKE '%""" + str(var10) + """%' OR [Tipo de caract#] is NULL) AND 
                                                            ([Tipo de dados] LIKE '%""" + str(var11) + """%' OR [Tipo de dados] is NULL) AND 
                                                            ([Local de Medição] LIKE '%""" + str(var12) + """%' OR [Local de Medição] is NULL) AND 
                                                            ([Resp# Qualidade] LIKE '%""" + str(var13) + """%' OR [Resp# Qualidade] is NULL) AND 
                                                            ([Resp# Manufatura] LIKE '%""" + str(var14) + """%' OR [Resp# Manufatura] is NULL) AND 
                                                            ([Produto] LIKE '%""" + str(var15) + """%' OR [Produto] is NULL) AND 
                                                            ([Projeto / ECM] LIKE '%""" + str(var16) + """%' OR [Projeto / ECM] is NULL) AND 
                                                            ([Data de Impl#] LIKE '%""" + str(var17) + """%' OR [Data de Impl#] is NULL) AND 
                                                            ([Status] LIKE '%""" + str(var18) + """%' OR [Status] is NULL)  AND 
                                                            ([R&R Solicitado] LIKE '%""" + str(var19) + """%' OR [R&R Solicitado] is NULL) AND 
                                                            ([# Estudo] LIKE '%""" + str(var20) + """%' OR [# Estudo] is NULL) AND 
                                                            ([Resultado] LIKE '%""" + str(var21) + """%' OR [Resultado] is NULL) AND 
                                                            ([Link1] LIKE '%%' OR [Link1] is NULL) AND 
                                                            ([# Estudo1] LIKE '%""" + str(var22) + """%' OR [# Estudo1] is NULL) AND 
                                                            ([Cp] LIKE '%""" + str(var23) + """%' OR [Cp] is NULL) AND 
                                                            ([Cpk] LIKE '%""" + str(var24) + """%' OR [Cpk] is NULL) AND 
                                                            ([PPM] LIKE '%""" + str(var25) + """%' OR [PPM] is NULL) AND 
                                                            ([Data] LIKE '%%' OR [Data] is NULL) AND 
                                                            ([Link2] LIKE '%%' OR [Link2] is NULL)

                                                  """

                            # query="""SELECT * FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL AND [# KC] LIKE '%""" + str(var0) + """%'
                            # AND [Part Number] LIKE '%""" + str(var1) + """%' AND [Rev#] LIKE '%""" + str(var2) + """%' AND
                            # [KC Similar] LIKE '%""" + str(var3) + """%' AND [Centro de Trabalho] LIKE '%""" + str(var4) + """%' AND
                            # [Processo] LIKE '%""" + str(var5) + """%' AND [Descrição] LIKE '%""" + str(var6) + """%'
                            # AND [Especificação] LIKE '%""" + str(var7) + """%' AND [Tolerância] LIKE '%""" + str(var8) + """%'
                            # AND [Unidade] LIKE '%""" + str(var9) + """%'
                            # AND [Tipo de caract#] LIKE '%""" + str(var10) + """%' AND [Tipo de dados] LIKE '%""" + str(var11) + """%'
                            # AND [Local de Medição] LIKE '%""" + str(var12) + """%' AND [Resp# Qualidade] LIKE '%""" + str(var13) + """%'
                            # AND [Resp# Manufatura] LIKE '%""" + str(var14) + """%' AND [Produto] LIKE '%""" + str(var15) + """%'
                            # AND [Projeto / ECM] LIKE '%""" + str(var16) + """%' AND [Data de Impl#] LIKE '%""" + str(var17) + """%'
                            # AND [Status] LIKE '%""" + str(var18) + """%'
                            # AND [R&R Solicitado] LIKE '%""" + str(var19) + """%' AND [# Estudo] LIKE '%""" + str(var20) + """%' AND [Resultado] LIKE '%""" + str(var21) + """%' AND [Link1] LIKE '%%'
                            # AND [# Estudo1] LIKE '%""" + str(var22) + """%' AND [Cp] LIKE '%""" + str(var23) + """%' AND [Cpk] LIKE '%""" + str(var24) + """%' AND [PPM] LIKE '%""" + str(var25) + """%' AND [Data] LIKE '%%' AND [Link2] LIKE '%%'
                            # ORDER BY [# KC] DESC
                            #
                            # """

                            for row in tree.get_children():
                                tree.delete(row)

                            cursor_SQL.execute(query)

                            data = []

                            for row in cursor_SQL:
                                # print(row)
                                data.append([*row])

                            conn_SQL.close()

                            for row in tree.get_children():
                                tree.delete(row)

                            tree.configure(yscrollcommand=scroll.set)

                            iterx = 0
                            for valx in data:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                               , valx[10], valx[11], valx[12], valx[13], valx[14]
                                                               , valx[15], valx[16], valx[17], valx[18], valx[21],
                                                               valx[22], valx[23],
                                                               valx[25], valx[26]
                                                               , valx[27], valx[28], valx[29]),
                                            tags=(str(valx[18]),))

                                iterx += 1

                            tree.tag_configure('EPDP', background='#FFF9CC')
                            tree.tag_configure('Máquina', background='#99CCFF')
                            tree.tag_configure('OFP', background='#99CCFF')
                            tree.tag_configure('Eliminada', background='#FF9999')
                            tree.tag_configure('Passivo', background='#D9D9D9')
                            tree.tag_configure('Obsoleto', background='#A6A6A6')

                            conn_SQL.close()

                        # "# KC", "Part Number", "Rev.", "KC Similar", "Centro de Trabalho",
                        # "Processo", "Descrição", "Especificação",
                        # "Tolerância", "Unidade", "Tipo de caract.", "Tipo de dados", "Local de Medição",
                        # "Resp. Qualidade", "Resp. Manufatura", "Produto", "Projeto / ECM",
                        # "Data de Impl.", "Status", "R&R Solicitado", "# Estudo", "Resultado", "# Estudo", "Cp", "Cpk", "PPM", "Data"

                        self.tkvarbtn0 = ttk.Button(window, text="", width=450)
                        self.tkvarbtn0.place(x=0, y=625, height=30)

                        self.tkvar0 = ttk.Combobox(window, text="tkvar0",
                                                   font=("Ariel", 8), values=list(
                                set([data[x][0] for x in range(0, len(data))])), width=8, justify='center')
                        self.tkvar0.place(x=0, y=630, )
                        self.tkvar0.set("# KC")

                        self.tkvar0.bind("<<ComboboxSelected>>", command)

                        self.tkvar1 = ttk.Combobox(window, text="tkvar1",
                                                   font=("Ariel", 8), values=Part_Number, width=8, justify='center')
                        self.tkvar1.place(x=70, y=630)
                        self.tkvar1.set("Part Number")
                        self.tkvar1.bind("<<ComboboxSelected>>", command)

                        self.tkvar2 = ttk.Combobox(window, text="tkvar2",
                                                   font=("Ariel", 8), values=Rev, width=8, justify='center')
                        self.tkvar2.place(x=140, y=630)
                        self.tkvar2.set("Rev.")

                        self.tkvar2.bind("<<ComboboxSelected>>", command)

                        self.tkvar3 = ttk.Combobox(window, text="tkvar3",
                                                   font=("Ariel", 8), values=KC_Similar, width=8, justify='center')
                        self.tkvar3.place(x=210, y=630)
                        self.tkvar3.set("KC Similar")

                        self.tkvar3.bind("<<ComboboxSelected>>", command)

                        self.tkvar4 = ttk.Combobox(window, text="tkvar4",
                                                   font=("Ariel", 8), values=Centro_de_Trabalho, width=8,
                                                   justify='center')
                        self.tkvar4.place(x=280, y=630)
                        self.tkvar4.set("Centro de Trabalho")

                        self.tkvar4.bind("<<ComboboxSelected>>", command)

                        self.tkvar5 = ttk.Combobox(window, text="tkvar5",
                                                   font=("Ariel", 8), values=Processo, width=8, justify='center')
                        self.tkvar5.place(x=350, y=630)
                        self.tkvar5.set("Processo")

                        self.tkvar5.bind("<<ComboboxSelected>>", command)

                        self.tkvar6 = ttk.Combobox(window, text="tkvar6",
                                                   font=("Ariel", 8), values=Descrição, width=8, justify='center')
                        self.tkvar6.place(x=420, y=630)
                        self.tkvar6.set("Descrição")
                        self.tkvar6.bind("<<ComboboxSelected>>", command)

                        self.tkvar7 = ttk.Combobox(window, text="tkvar7",
                                                   font=("Ariel", 8), values=Especificação, width=8, justify='center')
                        self.tkvar7.place(x=490, y=630)
                        self.tkvar7.set("Especificação")
                        self.tkvar7.bind("<<ComboboxSelected>>", command)

                        self.tkvar8 = ttk.Combobox(window, text="tkvar8",
                                                   font=("Ariel", 8), values=Tolerância, width=8, justify='center')
                        self.tkvar8.place(x=560, y=630)
                        self.tkvar8.set("Tolerância")
                        self.tkvar8.bind("<<ComboboxSelected>>", command)

                        self.tkvar9 = ttk.Combobox(window, text="tkvar9",
                                                   font=("Ariel", 8), values=Unidade, width=8, justify='center')
                        self.tkvar9.place(x=630, y=630)
                        self.tkvar9.set("Unidade")
                        self.tkvar9.bind("<<ComboboxSelected>>", command)

                        self.tkvar10 = ttk.Combobox(window, text="tkvar10",
                                                    font=("Ariel", 8), values=Tipo_de_caract, width=8, justify='center')
                        self.tkvar10.place(x=700, y=630)
                        self.tkvar10.set("Tipo de caract.")
                        self.tkvar10.bind("<<ComboboxSelected>>", command)

                        self.tkvar11 = ttk.Combobox(window, text="tkvar11",
                                                    font=("Ariel", 8), values=Tipo_de_dados, width=8, justify='center')
                        self.tkvar11.place(x=770, y=630)
                        self.tkvar11.set("Tipo de dados")
                        self.tkvar11.bind("<<ComboboxSelected>>", command)

                        self.tkvar12 = ttk.Combobox(window, text="tkvar12",
                                                    font=("Ariel", 8), values=Local_de_Medição, width=8,
                                                    justify='center')
                        self.tkvar12.place(x=840, y=630)
                        self.tkvar12.set("Local de Medição")
                        self.tkvar12.bind("<<ComboboxSelected>>", command)

                        self.tkvar13 = ttk.Combobox(window, text="tkvar13",
                                                    font=("Ariel", 8), values=Resp_Qualidade, width=8, justify='center')
                        self.tkvar13.place(x=910, y=630)
                        self.tkvar13.set("Resp. Qualidade")
                        self.tkvar13.bind("<<ComboboxSelected>>", command)

                        self.tkvar14 = ttk.Combobox(window, text="tkvar14",
                                                    font=("Ariel", 8), values=Resp_Manufatura, width=8,
                                                    justify='center')
                        self.tkvar14.place(x=980, y=630)
                        self.tkvar14.set("Resp. Manufatura")
                        self.tkvar14.bind("<<ComboboxSelected>>", command)

                        self.tkvar15 = ttk.Combobox(window, text="tkvar15",
                                                    font=("Ariel", 8), values=Produto, width=8, justify='center')
                        self.tkvar15.place(x=1050, y=630)
                        self.tkvar15.set("Produto")
                        self.tkvar15.bind("<<ComboboxSelected>>", command)

                        self.tkvar16 = ttk.Combobox(window, text="tkvar16",
                                                    font=("Ariel", 8), values=Projeto_ECM, width=8, justify='center')
                        self.tkvar16.place(x=1120, y=630)
                        self.tkvar16.set("Projeto / ECM")
                        self.tkvar16.bind("<<ComboboxSelected>>", command)

                        self.tkvar17 = ttk.Combobox(window, text="tkvar17",
                                                    font=("Ariel", 8), values=Data_de_Impl, width=8, justify='center')
                        self.tkvar17.place(x=1190, y=630)
                        self.tkvar17.set("Data de Impl.")
                        self.tkvar17.bind("<<ComboboxSelected>>", command)

                        self.tkvar18 = ttk.Combobox(window, text="tkvar18",
                                                    font=("Ariel", 8), values=Status, width=8, justify='center')
                        self.tkvar18.place(x=1260, y=630)
                        self.tkvar18.set("Status")
                        self.tkvar18.bind("<<ComboboxSelected>>", command)

                        self.tkvar19 = ttk.Combobox(window, text="tkvar19",
                                                    font=("Ariel", 8), values=RRSolicitado, width=8, justify='center')
                        self.tkvar19.place(x=1330, y=630)
                        self.tkvar19.set("R&R Solicitado")
                        self.tkvar19.bind("<<ComboboxSelected>>", command)

                        self.tkvar20 = ttk.Combobox(window, text="tkvar20",
                                                    font=("Ariel", 8), values=Estudo_rr, width=8, justify='center')
                        self.tkvar20.place(x=1400, y=630)
                        self.tkvar20.set("# Estudo")
                        self.tkvar20.bind("<<ComboboxSelected>>", command)

                        self.tkvar21 = ttk.Combobox(window, text="tkvar21",
                                                    font=("Ariel", 8), values=Resultado, width=8, justify='center')
                        self.tkvar21.place(x=1470, y=630)
                        self.tkvar21.set("Resultado")
                        self.tkvar21.bind("<<ComboboxSelected>>", command)

                        self.tkvar22 = ttk.Combobox(window, text="tkvar22",
                                                    font=("Ariel", 8), values=Estudo_cap, width=8, justify='center')
                        self.tkvar22.place(x=1540, y=630)
                        self.tkvar22.set("# Estudo")
                        self.tkvar22.bind("<<ComboboxSelected>>", command)

                        self.tkvar23 = ttk.Combobox(window, text="tkvar23",
                                                    font=("Ariel", 8), values=Cp, width=8, justify='center')
                        self.tkvar23.place(x=1610, y=630)
                        self.tkvar23.set("Cp")
                        self.tkvar23.bind("<<ComboboxSelected>>", command)

                        self.tkvar24 = ttk.Combobox(window, text="tkvar24",
                                                    font=("Ariel", 8), values=Cpk, width=8, justify='center')
                        self.tkvar24.place(x=1680, y=630)
                        self.tkvar24.set("Cpk")
                        self.tkvar24.bind("<<ComboboxSelected>>", command)

                        self.tkvar25 = ttk.Combobox(window, text="tkvar25",
                                                    font=("Ariel", 8), values=PPM, width=8, justify='center')
                        self.tkvar25.place(x=1750, y=630)
                        self.tkvar25.set("PPM")
                        self.tkvar25.bind("<<ComboboxSelected>>", command)

                        self.tkvarbtn1 = ttk.Button(window, text="SEARCH", width=17, command=command)
                        self.tkvarbtn1.place(x=1820, y=628)



                a = App()



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

            # if ((str(self.txtfld4.get()) != "")):
            #
            #     d2 = (str(self.txtfld4.get()))
            #
            # else:
            #
            #     messagebox.showwarning("Warning", "Missing Total Bottle Field")
            #     return (0)

            # try:
            #     temp = int((self.txtfld4.get()))
            #     d2 = (str(self.txtfld4.get()))
            #
            #
            #
            #
            #
            #
            # except:
            #     messagebox.showwarning("Warning", "Total Bottle field must be numeric")
            #     return (0)




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