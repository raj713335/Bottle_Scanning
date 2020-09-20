# https://svn-in.deere.com/svn/TCI_Emb_Group5_Projects/P0107_KC_Automation 

from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter import filedialog
from openpyxl import *

from tkinter import Entry, Frame, Label, StringVar
from tkinter.constants import *
from tkinter.messagebox import showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import pymssql
from openpyxl import *
from datetime import datetime
import os
import time
import xlwings as xw

from datetime import date
from datetime import timedelta

# def next(window):
#
#     #MICROSOFT SQL COMMAND TO ADD OR UPDATE TABLE IN KEY CHARACTERISTICS
#     print("HELLO")

plannedData = []
actualData = []
rrData = []
capabilityData = []
barwidth = 0.5
currentDate = datetime.now()


def user_add_kc():
    # CLASS FOR ADDING STATION

    class user_add_kc():

        def __init__(self, window):

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            shop_floor_canvax = tk.Canvas(window, width=screen_width, height=screen_height, background='white')
            shop_floor_canvax.grid(row=0, column=0)
            shop_floor_canvax.create_line((screen_width // 1.5), 0, (screen_width // 1.5), 750, fill='grey', width=3)
            shop_floor_canvax.create_line(-1, 71, screen_width, 71, fill='grey', width=3)

            load = cv2.imread('Images/header.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(1920), int(70)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)

            """load = cv2.imread('load.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(127), int(66)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=1790, y=0)"""

            # load = cv2.imread('background.png', 1)
            # cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            # load = Image.fromarray(cv2imagex1)
            # # load = load.resize((int(870), int(66)), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            # img = tk.Label(image=render)
            # img.image = render
            # img.place(x=0, y=70)

            """
            # COMMENTED FUNCTION FOR PLAYING VIDEO
            app = tk.Frame(window, bg="white")
            app.grid()
            # Create a label in the frame
            lmain = tk.Label(app)
            lmain.grid()

            # Capture from video File
            cap = cv2.VideoCapture('John Deere.mp4')

            # function for video streaming
            def video_stream():
                if (cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES)):
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                _, frame = cap.read()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                im5 = img.resize((int(1300), int(660)), Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=im5)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(1, video_stream)

            lmain = tk.Label(window, font=('Arial', int(1 * 3.5)), fg="black", bg='white',
                             anchor='center')
            lmain.place(x=0, y=70)
            video_stream()"""

            load = cv2.imread('IMAGES/start.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=0, y=70)

            def image_loader(image_pathx="0"):

                if image_pathx == "0":
                    image_path = 'rusty.jpg'
                else:
                    image_path = '//Gnpunnas1b/Temporary/Shubhashish/KC_Images/' + str(image_pathx) + '.png'

                try:
                    load = cv2.imread(image_path, 1)
                    cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                    load = Image.fromarray(cv2imagex1)
                    load = load.resize((int(765), int(357)), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(image=render)
                    img.image = render
                    img.place(x=1150, y=140)
                except:
                    load = cv2.imread('Images/rusty.jpg', 1)
                    cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                    load = Image.fromarray(cv2imagex1)
                    load = load.resize((int(765), int(357)), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(image=render)
                    img.image = render
                    img.place(x=1150, y=140)

            def image_loader_gkc(image_pathx="0"):

                if image_pathx == "0":
                    image_path = 'rusty.jpg'
                else:
                    image_path = '//Gnpunnas1b/Temporary/Shubhashish/KC_Images/' + str(image_pathx) + '.png'

                try:
                    load = cv2.imread(image_path, 1)
                    cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                    load = Image.fromarray(cv2imagex1)
                    load = load.resize((int(765), int(480)), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(image=render)
                    img.image = render
                    img.place(x=1150, y=140)
                except:
                    load = cv2.imread('Images/rusty.jpg', 1)
                    cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                    load = Image.fromarray(cv2imagex1)
                    load = load.resize((int(765), int(480)), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(image=render)
                    img.image = render
                    img.place(x=1150, y=140)

            # image_loader()

            def getvaluefromcap(CapNumber, kcid):
                resultCP = 0
                resultCPK = 0
                resultPPM = 0
                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()
                cursor_SQL2 = conn_SQL.cursor()
                query = """SELECT "Status", "KCData_Type","Group_KC" FROM KEY_CHARACTERISTICS WHERE "KC_Id" = %s """
                cursor_SQL.execute(query, kcid)
                kcdata = cursor_SQL.fetchone()
                cursor_SQL.close()

                kc_status = kcdata[0]
                kc_datatype = kcdata[1]
                gkc_no = kcdata[2]
                if (kc_datatype == 'Variável') & (kc_status == 'Máquina'):
                    loc = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + CapNumber + (
                        ".xlsx")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Dados']
                    resultCP = sheet.range('Z63').value
                    resultCPK = sheet.range('AD63').value
                elif (kc_datatype == 'Variável') & (kc_status != 'Máquina'):
                    loc = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + CapNumber + (
                        ".xlsm")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Dados']
                    resultCP = sheet.range('V59').value
                    resultCPK = sheet.range('Y61').value
                    resultPPM = sheet.range('V61').value
                elif (kc_datatype == 'Atributo'):
                    loc = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + CapNumber + (
                        ".xlsx")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Estudo de Capabilidade Atributo']
                    resultPPM = sheet.range('C73').value
                query2 = """UPDATE [CAPABILITY_STUDY] SET [CP] = '""" + str(resultCP) + """',[CPK]= '""" + str(
                    resultCPK) + """',[PPM]= '""" + str(resultPPM) + """' WHERE  [Cap_Study] ='""" + str(
                    CapNumber) + """' """
                cursor_SQL2.execute(query2)
                conn_SQL.commit()
                cursor_SQL.close()
                print(resultCPK, resultCP, resultPPM)
                return resultCPK, resultCP, resultPPM

            # a, b, c = getvaluefromcap('EC_00854', 'Atributo', 'Máquina')
            # print(a, b, c)
            # getvaluefromcap('EC_00854', 'Atributo', 'Máquina')

            def openCapFormat(kcid):
                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()
                cursor_SQL2 = conn_SQL.cursor()
                cursor_SQL3 = conn_SQL.cursor()
                cursor_SQL4 = conn_SQL.cursor()
                # query = """SELECT * FROM KEY_CHARACTERISTICS WHERE KC_ID=%s"""
                # query = """SELECT keys.[KC_No],keys.[Part_No],keys.[Responsible_QE],keys.[Responsible_ME],keys.[Revision],keys.[KC_Id],
                #             cap.[Cap_Study],cap.[Capability_Id],keys.[Status],keys.[KCData_Type],keys.[WorkCenter]
                #             FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] as keys
                #             LEFT JOIN  [PU_FA_Testing].[dbo].[CAPABILITY_STUDY] as cap
                #             ON keys.[KC_ID]=cap.[KC_ID]
                #             WHERE keys.[KC_ID]=%s"""
                query = """SELECT "KC_No","Part_No","Responsible_QE","Responsible_ME","Revision","KC_Id","Status","KCData_Type","WorkCenter","Process","Specification",
                            "Tolerance","Unit","Group_KC"
                            FROM KEY_CHARACTERISTICS
                            WHERE "KC_ID" = %s"""
                query2 = """SELECT TOP 1 TRY_CONVERT(int,RIGHT("Cap_Study", LEN("Cap_Study")-3)),"Capability_Id"  
                            FROM CAPABILITY_STUDY ORDER BY TRY_CONVERT(int,RIGHT("Cap_Study", LEN("Cap_Study")-3)) desc"""

                cursor_SQL.execute(query, kcid)
                kcdata = cursor_SQL.fetchone()
                cursor_SQL2.execute(query2)
                capadata = cursor_SQL2.fetchone()

                cap_no = str("EC_") + ((str("000000") + str(capadata[0] + 1))[-6:])
                # cap_no = 'EC_' + str(capadata[0] + 1)
                kc_no = kcdata[0]
                part_no = kcdata[1]
                me_name = kcdata[3]
                qe_name = kcdata[2]
                rev = kcdata[4]
                kc_id = kcdata[5]
                # cap_no = kcdata[6]
                # cap_id = kcdata[7]
                kc_status = kcdata[6]
                kc_datatype = kcdata[7]
                workstation = kcdata[8]
                process = kcdata[9]
                specification = kcdata[10]
                tolerence = kcdata[11]
                unit = kcdata[12]
                gkc_no = kcdata[13]
                cursor_SQL4.execute(
                    """SELECT [GKC_ID] FROM [PU_FA_Testing].[dbo].[GKC_Master] WHERE [GKC_Num]='""" + (
                        str(gkc_no)) + """"'""")
                gkcid = cursor_SQL4.fetchone()
                if gkcid == None:
                    gkcid = 0
                print(gkcid)
                presentdate = datetime.today()
                if kc_status == 'Máquina':
                    enddate = datetime.today() + timedelta(days=365)
                else:
                    enddate = datetime.today() + timedelta(days=730)
                empty = "-"
                query3 = """INSERT INTO [PU_FA_Testing].[dbo].[CAPABILITY_STUDY]([KC_Id],[Cap_Study],[Item],[Process],[Specification],[Tolerance],[Unit],[Cap_StudyDate],[Cap_NextStudyDate]
                            ,[CP],[CPK],[PPM],[Link],[GKC_Id],[Cap_Study_By]) VALUES(
                            '""" + str(kc_id) + """','""" + str(cap_no) + """','""" + str(part_no) + """','""" + str(
                    process) + """','""" + str(specification) + """','""" + str(tolerence) + """',
                            '""" + str(unit) + """','""" + str(presentdate.strftime('%m-%d-%Y')) + """','""" + str(
                    enddate.strftime('%m-%d-%Y')) + """','""" + str(empty) + """','""" + str(empty) + """','""" + str(
                    empty) + """','""" + str(empty) + """','""" + (str(gkcid)) + """','""" + str(empty) + """')"""
                cursor_SQL3.execute(query3)
                conn_SQL.commit()
                if kc_datatype == 'Variável':

                    if kc_status == 'Máquina':
                        # open F-CQ-311-01-04
                        loc = (r"excel\F-CQ-311-01-04.xlsx")
                        wb = xw.Book(loc)
                        sheet = wb.sheets['Dados']
                        sheet.range('D5').value = cap_no
                        sheet.range('D6').value = workstation
                        sheet.range('D7').value = datetime.today().strftime('%m-%d-%Y')
                        sheet.range('D9').value = kc_no
                        sheet.range('L5').value = me_name
                        sheet.range('L6').value = qe_name
                        # wb.save(loc)
                        # os.system('start excel.exe F-CQ-311-01-04.xlsx')
                        savepath = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + cap_no
                        wb.save(savepath)
                        print(kc_datatype, kc_status)
                    else:
                        # F-CQ-311-01-02
                        loc = (r"excel\F-CQ-311-01-02.xlsm")
                        wb = xw.Book(loc)
                        # wb=load_workbook(filename = 'F-CQ-311-01-02.xlsm', read_only = False, keep_vba = True)
                        sheet = wb.sheets['Dados']
                        sheet.range('D5').value = cap_no
                        sheet.range('D6').value = part_no
                        sheet.range('D7').value = rev
                        sheet.range('D8').value = datetime.today().strftime('%m-%d-%Y')
                        sheet.range('D9').value = kc_no
                        sheet.range('N7').value = me_name
                        sheet.range('N8').value = qe_name
                        # wb.save(loc)
                        # os.system('start excel.exe F-CQ-311-01-02.xlsm')
                        savepath = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + cap_no
                        wb.save(savepath)
                        print(kc_datatype, kc_status)

                if kc_datatype == 'Atributo':
                    # F-CQ-311-01-05
                    loc = (r"excel\F-CQ-311-01-05.xlsx")
                    # loc = (r"F-CQ-311-01-05.xlsx")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Estudo de Capabilidade Atributo']
                    # sheet = wb.active
                    sheet.range('D5').value = cap_no
                    sheet.range('D6').value = part_no
                    sheet.range('D7').value = rev
                    sheet.range('D8').value = datetime.today().strftime('%m-%d-%Y')
                    sheet.range('D9').value = kc_no
                    sheet.range('Y7').value = me_name
                    sheet.range('Y8').value = qe_name
                    savepath = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\capability\ ") + cap_no
                    wb.save(savepath)

            def next_randr_new(kc_rr=0, kc_cap=0):
                if kc_rr != 0:
                    RandR_next(kc_rr)

            def dashboard():

                global important_variable
                important_variable = 0

                load = cv2.imread('Images/background.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()  # for Planned Plot
                cursor_SQL2 = conn_SQL.cursor()  # for Plan vs Actual Plot
                cursor_SQL3 = conn_SQL.cursor()  # forR&R Comparison
                cursor_SQL4 = conn_SQL.cursor()  # for CPK Comparison
                # cursor_SQL5 = conn_SQL.cursor()     # For drop down list
                # Query to filter out KC by month - Due Date
                query = """SELECT COUNT("KC_Id"),MONTH(CONVERT(date,"Cap_NextStudyDate",105)),LEFT(DATENAME(month,CONVERT(date,"Cap_NextStudyDate",105)),3) 
                                                            FROM CAPABILITY_STUDY WHERE YEAR(CONVERT(date,"Cap_NextStudyDate",105)) = %s
                                                            GROUP BY MONTH(CONVERT(date,"Cap_NextStudyDate",105)),DATENAME(month,CONVERT(date,"Cap_NextStudyDate",105)) 
                                                            ORDER BY MONTH(CONVERT(date,"Cap_NextStudyDate",105))"""
                # Query to filter outKC by month - Created
                query2 = """SELECT COUNT("KC_Id"),MONTH(CONVERT(date,"Cap_StudyDate",105)),LEFT(DATENAME(month,CONVERT(date,"Cap_StudyDate",105)),3) 
                                                            FROM CAPABILITY_STUDY WHERE YEAR(CONVERT(date,"Cap_StudyDate",105)) = %s
                                                            GROUP BY MONTH(CONVERT(date,"Cap_StudyDate",105)),DATENAME(month,CONVERT(date,"Cap_StudyDate",105)) 
                                                            ORDER BY MONTH(CONVERT(date,"Cap_StudyDate",105))"""
                # Query to filter out R&R Values
                # query3 = """SELECT COUNT(RR_STUDY_No) FROM RR_STUDY WHERE (CONVERT(float,LEFT("RR",LEN("RR") - 1))) < 18.00"""
                query3 = """SELECT RR_STUDY_No,CONVERT(float,LEFT("RR",LEN("RR") - 1)) as RR_Value FROM RR_STUDY"""
                # Query to Get Capability Study values
                query4 = """SELECT "Cap_Study",TRY_CAST("CPK" as FLOAT) FROM CAPABILITY_STUDY"""
                # Query to get KC Values based on Input month and Year
                query5 = """SELECT keys."KC_No",keys."KC_Id" FROM KEY_CHARACTERISTICS as keys LEFT JOIN CAPABILITY_STUDY as cap 
                                                            ON keys."KC_ID"=cap."KC_Id" 
                                                            WHERE YEAR(CONVERT(date,cap."Cap_NextStudyDate",105)) = %s
                                                            AND DATENAME(month,CONVERT(date,cap."Cap_NextStudyDate",105)) = %s"""
                ################################################################################################
                ################# QUERY FOR PLANNED DATA ########################
                cursor_SQL.execute(query, currentDate.year)
                for row in cursor_SQL:
                    plannedData.append([*row])
                filterdData = []
                filterdMonth = []
                for var in plannedData:
                    filterdData.append(var[0])
                    filterdMonth.append(var[2])
                ################# QUERY FOR PLANNED VS ACTUAL DATA ########################
                cursor_SQL2.execute(query2, currentDate.year)
                for row in cursor_SQL2:
                    actualData.append([*row])

                filterdActualData = []
                filterdActualMonth = []
                for var in actualData:
                    filterdActualData.append(var[0])
                    filterdActualMonth.append(var[2])
                RR = 0
                totalRR = 0
                ################# QUERY FOR RR DATA ########################
                cursor_SQL3.execute(query3)
                for row in cursor_SQL3:
                    rrData.append([*row])
                for var in rrData:
                    totalRR += 1
                    if var[1] < 18.00:
                        RR += 1
                ################# QUERY FOR CP DATA ########################
                totalCPK = 0
                cpkApprove = 0
                cpkImprove = 0
                cpkRework = 0
                cpkMisc = 0
                cursor_SQL4.execute(query4)
                for row in cursor_SQL4:
                    capabilityData.append([*row])
                for var in capabilityData:
                    totalCPK += 1
                    if var[1] == None:
                        cpkMisc += 1
                    else:
                        if var[1] >= 1.33:
                            cpkApprove += 1
                        if 1.33 > var[1] >= 1: cpkImprove += 1
                        if var[1] < 1: cpkRework += 1

                ###########################################################
                ################### PLOT GRAPHS ###########################
                fig = plt.figure(figsize=(12, 8), dpi=100)
                ax1 = fig.add_subplot(221)
                ax2 = fig.add_subplot(222)
                ax3 = fig.add_subplot(223)
                ax4 = fig.add_subplot(224)
                newFilterdMonth = [s + str(currentDate.year)[:-2] for s in filterdMonth]
                newFilterdActualMonth = [a + str(currentDate.year)[:-2] for a in filterdActualMonth]
                # ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
                bars1 = ax1.bar(newFilterdMonth, filterdData, width=0.8, color='blue')
                for bar1 in bars1:
                    yval1 = bar1.get_height()
                    ax1.text(bar1.get_x() + 0.25, yval1 + .05, yval1)
                bars2 = ax2.bar(newFilterdActualMonth, filterdActualData, width=0.2, color='green', align='edge')
                bars3 = ax2.bar(newFilterdMonth, filterdData, width=-0.2, color='red', align='edge')
                # bars2 = ax2.bar(filterdActualMonth, filterdActualData, width=0.2, color='green', align='edge')
                # bars3 = ax2.bar(filterdMonth, filterdData, width=-0.2, color='red', align='edge')
                for bar2 in bars2:
                    yval2 = bar2.get_height()
                    ax2.text(bar2.get_x(), yval2 + .05, yval2)
                for bar3 in bars3:
                    yval3 = bar3.get_height()
                    ax2.text(bar3.get_x() - 0.2, yval3 + .05, yval3)
                sizes1 = [RR, (totalRR - RR)]
                colors1 = ['gold', 'green']
                labels1 = ['RR <18%', 'RR>18%']
                explode1 = (0.01, 0)
                sizes2 = [cpkApprove, cpkImprove, cpkRework]
                colors2 = ['green', 'orange', 'red', 'black']
                labels2 = ['CPK>=1.33', '1.33>CPK>=1', 'CPK<1']
                ax1.legend(["Planned KC"])

                ax3.pie(sizes1, explode=explode1, colors=colors1, autopct='%.2f%%', startangle=30)
                ax3.axis('equal')
                ax3.legend(labels1)
                ax4.pie(sizes2, colors=colors2, labels=sizes2)
                ax4.axis('equal')
                ax4.legend(labels2)
                ax1.set_title('Execution Plan')
                ax2.set_title('Planned vs Actual')
                ax3.set_title('R&R Summary')
                ax4.set_title('CPK Summary')
                plt.subplots_adjust(hspace=0.5)
                conn_SQL.close()

                canvas = FigureCanvasTkAgg(fig, master=user_add)  # A tk.DrawingArea.
                canvas.draw()
                canvas.get_tk_widget().place(x=300, y=175)
                #####################################################################
                ########### Code for Dropdown #######################################
                mainframe = Frame(user_add)
                mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                mainframe.place(x=1600, y=175)
                # mainframe.pack(pady=100, padx=100) # Might need to change to place
                tkvar = StringVar(user_add)
                tkvar2 = IntVar(user_add)
                v = IntVar(user_add)
                v.set(1)
                choicesMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                'September',
                                'October', 'November', 'December']
                choicesYear = [0000]
                for x in range(2006, datetime.now().year + 1):
                    choicesYear.append(x)
                # tkvar.set('Month')  # set the default option

                present_Year = datetime.now().year
                # present_month=datetime.now().month
                tkvar.set("January")
                tkvar2.set(present_Year)
                # popupMenu1 = OptionMenu(mainframe, tkvar, choicesMonth[0], *choicesMonth)
                # popupMenu2 = OptionMenu(mainframe, tkvar2, choicesYear[0], *choicesYear)

                popupMenu1 = ttk.Combobox(mainframe, text=tkvar, font=("Ariel", 10), values=choicesMonth, width=13,
                                          justify='center', state='readonly')
                popupMenu2 = ttk.Combobox(mainframe, text=tkvar2, font=("Ariel", 10), values=choicesYear, width=13,
                                          justify='center', state='readonly')
                # popupMenu3 = ttk.Combobox(mainframe, font=("Ariel", 10), values=selectedKCs, width=13,justify='center', state='readonly')
                popupMenu1.grid(row=1, column=1)
                popupMenu2.grid(row=1, column=2)

                # popupMenu3.grid(row=2, column=1)

                def change_dropdown(*args):
                    self.lb102 = Label(window, text="KC ID",
                                       font=("Ariel", 12), bg='#feffd9', fg='#34943a')
                    self.lb102.place(x=1530, y=195)
                    conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                               "jdaat2012", "PU_FA_Testing")
                    cursor_SQL5 = conn_SQL.cursor()
                    data = []
                    selectedKCs = []
                    a = tkvar2.get()
                    b = tkvar.get()
                    # print(b)
                    # print(a)
                    cursor_SQL5.execute(query5, (a, b))
                    for row in cursor_SQL5:
                        data.append([*row])
                    # print(data)
                    counter = 0
                    for kc, val in data:
                        # ttk.Radiobutton(mainframe,
                        #                 text=kc,
                        #                 variable=v,
                        #                 command=ShowChoice,
                        #                 value=val).grid(row=2 + counter, column=1)
                        # ttk.Radiobutton(mainframe,
                        #                 text=kc,
                        #                 variable=v,
                        #                 command=ShowChoice,
                        #                 value=val).grid(row=2 + counter, column=1)
                        selectedKCs.append(kc)
                        counter += 1
                    conn_SQL.close()
                    popupMenu3 = Combobox(mainframe, font=("Ariel", 10), values=selectedKCs, width=29,
                                          justify='center', state='readonly')
                    popupMenu3.grid(row=2, column=1, columnspan=2)

                    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    # selected = popupMenu3.SelectedItem.ToString()
                    # print(selected)
                    def ShowChoice(a):
                        # print(v.get())
                        global important_variable
                        important_variable = popupMenu3.get()
                        # print(popupMenu3.get())
                        # print(important_variable)
                        return important_variable

                    popupMenu3.bind("<<ComboboxSelected>>", ShowChoice)

                # link function to change dropdown
                tkvar2.trace('w', change_dropdown)
                tkvar.trace('w', change_dropdown)

                # selected = popupMenu3.SelectedItem.ToString();
                # print(selected)
                # conn_SQL.close()

                # 'KC_01202'

                def dash_master():
                    master_id_send = 0

                    print(important_variable)

                    try:
                        master_id_send = important_variable
                    except:
                        master_id_send = 0

                    print(master_id_send, "\n")

                    master(master_id_send)

                def dash_rr():

                    rr_id_send = 0

                    conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                               "jdaat2012", "PU_FA_Testing")
                    cursor_SQL = conn_SQL.cursor()

                    cursor_SQL.execute("""SELECT TOP 1 [RR_STUDY_No] FROM [PU_FA_Testing].[dbo].[RR_STUDY] 
WHERE [KC_No]='""" + str(important_variable) + """'""")

                    try:
                        for row in cursor_SQL:
                            rr_id_send = row
                    except:
                        rr_id_send = 0

                    conn_SQL.close()

                    if rr_id_send != 0:

                        RandR(rr_id_send)
                    else:
                        RandR_next(important_variable)

                def dash_cabs():

                    cabs_id_send = 0

                    conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                               "jdaat2012", "PU_FA_Testing")
                    cursor_SQL = conn_SQL.cursor()

                    cursor_SQL.execute(
                        """
SELECT TOP 1 [Cap_Study] FROM [PU_FA_Testing].[dbo].[CAPABILITY_STUDY] 
WHERE KC_Id=(SELECT [KC_ID] FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] WHERE  [KC_No]='""" + str(
                            important_variable) + """') ORDER BY [Cap_NextStudyDate] """)

                    try:
                        for row in cursor_SQL:
                            cabs_id_send = row[0]
                    except:
                        cabs_id_send = 0

                    # print(cap_id_send)

                    conn_SQL.close()

                    # print(cabs_id_send,"xx",important_variable)

                    if cabs_id_send != 0:
                        cabs(cabs_id_send)
                    else:
                        cabs_next(important_variable)

                self.btn1 = ttk.Button(user_add, text="MASTER", width=20, command=dash_master)
                self.btn1.place(x=1550, y=800, width=150, height=50)

                self.btn3 = ttk.Button(user_add, text="R&R", width=20, command=dash_rr)
                self.btn3.place(x=1730, y=800, width=150, height=50)

                self.btn3 = ttk.Button(user_add, text="CAPABILITY", width=20, command=dash_cabs)
                self.btn3.place(x=1550, y=900, width=150, height=50)

                self.btn4 = ttk.Button(user_add, text="GROUP_KC", width=20, command=gkc_master)
                self.btn4.place(x=1730, y=900, width=150, height=50)

                self.lb100 = Label(window, text="Month",
                                   font=("Ariel", 12), bg='#feffd9', fg='#34943a')
                self.lb100.place(x=1630, y=150)

                self.lb101 = Label(window, text="Year",
                                   font=("Ariel", 12), bg='#feffd9', fg='#34943a')
                self.lb101.place(x=1745, y=150)

            def openRRFormat(kcid):
                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()
                cursor_SQL2 = conn_SQL.cursor()
                # query = """SELECT * FROM KEY_CHARACTERISTICS WHERE KC_ID=%s"""
                query = """SELECT keys.[WorkCenter],keys.[Part_No],keys.[Responsible_QE],keys.[Responsible_ME],keys.[Description],keys.[KC_Id],
                            rr.[RR_STUDY_No],rr.[Item],rr.[Created_Date],keys.[KCData_Type],keys.[Specification],keys.[Unit],rr.[Instrument]
                            FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] as keys
                            LEFT JOIN  [PU_FA_Testing].[dbo].[RR_STUDY] as rr 
                            ON keys.[KC_ID]=rr.[KC_ID] 
                            WHERE keys.[KC_ID]=%s
                            ORDER BY rr.[RR_STUDY_No] desc"""

                query2 = """SELECT TOP 1 TRY_CONVERT(int,RIGHT("Cap_Study", LEN("Cap_Study")-3)),"Capability_Id"  
                            FROM CAPABILITY_STUDY ORDER BY "Cap_Study" desc"""
                # kcdata = []
                cursor_SQL.execute(query, kcid)
                kcdata = cursor_SQL.fetchone()
                kc_center = kcdata[0]
                # part_no=kcdata[1]
                # qe_name = kcdata[2]
                # me_name=kcdata[3]
                # kc_desc = kcdata[4]
                # kc_id=kcdata[5]
                rr_no = kcdata[6]
                rr_item = kcdata[7]
                # rr_date = kcdata[8]
                kc_datatype = kcdata[9]
                kc_spec = kcdata[10]
                kc_unit = kcdata[11]
                rr_instrument = kcdata[12]
                print(rr_no)
                # if cap_id == None:
                #     cursor_SQL2.execute(query2)
                #     capadata = cursor_SQL2.fetchone()
                #     cap_no = 'EC_'+str(capadata[0]+1)
                # print(cap_no)
                if kc_datatype == 'Variável':
                    # open F-CQ-311-01-04
                    loc = (r"excel\F-CQ-313-01-01.xlsm")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Coleta de Dados']
                    sheet.range('D5').value = rr_no
                    sheet.range('D6').value = datetime.today().strftime('%d-%m-%Y')
                    sheet.range('D7').value = rr_item
                    sheet.range('D12').value = kc_spec
                    sheet.range('D14').value = kc_unit
                    sheet.range('H6').value = kc_center
                    sheet.range('H12').value = rr_instrument
                    # wb.save(loc)
                    # os.system('start excel.exe F-CQ-313-01-01.xlsm')
                    savepath = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\rr\ ") + rr_no
                    wb.save(savepath)
                if kc_datatype == 'Atributo':
                    # F-CQ-311-01-05
                    loc = (r"excel\F-CQ-313-01-02.xlsm")
                    wb = xw.Book(loc)
                    sheet = wb.sheets['Entrada_de_dados']
                    sheet.range('E6').value = rr_no
                    sheet.range('E7').value = rr_item
                    sheet.range('E9').value = datetime.today().strftime('%d-%m-%Y')
                    sheet.range('E14').value = kc_spec
                    sheet.range('L7').value = kc_center
                    # wb.save(loc)
                    # os.system('start excel.exe F-CQ-313-01-02.xlsm')
                    savepath = (r"\\Gnpunnas1a\Embedded_Systems\Temporary\kcmanagementtrial\rr\ ") + rr_no
                    wb.save(savepath)

            # def side_search():
            #
            #     conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
            #                                "jdaat2012", "PU_FA_Testing")
            #     cursor_SQL = conn_SQL.cursor()
            #
            #     query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKC_Master]"""
            #
            #     cursor_SQL.execute(query)
            #
            #     data = []
            #
            #     for row in cursor_SQL:
            #         #print(row)
            #         data.append([*row])
            #
            #
            #     cursor_SQL.close()
            #
            #
            #
            #     class App:
            #         def __init__(self):
            #
            #             def selectItem(a):
            #                 curItem = tree.focus()
            #                 #print(tree.item(curItem)['values'])
            #                 quantifiers = (tree.item(curItem)['values'])
            #
            #                 def gkc():
            #                     # CLASS FOR ADDING STATION
            #                     class GKC():
            #
            #                         def __init__(self, window):
            #                             load = cv2.imread('background.png', 1)
            #                             cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            #                             load = Image.fromarray(cv2imagex1)
            #                             # load = load.resize((int(870), int(66)), Image.ANTIALIAS)
            #                             render = ImageTk.PhotoImage(load)
            #                             img = tk.Label(image=render)
            #                             img.image = render
            #                             img.place(x=0, y=70)
            #
            #                             # LABEL AND TEXT BOX TO ENTER DETAILS OF ALL ELEMENTS OF A STATION
            #                             self.lb_title = Label(window, text="GROUP KC",
            #                                                   font=("Ariel", 20, 'underline'), bg='white')
            #                             self.lb_title.place(x=550, y=110)
            #
            #                             self.lb1 = Label(window, text="#KC", fg='black',
            #                                              font=("Ariel", 15), bg='white')
            #                             self.lb1.place(x=5, y=73)
            #
            #                             self.txtfld1 = ttk.Combobox(window, text="#KC",
            #                                                         font=("Ariel", 15))
            #                             self.txtfld1.place(x=85, y=73)
            #
            #                             self.txtfld1.config(state=DISABLED)
            #
            #                             self.lb8 = Label(window, text="GKC_Num",
            #                                              font=("Ariel", 15), bg='white')
            #                             self.lb8.place(x=60, y=200)
            #
            #                             self.txtfld8_cap = ttk.Combobox(window, text="GKC_Num",
            #                                                             font=("Ariel", 15), values=list(
            #                                     set([data[x][1] for x in range(0, len(data))])))
            #                             self.txtfld8_cap.place(x=300, y=200)
            #
            #                             gkc_no = max(list(map(int, set([data[x][1][4:] for x in range(0, len(data))]))))
            #
            #                             gkc_no = str("GKC_") + ((str("00000") + str(int(gkc_no) + 1))[-5:])
            #
            #                             self.txtfld8_cap.set(gkc_no)
            #                             self.txtfld8_cap.configure(state=DISABLED)
            #
            #                             self.lb9 = Label(window, text="GKC_Desc",
            #                                              font=("Ariel", 15), bg='white')
            #                             self.lb9.place(x=650, y=200)
            #
            #                             self.txtfld9_cap = ttk.Combobox(window,
            #                                                             text="GKC_Desc",
            #                                                             font=("Ariel", 15), values=list(
            #                                     set([data[x][2] for x in range(0, len(data))])))
            #                             self.txtfld9_cap.place(x=890, y=200)
            #                             self.txtfld9_cap.set("")
            #
            #                             self.lb12 = Label(window, text="Espec.",
            #                                               font=("Ariel", 15), bg='white')
            #                             self.lb12.place(x=60, y=350)
            #
            #                             self.txtfld12_cap = ttk.Combobox(window, text="Espec.",
            #                                                              font=("Ariel", 15), values=list(
            #                                     set([data[x][3] for x in range(0, len(data))])))
            #                             self.txtfld12_cap.place(x=300, y=350)
            #                             self.txtfld12_cap.set("")
            #
            #                             self.lb13 = Label(window, text="Tol.", fg='black',
            #                                               font=("Ariel", 15), bg='white')
            #                             self.lb13.place(x=650, y=350)
            #
            #                             self.txtfld13_cap = ttk.Combobox(window,
            #
            #                                                              text="Tol.",
            #                                                              font=("Ariel", 15), values=list(
            #                                     set([data[x][4] for x in range(0, len(data))])))
            #                             self.txtfld13_cap.place(x=890, y=350)
            #                             self.txtfld13_cap.set("")
            #
            #                             self.lb16 = Label(window, text="Unid.", fg='black',
            #                                               font=("Ariel", 15), bg='white')
            #                             self.lb16.place(x=60, y=500)
            #
            #                             self.txtfld16_cap = ttk.Combobox(window, text="Unid.",
            #                                                              font=("Ariel", 15), values=list(
            #                                     set([data[x][5] for x in range(0, len(data))])))
            #                             self.txtfld16_cap.place(x=300, y=500)
            #                             self.txtfld16_cap.set("")
            #
            #                             self.lb17 = Label(window, text="GKC_CreatedDate", fg='black',
            #                                               font=("Ariel", 15), bg='white')
            #                             self.lb17.place(x=650, y=500)
            #
            #                             self.txtfld17_cap = ttk.Combobox(window,
            #
            #                                                              text="GKC_CreatedDate",
            #                                                              font=("Ariel", 15), values=list(
            #                                     set([data[x][6] for x in range(0, len(data))])))
            #                             self.txtfld17_cap.place(x=890, y=500)
            #                             self.txtfld17_cap.set("")
            #
            #                             self.btn_submit = ttk.Button(window, text="SUBMIT")
            #                             self.btn_submit.place(x=520, y=650, width=250, height=60)
            #
            #                     GKC(user_add)
            #
            #                 # self.btn_low1 = ttk.Button(window, text="ADD GKC ", width=20, command=gkc)
            #                 # self.btn_low1.place(x=0, y=957, width=1920, height=61)
            #
            #             frame = Frame(user_add)
            #             frame.place(x=1282, y=380)
            #
            #             # print(data)
            #
            #             tree = ttk.Treeview(frame,
            #                                 columns=(1, 2, 3, 4, 5, 6, 7),
            #                                 height=7, show="headings")
            #             tree.pack(side='left')
            #             tree.bind('<ButtonRelease-1>', selectItem)
            #
            #             val = ["GKC_ID", "GKC_Num", "GKC_Desc", "GKC_Spec", "GKC_Tolerance",
            #                    "GKC_Unit", "GKC_CreatedDate"]
            #
            #             for i in range(1, len(val) + 1):
            #                 tree.heading(i, text=val[i - 1])
            #
            #             # tree.heading(2, text="Column 2")
            #             # tree.heading(3, text="Column 3")
            #
            #             for i in range(1, len(val) + 1):
            #                 tree.column(i, width=89)
            #
            #             # tree.column(2, width=100)
            #             # tree.column(3, width=100)
            #
            #             scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
            #             scroll.pack(side='right', fill='y')
            #
            #             """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
            #             scrollx.pack(side='bottom', fill='x')"""
            #
            #             tree.configure(yscrollcommand=scroll.set)
            #
            #             iterx = 0
            #             for valx in data:
            #                 if iterx % 2 == 0:
            #                     tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
            #                                                    , valx[5], valx[6]),
            #                                 tags=('odd',))
            #                 else:
            #                     tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
            #                                                    , valx[5], valx[6]),
            #                                 tags=('even',))
            #
            #                 iterx += 1
            #
            #             tree.tag_configure('odd', background='#E8E8E8')
            #             tree.tag_configure('even', background='#FFFFFF')
            #
            #             conn_SQL.close()
            #
            #     a = App()
            #
            #     def hex2rgb(str_rgb):
            #         try:
            #             rgb = str_rgb[1:]
            #
            #             if len(rgb) == 6:
            #                 r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
            #             elif len(rgb) == 3:
            #                 r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
            #             else:
            #                 raise ValueError()
            #         except:
            #             raise ValueError("Invalid value %r provided for rgb color." % str_rgb)
            #
            #         return tuple(int(v, 16) for v in (r, g, b))
            #
            #     class Placeholder_State(object):
            #         __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'contains_placeholder'
            #
            #     def add_placeholder_to(entry, placeholder, color="grey", font=None):
            #         normal_color = entry.cget("fg")
            #         normal_font = entry.cget("font")
            #
            #         if font is None:
            #             font = normal_font
            #
            #         state = Placeholder_State()
            #         state.normal_color = normal_color
            #         state.normal_font = normal_font
            #         state.placeholder_color = color
            #         state.placeholder_font = font
            #         state.placeholder_text = placeholder
            #         state.contains_placeholder = True
            #
            #         def on_focusin(event, entry=entry, state=state):
            #             if state.contains_placeholder:
            #                 entry.delete(0, "end")
            #                 entry.config(fg=state.normal_color, font=state.normal_font)
            #
            #                 state.contains_placeholder = False
            #
            #         def on_focusout(event, entry=entry, state=state):
            #             if entry.get() == '':
            #                 entry.insert(0, state.placeholder_text)
            #                 entry.config(fg=state.placeholder_color, font=state.placeholder_font)
            #
            #                 state.contains_placeholder = True
            #
            #         entry.insert(0, placeholder)
            #         entry.config(fg=color, font=font)
            #
            #         entry.bind('<FocusIn>', on_focusin, add="+")
            #         entry.bind('<FocusOut>', on_focusout, add="+")
            #
            #         entry.placeholder_state = state
            #
            #         return state
            #
            #     class SearchBox(Frame):
            #         def __init__(self, master, entry_width=43, entry_font=None, entry_background="white",
            #                      entry_highlightthickness=10,
            #                      button_text="Search", button_ipadx=10, button_background="#009688",
            #                      button_foreground="white",
            #                      button_font=None, opacity=0.8, placeholder=None, placeholder_font=None,
            #                      placeholder_color="grey",
            #                      spacing=3, command=None):
            #             Frame.__init__(self, master)
            #
            #             self._command = command
            #
            #             self.entry = Entry(self, width=entry_width, background=entry_background,
            #                                highlightcolor=button_background,
            #                                highlightthickness=entry_highlightthickness,
            #                                font=("Ariel", 10))
            #             self.entry.pack(side=LEFT, fill=BOTH, ipady=1, padx=(0, spacing))
            #
            #             if entry_font:
            #                 self.entry.configure(font=entry_font)
            #
            #             if placeholder:
            #                 add_placeholder_to(self.entry, placeholder, color=placeholder_color,
            #                                    font=placeholder_font)
            #
            #             self.entry.bind("<Escape>", lambda event: self.entry.nametowidget(".").focus())
            #             self.entry.bind("<Return>", self._on_execute_command)
            #
            #             opacity = float(opacity)
            #
            #             if button_background.startswith("#"):
            #                 r, g, b = hex2rgb(button_background)
            #             else:
            #                 # Color name
            #                 r, g, b = master.winfo_rgb(button_background)
            #
            #             r = int(opacity * r)
            #             g = int(opacity * g)
            #             b = int(opacity * b)
            #
            #             if r <= 255 and g <= 255 and b <= 255:
            #                 self._button_activebackground = '#%02x%02x%02x' % (r, g, b)
            #             else:
            #                 self._button_activebackground = '#%04x%04x%04x' % (r, g, b)
            #
            #             self._button_background = button_background
            #
            #             """window, state = "readonly",
            #             values = [0],
            #             text = "Espec.",
            #             font = ("Ariel", 20)"""
            #
            #             self.button_label1 = ttk.Combobox(self, state="readonly",
            #                                               values=["GKC_ID", "GKC_Num", "GKC_Desc", "GKC_Spec",
            #                                                       "GKC_Tolerance",
            #                                                       "GKC_Unit", "GKC_CreatedDate"]
            #                                               ,
            #                                               background=button_background,
            #                                               foreground=button_foreground, width=10,
            #                                               font=("Ariel", 7), justify='center')
            #
            #             self.button_label1.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
            #
            #             self.button_label = Label(self, text=button_text, background=button_background,
            #                                       foreground=button_foreground, width=20,
            #                                       font=button_font)
            #             if entry_font:
            #                 self.button_label.configure(font=button_font)
            #
            #             self.button_label.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
            #
            #             self.button_label.bind("<Enter>", self._state_active)
            #             self.button_label.bind("<Leave>", self._state_normal)
            #
            #             self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)
            #
            #         def get_text(self):
            #             entry = self.entry
            #             if hasattr(entry, "placeholder_state"):
            #                 if entry.placeholder_state.contains_placeholder:
            #                     return ""
            #                 else:
            #                     return entry.get()
            #             else:
            #                 return entry.get()
            #
            #         def set_text(self, text):
            #             entry = self.entry
            #             if hasattr(entry, "placeholder_state"):
            #                 entry.placeholder_state.contains_placeholder = False
            #
            #             entry.delete(0, END)
            #             entry.insert(0, text)
            #
            #         def clear(self):
            #             self.entry_var.set("")
            #
            #         def focus(self):
            #             self.entry.focus()
            #
            #         def _on_execute_command(self, event):
            #             val = self.button_label1.get()
            #
            #             text = self.get_text()
            #             self._command(text, val)
            #
            #         def _state_normal(self, event):
            #             self.button_label.configure(background=self._button_background)
            #
            #         def _state_active(self, event):
            #             self.button_label.configure(background=self._button_activebackground)
            #
            #     def command(text, val):
            #         # print(text,val)
            #         # print(len(val))
            #         if val == "" and text == "":
            #             showinfo("Enter Parameters", "searching:NULL")
            #             return 0
            #
            #         conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
            #                                    "jdaat2012", "PU_FA_Testing")
            #         cursor_SQL = conn_SQL.cursor()
            #
            #         if len(text) == 0:
            #             query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKC_Master]"""
            #         else:
            #             #print(val,text)
            #             query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKC_Master] WHERE """ + str(
            #                 val) + """='""" + str(text) + """'"""
            #
            #         cursor_SQL.execute(query)
            #
            #         data = []
            #
            #
            #
            #         for row in cursor_SQL:
            #             # print(row)
            #             data.append([*row])
            #
            #         cursor_SQL.close()
            #
            #         frame = Frame(user_add)
            #         frame.place(x=1282, y=380)
            #
            #         # print(data)
            #
            #         tree = ttk.Treeview(frame,
            #                             columns=(1, 2, 3, 4, 5, 6, 7),
            #                             height=11, show="headings")
            #         tree.pack(side='left')
            #
            #         val = ["GKC_ID", "GKC_Num", "GKC_Desc", "GKC_Spec", "GKC_Tolerance",
            #                "GKC_Unit", "GKC_CreatedDate"]
            #         for i in range(1, len(val) + 1):
            #             tree.heading(i, text=val[i - 1])
            #
            #         # tree.heading(2, text="Column 2")
            #         # tree.heading(3, text="Column 3")
            #
            #         for i in range(1, len(val) + 1):
            #             tree.column(i, width=89)
            #
            #         # tree.column(2, width=100)
            #         # tree.column(3, width=100)
            #
            #         scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
            #         scroll.pack(side='right', fill='y')
            #
            #         """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
            #         scrollx.pack(side='bottom', fill='x')"""
            #
            #         tree.configure(yscrollcommand=scroll.set)
            #
            #         iterx = 0
            #         for valx in data:
            #             if iterx % 2 == 0:
            #                 tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
            #                                                , valx[5], valx[6]),
            #                             tags=('odd',))
            #             else:
            #                 tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
            #                                                , valx[5], valx[6]),
            #                             tags=('even',))
            #
            #             iterx += 1
            #
            #         tree.tag_configure('odd', background='#E8E8E8')
            #         tree.tag_configure('even', background='#FFFFFF')
            #
            #         conn_SQL.close()
            #
            #     Label(user_add, text="SEARCH ", font=("Ariel", 10), bg='#E8E8E8', width=9).place(x=1280,
            #                                                                                                  y=358)
            #     SearchBox(user_add, command=command, placeholder="Type and press enter",
            #               entry_highlightthickness=0).place(x=1355, y=358)
            #
            #
            #
            #     #tree.column(i, width=89)
            #     #frame.place(x=1280, y=380)

            # side_search()

            def master(id_master=0):

                load = cv2.imread('Images/start.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/background.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/legend.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(765), int(120)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=1150, y=500)

                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()

                # DATABASE FOR MASTER TABLE

                query = """SELECT *  FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL ORDER BY [# KC] DESC"""

                cursor_SQL.execute(query)

                data = []

                for row in cursor_SQL:
                    # print(row)
                    data.append([*row])

                image_loader()

                conn_SQL.close()

                # "# KC", "Part Number", "Rev.", "KC Similar", "Centro de Trabalho",
                # "Processo", "Descrição", "Especificação",
                # "Tolerância", "Unidade", "Tipo de caract.", "Tipo de dados", "Local de Medição",
                # "Resp. Qualidade", "Resp. Manufatura", "Produto", "Projeto / ECM",
                # "Data de Impl.", "Status", "R&R Solicitado", "# Estudo", "Resultado", "# Estudo", "Cp", "Cpk", "PPM", "Data"

                Part_Number = []
                Rev = []
                KC_Similar = []
                Centro_de_Trabalho = []
                Processo = []
                Descrição = []
                Especificação = []
                Tolerância = []
                Unidade = []
                Tipo_de_caract = []
                Tipo_de_dados = []
                Local_de_Medição = []
                Resp_Qualidade = []
                Resp_Manufatura = []
                Produto = []
                Projeto_ECM = []
                Data_de_Impl = []
                Status = []

                RRSolicitado = []
                Estudo_rr = []
                Resultado = []
                Estudo_cap = []
                Cp = []
                Cpk = []
                PPM = []
                Data = []

                for x in range(0, len(data)):
                    if data[x][1] != None:
                        Part_Number.append(data[x][1])

                Part_Number = sorted(set(Part_Number))

                for x in range(0, len(data)):
                    if data[x][2] != None:
                        Rev.append(data[x][2])

                Rev = sorted(set(Rev))

                for x in range(0, len(data)):
                    if data[x][3] != None:
                        KC_Similar.append(data[x][3])

                KC_Similar = sorted(set(KC_Similar))

                for x in range(0, len(data)):
                    if data[x][4] != None:
                        Centro_de_Trabalho.append(data[x][4])

                Centro_de_Trabalho = sorted(set(Centro_de_Trabalho))

                for x in range(0, len(data)):
                    if data[x][5] != None:
                        Processo.append(data[x][5])

                Processo = sorted(set(Processo))

                for x in range(0, len(data)):
                    if data[x][6] != None:
                        Descrição.append(data[x][6])

                Descrição = sorted(set(Descrição))

                for x in range(0, len(data)):
                    if data[x][7] != None:
                        Especificação.append(data[x][7])

                Especificação = sorted(set(Especificação))

                for x in range(0, len(data)):
                    if data[x][8] != None:
                        Tolerância.append(data[x][8])

                Tolerância = sorted(set(Tolerância))

                for x in range(0, len(data)):
                    if data[x][9] != None:
                        Unidade.append(data[x][9])

                Unidade = sorted(set(Unidade))

                for x in range(0, len(data)):
                    if data[x][10] != None:
                        Tipo_de_caract.append(data[x][10])

                Tipo_de_caract = sorted(set(Tipo_de_caract))

                for x in range(0, len(data)):
                    if data[x][11] != None:
                        Tipo_de_dados.append(data[x][11])

                Tipo_de_dados = sorted(set(Tipo_de_dados))

                for x in range(0, len(data)):
                    if data[x][12] != None:
                        Local_de_Medição.append(data[x][12])

                Local_de_Medição = sorted(set(Local_de_Medição))

                for x in range(0, len(data)):
                    if data[x][13] != None:
                        Resp_Qualidade.append(data[x][13])

                Resp_Qualidade = sorted(set(Resp_Qualidade))

                for x in range(0, len(data)):
                    if data[x][14] != None:
                        Resp_Manufatura.append(data[x][14])

                Resp_Manufatura = sorted(set(Resp_Manufatura))

                for x in range(0, len(data)):
                    if data[x][15] != None:
                        Produto.append(data[x][15])

                Produto = sorted(set(Produto))

                for x in range(0, len(data)):
                    if data[x][16] != None:
                        Projeto_ECM.append(data[x][16])

                Projeto_ECM = sorted(set(Projeto_ECM))

                for x in range(0, len(data)):
                    if data[x][17] != None:
                        Data_de_Impl.append(data[x][17])

                Data_de_Impl = sorted(set(Data_de_Impl))

                for x in range(0, len(data)):
                    if data[x][18] != None:
                        Status.append(data[x][18])

                Status = sorted(set(Status))

                for x in range(0, len(data)):
                    if data[x][21] != None:
                        RRSolicitado.append(data[x][21])

                RRSolicitado = sorted(set(RRSolicitado))

                for x in range(0, len(data)):
                    if data[x][22] != None:
                        Estudo_rr.append(data[x][22])

                Estudo_rr = sorted(set(Estudo_rr))

                for x in range(0, len(data)):
                    if data[x][23] != None:
                        Resultado.append(data[x][23])

                Resultado = sorted(set(Resultado))

                for x in range(0, len(data)):
                    if data[x][25] != None:
                        Estudo_cap.append(data[x][25])

                Estudo_cap = sorted(set(Estudo_cap))

                for x in range(0, len(data)):
                    if data[x][26] != None:
                        Cp.append(data[x][26])

                Cp = sorted(set(Cp))

                for x in range(0, len(data)):
                    if data[x][27] != None:
                        Cpk.append(data[x][27])

                Cpk = sorted(set(Cpk))

                print(Cpk)

                for x in range(0, len(data)):
                    if data[x][28] != None:
                        PPM.append(data[x][28])

                PPM = sorted(set(PPM))

                for x in range(0, len(data)):
                    if data[x][29] != None:
                        Data.append(data[x][29])

                Data = sorted(set(Data))

                #
                # (list(
                #     set([data[x][1] for x in range(0, len(data))]))))
                #

                def user_add_station():
                    # CLASS FOR ADDING STATION
                    class User_Add_station():

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
                                                  font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9', fg='#34943a')
                            self.lb_title.place(x=400, y=150)

                            kc_no = max(list(map(int, set([data[x][0][3:] for x in range(0, len(data))]))))
                            kc_no = str("KC_") + ((str("00000") + str(int(kc_no) + 1))[-5:])

                            self.lb1 = Label(window, text="#KC",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            self.lb1.place(x=5, y=142)  # bg='#feffd9'

                            self.txtfld1 = ttk.Combobox(window, text="#KC",
                                                        font=("Ariel", 10))
                            self.txtfld1.place(x=60, y=140)
                            self.txtfld1.set(kc_no)
                            self.txtfld1.config(state=DISABLED)

                            self.lb2 = Label(window, text="Part Number",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb2.place(x=80, y=230)

                            self.txtfld2 = ttk.Combobox(window, text="Part Number",
                                                        font=("Ariel", 10), values=Part_Number)
                            self.txtfld2.place(x=210, y=230)

                            self.txtfld2.set("")

                            self.lb3 = Label(window, text="Rev.",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb3.place(x=420, y=230)

                            self.txtfld3 = ttk.Combobox(window, text="Rev.",
                                                        font=("Ariel", 10), values=Rev)
                            self.txtfld3.place(x=550, y=230)

                            self.txtfld3.set("")

                            self.lb4 = Label(window, text="Centro de Traball",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb4.place(x=760, y=230)

                            self.txtfld4 = ttk.Combobox(window, text="Centro de Traball",
                                                        font=("Ariel", 10), values=Centro_de_Trabalho)
                            self.txtfld4.place(x=890, y=230)

                            self.txtfld4.set("")

                            self.lb5 = Label(window, text="KC Similar",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb5.place(x=760, y=310)

                            self.txtfld5 = ttk.Combobox(window, text="KC Similar", state="readonly",
                                                        font=("Ariel", 10), values=KC_Similar)
                            self.txtfld5.place(x=890, y=310)
                            self.txtfld5.configure(state=DISABLED)

                            # self.btm_kc_sim_check=ttk.bu

                            self.txtfld5.set("")

                            self.lb6 = Label(window, text="Processo",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb6.place(x=420, y=270)

                            self.txtfld6 = ttk.Combobox(window,
                                                        text="Processo",
                                                        font=("Ariel", 10), values=Processo)
                            self.txtfld6.place(x=550, y=270)

                            self.txtfld6.set("")

                            self.lb7 = Label(window, text="Descrição",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb7.place(x=760, y=270)

                            self.txtfld7 = ttk.Combobox(window,

                                                        text="Descrição",
                                                        font=("Ariel", 10), values=Descrição)
                            self.txtfld7.place(x=890, y=270)

                            self.txtfld7.set("")

                            self.lb8 = Label(window, text="Especificação",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb8.place(x=80, y=310)

                            self.txtfld8 = ttk.Combobox(window, text="Especificação",
                                                        font=("Ariel", 10), values=Especificação)
                            self.txtfld8.place(x=210, y=310)

                            self.txtfld8.set("")

                            self.lb9 = Label(window, text="Tolerância",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb9.place(x=420, y=310)

                            self.txtfld9 = ttk.Combobox(window,

                                                        text="Tolerância",
                                                        font=("Ariel", 10), values=Tolerância)
                            self.txtfld9.place(x=550, y=310)

                            self.txtfld9.set("")

                            self.lb10 = Label(window, text="Unidade",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb10.place(x=80, y=270)

                            self.txtfld10 = ttk.Combobox(window, text="Unidade",
                                                         font=("Ariel", 10), values=Unidade)
                            self.txtfld10.place(x=210, y=270)

                            self.txtfld10.set("")

                            self.lb11 = Label(window, text="Tipo de caract.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb11.place(x=80, y=350)

                            self.txtfld11 = ttk.Combobox(window,
                                                         text="Tipo de caract.",
                                                         font=("Ariel", 10), values=Tipo_de_caract)
                            self.txtfld11.place(x=210, y=350)

                            self.txtfld11.set("")

                            self.lb12 = Label(window, text="Tipo de dados",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb12.place(x=420, y=350)

                            self.txtfld12 = ttk.Combobox(window, text="Tipo de dados",
                                                         font=("Ariel", 10), values=Tipo_de_dados)
                            self.txtfld12.place(x=550, y=350)

                            self.txtfld12.set("")

                            self.lb13 = Label(window, text="Local de Medição",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb13.place(x=760, y=350)

                            self.txtfld13 = ttk.Combobox(window,
                                                         text="Local de Medição",
                                                         font=("Ariel", 10), values=Local_de_Medição)
                            self.txtfld13.place(x=890, y=350)

                            self.txtfld13.set("")

                            self.lb14 = Label(window, text="Resp. Qualidade",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb14.place(x=80, y=390)

                            self.txtfld14 = ttk.Combobox(window, text="Resp. Qualidade",
                                                         font=("Ariel", 10), values=Resp_Qualidade)
                            self.txtfld14.place(x=210, y=390)

                            self.txtfld14.set("")

                            self.lb15 = Label(window, text="Resp. Manufatura",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb15.place(x=420, y=390)

                            self.txtfld15 = ttk.Combobox(window,
                                                         text="Resp. Manufatura",
                                                         font=("Ariel", 10), values=Resp_Manufatura)
                            self.txtfld15.place(x=550, y=390)

                            self.txtfld15.set("")

                            self.lb16 = Label(window, text="Produto",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb16.place(x=760, y=390)

                            self.txtfld16 = ttk.Combobox(window, text="Produto",
                                                         font=("Ariel", 10), values=Produto)
                            self.txtfld16.place(x=890, y=390)
                            self.txtfld16.set("")

                            self.lb17 = Label(window, text="Projeto / ECM",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb17.place(x=80, y=430)

                            self.txtfld17 = ttk.Combobox(window,
                                                         text="Projeto / ECM",
                                                         font=("Ariel", 10), values=Projeto_ECM)
                            self.txtfld17.place(x=210, y=430)
                            self.txtfld17.set("")

                            self.lb18 = Label(window, text="Data de Impl.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb18.place(x=420, y=430)

                            from datetime import date
                            from datetime import timedelta

                            today = date.today()

                            # dd/mm/YY
                            d1 = today.strftime("%d-%m-%Y")
                            print(d1)

                            self.txtfld18 = ttk.Combobox(window, text="Data de Impl.",
                                                         font=("Ariel", 10), values=Data_de_Impl)
                            self.txtfld18.place(x=550, y=430)
                            self.txtfld18.set(d1)

                            self.lb19 = Label(window, text="Status",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb19.place(x=760, y=430)

                            self.txtfld19 = ttk.Combobox(window,
                                                         text="Status", state="readonly",
                                                         font=("Ariel", 10), values=Status)
                            self.txtfld19.place(x=890, y=430)

                            self.txtfld19.set("")

                            # RR CODES FOR BOXES

                            # self.lb20 = Label(window, text="Estudo RR",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb20.place(x=80, y=480)
                            #
                            # self.txtfld20 = ttk.Combobox(window,
                            #                              text="Estudo RR",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][15] for x in range(0, len(data))])))
                            # self.txtfld20.place(x=210, y=480)
                            # self.txtfld20.set("")
                            # self.txtfld20.configure(state=DISABLED)

                            self.lb21 = Label(window, text="R&R Solicitado",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=14, anchor='e')
                            self.lb21.place(x=420, y=480)

                            self.txtfld21 = ttk.Combobox(window, text="R&R Solicitado", state="readonly",
                                                         font=("Ariel", 10), values=["Não", "Sim"])
                            self.txtfld21.place(x=550, y=480)
                            self.txtfld21.set("")

                            # self.txtfld21.configure(state=DISABLED)

                            # self.lb22 = Label(window, text="Resultado",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb22.place(x=760, y=480)
                            #
                            # self.txtfld22 = ttk.Combobox(window,
                            #                              text="Resultado", state="readonly",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][17] for x in range(0, len(data))])))
                            # self.txtfld22.place(x=890, y=480)
                            #
                            # self.txtfld22.set("")
                            # self.txtfld22.configure(state=DISABLED)
                            #
                            #
                            #
                            # # TABLE FOR CAPABILITY
                            #
                            # self.lb30 = Label(window, text="Estudo CAP",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb30.place(x=80, y=520)
                            #
                            # self.txtfld30 = ttk.Combobox(window,
                            #                              text="Estudo CAP",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][15] for x in range(0, len(data))])))
                            # self.txtfld30.place(x=210, y=520)
                            # self.txtfld30.set("")
                            # self.txtfld30.configure(state=DISABLED)
                            #
                            # self.lb31 = Label(window, text="CP",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb31.place(x=420, y=520)
                            #
                            # self.txtfld31 = ttk.Combobox(window, text="CP",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][16] for x in range(0, len(data))])))
                            # self.txtfld31.place(x=550, y=520)
                            # self.txtfld31.set("")
                            # self.txtfld31.configure(state=DISABLED)
                            #
                            # self.lb32 = Label(window, text="CPK",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb32.place(x=760, y=520)
                            #
                            # self.txtfld32 = ttk.Combobox(window,
                            #                              text="CPK", state="readonly",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][17] for x in range(0, len(data))])))
                            # self.txtfld32.place(x=890, y=520)
                            #
                            # self.txtfld32.set("")
                            # self.txtfld32.configure(state=DISABLED)

                            # self.lb33 = Label(window, text="PPM",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb33.place(x=80, y=550)
                            #
                            # self.txtfld33 = ttk.Combobox(window,
                            #                              text="PPM",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][15] for x in range(0, len(data))])))
                            # self.txtfld33.place(x=210, y=550)
                            # self.txtfld33.set("")
                            # self.txtfld33.configure(state=DISABLED)
                            #
                            # self.lb34 = Label(window, text="Data",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb34.place(x=420, y=550)
                            #
                            # self.txtfld34 = ttk.Combobox(window, text="Data",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][16] for x in range(0, len(data))])))
                            # self.txtfld34.place(x=550, y=550)
                            # self.txtfld34.set("")
                            # self.txtfld34.configure(state=DISABLED)
                            #
                            # self.lb35 = Label(window, text="Link",
                            #                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            # self.lb35.place(x=760, y=550)
                            #
                            # self.txtfld35 = ttk.Combobox(window,
                            #                              text="Link", state="readonly",
                            #                              font=("Ariel", 10), values=list(
                            #         set([data[x][17] for x in range(0, len(data))])))
                            # self.txtfld35.place(x=890, y=550)
                            #
                            # self.txtfld35.set("")
                            # self.txtfld35.configure(state=DISABLED)

                            self.btn3 = ttk.Button(user_add, text="R&R", style='my.TButton', width=20, command=RandR)
                            self.btn3.place(x=460, y=70, width=230, height=70)

                            self.btn4 = ttk.Button(user_add, text="CAPABILITY", style='my.TButton', width=20,
                                                   command=cabs)
                            self.btn4.place(x=690, y=70, width=230, height=70)

                            # KC_dd = self.txtfld1.get()
                            # Part_number = self.txtfld2.get()
                            # Rev = self.txtfld3.get()
                            # Centro = self.txtfld4.get()
                            # Kc_Similar = self.txtfld5.get()
                            # Processo = self.txtfld6.get()
                            # Descri = self.txtfld7.get()
                            # Expec = self.txtfld8.get()
                            # Tolerancia = self.txtfld9.get()
                            # Uniade = self.txtfld10.get()
                            # Tipoc = self.txtfld11.get()
                            # Tipod = self.txtfld12.get()
                            # local = self.txtfld13.get()
                            # respq = self.txtfld14.get()
                            # respm = self.txtfld15.get()
                            # produdo = self.txtfld16.get()
                            # proj = self.txtfld17.get()
                            # data = self.txtfld18.get()
                            # status = self.txtfld19.get()

                            def kc_similar():
                                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                           "jdaat2012", "PU_FA_Testing")
                                cursor_SQL = conn_SQL.cursor()

                                query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKCmaster] 
                                WHERE [Espec#]='""" + str(self.txtfld8.get()).strip() + """' AND [Tol#]='""" + str(
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

                            def kc_rr():

                                pass

                            def kc_cap():

                                pass

                            # def submit():
                            #     KC_dd = self.txtfld1.get()
                            #     Part_number = self.txtfld2.get()
                            #     Rev = self.txtfld3.get()
                            #     Centro = self.txtfld4.get()
                            #     Kc_Similar = self.txtfld5.get()
                            #     Processo = self.txtfld6.get()
                            #     Descri = self.txtfld7.get()
                            #     Expec = self.txtfld8.get()
                            #     Tolerancia = self.txtfld9.get()
                            #     Uniade = self.txtfld10.get()
                            #     Tipoc = self.txtfld11.get()
                            #     Tipod = self.txtfld12.get()
                            #     local = self.txtfld13.get()
                            #     respq = self.txtfld14.get()
                            #     respm = self.txtfld15.get()
                            #     produdo = self.txtfld16.get()
                            #     proj = self.txtfld17.get()
                            #     data = self.txtfld18.get()
                            #     status = self.txtfld19.get()
                            #
                            #     # print(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo, Descri, Expec,
                            #     #       Tolerancia, Uniade, Tipoc, Tipod,
                            #     #       local, respq, respm, produdo, proj, data, status)
                            #
                            #     next_randr_update(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo, Descri, Expec,
                            #                       Tolerancia, Uniade, Tipoc, Tipod,
                            #                       local, respq, respm, produdo, proj, data, status)

                            self.btn_kc_sim_check = ttk.Button(window, text="", command=kc_similar)
                            self.btn_kc_sim_check.place(x=1060, y=310, width=25, height=23)

                            """
                            self.btn_rr_check=ttk.Button(window, text="", command=kc_rr)
                            self.btn_rr_check.place(x=380, y=480, width=25, height=23)

                            self.btn_cap_check = ttk.Button(window, text="", command=kc_cap)
                            self.btn_cap_check.place(x=380, y=520, width=25, height=23)
                            """

                            def visitcabs():
                                try:
                                    CABS_ID = self.txtfld20.get()
                                    # print(CABS_ID)

                                    if CABS_ID != "":

                                        # print(CABS_ID)
                                        cabs(CABS_ID)
                                    else:
                                        tk.messagebox.showerror("CREATE RR STUDY", "RR STUDY NOT APPROVED")
                                except:
                                    tk.messagebox.showerror("CREATE RR STUDY", "RR STUDY NOT APPROVED")

                            # self.btn_new_study = ttk.Button(window, text="NEW STUDY",command=visitcabs)
                            # self.btn_new_study.place(x=210, y=580, width=165, height=40)

                            def next_step_insert():

                                MsgBox = tk.messagebox.askquestion('INSERT VALUES',
                                                                   'Are you sure you want to insert data to Master List',
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
                                                                 '""" + str(Part_number) + """', 
                                                                 '""" + str(Rev) + """',
                                                                '""" + str(Kc_Similar) + """', 
                                                                '""" + str(Centro) + """', 
                                                                '""" + str(Processo) + """',
                                                                '""" + str(Descri) + """', 
                                                                '""" + str(Expec) + """',
                                                                '""" + str(Tolerancia) + """',
                                                           '""" + str(Uniade) + """',
                                                            '""" + str(Tipoc) + """',
                                                           '""" + str(Tipod) + """',
                                                          '""" + str(local) + """',
                                                         '""" + str(respq) + """', 
                                                      '""" + str(respm) + """',
                                                       '""" + str(produdo) + """',
                                                    '""" + str(proj) + """',
                                                    '""" + str(data) + """',
                                                    '""" + str(status) + """','','','""" + str(yes_no) + """','','','','','','','','','','','','','',(SELECT GETDATE())
                                                    )

                                                                """

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()
                                            cursor_SQL.close()

                                            # tk.messagebox.showerror("", "WRONG VALUES")

                                            messagebox.showinfo("information", "Added Sucessfully")

                                            # print(local)

                                            if Descri == "Torque" or local == "Lab. CMM" or (
                                                    self.txtfld21.get() == "Não"):
                                                master()
                                            else:
                                                RandR(kc_id=KC_dd, rr_id=0)




                                        except:

                                            messagebox.showerror("error", "Error")


                                    else:

                                        messagebox.showwarning("warning", "Enter Values")


                                else:
                                    tk.messagebox.showinfo('MESSAGE', 'You will now return to the master screen')

                            def turn_button(x=0):
                                if self.txtfld21.get() == "Sim":
                                    self.btn_submit = ttk.Button(window, text="NEXT", command=next_step_insert)
                                    self.btn_submit.place(x=890, y=580, width=165, height=40)
                                else:
                                    self.btn_submit = ttk.Button(window, text="INSERT", command=next_step_insert)
                                    self.btn_submit.place(x=890, y=580, width=165, height=40)

                            self.txtfld21.bind("<<ComboboxSelected>>", turn_button)

                    User_Add_station(user_add)

                # user_add_station()

                class App:
                    def __init__(self):

                        def selectItem(a):
                            curItem = tree.focus()
                            # print(tree.item(curItem)['values'])
                            quantifiers = (tree.item(curItem)['values'])

                            if id_master != 0:
                                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                           "jdaat2012", "PU_FA_Testing")
                                cursor_SQL = conn_SQL.cursor()

                                cursor_SQL.execute("""
SELECT * FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] WHERE [IsObsolete]=0 AND [KC_No]='""" + (
                                    str(id_master).strip()) + """'""")

                                for row in cursor_SQL:
                                    quantifiers = row

                                quantifiers = quantifiers[:-1]

                                conn_SQL.close()

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
                                                                                                     '""" + str(respq) + """', 
                                                                                                  '""" + str(respm) + """',
                                                                                                   '""" + str(produdo) + """',
                                                                                                '""" + str(proj) + """',
                                                                                                '""" + str(data) + """',
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
                        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
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

                if id_master == 0:
                    user_add_station()
                else:
                    a = App()

                a = App()

            def RandR(kc_id=0, rr_id=0):

                load = cv2.imread('Images/start.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/background.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/legend_RR.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(765), int(120)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=1150, y=500)

                image_loader()

                def rr_new():

                    class RR():

                        def __init__(self, window):

                            load = cv2.imread('Images/background.png', 1)
                            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                            load = Image.fromarray(cv2imagex1)
                            load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                            render = ImageTk.PhotoImage(load)
                            img = tk.Label(image=render)
                            img.image = render
                            img.place(x=0, y=140)

                            self.lb_title = Label(window, text="R&R",
                                                  font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9', fg='#34943a')
                            self.lb_title.place(x=550, y=170)

                            self.lb1 = Label(window, text="# KC",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            self.lb1.place(x=5, y=142)

                            self.txtfld1_rr = ttk.Combobox(window, text="#KC_rr", state='readonly',
                                                           font=("Ariel", 10), values=KC)
                            self.txtfld1_rr.place(x=60, y=140)
                            self.txtfld1_rr.set(KC[0])

                            self.lb8 = Label(window, text="Nº Estudo",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb8.place(x=60, y=250)

                            rr_no = Estudo_RR[1][3:]

                            rr_nox = str("RR_") + ((str("00000") + str(int((rr_no)) + 1))[-5:])

                            self.txtfld8_rr = ttk.Combobox(window, text="Nº Estudo", state="readonly",
                                                           font=("Ariel", 10), values=Estudo_RR)
                            self.txtfld8_rr.place(x=230, y=250)
                            self.txtfld8_rr.set(rr_nox)

                            # self.txtfld8_rr.configure(state=DISABLED)

                            self.lb9 = Label(window, text="Item",
                                             font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb9.place(x=620, y=250)

                            self.txtfld9_rr = ttk.Combobox(window,

                                                           text="Item",
                                                           font=("Ariel", 10), values=Item)
                            self.txtfld9_rr.place(x=780, y=250)
                            self.txtfld9_rr.set("")

                            self.lb10 = Label(window, text="Descrição KC",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb10.place(x=60, y=290)

                            self.txtfld10_rr = ttk.Combobox(window, text="Descrição KC",
                                                            font=("Ariel", 10), values=Descrição_KC)
                            self.txtfld10_rr.place(x=230, y=290)
                            self.txtfld10_rr.set("")

                            self.lb11 = Label(window, text="Espec.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb11.place(x=620, y=290)

                            self.txtfld11_rr = ttk.Combobox(window,

                                                            text="Espec.",
                                                            font=("Ariel", 10), values=Espec)
                            self.txtfld11_rr.place(x=780, y=290)
                            self.txtfld11_rr.set("")

                            self.lb12 = Label(window, text="Tol.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb12.place(x=60, y=330)

                            self.txtfld12_rr = ttk.Combobox(window, text="Tol.",
                                                            font=("Ariel", 10), values=Tol)
                            self.txtfld12_rr.place(x=230, y=330)
                            self.txtfld12_rr.set("")

                            self.lb13 = Label(window, text="Unid.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb13.place(x=620, y=330)

                            self.txtfld13_rr = ttk.Combobox(window,

                                                            text="Unid.",
                                                            font=("Ariel", 10), values=Unid)
                            self.txtfld13_rr.place(x=780, y=330)
                            self.txtfld13_rr.set("")

                            self.lb14 = Label(window, text="Família",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb14.place(x=60, y=370)

                            self.txtfld14_rr = ttk.Combobox(window, text="Família",
                                                            font=("Ariel", 10), values=Família)
                            self.txtfld14_rr.place(x=230, y=370)
                            self.txtfld14_rr.set("")

                            self.lb15 = Label(window, text="Instrumento",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb15.place(x=620, y=370)

                            self.txtfld15_rr = ttk.Combobox(window,

                                                            text="Instrumento",
                                                            font=("Ariel", 10), values=Instrumento)
                            self.txtfld15_rr.place(x=780, y=370)
                            self.txtfld15_rr.set("")

                            self.lb16 = Label(window, text="Estudo",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb16.place(x=60, y=410)

                            self.txtfld16_rr = ttk.Combobox(window, text="Estudo",
                                                            font=("Ariel", 10), values=Estudo)
                            self.txtfld16_rr.place(x=230, y=410)
                            self.txtfld16_rr.set("")

                            self.lb17 = Label(window, text="R&R",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb17.place(x=620, y=410)

                            print(RR, "hggs")

                            self.txtfld17_rr = ttk.Combobox(window,

                                                            text="R&R",
                                                            font=("Ariel", 10), values=RR_data)
                            self.txtfld17_rr.place(x=780, y=410)
                            self.txtfld17_rr.set("")

                            self.lb18 = Label(window, text="Classificação",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb18.place(x=60, y=450)

                            self.txtfld18_rr = ttk.Combobox(window, text="Classificação.",
                                                            font=("Ariel", 10), values=Classificação)
                            self.txtfld18_rr.place(x=230, y=450)
                            self.txtfld18_rr.set("")

                            self.lb19 = Label(window, text="Data",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb19.place(x=620, y=450)

                            self.txtfld19_rr = ttk.Combobox(window,

                                                            text="Data",
                                                            font=("Ariel", 10), values=Data)
                            self.txtfld19_rr.place(x=780, y=450)
                            self.txtfld19_rr.set("")

                            self.lb19_link = Label(window, text="Report Link",
                                                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            self.lb19_link.place(x=700, y=142)

                            self.txtfld19_rr_link = Entry(window,

                                                          text="url",
                                                          font=("Ariel", 10))
                            self.txtfld19_rr_link.place(x=800, y=140, width=345)
                            self.txtfld19_rr_link.insert(0, " ")

                            def study_rr():
                                KC_rr = self.txtfld1_rr.get()
                                RR_Study_No = self.txtfld8_rr.get()
                                Item = self.txtfld9_rr.get()
                                Description = self.txtfld10_rr.get()
                                RR_Specification = self.txtfld11_rr.get()
                                RR_Tolerance = self.txtfld12_rr.get()
                                RR_Unit = self.txtfld13_rr.get()
                                RR_Family = self.txtfld14_rr.get()
                                Instrument = self.txtfld15_rr.get()
                                RR_Study = self.txtfld16_rr.get()
                                RR = self.txtfld17_rr.get()
                                Classification = self.txtfld18_rr.get()
                                Created_Date = self.txtfld19_rr.get()
                                link = self.txtfld19_rr_link.get()

                                messagebox.showwarning("FIRST SUBMIT", "PLEASE FILL UP AND SUBMIT BEFORE YOU PROCEED")

                            def insert_rr():

                                MsgBox = tk.messagebox.askquestion('INSERT DATA',
                                                                   'Are you sure you want to insert data to RR TABLE with RR ID ' + self.txtfld8_rr.get() + ' AND KC ID ' + self.txtfld1_rr.get(),
                                                                   icon='warning')

                                # print(quantifiers)
                                if MsgBox == 'yes':

                                    print(self.txtfld19_rr_link.get())

                                    KC_rr = self.txtfld1_rr.get()
                                    RR_Study_No = self.txtfld8_rr.get()
                                    Item = self.txtfld9_rr.get()
                                    Description = self.txtfld10_rr.get()
                                    RR_Specification = self.txtfld11_rr.get()
                                    RR_Tolerance = self.txtfld12_rr.get()
                                    RR_Unit = self.txtfld13_rr.get()
                                    RR_Family = self.txtfld14_rr.get()
                                    Instrument = self.txtfld15_rr.get()
                                    RR_Study = self.txtfld16_rr.get()
                                    RR = self.txtfld17_rr.get()
                                    Classification = self.txtfld18_rr.get()
                                    Created_Date = self.txtfld19_rr.get()
                                    link = self.txtfld19_rr_link.get()

                                    if ((str(self.txtfld1_rr.get())).strip() != "" and (
                                            str(self.txtfld8_rr.get())).strip() != "" and (
                                            str(self.txtfld9_rr.get())).strip() != "" and (
                                            str(self.txtfld10_rr.get())).strip() != "" and (
                                            str(self.txtfld11_rr.get())).strip() != ""
                                            and (str(self.txtfld12_rr.get())).strip() != ""
                                            and (str(self.txtfld13_rr.get())).strip() != ""
                                            and (str(self.txtfld14_rr.get())).strip() != ""
                                            and (str(self.txtfld15_rr.get())).strip() != ""
                                            and (str(self.txtfld16_rr.get())).strip() != ""
                                            and (str(self.txtfld17_rr.get())).strip() != ""
                                            and (str(self.txtfld18_rr.get())).strip() != ""
                                            and (str(self.txtfld19_rr.get())).strip() != ""
                                    ):

                                        try:

                                            Req_rr = ""
                                            Req_Result = ""

                                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                                       "jdaat",
                                                                       "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            #                 query = """INSERT INTO [PU_FA_Testing].[dbo].[RR_STUDY]([KC_ID],[RR_STUDY_No],[Req_RR],[RR_Result],[Report_Link],[Item],[Description],[RR_Specification],
                                            # [RR_Tolerance],[RR_Unit],[RR_Family],[Instrument],[RR_Study],[RR],[Classification] ,[Created_Date])
                                            #                 VALUES((SELECT TOP 1 [KC_ID] FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] WHERE [KC_No]='""" + (
                                            #                     (str(self.txtfld1_rr.get())).strip()) + """')
                                            #                 ,'""" + ((str(self.txtfld8_rr.get())).strip()) + """','""" +str(Req_rr) + """','""" +str(Req_Result) + """','""" +((str(self.txtfld19_rr_link.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld9_rr.get())).strip()) + """','""" + (
                                            #                             (str(self.txtfld10_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld11_rr.get())).strip()) + """','""" + (
                                            #                             (str(self.txtfld12_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld13_rr.get())).strip()) + """','""" + (
                                            #                             (str(self.txtfld14_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld15_rr.get())).strip()) + """','""" + (
                                            #                             (str(self.txtfld16_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld17_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld18_rr.get())).strip()) + """',
                                            #                 '""" + ((str(self.txtfld19_rr.get())).strip()) + """'
                                            #                 )"""

                                            query = """INSERT INTO [PU_FA_Testing].[dbo].[RRmaster]
               ([# KC],[Nº Estudo],[Item],[Descrição KC],[Espec#],[Tol#],[Unid#],[Família],[Instrumento],[Estudo],[R&R],
               [Classificação],[Data],[Link])
               VALUES('""" + (KC_rr) + """',
                      '""" + (RR_Study_No) + """',
                      '""" + (Item) + """', 
                      '""" + (Description) + """' ,
                      '""" + (RR_Specification) + """',
                      '""" + (RR_Tolerance) + """',
                      '""" + (RR_Unit) + """',
                      '""" + (RR_Family) + """',
                      '""" + (Instrument) + """',
                      '""" + (RR_Study) + """',
                      '""" + (RR) + """',
                      '""" + (Classification) + """',
                      '""" + (Created_Date) + """','""" + (link) + """')"""

                                            # print(query)

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()

                                            query = """UPDATE [PU_FA_Testing].[dbo].[KC] SET [# Estudo]='""" + (
                                                RR_Study_No) + """' , Resultado='""" + (
                                                        Classification) + """' WHERE [# KC]='""" + (KC_rr) + """'"""

                                            # print(query)

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()

                                            cursor_SQL.close()

                                            # tk.messagebox.showerror("", "WRONG VALUES")

                                            messagebox.showinfo("Information", "Added Sucessfully")

                                            MsgBoxx = tk.messagebox.askquestion('INFORMATION',
                                                                                'DO YOU WANT TO CREATE CAPABILITY STUDY WITH KC ID ' + (
                                                                                    KC_rr),
                                                                                icon='warning')

                                            if MsgBoxx == 'yes':
                                                cabs(kc_id)
                                            else:
                                                master()



                                        except:

                                            messagebox.showerror("error", "Error")





                                    else:

                                        messagebox.showwarning("warning", "Enter Values")

                                else:
                                    tk.messagebox.showinfo('Return', 'You will now return to the RR Table')

                            self.btn_submit = ttk.Button(window, text="SUBMIT", command=insert_rr)
                            self.btn_submit.place(x=230, y=550, width=165, height=50)

                            self.btn_cap_study = ttk.Button(window, text="NEW STUDY", command=study_rr)
                            self.btn_cap_study.place(x=780, y=550, width=165, height=50)

                    RR(user_add)

                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()

                query = """SELECT * FROM [PU_FA_Testing].[dbo].[RRmaster] WHERE [Nº Estudo] IS NOT NULL ORDER BY [Nº Estudo] DESC"""

                cursor_SQL.execute(query)

                data = []

                KC_codes = []

                for row in cursor_SQL:
                    # print(row)
                    data.append([*row])

                query = """SELECT [# KC]  FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL ORDER BY [# KC] DESC"""

                cursor_SQL.execute(query)

                for row in cursor_SQL:
                    KC_codes.append(*row)

                # "# KC","Nº Estudo","Item","Descrição KC","Espec.","Tol.","Unid.","Família","Instrumento","Estudo","R&R","Classificação","Data","Link"

                KC = sorted(set(KC_codes), reverse=True)
                Estudo_RR = []
                Item = []
                Descrição_KC = []
                Espec = []
                Tol = []
                Unid = []
                Família = []
                Instrumento = []
                Estudo = []
                RR_data = []
                Classificação = []
                Data = []
                Link = []

                for x in range(0, len(data)):
                    if data[x][1] != None:
                        Estudo_RR.append(data[x][1])

                Estudo_RR = sorted(set(Estudo_RR), reverse=True)

                Estudo_RR.insert(0, "NOT APPLICABLE")

                for x in range(0, len(data)):
                    if data[x][2] != None:
                        Item.append(data[x][2])

                Item = sorted(set(Item))

                for x in range(0, len(data)):
                    if data[x][3] != None:
                        Descrição_KC.append(data[x][3])

                Descrição_KC = sorted(set(Descrição_KC))

                for x in range(0, len(data)):
                    if data[x][4] != None:
                        Espec.append(data[x][4])

                Espec = sorted(set(Espec))

                for x in range(0, len(data)):
                    if data[x][5] != None:
                        Tol.append(data[x][5])

                Tol = sorted(set(Tol))

                for x in range(0, len(data)):
                    if data[x][6] != None:
                        Unid.append(data[x][6])

                Unid = sorted(set(Unid))

                for x in range(0, len(data)):
                    if data[x][7] != None:
                        Família.append(data[x][7])

                Família = sorted(set(Família))

                for x in range(0, len(data)):
                    if data[x][8] != None:
                        Instrumento.append(data[x][8])

                Instrumento = sorted(set(Instrumento))

                for x in range(0, len(data)):
                    if data[x][9] != None:
                        Estudo.append(data[x][9])

                Estudo = sorted(set(Estudo))

                for x in range(0, len(data)):
                    if data[x][10] != None:
                        RR_data.append(data[x][10])

                RR_data = sorted(set(RR_data))

                for x in range(0, len(data)):
                    if data[x][11] != None:
                        Classificação.append(data[x][11])

                Classificação = sorted(set(Classificação))

                for x in range(0, len(data)):
                    if data[x][12] != None:
                        Data.append(data[x][12])

                Data = sorted(set(Data), reverse=True)

                class App:
                    def __init__(self):

                        def selectItem(a):
                            curItem = tree.focus()

                            # print(tree.item(curItem)['values'])
                            quantifiers = (tree.item(curItem)['values'])

                            if rr_id != 0:
                                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                           "jdaat2012", "PU_FA_Testing")
                                cursor_SQL = conn_SQL.cursor()

                                cursor_SQL.execute(
                                    """SELECT * FROM [PU_FA_Testing].[dbo].[RR_STUDY] WHERE [RR_STUDY_No]='""" + (
                                        str(id_rr).strip()) + """'""")

                                for row in cursor_SQL:
                                    quantifiers = row

                                quantifiers = quantifiers[:-1]

                                conn_SQL.close()

                            # print(quantifiers)

                            def rr_modify():
                                # CLASS FOR ADDING STATION
                                class RR():

                                    def __init__(self, window):
                                        load = cv2.imread('Images/background.png', 1)
                                        cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                                        load = Image.fromarray(cv2imagex1)
                                        load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                                        render = ImageTk.PhotoImage(load)
                                        img = tk.Label(image=render)
                                        img.image = render
                                        img.place(x=0, y=140)

                                        try:
                                            image_loader(str(quantifiers[2]))
                                        except:
                                            pass

                                        # LABEL AND TEXT BOX TO ENTER DETAILS OF ALL ELEMENTS OF A STATION
                                        self.lb_title = Label(window, text="R&R",
                                                              font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9',
                                                              fg='#34943a')
                                        self.lb_title.place(x=550, y=170)

                                        self.lb1 = Label(window, text="#KC",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                                        self.lb1.place(x=5, y=142)

                                        self.txtfld1_rr = ttk.Combobox(window, text="#KC_rr",
                                                                       font=("Ariel", 10))
                                        self.txtfld1_rr.place(x=60, y=140)
                                        self.txtfld1_rr.set(quantifiers[0])

                                        self.lb8 = Label(window, text="Nº Estudo",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                         anchor='e')
                                        self.lb8.place(x=60, y=250)

                                        rr_no = Estudo_RR[1][3:]

                                        rr_nox = str("RR_") + ((str("00000") + str(int((rr_no)) + 1))[-5:])

                                        self.txtfld8_rr = ttk.Combobox(window, text="Nº Estudo", state="readonly",
                                                                       font=("Ariel", 10), values=Estudo_RR)
                                        self.txtfld8_rr.place(x=230, y=250)
                                        self.txtfld8_rr.set(quantifiers[1])

                                        # self.txtfld8_rr.configure(state=DISABLED)

                                        self.lb9 = Label(window, text="Item",
                                                         font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                         anchor='e')
                                        self.lb9.place(x=620, y=250)

                                        self.txtfld9_rr = ttk.Combobox(window,

                                                                       text="Item",
                                                                       font=("Ariel", 10), values=Item)
                                        self.txtfld9_rr.place(x=780, y=250)
                                        self.txtfld9_rr.set(quantifiers[2])

                                        self.lb10 = Label(window, text="Descrição KC",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb10.place(x=60, y=290)

                                        self.txtfld10_rr = ttk.Combobox(window, text="Descrição KC",
                                                                        font=("Ariel", 10), values=Descrição_KC)
                                        self.txtfld10_rr.place(x=230, y=290)
                                        self.txtfld10_rr.set(quantifiers[3])

                                        self.lb11 = Label(window, text="Espec.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb11.place(x=620, y=290)

                                        self.txtfld11_rr = ttk.Combobox(window,

                                                                        text="Espec.",
                                                                        font=("Ariel", 10), values=Espec)
                                        self.txtfld11_rr.place(x=780, y=290)
                                        self.txtfld11_rr.set(quantifiers[4])

                                        self.lb12 = Label(window, text="Tol.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb12.place(x=60, y=330)

                                        self.txtfld12_rr = ttk.Combobox(window, text="Tol.",
                                                                        font=("Ariel", 10), values=Tol)
                                        self.txtfld12_rr.place(x=230, y=330)
                                        self.txtfld12_rr.set(quantifiers[5])

                                        self.lb13 = Label(window, text="Unid.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb13.place(x=620, y=330)

                                        self.txtfld13_rr = ttk.Combobox(window,

                                                                        text="Unid.",
                                                                        font=("Ariel", 10), values=Unid)
                                        self.txtfld13_rr.place(x=780, y=330)
                                        self.txtfld13_rr.set(quantifiers[6])

                                        self.lb14 = Label(window, text="Família",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb14.place(x=60, y=370)

                                        self.txtfld14_rr = ttk.Combobox(window, text="Família",
                                                                        font=("Ariel", 10), values=Família)
                                        self.txtfld14_rr.place(x=230, y=370)
                                        self.txtfld14_rr.set(quantifiers[7])

                                        self.lb15 = Label(window, text="Instrumento",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb15.place(x=620, y=370)

                                        self.txtfld15_rr = ttk.Combobox(window,

                                                                        text="Instrumento",
                                                                        font=("Ariel", 10), values=Instrumento)
                                        self.txtfld15_rr.place(x=780, y=370)
                                        self.txtfld15_rr.set(quantifiers[8])

                                        self.lb16 = Label(window, text="Estudo",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb16.place(x=60, y=410)

                                        self.txtfld16_rr = ttk.Combobox(window, text="Estudo",
                                                                        font=("Ariel", 10), values=Estudo)
                                        self.txtfld16_rr.place(x=230, y=410)
                                        self.txtfld16_rr.set(quantifiers[9])

                                        self.lb17 = Label(window, text="R&R",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb17.place(x=620, y=410)

                                        self.txtfld17_rr = ttk.Combobox(window,

                                                                        text="R&R",
                                                                        font=("Ariel", 10), values=RR_data)
                                        self.txtfld17_rr.place(x=780, y=410)
                                        self.txtfld17_rr.set(quantifiers[10])

                                        self.lb18 = Label(window, text="Classificação",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb18.place(x=60, y=450)

                                        self.txtfld18_rr = ttk.Combobox(window, text="Classificação.",
                                                                        font=("Ariel", 10), values=Classificação)
                                        self.txtfld18_rr.place(x=230, y=450)
                                        self.txtfld18_rr.set(quantifiers[11])

                                        self.lb19 = Label(window, text="Data",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb19.place(x=620, y=450)

                                        self.txtfld19_rr = ttk.Combobox(window,

                                                                        text="Data",
                                                                        font=("Ariel", 10), values=Data)
                                        self.txtfld19_rr.place(x=780, y=450)
                                        self.txtfld19_rr.set(quantifiers[12])

                                        self.lb19_link = Label(window, text="Report Link",
                                                               font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                                        self.lb19_link.place(x=700, y=142)

                                        self.txtfld19_rr_link = Entry(window,

                                                                      text="url",
                                                                      font=("Ariel", 10))
                                        self.txtfld19_rr_link.place(x=800, y=140, width=345)

                                        self.txtfld19_rr_link.delete(0, END)

                                        self.txtfld19_rr_link.insert(0, str(quantifiers[13]))

                                        def study_rr():
                                            KC_rr = quantifiers[0]
                                            RR_Study_No = self.txtfld8_rr.get()
                                            Item = self.txtfld9_rr.get()
                                            Description = self.txtfld10_rr.get()
                                            RR_Specification = self.txtfld11_rr.get()
                                            RR_Tolerance = self.txtfld12_rr.get()
                                            RR_Unit = self.txtfld13_rr.get()
                                            RR_Family = self.txtfld14_rr.get()
                                            Instrument = self.txtfld15_rr.get()
                                            RR_Study = self.txtfld16_rr.get()
                                            RR = self.txtfld17_rr.get()
                                            Classification = self.txtfld18_rr.get()
                                            Created_Date = self.txtfld19_rr.get()

                                            openRRFormat(KC_rr)

                                            # print(KC_rr,
                                            # RR_Study_No,
                                            # Item ,
                                            # Description,
                                            # RR_Specification,
                                            # RR_Tolerance,
                                            # RR_Unit,
                                            # RR_Family ,
                                            # Instrument,
                                            # RR_Study ,
                                            # RR,
                                            # Classification,
                                            # Created_Date)

                                            # respq = self.txtfld8_cap.get()
                                            # respm = self.txtfld8_cap.get()
                                            # produdo = self.txtfld8_cap.get()
                                            # proj = self.txtfld8_cap.get()
                                            # data = self.txtfld8_cap.get()
                                            # status = self.txtfld8_cap.get()
                                            #
                                            # print(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo, Descri, Expec,
                                            #       Tolerancia, Uniade, Tipoc, Tipod,
                                            #       local, respq, respm, produdo, proj, data, status)
                                            #
                                            # next_randr_update(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo,
                                            #                   Descri, Expec,
                                            #                   Tolerancia, Uniade, Tipoc, Tipod,
                                            #                   local, respq, respm, produdo, proj, data, status)

                                        def update_cap():

                                            # print(quantifiers)

                                            if ((str(self.txtfld1_rr.get())).strip() != "" and (
                                                    str(self.txtfld8_rr.get())).strip() != "" and (
                                                    str(self.txtfld9_rr.get())).strip() != "" and (
                                                    str(self.txtfld10_rr.get())).strip() != "" and (
                                                    str(self.txtfld11_rr.get())).strip() != ""
                                                    and (str(self.txtfld12_rr.get())).strip() != ""
                                                    and (str(self.txtfld13_rr.get())).strip() != ""
                                                    and (str(self.txtfld14_rr.get())).strip() != ""
                                                    and (str(self.txtfld15_rr.get())).strip() != ""
                                                    and (str(self.txtfld16_rr.get())).strip() != ""
                                                    and (str(self.txtfld17_rr.get())).strip() != ""
                                                    and (str(self.txtfld18_rr.get())).strip() != ""
                                                    and (str(self.txtfld19_rr.get())).strip() != ""
                                            ):

                                                try:

                                                    Req_rr = ""
                                                    Req_Result = ""

                                                    conn_SQL = pymssql.connect(
                                                        "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                        "jdaat",
                                                        "jdaat2012", "PU_FA_Testing")
                                                    cursor_SQL = conn_SQL.cursor()

                                                    query = """UPDATE [PU_FA_Testing].[dbo].[RR_STUDY]
                                    SET  
                                    [RR_Study_No] ='""" + ((str(self.txtfld8_rr.get())).strip()) + """' ,
                                    [Req_RR]='""" + str(Req_rr) + """',
                                    [RR_Result]='""" + str(Req_Result) + """',
                                    [Report_Link]='""" + ((str(self.txtfld19_rr_link.get())).strip()) + """',
                                    [Item] ='""" + ((str(
                                                        self.txtfld9_rr.get())).strip()) + """', [Description] = '""" + (
                                                                (str(self.txtfld10_rr.get())).strip()) + """' , 
                                    [RR_Specification] = '""" + ((str(
                                                        self.txtfld11_rr.get())).strip()) + """',  [RR_Tolerance] = '""" + (
                                                                (str(self.txtfld12_rr.get())).strip()) + """',  
                                    [RR_Unit] = '""" + ((str(
                                                        self.txtfld13_rr.get())).strip()) + """',  [RR_Family] = '""" + (
                                                                (str(self.txtfld14_rr.get())).strip()) + """',  
                                    [Instrument] = '""" + ((str(
                                                        self.txtfld15_rr.get())).strip()) + """',[RR_Study] = '""" + (
                                                                (str(self.txtfld16_rr.get())).strip()) + """',
                                                                [RR] = '""" + (
                                                                (str(self.txtfld17_rr.get())).strip()) + """',
                                     [Classification] = '""" + ((str(self.txtfld18_rr.get())).strip()) + """',  
                                     [Created_Date] = '""" + ((str(
                                                        self.txtfld19_rr.get())).strip()) + """'
                                     WHERE [RR_ID]='""" + str(quantifiers[-1]) + """'"""

                                                    # print(query)

                                                    cursor_SQL.execute(query)
                                                    conn_SQL.commit()
                                                    cursor_SQL.close()

                                                    # tk.messagebox.showerror("", "WRONG VALUES")

                                                    messagebox.showinfo("information", "Updated Sucessfully")

                                                    RandR()

                                                except:

                                                    messagebox.showerror("error", "Error")


                                            else:

                                                messagebox.showwarning("warning", "Enter Values")

                                        # self.btn_submit = ttk.Button(window, text="UPDATE", command=update_cap)
                                        # self.btn_submit.place(x=230, y=550, width=165, height=50)

                                        self.btn_cap_study = ttk.Button(window, text="NEW R&R STUDY", command=study_rr)
                                        self.btn_cap_study.place(x=780, y=550, width=165, height=50)

                                        # self.btn_submit = ttk.Button(window, text="SUBMIT")
                                        # self.btn_submit.place(x=520, y=650, width=250, height=60)

                                RR(user_add)

                            rr_modify()

                        frame = Frame(user_add)
                        frame.place(x=0, y=650)

                        # print(data)

                        tree = ttk.Treeview(frame,
                                            columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                                            height=17, show="headings")
                        tree.pack(side='left')
                        tree.bind('<ButtonRelease-1>', selectItem)

                        if id_rr != 0:
                            selectItem(a=id_rr)

                        # "# KC", "Nº Estudo", "Item", "Descrição KC", "Espec.", "Tol.", "Unid.", "Família", "Instrumento", "Estudo", "R&R", "Classificação", "Data", "Link"

                        val = ["# KC", "Nº Estudo", "Item.", "Descrição KC",
                               "Espec", "Tol.", "Unid.",
                               "Família", "Instrumento", "Estudo", "R&R", "Classificação",
                               "Data", "Link"]

                        for i in range(1, len(val) + 1):
                            tree.heading(i, text=val[i - 1])

                        # tree.heading(2, text="Column 2")
                        # tree.heading(3, text="Column 3")

                        for i in range(1, len(val) + 1):
                            tree.column(i, width=136, anchor='center')

                        # tree.column(2, width=100)
                        # tree.column(3, width=100)

                        scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
                        scroll.pack(side='right', fill='y')

                        """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
                        scrollx.pack(side='bottom', fill='x')"""

                        tree.configure(yscrollcommand=scroll.set)

                        iterx = 0
                        for valx in data:

                            percentage = str(round((valx[10] * 100), 3)) + "%"
                            if float(percentage[:-1]) > 18:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                               , percentage, valx[11], valx[12], valx[13]),
                                            tags=('odd',))
                            else:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                               , percentage, valx[11], valx[12], valx[13]),
                                            tags=('even',))

                            iterx += 1

                        tree.tag_configure('odd', background='#008001')
                        tree.tag_configure('even', background='#FFFF00')

                        conn_SQL.close()

                        def command(x=0):

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

                            if (self.tkvar0.get()) != '# KC':
                                var0 = self.tkvar0.get()
                            if (self.tkvar1.get()) != 'Nº Estudo':
                                var1 = self.tkvar1.get()
                            if (self.tkvar2.get()) != 'Item':
                                var2 = self.tkvar2.get()
                            if (self.tkvar3.get()) != 'Descrição KC':
                                var3 = self.tkvar3.get()
                            if (self.tkvar4.get()) != 'Espec.':
                                var4 = self.tkvar4.get()
                            if (self.tkvar5.get()) != 'Tol.':
                                var5 = self.tkvar5.get()
                            if (self.tkvar6.get()) != 'Unid.':
                                var6 = self.tkvar6.get()
                            if (self.tkvar7.get()) != 'Família':
                                var7 = self.tkvar7.get()
                            if (self.tkvar8.get()) != 'Instrumento':
                                var8 = self.tkvar8.get()
                            if (self.tkvar9.get()) != 'Estudo':
                                var9 = self.tkvar9.get()
                            if (self.tkvar10.get()) != 'R&R':
                                var10 = self.tkvar10.get()
                            if (self.tkvar11.get()) != 'Classificação':
                                var11 = self.tkvar11.get()
                            if (self.tkvar12.get()) != 'Data':
                                var12 = self.tkvar12.get()

                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                       "jdaat2012", "PU_FA_Testing")
                            cursor_SQL = conn_SQL.cursor()

                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[RRmaster] WHERE [# KC] LIKE '%""" + str(
                                var0) + """%' 
                            AND ([Nº Estudo] LIKE '%""" + str(var1) + """%' OR [Nº Estudo] IS NULL)

                                                AND ([Item] LIKE '%""" + str(var2) + """%' OR [Item] IS NULL)
                            AND ([Descrição KC] LIKE '%""" + str(var3) + """%' OR [Descrição KC] IS NULL)
                                                AND ([Espec#] LIKE '%""" + str(var4) + """%' OR [Espec#] IS NULL)
                            AND ([Tol#] LIKE '%""" + str(var5) + """%' OR [Tol#] IS NULL)
                                                AND ([Unid#] LIKE '%""" + str(var6) + """%' OR [Unid#] IS NULL)
                            AND ([Família] LIKE '%""" + str(var7) + """%' OR [Família] IS NULL)
                                                AND ([Instrumento] LIKE '%""" + str(var8) + """%' OR [Instrumento] IS NULL)
                            AND ([Estudo] LIKE '%""" + str(var9) + """%' OR [Estudo] IS NULL)
                                                AND ([R&R] LIKE '%""" + str(var10) + """%' OR [R&R] IS NULL)
                            AND ([Classificação] LIKE '%""" + str(var11) + """%' OR [Classificação] IS NULL)
                                                AND ([Data] LIKE '%""" + str(var12) + """%' OR [Data] IS NULL)

                            """

                            # print(query)

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

                                percentage = str(round((valx[10] * 100), 3)) + "%"
                                if float(percentage[:-1]) > 18:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , percentage, valx[11], valx[12], valx[13]),
                                                tags=('odd',))
                                else:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , percentage, valx[11], valx[12], valx[13]),
                                                tags=('even',))

                                iterx += 1

                            tree.tag_configure('odd', background='#008001')
                            tree.tag_configure('even', background='#FFFF00')

                            conn_SQL.close()

                        self.tkvarbtn0 = ttk.Button(window, text="", width=450)
                        self.tkvarbtn0.place(x=0, y=625, height=30)

                        self.tkvar0 = ttk.Combobox(window, text="tkvar0",
                                                   font=("Ariel", 10), values=KC, width=17, justify='center')
                        self.tkvar0.place(x=0, y=629)
                        self.tkvar0.set("# KC")

                        self.tkvar0.bind("<<ComboboxSelected>>", command)

                        self.tkvar1 = ttk.Combobox(window, text="tkvar1",
                                                   font=("Ariel", 10), values=Estudo_RR, width=16, justify='center')
                        self.tkvar1.place(x=138, y=629)
                        self.tkvar1.set("Nº Estudo")
                        self.tkvar1.bind("<<ComboboxSelected>>", command)

                        self.tkvar2 = ttk.Combobox(window, text="tkvar2",
                                                   font=("Ariel", 10), values=Item, width=17, justify='center')
                        self.tkvar2.place(x=270, y=629)
                        self.tkvar2.set("Item")

                        self.tkvar2.bind("<<ComboboxSelected>>", command)

                        self.tkvar3 = ttk.Combobox(window, text="tkvar3",
                                                   font=("Ariel", 10), values=Descrição_KC, width=16, justify='center')
                        self.tkvar3.place(x=410, y=629)
                        self.tkvar3.set("Descrição KC")

                        self.tkvar3.bind("<<ComboboxSelected>>", command)

                        self.tkvar4 = ttk.Combobox(window, text="tkvar4",
                                                   font=("Ariel", 10), values=Espec, width=17, justify='center')
                        self.tkvar4.place(x=543, y=629)
                        self.tkvar4.set("Espec.")

                        self.tkvar4.bind("<<ComboboxSelected>>", command)

                        self.tkvar5 = ttk.Combobox(window, text="tkvar5",
                                                   font=("Ariel", 10), values=Tol, width=17, justify='center')
                        self.tkvar5.place(x=680, y=629)
                        self.tkvar5.set("Tol.")

                        self.tkvar5.bind("<<ComboboxSelected>>", command)

                        self.tkvar6 = ttk.Combobox(window, text="tkvar6",
                                                   font=("Ariel", 10), values=Unid, width=16, justify='center')
                        self.tkvar6.place(x=818, y=629)
                        self.tkvar6.set("Unid.")
                        self.tkvar6.bind("<<ComboboxSelected>>", command)

                        self.tkvar7 = ttk.Combobox(window, text="tkvar7",
                                                   font=("Ariel", 10), values=Família, width=17, justify='center')
                        self.tkvar7.place(x=948, y=629)
                        self.tkvar7.set("Família")
                        self.tkvar7.bind("<<ComboboxSelected>>", command)

                        self.tkvar8 = ttk.Combobox(window, text="tkvar8",
                                                   font=("Ariel", 10), values=Instrumento, width=17, justify='center')
                        self.tkvar8.place(x=1086, y=629)
                        self.tkvar8.set("Instrumento")
                        self.tkvar8.bind("<<ComboboxSelected>>", command)

                        self.tkvar9 = ttk.Combobox(window, text="tkvar9",
                                                   font=("Ariel", 10), values=Estudo, width=16, justify='center')
                        self.tkvar9.place(x=1224, y=629)
                        self.tkvar9.set("Estudo")
                        self.tkvar9.bind("<<ComboboxSelected>>", command)

                        self.tkvar10 = ttk.Combobox(window, text="tkvar10",
                                                    font=("Ariel", 10), values=RR_data, width=17, justify='center')
                        self.tkvar10.place(x=1355, y=629)
                        self.tkvar10.set("R&R")
                        self.tkvar10.bind("<<ComboboxSelected>>", command)

                        self.tkvar11 = ttk.Combobox(window, text="tkvar11",
                                                    font=("Ariel", 10), values=Classificação, width=17,
                                                    justify='center')
                        self.tkvar11.place(x=1495, y=629)
                        self.tkvar11.set("Classificação")
                        self.tkvar11.bind("<<ComboboxSelected>>", command)

                        self.tkvar12 = ttk.Combobox(window, text="tkvar12",
                                                    font=("Ariel", 10), values=Data, width=16, justify='center')
                        self.tkvar12.place(x=1634, y=629)
                        self.tkvar12.set("Data")
                        self.tkvar12.bind("<<ComboboxSelected>>", command)

                        self.tkvarbtn1 = ttk.Button(window, text="SEARCH", width=22, command=command)
                        self.tkvarbtn1.place(x=1768, y=628)

                if id_rr == 0:
                    rr_new()
                else:
                    a = App()

                a = App()

            def cabs(id_cabs=0):

                load = cv2.imread('Images/start.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/background.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/legend_CPK.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(765), int(120)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=1150, y=500)

                # side_search()

                def capability_new():

                    # CLASS FOR ADDING STATION
                    class Capability():

                        def __init__(self, window):
                            load = cv2.imread('Images/background.png', 1)
                            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                            load = Image.fromarray(cv2imagex1)
                            load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                            render = ImageTk.PhotoImage(load)
                            img = tk.Label(image=render)
                            img.image = render
                            img.place(x=0, y=140)

                            image_loader()

                            self.lb_title = Label(window, text="Capability", fg='#34943a',
                                                  font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9')
                            self.lb_title.place(x=500, y=170)

                            self.lb1 = Label(window, text="#KC", fg='#34943a',
                                             font=("Ariel", 10), bg='#feffd9')
                            self.lb1.place(x=5, y=142)

                            self.txtfld1 = ttk.Combobox(window, text="#KC_CAP", state='readonly',
                                                        font=("Ariel", 10), values=KC)
                            self.txtfld1.place(x=60, y=140)

                            self.txtfld1.set(str(KC[0]))

                            # self.txtfld1.config(state=DISABLED)

                            self.lb8 = Label(window, text="#Estudo", fg='#34943a',
                                             font=("Ariel", 10), bg='#feffd9', width=19, anchor='e')
                            self.lb8.place(x=60, y=250)

                            self.txtfld8_cap = ttk.Combobox(window, text="#Estudo",
                                                            font=("Ariel", 10),
                                                            values=Estudo_CAP)
                            self.txtfld8_cap.place(x=230, y=250)

                            cap_no = Estudo_CAP[1][3:]

                            cap_no = str("EC_") + ((str("000000") + str(int(cap_no) + 1))[-6:])

                            self.txtfld8_cap.set(cap_no)

                            self.lb9 = Label(window, text="Item", fg='#34943a',
                                             font=("Ariel", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb9.place(x=620, y=250)

                            self.txtfld9_cap = ttk.Combobox(window,
                                                            text="Item",
                                                            font=("Ariel", 10),
                                                            values=Item)
                            self.txtfld9_cap.place(x=780, y=250)
                            self.txtfld9_cap.set("")

                            self.lb10 = Label(window, text="Processo",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb10.place(x=60, y=290)

                            self.txtfld10_cap = ttk.Combobox(window, text="Processo",
                                                             font=("Ariel", 10), values=Processo)
                            self.txtfld10_cap.place(x=230, y=290)
                            self.txtfld10_cap.set("")

                            self.lb11 = Label(window, text="Espec.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb11.place(x=620, y=290)

                            self.txtfld11_cap = ttk.Combobox(window,

                                                             text="Espec.",
                                                             font=("Ariel", 10), values=Espec)
                            self.txtfld11_cap.place(x=780, y=290)
                            self.txtfld11_cap.set("")

                            self.lb12 = Label(window, text="Tol.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb12.place(x=60, y=330)

                            self.txtfld12_cap = ttk.Combobox(window, text="Tol.",
                                                             font=("Ariel", 10), values=Tol)
                            self.txtfld12_cap.place(x=230, y=330)
                            self.txtfld12_cap.set("")

                            self.lb13 = Label(window, text="Unid.",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb13.place(x=620, y=330)

                            self.txtfld13_cap = ttk.Combobox(window,

                                                             text="Unid.",
                                                             font=("Ariel", 10), values=Unid)
                            self.txtfld13_cap.place(x=780, y=330)
                            self.txtfld13_cap.set("")

                            self.lb14 = Label(window, text="CP",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb14.place(x=60, y=370)

                            self.txtfld14_cap = ttk.Combobox(window, text="CP",
                                                             font=("Ariel", 10), values=CP)
                            self.txtfld14_cap.place(x=230, y=370)
                            self.txtfld14_cap.set("")
                            self.txtfld14_cap.configure(state=DISABLED)

                            self.lb15 = Label(window, text="CPK",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb15.place(x=620, y=370)

                            self.txtfld15_cap = ttk.Combobox(window,

                                                             text="CPK",
                                                             font=("Ariel", 10), values=CPK)
                            self.txtfld15_cap.place(x=780, y=370)
                            self.txtfld15_cap.set("")
                            self.txtfld15_cap.configure(state=DISABLED)

                            self.lb16 = Label(window, text="PPM",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb16.place(x=60, y=410)

                            self.txtfld16_cap = ttk.Combobox(window, text="PPM",
                                                             font=("Ariel", 10), values=PPM)
                            self.txtfld16_cap.place(x=230, y=410)
                            self.txtfld16_cap.set("")
                            self.txtfld16_cap.configure(stat=DISABLED)

                            from datetime import date
                            from datetime import timedelta

                            today = date.today()

                            # dd/mm/YY
                            d1 = today.strftime("%d-%m-%Y")
                            print(d1)

                            EndDate = date.today() + timedelta(days=730)
                            EndDate = EndDate.strftime("%d-%m-%Y")

                            # print(EndDate)

                            self.lb17 = Label(window, text="Data do Estudo",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb17.place(x=620, y=410)

                            self.txtfld17_cap = ttk.Combobox(window,

                                                             text="Data do Estudo",
                                                             font=("Ariel", 10), values=Data_do_Estudo)
                            self.txtfld17_cap.place(x=780, y=410)
                            self.txtfld17_cap.set(d1)

                            self.lb18 = Label(window, text="Próximo estudo",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19, anchor='e')
                            self.lb18.place(x=60, y=450)

                            self.txtfld18_cap = ttk.Combobox(window, text="Próximo estudo",
                                                             font=("Ariel", 10), values=Próximo_estudo)
                            self.txtfld18_cap.place(x=230, y=450)
                            self.txtfld18_cap.set(EndDate)

                            self.lb19 = Label(window, text="GKC",
                                              font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18, anchor='e')
                            self.lb19.place(x=620, y=450)

                            self.txtfld19_cap = ttk.Combobox(window,

                                                             text="GKC",
                                                             font=("Ariel", 10), values=GKC)
                            self.txtfld19_cap.place(x=780, y=450)
                            self.txtfld19_cap.set("")
                            self.txtfld19_cap.configure(state=DISABLED)

                            self.lb19_link = Label(window, text="Report Link",
                                                   font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                            self.lb19_link.place(x=700, y=142)

                            self.txtfld19_cap_link = Entry(window,

                                                           text="url",
                                                           font=("Ariel", 10))
                            self.txtfld19_cap_link.place(x=800, y=140, width=345)
                            self.txtfld19_cap_link.delete(0, END)

                            self.txtfld19_cap_link.insert(0, "")

                            def kc_similar():
                                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                           "jdaat2012", "PU_FA_Testing")
                                cursor_SQL = conn_SQL.cursor()

                                query = """SELECT [GKC_Num] FROM [PU_FA_Testing].[dbo].[GKC_Master] 
                                                                    WHERE [GKC_Spec]='""" + str(
                                    self.txtfld11_cap.get()).strip() + """' AND [GKC_Tolerance]='""" + str(
                                    self.txtfld12_cap.get().strip()) + """'"""

                                cursor_SQL.execute(query)

                                kc_similar = ["Não"]

                                for row in cursor_SQL:
                                    # print(row)
                                    kc_similar.append(row[0])

                                # print(kc_similar, str(self.txtfld8.get()), str(self.txtfld9.get()))

                                # self.txtfld5.set(kc_similar)

                                self.txtfld19_cap = ttk.Combobox(window, text="KC Similar", state="readonly",
                                                                 font=("Ariel", 10),
                                                                 values=kc_similar)
                                self.txtfld19_cap.place(x=780, y=450)

                            def submit():

                                KC_cap = self.txtfld1.get()
                                Estudo = self.txtfld8_cap.get()
                                Item = self.txtfld9_cap.get()
                                Processo = self.txtfld10_cap.get()
                                Espec = self.txtfld11_cap.get()
                                Tol = self.txtfld12_cap.get()
                                Unid = self.txtfld13_cap.get()
                                CP = self.txtfld14_cap.get()
                                CPK = self.txtfld15_cap.get()
                                PPM = self.txtfld16_cap.get()
                                Data_do_Estudo = self.txtfld17_cap.get()
                                Proximo = self.txtfld18_cap.get()
                                GKC = self.txtfld19_cap.get()

                                # print(KC_cap)

                                messagebox.showwarning("FIRST SUBMIT", "PLEASE FILL UP AND SUBMIT BEFORE YOU PROCEED")

                                # respq = self.txtfld8_cap.get()
                                # respm = self.txtfld8_cap.get()
                                # produdo = self.txtfld8_cap.get()
                                # proj = self.txtfld8_cap.get()
                                # data = self.txtfld8_cap.get()
                                # status = self.txtfld8_cap.get()
                                #
                                # print(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo, Descri, Expec,
                                #       Tolerancia, Uniade, Tipoc, Tipod,
                                #       local, respq, respm, produdo, proj, data, status)
                                #
                                # next_randr_update(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo,
                                #                   Descri, Expec,
                                #                   Tolerancia, Uniade, Tipoc, Tipod,
                                #                   local, respq, respm, produdo, proj, data, status)

                            def insert_cap():

                                # print(quantifiers)

                                if ((str(self.txtfld1.get())).strip() != "" and (
                                        str(self.txtfld8_cap.get())).strip() != "" and (
                                        str(self.txtfld9_cap.get())).strip() != "" and (
                                        str(self.txtfld10_cap.get())).strip() != "" and (
                                        str(self.txtfld11_cap.get())).strip() != ""
                                        and (str(self.txtfld12_cap.get())).strip() != ""
                                        and (str(self.txtfld13_cap.get())).strip() != ""
                                        and (str(self.txtfld17_cap.get())).strip() != ""
                                        and (str(self.txtfld18_cap.get())).strip() != ""
                                        and (str(self.txtfld19_cap.get())).strip() != ""
                                ):

                                    GKC = ((str(self.txtfld19_cap.get())).strip())

                                    if GKC == 'None' or GKC == 'Não':

                                        try:

                                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                                       "jdaat",
                                                                       "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """INSERT INTO [PU_FA_Testing].[dbo].[CAPABILITY_STUDY]([KC_Id],[Cap_Study],[Item],[Process],[Specification],
    [Tolerance],[Unit],[CP],[CPK],[PPM],[Cap_StudyDate],[Cap_NextStudyDate] ,[Link],[GKC_Id])
                    VALUES((SELECT TOP 1 [KC_ID] FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] WHERE [KC_No]='""" + (
                                                (str(self.txtfld1.get())).strip()) + """')
                    ,'""" + ((str(self.txtfld8_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld9_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld10_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld11_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld12_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld13_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld14_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld15_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld16_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld17_cap.get())).strip()) + """',
                    '""" + ((str(self.txtfld18_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld19_cap_link.get())).strip()) + """',
                    NULL)"""

                                            # print(query)

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()
                                            cursor_SQL.close()

                                            # tk.messagebox.showerror("", "WRONG VALUES")

                                            messagebox.showinfo("information", "Added Sucessfully")

                                            cabs()

                                        except:

                                            messagebox.showerror("error", "Error")



                                    else:

                                        try:

                                            conn_SQL = pymssql.connect(
                                                "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                "jdaat",
                                                "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """INSERT INTO [PU_FA_Testing].[dbo].[CAPABILITY_STUDY]([KC_Id],[Cap_Study],[Item],[Process],[Specification],
                                                [Tolerance],[Unit],[CP],[CPK],[PPM],[Cap_StudyDate],[Cap_NextStudyDate] ,[Link],[GKC_Id])
                                                                VALUES((SELECT TOP 1 [KC_ID] FROM [PU_FA_Testing].[dbo].[KEY_CHARACTERISTICS] WHERE [KC_No]='""" + (
                                                (str(self.txtfld1.get())).strip()) + """')
                                                                ,'""" + ((str(self.txtfld8_cap.get())).strip()) + """',
                                                                '""" + (
                                                        (str(self.txtfld9_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld10_cap.get())).strip()) + """',
                                                                '""" + (
                                                        (str(self.txtfld11_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld12_cap.get())).strip()) + """',
                                                                '""" + (
                                                        (str(self.txtfld13_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld14_cap.get())).strip()) + """',
                                                                '""" + (
                                                        (str(self.txtfld15_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld16_cap.get())).strip()) + """',
                                                                '""" + ((str(self.txtfld17_cap.get())).strip()) + """',
                                                                '""" + (
                                                        (str(self.txtfld18_cap.get())).strip()) + """','""" + (
                                                        (str(self.txtfld19_cap_link.get())).strip()) + """',
        (SELECT [GKC_ID] FROM [PU_FA_Testing].[dbo].[GKC_Master] WHERE [GKC_Num]='""" + (
                                                        (str(self.txtfld19_cap.get())).strip()) + """'))"""

                                            # print(query)

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()
                                            cursor_SQL.close()

                                            # tk.messagebox.showerror("", "WRONG VALUES")

                                            messagebox.showinfo("information", "Added Sucessfully")

                                            cabs()

                                        except:

                                            messagebox.showerror("error", "Error")





                                else:

                                    messagebox.showwarning("warning", "Enter Values")

                            self.btn_kc_sim_check = ttk.Button(window, text="", command=kc_similar)
                            self.btn_kc_sim_check.place(x=960, y=450, width=25, height=23)

                            self.btn_submit = ttk.Button(window, text="SUBMIT", command=insert_cap)
                            self.btn_submit.place(x=230, y=550, width=165, height=50)

                            self.btn_cap_study = ttk.Button(window, text="NEW STUDY", command=submit)
                            self.btn_cap_study.place(x=780, y=550, width=165, height=50)

                            # self.btn_submit = ttk.Button(window, text="SUBMIT")
                            # self.btn_submit.place(x=520, y=650, width=250, height=60)

                    Capability(user_add)

                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()

                query = """SELECT * FROM [PU_FA_Testing].[dbo].[Capamaster] WHERE [# Estudo] IS NOT NULL ORDER BY [# Estudo] DESC"""

                cursor_SQL.execute(query)

                data = []

                KC_codes = []

                for row in cursor_SQL:
                    data.append([*row])

                query = """SELECT [# KC]  FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL ORDER BY [# KC] DESC"""

                cursor_SQL.execute(query)

                for row in cursor_SQL:
                    KC_codes.append(*row)

                KC = sorted(set(KC_codes), reverse=True)
                Estudo_CAP = []
                Item = []
                Processo = []
                Espec = []
                Tol = []
                Unid = []
                CP = []
                CPK = []
                PPM = []
                Data_do_Estudo = []
                Próximo_estudo = []
                GKC = []

                for x in range(0, len(data)):
                    if data[x][1] != None:
                        Estudo_CAP.append(data[x][1])

                Estudo_CAP = sorted(set(Estudo_CAP), reverse=True)

                Estudo_CAP.insert(0, "NOT APPLICABLE")

                for x in range(0, len(data)):
                    if data[x][2] != None:
                        Item.append(data[x][2])

                Item = sorted(set(Item))

                for x in range(0, len(data)):
                    if data[x][3] != None:
                        Processo.append(data[x][3])

                Processo = sorted(set(Processo))

                for x in range(0, len(data)):
                    if data[x][4] != None:
                        Espec.append(data[x][4])

                Espec = sorted(set(Espec))

                for x in range(0, len(data)):
                    if data[x][5] != None:
                        Tol.append(data[x][5])

                Tol = sorted(set(Tol))

                for x in range(0, len(data)):
                    if data[x][6] != None:
                        Unid.append(data[x][6])

                Unid = sorted(set(Unid))

                for x in range(0, len(data)):
                    if data[x][7] != None:
                        CP.append(data[x][7])

                CP = sorted(set(CP))

                for x in range(0, len(data)):
                    if data[x][8] != None:
                        CPK.append(data[x][8])

                CPK = sorted(set(CPK))

                for x in range(0, len(data)):
                    if data[x][9] != None:
                        PPM.append(data[x][9])

                PPM = sorted(set(PPM))

                for x in range(0, len(data)):
                    if data[x][10] != None:
                        Data_do_Estudo.append(data[x][10])

                Data_do_Estudo = sorted(set(Data_do_Estudo))

                for x in range(0, len(data)):
                    if data[x][11] != None:
                        Próximo_estudo.append(data[x][11])

                Próximo_estudo = sorted(set(Próximo_estudo))

                for x in range(0, len(data)):
                    if data[x][13] != None:
                        GKC.append(data[x][13])

                GKC = sorted(set(GKC), reverse=True)

                class App:
                    def __init__(self):

                        def selectItem(a):
                            curItem = tree.focus()
                            # print(tree.item(curItem)['values'])
                            quantifiers = (tree.item(curItem)['values'])

                            if id_cabs != 0:
                                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                           "jdaat2012", "PU_FA_Testing")
                                cursor_SQL = conn_SQL.cursor()

                                cursor_SQL.execute(
                                    """SELECT * FROM [PU_FA_Testing].[dbo].[CAPABILITY_STUDY] WHERE [Cap_Study]='""" + (
                                        str(id_cabs).strip()) + """'""")

                                for row in cursor_SQL:
                                    quantifiers = row

                                # print(quantifiers)

                                conn_SQL.close()

                            def capability_modify():

                                # CLASS FOR ADDING STATION
                                class Capability():

                                    def __init__(self, window):
                                        load = cv2.imread('Images/background.png', 1)
                                        cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                                        load = Image.fromarray(cv2imagex1)
                                        load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                                        render = ImageTk.PhotoImage(load)
                                        img = tk.Label(image=render)
                                        img.image = render
                                        img.place(x=0, y=140)

                                        image_loader()

                                        self.lb_title = Label(window, text="Capability", fg='#34943a',
                                                              font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9')
                                        self.lb_title.place(x=500, y=170)

                                        self.lb1 = Label(window, text="#KC", fg='#34943a',
                                                         font=("Ariel", 10), bg='#feffd9')
                                        self.lb1.place(x=5, y=142)

                                        self.txtfld1 = ttk.Combobox(window, text="#KC_CAP", state='readonly',
                                                                    font=("Ariel", 10), values=KC)
                                        self.txtfld1.place(x=60, y=140)

                                        self.txtfld1.set(quantifiers[0])

                                        # self.txtfld1.config(state=DISABLED)

                                        self.lb8 = Label(window, text="#Estudo", fg='#34943a',
                                                         font=("Ariel", 10), bg='#feffd9', width=19, anchor='e')
                                        self.lb8.place(x=60, y=250)

                                        self.txtfld8_cap = ttk.Combobox(window, text="#Estudo",
                                                                        font=("Ariel", 10),
                                                                        values=Estudo_CAP)
                                        self.txtfld8_cap.place(x=230, y=250)

                                        cap_no = Estudo_CAP[1][3:]

                                        cap_no = str("EC_") + ((str("000000") + str(int(cap_no) + 1))[-6:])

                                        self.txtfld8_cap.set(quantifiers[1])

                                        self.lb9 = Label(window, text="Item", fg='#34943a',
                                                         font=("Ariel", 10), bg='#feffd9', width=18, anchor='e')
                                        self.lb9.place(x=620, y=250)

                                        self.txtfld9_cap = ttk.Combobox(window,
                                                                        text="Item",
                                                                        font=("Ariel", 10),
                                                                        values=Item)
                                        self.txtfld9_cap.place(x=780, y=250)
                                        self.txtfld9_cap.set(quantifiers[2])

                                        self.lb10 = Label(window, text="Processo",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb10.place(x=60, y=290)

                                        self.txtfld10_cap = ttk.Combobox(window, text="Processo",
                                                                         font=("Ariel", 10), values=Processo)
                                        self.txtfld10_cap.place(x=230, y=290)
                                        self.txtfld10_cap.set(quantifiers[3])

                                        self.lb11 = Label(window, text="Espec.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb11.place(x=620, y=290)

                                        self.txtfld11_cap = ttk.Combobox(window,

                                                                         text="Espec.",
                                                                         font=("Ariel", 10), values=Espec)
                                        self.txtfld11_cap.place(x=780, y=290)
                                        self.txtfld11_cap.set(quantifiers[4])

                                        self.lb12 = Label(window, text="Tol.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb12.place(x=60, y=330)

                                        self.txtfld12_cap = ttk.Combobox(window, text="Tol.",
                                                                         font=("Ariel", 10), values=Tol)
                                        self.txtfld12_cap.place(x=230, y=330)
                                        self.txtfld12_cap.set(quantifiers[5])

                                        self.lb13 = Label(window, text="Unid.",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb13.place(x=620, y=330)

                                        self.txtfld13_cap = ttk.Combobox(window,

                                                                         text="Unid.",
                                                                         font=("Ariel", 10), values=Unid)
                                        self.txtfld13_cap.place(x=780, y=330)
                                        self.txtfld13_cap.set(quantifiers[6])

                                        self.lb14 = Label(window, text="CP",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb14.place(x=60, y=370)

                                        self.txtfld14_cap = ttk.Combobox(window, text="CP",
                                                                         font=("Ariel", 10), values=CP)
                                        self.txtfld14_cap.place(x=230, y=370)
                                        self.txtfld14_cap.set(quantifiers[7])
                                        self.txtfld14_cap.configure(state=DISABLED)

                                        self.lb15 = Label(window, text="CPK",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb15.place(x=620, y=370)

                                        self.txtfld15_cap = ttk.Combobox(window,

                                                                         text="CPK",
                                                                         font=("Ariel", 10), values=CPK)
                                        self.txtfld15_cap.place(x=780, y=370)
                                        self.txtfld15_cap.set(quantifiers[8])
                                        self.txtfld15_cap.configure(state=DISABLED)

                                        self.lb16 = Label(window, text="PPM",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb16.place(x=60, y=410)

                                        self.txtfld16_cap = ttk.Combobox(window, text="PPM",
                                                                         font=("Ariel", 10), values=PPM)
                                        self.txtfld16_cap.place(x=230, y=410)
                                        self.txtfld16_cap.set(quantifiers[9])
                                        self.txtfld16_cap.configure(stat=DISABLED)

                                        from datetime import date
                                        from datetime import timedelta

                                        today = date.today()

                                        # dd/mm/YY
                                        d1 = today.strftime("%d-%m-%Y")
                                        print(d1)

                                        EndDate = date.today() + timedelta(days=730)
                                        EndDate = EndDate.strftime("%d-%m-%Y")

                                        # print(EndDate)

                                        self.lb17 = Label(window, text="Data do Estudo",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb17.place(x=620, y=410)

                                        self.txtfld17_cap = ttk.Combobox(window,

                                                                         text="Data do Estudo",
                                                                         font=("Ariel", 10), values=Data_do_Estudo)
                                        self.txtfld17_cap.place(x=780, y=410)
                                        self.txtfld17_cap.set(quantifiers[10])

                                        self.lb18 = Label(window, text="Próximo estudo",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=19,
                                                          anchor='e')
                                        self.lb18.place(x=60, y=450)

                                        self.txtfld18_cap = ttk.Combobox(window, text="Próximo estudo",
                                                                         font=("Ariel", 10), values=Próximo_estudo)
                                        self.txtfld18_cap.place(x=230, y=450)
                                        self.txtfld18_cap.set(quantifiers[11])

                                        self.lb19 = Label(window, text="GKC",
                                                          font=("Ariel", 10), bg='#feffd9', fg='#34943a', width=18,
                                                          anchor='e')
                                        self.lb19.place(x=620, y=450)

                                        self.txtfld19_cap = ttk.Combobox(window,

                                                                         text="GKC",
                                                                         font=("Ariel", 10), values=GKC)
                                        self.txtfld19_cap.place(x=780, y=450)
                                        self.txtfld19_cap.set(quantifiers[12])

                                        self.lb19_link = Label(window, text="Report Link",
                                                               font=("Ariel", 10), bg='#feffd9', fg='#34943a')
                                        self.lb19_link.place(x=700, y=142)

                                        self.txtfld19_cap_link = Entry(window,

                                                                       text="url",
                                                                       font=("Ariel", 10))
                                        self.txtfld19_cap_link.place(x=800, y=140, width=345)
                                        self.txtfld19_cap_link.delete(0, END)

                                        self.txtfld19_cap_link.insert(0, str(quantifiers[13]))

                                        def kc_similar():
                                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                                       "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKCmaster] 
                                            WHERE [Espec#]='""" + str(
                                                self.txtfld11_cap.get()).strip() + """' AND [Tol#]='""" + str(
                                                self.txtfld12_cap.get().strip()) + """'"""

                                            cursor_SQL.execute(query)

                                            print(query)

                                            kc_similar = ["Não"]

                                            for row in cursor_SQL:
                                                # print(row)
                                                kc_similar.append(row[0])

                                            conn_SQL.close()

                                            kc_similar = set(kc_similar)
                                            # print(kc_similar)

                                            self.txtfld19_cap = ttk.Combobox(window, text="KC Similar",
                                                                             state="readonly",
                                                                             font=("Ariel", 10),
                                                                             values=list(kc_similar))
                                            self.txtfld19_cap.place(x=780, y=450)

                                        def submit():
                                            KC_cap = quantifiers[0]
                                            Estudo = self.txtfld8_cap.get()
                                            Item = self.txtfld9_cap.get()
                                            Processo = self.txtfld10_cap.get()
                                            Espec = self.txtfld11_cap.get()
                                            Tol = self.txtfld12_cap.get()
                                            Unid = self.txtfld13_cap.get()
                                            CP = self.txtfld14_cap.get()
                                            CPK = self.txtfld15_cap.get()
                                            PPM = self.txtfld16_cap.get()
                                            Data_do_Estudo = self.txtfld17_cap.get()
                                            Proximo = self.txtfld18_cap.get()
                                            GKC = self.txtfld19_cap.get()

                                            # print(KC_cap)

                                            openCapFormat(KC_cap)

                                            # respq = self.txtfld8_cap.get()
                                            # respm = self.txtfld8_cap.get()
                                            # produdo = self.txtfld8_cap.get()
                                            # proj = self.txtfld8_cap.get()
                                            # data = self.txtfld8_cap.get()
                                            # status = self.txtfld8_cap.get()
                                            #
                                            # print(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo, Descri, Expec,
                                            #       Tolerancia, Uniade, Tipoc, Tipod,
                                            #       local, respq, respm, produdo, proj, data, status)
                                            #
                                            # next_randr_update(KC_dd, Part_number, Rev, Centro, Kc_Similar, Processo,
                                            #                   Descri, Expec,
                                            #                   Tolerancia, Uniade, Tipoc, Tipod,
                                            #                   local, respq, respm, produdo, proj, data, status)

                                        def update_cap():

                                            # print(quantifiers)

                                            if ((str(self.txtfld1.get())).strip() != "" and (
                                                    str(self.txtfld8_cap.get())).strip() != "" and (
                                                    str(self.txtfld9_cap.get())).strip() != "" and (
                                                    str(self.txtfld10_cap.get())).strip() != "" and (
                                                    str(self.txtfld11_cap.get())).strip() != ""
                                                    and (str(self.txtfld12_cap.get())).strip() != ""
                                                    and (str(self.txtfld13_cap.get())).strip() != ""
                                                    and (str(self.txtfld14_cap.get())).strip() != ""
                                                    and (str(self.txtfld15_cap.get())).strip() != ""
                                                    and (str(self.txtfld16_cap.get())).strip() != ""
                                                    and (str(self.txtfld17_cap.get())).strip() != ""
                                                    and (str(self.txtfld18_cap.get())).strip() != ""
                                                    and (str(self.txtfld19_cap.get())).strip() != ""
                                            ):

                                                GKC = ((str(self.txtfld19_cap.get())).strip())

                                                if GKC == 'None' or GKC == 'Não':

                                                    try:

                                                        conn_SQL = pymssql.connect(
                                                            "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                            "jdaat",
                                                            "jdaat2012", "PU_FA_Testing")
                                                        cursor_SQL = conn_SQL.cursor()

                                                        query = """UPDATE [PU_FA_Testing].[dbo].[CAPABILITY_STUDY] 
    SET 
    [Cap_Study] ='""" + ((str(self.txtfld8_cap.get())).strip()) + """' ,
    [Item] ='""" + ((str(self.txtfld9_cap.get())).strip()) + """', [Process] = '""" + (
                                                            (str(self.txtfld10_cap.get())).strip()) + """' , 
    [Specification] = '""" + ((str(self.txtfld11_cap.get())).strip()) + """',  [Tolerance] = '""" + (
                                                                    (str(self.txtfld12_cap.get())).strip()) + """',  
    [Unit] = '""" + ((str(self.txtfld13_cap.get())).strip()) + """',  [CP] = '""" + (
                                                                    (str(self.txtfld14_cap.get())).strip()) + """',  
    [CPK] = '""" + ((str(self.txtfld15_cap.get())).strip()) + """',[PPM] = '""" + (
                                                                    (str(self.txtfld16_cap.get())).strip()) + """',
     [Cap_StudyDate] = '""" + ((str(self.txtfld17_cap.get())).strip()) + """',  
     [Cap_NextStudyDate] = '""" + ((str(self.txtfld18_cap.get())).strip()) + """',  [Link] = '""" + str(
                                                            self.txtfld19_cap_link.get()) + """',  
     [GKC_Id] = NULL , [Cap_Study_By] = '""" + (str(quantifiers[14])) + """' 
     WHERE [Capability_Id]='""" + str(quantifiers[15]) + """'"""

                                                        # print(query)

                                                        cursor_SQL.execute(query)
                                                        conn_SQL.commit()
                                                        cursor_SQL.close()

                                                        # tk.messagebox.showerror("", "WRONG VALUES")

                                                        messagebox.showinfo("information", "Updated Sucessfully")

                                                        cabs()

                                                    except:

                                                        messagebox.showerror("error", "Error")


                                                else:

                                                    try:

                                                        conn_SQL = pymssql.connect(
                                                            "FPUNPUSQLDEV2.jdnet.deere.com\INST2",
                                                            "jdaat",
                                                            "jdaat2012", "PU_FA_Testing")
                                                        cursor_SQL = conn_SQL.cursor()

                                                        query = """UPDATE [PU_FA_Testing].[dbo].[CAPABILITY_STUDY] 
                                                        SET [KC_Id] ='""" + ((str(self.txtfld1.get())).strip()) + """' , 
                                                        [Cap_Study] ='""" + ((str(self.txtfld8_cap.get())).strip()) + """' ,
                                                        [Item] ='""" + ((str(
                                                            self.txtfld9_cap.get())).strip()) + """', [Process] = '""" + (
                                                                    (str(self.txtfld10_cap.get())).strip()) + """' , 
                                                        [Specification] = '""" + ((str(
                                                            self.txtfld11_cap.get())).strip()) + """',  [Tolerance] = '""" + (
                                                                    (str(self.txtfld12_cap.get())).strip()) + """',  
                                                        [Unit] = '""" + ((str(
                                                            self.txtfld13_cap.get())).strip()) + """',  [CP] = '""" + (
                                                                    (str(self.txtfld14_cap.get())).strip()) + """',  
                                                        [CPK] = '""" + ((str(
                                                            self.txtfld15_cap.get())).strip()) + """',[PPM] = '""" + (
                                                                    (str(self.txtfld16_cap.get())).strip()) + """',
                                                         [Cap_StudyDate] = '""" + (
                                                                    (str(self.txtfld17_cap.get())).strip()) + """',  
                                                         [Cap_NextStudyDate] = '""" + ((str(
                                                            self.txtfld18_cap.get())).strip()) + """',  [Link] = '""" + str(
                                                            self.txtfld19_cap_link.get()) + """',  
                                                         [GKC_Id] = '""" + ((str(
                                                            self.txtfld19_cap.get())).strip()) + """' , [Cap_Study_By] = '""" + (
                                                                    str(quantifiers[14])) + """' 
                                                         WHERE [Capability_Id]='""" + str(quantifiers[15]) + """'"""

                                                        # print(query)

                                                        cursor_SQL.execute(query)
                                                        conn_SQL.commit()
                                                        cursor_SQL.close()

                                                        # tk.messagebox.showerror("", "WRONG VALUES")

                                                        messagebox.showinfo("information", "Updated Sucessfully")

                                                        cabs()

                                                    except:

                                                        messagebox.showerror("error", "Error")





                                            else:

                                                messagebox.showwarning("warning", "Enter Values")

                                        self.btn_kc_sim_check = ttk.Button(window, text="", command=kc_similar)
                                        self.btn_kc_sim_check.place(x=960, y=450, width=25, height=23)

                                        # kc_similar()

                                        # JINGA LALA HU HU

                                        def fetch():
                                            print(quantifiers)
                                            x, y, z = getvaluefromcap(str(quantifiers[1]), str(quantifiers[0]))
                                            print(str(quantifiers[1]), str(quantifiers[0]))
                                            print(x, y, z)
                                            self.txtfld14_cap.set(x)
                                            self.txtfld15_cap.set(y)
                                            self.txtfld16_cap.set(z)

                                        self.btn_submit = ttk.Button(window, text="UPDATE", command=update_cap)
                                        self.btn_submit.place(x=230, y=550, width=165, height=50)

                                        self.btn_cap_study = ttk.Button(window, text="NEW STUDY", command=submit)
                                        self.btn_cap_study.place(x=780, y=550, width=165, height=50)

                                        self.btn_cap_fetch = ttk.Button(window, text="", command=fetch)
                                        self.btn_cap_fetch.place(x=950, y=370, width=23, height=23)

                                Capability(user_add)

                            capability_modify()

                        frame = Frame(user_add)
                        frame.place(x=0, y=650)

                        tree = ttk.Treeview(frame,
                                            columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
                                            height=17, show="headings")
                        tree.pack(side='left')
                        tree.bind('<ButtonRelease-1>', selectItem)

                        if id_cabs != 0:
                            selectItem(id_cabs)

                        val = ["# KC", "# Estudo", "Item", "Processo", "Espec.", "Tol.", "Unid.", "CP", "CPK", "PPM",
                               "Data do Estudo", "Próximo estudo", "GKC", "Link"]

                        for i in range(1, len(val) + 1):
                            tree.heading(i, text=val[i - 1])

                        # tree.heading(2, text="Column 2")
                        # tree.heading(3, text="Column 3")

                        for i in range(1, len(val) + 1):
                            tree.column(i, width=136, anchor='center')

                        # tree.column(2, width=100)
                        # tree.column(3, width=100)

                        scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
                        scroll.pack(side='right', fill='y')

                        """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
                        scrollx.pack(side='bottom', fill='x')"""

                        tree.configure(yscrollcommand=scroll.set)

                        iterx = 0
                        for valx in data:
                            try:
                                if float(valx[8]) >= 1.33:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , valx[10], valx[11], valx[13], valx[12]),
                                                tags=('odd',))
                                elif (float(valx[8]) < 1.33) and (float(valx[8]) <= 1):
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , valx[10], valx[11], valx[13], valx[12]),
                                                tags=('even',))
                                else:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , valx[10], valx[11], valx[13], valx[12]),
                                                tags=('quex',))
                            except:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                               , valx[10], valx[11], valx[13], valx[12]),
                                            tags=('quex',))

                            iterx += 1

                        tree.tag_configure('odd', background='#008001')
                        tree.tag_configure('quex', background='#F73F09')
                        tree.tag_configure('even', background='#FF9B00')

                        conn_SQL.close()

                        def command(x=0):

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

                            if (self.tkvar0.get()) != '# KC':
                                var0 = self.tkvar0.get()
                            if (self.tkvar1.get()) != '# Estudo':
                                var1 = self.tkvar1.get()
                            if (self.tkvar2.get()) != 'Item':
                                var2 = self.tkvar2.get()
                            if (self.tkvar3.get()) != 'Processo':
                                var3 = self.tkvar3.get()
                            if (self.tkvar4.get()) != 'Espec.':
                                var4 = self.tkvar4.get()
                            if (self.tkvar5.get()) != 'Tol.':
                                var5 = self.tkvar5.get()
                            if (self.tkvar6.get()) != 'Unid.':
                                var6 = self.tkvar6.get()
                            if (self.tkvar7.get()) != 'CP':
                                var7 = self.tkvar7.get()
                            if (self.tkvar8.get()) != 'CPK':
                                var8 = self.tkvar8.get()
                            if (self.tkvar9.get()) != 'PPM':
                                var9 = self.tkvar9.get()
                            if (self.tkvar10.get()) != 'Data do Estudo':
                                var10 = self.tkvar10.get()
                            if (self.tkvar11.get()) != 'Próximo estudo':
                                var11 = self.tkvar11.get()
                            if (self.tkvar12.get()) != 'GKC':
                                var12 = self.tkvar12.get()

                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                       "jdaat2012", "PU_FA_Testing")
                            cursor_SQL = conn_SQL.cursor()

                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[CapaMaster] WHERE [# KC] LIKE '%""" + str(
                                var0) + """%' 
                            AND ([# Estudo] LIKE '%""" + str(var1) + """%' OR [# Estudo] IS NULL)
                                                AND ([Item] LIKE '%""" + str(var2) + """%' OR [Item] IS NULL)
                                                AND ([Processo] LIKE '%""" + str(var3) + """%' OR [Processo] IS NULL)
                                                AND ([Espec#] LIKE '%""" + str(var4) + """%' OR [Espec#] IS NULL)
                                                AND ([Tol#] LIKE '%""" + str(var5) + """%' OR [Tol#] IS NULL)
                            AND ([Unid#] LIKE '%""" + str(var6) + """%' OR [Unid#] IS NULL)
                                                AND ([CP] LIKE '%""" + str(var7) + """%' OR [CP] IS NULL)
                            AND ([CPK] LIKE '%""" + str(var8) + """%' OR [CPK] IS NULL)
                                                AND ([PPM] LIKE '%""" + str(var9) + """%' OR [PPM] IS NULL)
                            AND ([Data do Estudo] LIKE '%""" + str(var10) + """%' OR [Data do Estudo] IS NULL)
                                                AND ([Próximo estudo] LIKE '%""" + str(var11) + """%' OR [Próximo estudo] IS NULL)
                            AND ([Link] LIKE '%%' OR [Link] IS NULL)
                                                AND ([GKC] LIKE '%""" + str(var12) + """%' OR [GKC] IS NULL)      

                            """

                            # print(query)

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
                                try:
                                    if float(valx[8]) >= 1.33:
                                        tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                       , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                       , valx[10], valx[11], valx[13], valx[12]),
                                                    tags=('odd',))
                                    elif (float(valx[8]) < 1.33) and (float(valx[8]) <= 1):
                                        tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                       , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                       , valx[10], valx[11], valx[13], valx[12]),
                                                    tags=('even',))
                                    else:
                                        tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                       , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                       , valx[10], valx[11], valx[13], valx[12],
                                                                       ),
                                                    tags=('quex',))
                                except:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6], valx[7], valx[8], valx[9]
                                                                   , valx[10], valx[11], valx[13], valx[12]),
                                                tags=('quex',))

                                iterx += 1

                            tree.tag_configure('odd', background='#008001')
                            tree.tag_configure('quex', background='#F73F09')
                            tree.tag_configure('even', background='#FF9B00')

                            conn_SQL.close()

                        self.tkvarbtn0 = ttk.Button(window, text="", width=450)
                        self.tkvarbtn0.place(x=0, y=625, height=30)

                        self.tkvar0 = ttk.Combobox(window, text="tkvar0",
                                                   font=("Ariel", 10), values=KC, width=17, justify='center')
                        self.tkvar0.place(x=0, y=629)
                        self.tkvar0.set("# KC")

                        self.tkvar0.bind("<<ComboboxSelected>>", command)

                        self.tkvar1 = ttk.Combobox(window, text="tkvar1",
                                                   font=("Ariel", 10), values=Estudo_CAP, width=16, justify='center')
                        self.tkvar1.place(x=138, y=629)
                        self.tkvar1.set("# Estudo")
                        self.tkvar1.bind("<<ComboboxSelected>>", command)

                        self.tkvar2 = ttk.Combobox(window, text="tkvar2",
                                                   font=("Ariel", 10), values=Item, width=17, justify='center')
                        self.tkvar2.place(x=270, y=629)
                        self.tkvar2.set("Item")

                        self.tkvar2.bind("<<ComboboxSelected>>", command)

                        self.tkvar3 = ttk.Combobox(window, text="tkvar3",
                                                   font=("Ariel", 10), values=Processo, width=16, justify='center')
                        self.tkvar3.place(x=410, y=629)
                        self.tkvar3.set("Processo")

                        self.tkvar3.bind("<<ComboboxSelected>>", command)

                        self.tkvar4 = ttk.Combobox(window, text="tkvar4",
                                                   font=("Ariel", 10), values=Espec, width=17, justify='center')
                        self.tkvar4.place(x=543, y=629)
                        self.tkvar4.set("Espec.")

                        self.tkvar4.bind("<<ComboboxSelected>>", command)

                        self.tkvar5 = ttk.Combobox(window, text="tkvar5",
                                                   font=("Ariel", 10), values=Tol, width=17, justify='center')
                        self.tkvar5.place(x=680, y=629)
                        self.tkvar5.set("Tol.")

                        self.tkvar5.bind("<<ComboboxSelected>>", command)

                        self.tkvar6 = ttk.Combobox(window, text="tkvar6",
                                                   font=("Ariel", 10), values=Unid, width=16, justify='center')
                        self.tkvar6.place(x=818, y=629)
                        self.tkvar6.set("Unid.")
                        self.tkvar6.bind("<<ComboboxSelected>>", command)

                        self.tkvar7 = ttk.Combobox(window, text="tkvar7",
                                                   font=("Ariel", 10), values=CP, width=17, justify='center')
                        self.tkvar7.place(x=948, y=629)
                        self.tkvar7.set("CP")
                        self.tkvar7.bind("<<ComboboxSelected>>", command)

                        self.tkvar8 = ttk.Combobox(window, text="tkvar8",
                                                   font=("Ariel", 10), values=CPK, width=17, justify='center')
                        self.tkvar8.place(x=1086, y=629)
                        self.tkvar8.set("CPK")
                        self.tkvar8.bind("<<ComboboxSelected>>", command)

                        self.tkvar9 = ttk.Combobox(window, text="tkvar9",
                                                   font=("Ariel", 10), values=PPM, width=16, justify='center')
                        self.tkvar9.place(x=1224, y=629)
                        self.tkvar9.set("PPM")
                        self.tkvar9.bind("<<ComboboxSelected>>", command)

                        self.tkvar10 = ttk.Combobox(window, text="tkvar10",
                                                    font=("Ariel", 10), values=Data_do_Estudo, width=17,
                                                    justify='center')
                        self.tkvar10.place(x=1355, y=629)
                        self.tkvar10.set("Data do Estudo")
                        self.tkvar10.bind("<<ComboboxSelected>>", command)

                        self.tkvar11 = ttk.Combobox(window, text="tkvar11",
                                                    font=("Ariel", 10), values=Próximo_estudo, width=17,
                                                    justify='center')
                        self.tkvar11.place(x=1495, y=629)
                        self.tkvar11.set("Próximo estudo")
                        self.tkvar11.bind("<<ComboboxSelected>>", command)

                        self.tkvar12 = ttk.Combobox(window, text="tkvar12",
                                                    font=("Ariel", 10), values=GKC, width=16, justify='center')
                        self.tkvar12.place(x=1634, y=629)
                        self.tkvar12.set("GKC")
                        self.tkvar12.bind("<<ComboboxSelected>>", command)

                        self.tkvarbtn1 = ttk.Button(window, text="SEARCH", width=22, command=command)
                        self.tkvarbtn1.place(x=1768, y=628)

                if id_cabs == 0:
                    capability_new()
                else:
                    a = App()

                a = App()

            def gkc_master():

                load = cv2.imread('Images/start.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1010)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/background.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1145), int(480)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=140)

                load = cv2.imread('Images/legend.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(765), int(120)), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=1150, y=500)

                image_loader_gkc()

                def gkc():

                    class GKC():

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
                            self.lb_title = Label(window, text="GROUP KC", fg='#34943a',
                                                  font=("Ariel", 25, 'bold', 'underline'), bg='#feffd9')
                            self.lb_title.place(x=500, y=170)

                            self.lb1 = Label(window, text="#KC", fg='#34943a',
                                             font=("Ariel", 10), bg='#feffd9')
                            self.lb1.place(x=5, y=142)

                            self.txtfld1 = ttk.Combobox(window, text="#KC_CAP", state='readonly',
                                                        font=("Ariel", 10), values=KC)
                            self.txtfld1.place(x=60, y=140)

                            self.txtfld1.set("")

                            self.lb8 = Label(window, text="GKC", fg='#34943a',
                                             font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb8.place(x=60, y=250)

                            self.txtfld8_cap = ttk.Combobox(window, text="GKC", state='readonly',
                                                            font=("Arial", 10),
                                                            values=sorted(
                                                                list(set([data[x][0] for x in range(0, len(data))])),
                                                                reverse=True))
                            self.txtfld8_cap.place(x=230, y=250)

                            gkc_no = max(list(map(int, set([data[x][0][4:] for x in range(0, len(data))]))))

                            gkc_no = str("GKC_") + ((str("000") + str(int(gkc_no) + 1))[-3:])

                            self.txtfld8_cap.set(gkc_no)
                            # self.txtfld8_cap.configure(state=DISABLED)

                            self.lb9 = Label(window, text="Desc.", fg='#34943a',
                                             font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb9.place(x=60, y=290)

                            self.txtfld9_cap = ttk.Combobox(window,
                                                            text="Desc.",
                                                            font=("Arial", 10),
                                                            values=Desc_KC)
                            self.txtfld9_cap.place(x=230, y=290)
                            self.txtfld9_cap.set("")

                            self.lb12 = Label(window, text="Espec.", fg='#34943a',
                                              font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb12.place(x=60, y=330)

                            self.txtfld12_cap = ttk.Combobox(window, text="Espec.",
                                                             font=("Arial", 10), values=Espec)
                            self.txtfld12_cap.place(x=230, y=330)
                            self.txtfld12_cap.set("")

                            self.lb13 = Label(window, text="Tol.", fg='#34943a',
                                              font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb13.place(x=60, y=370)

                            self.txtfld13_cap = ttk.Combobox(window,

                                                             text="Tol.",
                                                             font=("Arial", 10), values=Tol)
                            self.txtfld13_cap.place(x=230, y=370)
                            self.txtfld13_cap.set("")

                            self.lb16 = Label(window, text="Unid.", fg='#34943a',
                                              font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb16.place(x=60, y=410)

                            self.txtfld16_cap = ttk.Combobox(window, text="Unid.",
                                                             font=("Arial", 10), values=Unid)
                            self.txtfld16_cap.place(x=230, y=410)
                            self.txtfld16_cap.set("")

                            self.lb17 = Label(window, text="Item", fg='#34943a',
                                              font=("Arial", 10), bg='#feffd9', width=18, anchor='e')
                            self.lb17.place(x=60, y=450)

                            from datetime import date

                            today = date.today()

                            # dd/mm/YY
                            d1 = today.strftime("%d-%m-%Y")
                            # print(d1)

                            self.txtfld17_cap = ttk.Combobox(window,

                                                             text="Item",
                                                             font=("Arial", 10), values=Item)
                            self.txtfld17_cap.place(x=230, y=450)
                            self.txtfld17_cap.set("")

                            def submit_gkc():

                                MsgBox = tk.messagebox.askquestion('INFORMATION',
                                                                   'Are you sure you want to insert data to GKC with GKC ID ' + str(
                                                                       str(self.txtfld8_cap.get())),
                                                                   icon='warning')
                                if MsgBox == 'yes':

                                    if ((str(self.txtfld1.get())).strip() != "" and (
                                    str(self.txtfld17_cap.get())).strip() != "" and (
                                    str(self.txtfld9_cap.get())).strip() != "" and (
                                    str(self.txtfld12_cap.get())).strip() != "" and (
                                    str(self.txtfld13_cap.get())).strip() != "" and (
                                    str(self.txtfld16_cap.get())).strip() != "" and (
                                    str(self.txtfld17_cap.get())).strip() != ""):

                                        try:

                                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                                       "jdaat2012", "PU_FA_Testing")
                                            cursor_SQL = conn_SQL.cursor()

                                            query = """INSERT INTO [PU_FA_Testing].[dbo].[GKCmaster]
                                        VALUES('""" + str(self.txtfld8_cap.get()) + """','""" + str(
                                                self.txtfld1.get()) + """','""" + str(
                                                self.txtfld17_cap.get()) + """','""" + str(self.txtfld9_cap.get()) + """',
                                        '""" + str(self.txtfld12_cap.get()) + """','""" + str(self.txtfld13_cap.get()) + """'
                                        ,'""" + str(self.txtfld16_cap.get()) + """')"""

                                            cursor_SQL.execute(query)
                                            conn_SQL.commit()
                                            cursor_SQL.close()

                                            # tk.messagebox.showerror("", "WRONG VALUES")

                                            messagebox.showinfo("information", "Added Sucessfully")

                                            gkc_master()

                                        except:

                                            messagebox.showerror("error", "Error")

                                    else:

                                        messagebox.showwarning("warning", "Enter Values")
                                else:
                                    tk.messagebox.showinfo('INFORMATION', 'You will now return to the GKC screen')

                            self.btn_submit = ttk.Button(window, text="SUBMIT", command=submit_gkc)
                            self.btn_submit.place(x=470, y=555, width=200, height=50)

                    GKC(user_add)

                conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                           "jdaat2012", "PU_FA_Testing")
                cursor_SQL = conn_SQL.cursor()

                query = """SELECT * FROM [PU_FA_Testing].[dbo].[GKCmaster] WHERE [# GKC] IS NOT NULL ORDER BY [# GKC] DESC"""

                cursor_SQL.execute(query)

                data = []

                for row in cursor_SQL:
                    # print(row)
                    data.append([*row])

                KC_codes = []

                for row in cursor_SQL:
                    data.append([*row])

                query = """SELECT [# KC]  FROM [PU_FA_Testing].[dbo].[KC] WHERE [# KC] IS NOT NULL ORDER BY [# KC] DESC"""

                cursor_SQL.execute(query)

                for row in cursor_SQL:
                    KC_codes.append(*row)

                KC = sorted(set(KC_codes), reverse=True)
                Estudo_GKC = []
                Item = []
                Desc_KC = []
                Espec = []
                Tol = []
                Unid = []

                for x in range(0, len(data)):
                    if data[x][0] != None:
                        Estudo_GKC.append(data[x][0])

                Estudo_GKC = sorted(set(Estudo_GKC), reverse=True)

                Estudo_GKC.insert(0, "NOT APPLICABLE")

                for x in range(0, len(data)):
                    if data[x][2] != None:
                        Item.append(data[x][2])

                Item = sorted(set(Item))

                for x in range(0, len(data)):
                    if data[x][3] != None:
                        Desc_KC.append(data[x][3])

                Desc_KC = sorted(set(Desc_KC))

                for x in range(0, len(data)):
                    if data[x][4] != None:
                        Espec.append(data[x][4])

                Espec = sorted(set(Espec))

                for x in range(0, len(data)):
                    if data[x][5] != None:
                        Tol.append(data[x][5])

                Tol = sorted(set(Tol))

                for x in range(0, len(data)):
                    if data[x][6] != None:
                        Unid.append(data[x][6])

                Unid = sorted(set(Unid))

                cursor_SQL.close()

                gkc()

                class App:
                    def __init__(self):

                        def selectItem(a):
                            curItem = tree.focus()
                            # print(tree.item(curItem)['values'])
                            quantifiers = (tree.item(curItem)['values'])

                            image_loader_gkc(quantifiers[2])

                        frame = Frame(user_add)
                        frame.place(x=0, y=650)

                        # print(data)

                        tree = ttk.Treeview(frame,
                                            columns=(1, 2, 3, 4, 5, 6, 7),
                                            height=17, show="headings")
                        tree.pack(side='left')
                        tree.bind('<ButtonRelease-1>', selectItem)

                        val = ["# GKC", "# KC", "Item", "Desc#KC", "Espec#", "Tol#", "Unid#"]

                        for i in range(1, len(val) + 1):
                            tree.heading(i, text=val[i - 1])

                        # tree.heading(2, text="Column 2")
                        # tree.heading(3, text="Column 3")

                        for i in range(1, len(val) + 1):
                            tree.column(i, width=272, anchor='center')

                        scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
                        scroll.pack(side='right', fill='y')

                        """scrollx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
                        scrollx.pack(side='bottom', fill='x')"""

                        tree.configure(yscrollcommand=scroll.set)

                        iterx = 0
                        for valx in data:
                            if iterx % 2 == 0:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6]),
                                            tags=('odd',))
                            else:
                                tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                               , valx[5], valx[6]),
                                            tags=('even',))

                            iterx += 1

                        tree.tag_configure('odd', background='#E8E8E8')
                        tree.tag_configure('even', background='#FFFFFF')

                        conn_SQL.close()

                        def command(x=0):

                            var0 = ""
                            var1 = ""
                            var2 = ""
                            var3 = ""
                            var4 = ""
                            var5 = ""
                            var6 = ""

                            if (self.tkvar0.get()) != '# GKC':
                                var0 = self.tkvar0.get()
                            if (self.tkvar1.get()) != '# KC':
                                var1 = self.tkvar1.get()
                            if (self.tkvar2.get()) != 'Item':
                                var2 = self.tkvar2.get()
                            if (self.tkvar3.get()) != 'Desc#KC':
                                var3 = self.tkvar3.get()
                            if (self.tkvar4.get()) != 'Espec#':
                                var4 = self.tkvar4.get()
                            if (self.tkvar5.get()) != 'Tol#':
                                var5 = self.tkvar5.get()

                            # print(var0,var1,var2,var3,var4,var5,var6)

                            conn_SQL = pymssql.connect("FPUNPUSQLDEV2.jdnet.deere.com\INST2", "jdaat",
                                                       "jdaat2012", "PU_FA_Testing")
                            cursor_SQL = conn_SQL.cursor()

                            query = """SELECT * FROM [PU_FA_Testing].[dbo].[gkcmaster] WHERE 
                                                              [# GKC] LIKE '%""" + str(var0) + """%' 
                                                              AND ([# KC] LIKE '%""" + str(var1) + """%' OR [# KC]  IS NULL) 
                                                              AND ([Item] LIKE '%""" + str(var2) + """%' OR [Item]  IS NULL)
                                                              AND ([Desc# KC] LIKE '%""" + str(var3) + """%' OR [Desc# KC]  IS NULL) 
                                                              AND ([Espec#] LIKE '%""" + str(var4) + """%' OR [Espec#]  IS NULL)
                                      AND ([Tol#] LIKE '%""" + str(var5) + """%' OR [Tol#]  IS NULL)

                                      """

                            # print(query)

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
                                if iterx % 2 == 0:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6]),
                                                tags=('odd',))
                                else:
                                    tree.insert('', 'end', values=(valx[0], valx[1], valx[2], valx[3], valx[4]
                                                                   , valx[5], valx[6]),
                                                tags=('even',))

                                iterx += 1

                            tree.tag_configure('odd', background='#E8E8E8')
                            tree.tag_configure('even', background='#FFFFFF')

                            conn_SQL.close()

                        self.tkvarbtn0 = ttk.Button(window, text="", width=450)
                        self.tkvarbtn0.place(x=0, y=625, height=30)

                        Label(user_add, text="SEARCH", font=("Ariel", 10), justify='left', bg='#E8E8E8',
                              width=35).place(
                            x=0, y=629)

                        self.tkvar0 = ttk.Combobox(window, text="tkvar0",
                                                   font=("Ariel", 10), values=Estudo_GKC, width=36, justify='center')
                        self.tkvar0.place(x=0, y=629)
                        self.tkvar0.set("# GKC")
                        self.tkvar0.bind("<<ComboboxSelected>>", command)

                        self.tkvar1 = ttk.Combobox(window, text="tkvar1",
                                                   font=("Ariel", 10), values=list(
                                set([data[x][1] for x in range(0, len(data))])), width=36, justify='center')
                        self.tkvar1.place(x=274, y=629)
                        self.tkvar1.set("# KC")
                        self.tkvar1.bind("<<ComboboxSelected>>", command)

                        self.tkvar2 = ttk.Combobox(window, text="tkvar2",
                                                   font=("Ariel", 10), values=Item, width=36, justify='center')
                        self.tkvar2.place(x=546, y=629)
                        self.tkvar2.set("Item")

                        self.tkvar2.bind("<<ComboboxSelected>>", command)

                        self.tkvar3 = ttk.Combobox(window, text="tkvar3",
                                                   font=("Ariel", 10), values=Desc_KC, width=36, justify='center')
                        self.tkvar3.place(x=818, y=629)
                        self.tkvar3.set("Desc#KC")

                        self.tkvar3.bind("<<ComboboxSelected>>", command)

                        self.tkvar4 = ttk.Combobox(window, text="tkvar4",
                                                   font=("Ariel", 10), values=Espec, width=36, justify='center')
                        self.tkvar4.place(x=1090, y=629)
                        self.tkvar4.set("Espec#")

                        self.tkvar4.bind("<<ComboboxSelected>>", command)

                        self.tkvar5 = ttk.Combobox(window, text="tkvar5",
                                                   font=("Ariel", 10), values=Tol, width=36, justify='center')
                        self.tkvar5.place(x=1362, y=629)
                        self.tkvar5.set("Tol#")

                        self.tkvar5.bind("<<ComboboxSelected>>", command)

                        self.tkvarbtn1 = ttk.Button(window, text="SEARCH", width=44, command=command)
                        self.tkvarbtn1.place(x=1637, y=628)

                a = App()

            s = ttk.Style()
            s.configure('my.TButton', font=('Aerial', 12, 'bold'))
            # b = ttk.Button(mainframe, text='Press me', style='my.TButton',

            self.btn0 = ttk.Button(user_add, text="DASHBOARD", style='my.TButton', width=20, command=dashboard)
            self.btn0.place(x=0, y=70, width=230, height=70)

            self.btn1 = ttk.Button(user_add, text="MASTER", style='my.TButton', width=20, command=master)
            self.btn1.place(x=230, y=70, width=230, height=70)

            self.btn3 = ttk.Button(user_add, text="R&R", style='my.TButton', width=20, command=RandR)
            self.btn3.place(x=460, y=70, width=230, height=70)

            self.btn4 = ttk.Button(user_add, text="CAPABILITY", style='my.TButton', width=20, command=cabs)
            self.btn4.place(x=690, y=70, width=230, height=70)

            self.btn5 = ttk.Button(user_add, text="GROUP_KC", style='my.TButton', width=20, command=gkc_master)
            self.btn5.place(x=920, y=70, width=230, height=70)

            dashboard()
            # cabs_next('KC_00749')

            # cabs_next('KC_01155')

        def quit(self):
            user_add.destroy()

    user_add = tk.Tk()
    user_add.iconbitmap(default='IMAGES/favicon.ico')
    # user_add.overrideredirect(True)
    # user_add.geometry("{0}x{1}+0+0".format(user_add.winfo_screenwidth(), user_add.winfo_screenheight()))
    user_login_window = user_add_kc(user_add)
    user_add.config(background='white')
    user_add.attributes('-alpha', 1)

    user_add.title('KC MANAGEMENT')
    user_add.geometry("1920x1080")
    user_add.mainloop()


if __name__ == "__main__":
    user_add_kc()
