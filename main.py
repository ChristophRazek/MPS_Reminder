import win32com.client as win32
import warnings
import pyodbc
import pandas as pd
import SQL as s
from datetime import date

warnings.filterwarnings('ignore')
today = date.today()

#Datenbankverbindung
connx_string = r'DRIVER={SQL Server}; server=172.19.128.2\emeadb; database=emea_enventa_live; UID=usr_razek; PWD=wB382^%H3INJ'
conx = pyodbc.connect(connx_string)

#Reading SQL for open MPS
df = pd.read_sql_query(s.offene_MPS, conx)

#Adjusting File
df['PO'] = df['PO'].astype('int64')
df['MPS Received'] = 'no'
df.to_excel(r'S:\EMEA\Kontrollabfragen\MPS_Reminder.xlsx', index= False)



def send_mail():

    receivers = ['yian.su@emea-cosmetics.com']
    cc = ['christoph.razek@emea-cosmetics.com','dzanana.dautefendic@emea-cosmetics.com']

    #creating an win32 object/mail object
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)


    #mail.Font.Name = 'Georgia'
    mail.To = ";".join(receivers)
    mail.CC = ";".join(cc)
    mail.Subject = f'MPS Reminder'
    mail.HTMLBody = """<font face='Calibri, Calibri, monospace'>
    Good Day, <br><br>
    Please send us Mass Production Samples (MPS) in the list attached as the delivery dates will soon be reached.<br>
    In case there are problems, please inform us as soon as possible.<br>
    If you have any questions please feel free to contact me (yian.su@emea-cosmetics.com).<br><br>
    Thank you and kind regards.<br>
    <br>
    您好，<br>
    請盡快寄出MPS。若有任何問題，請提前通知，謝謝。 
    </font>"""
    mail.Attachments.Add(r'S:\EMEA\Kontrollabfragen\MPS_Reminder.xlsx')

    mail.Display()
    mail.Save()
    #mail.Send()

#Email nur senden wenn Liefertermin innerhalb des Zeitfensters
if df.shape[0] == 0:
    with open(r'S:\EMEA\Kontrollabfragen\MPS_Reminder.txt','w') as file:
        file.write(f'Keine MPS Erinnerung da am {today} keine Liefertermine innerhalb des Zeitfensters!')
else:
    send_mail()
    with open(r'S:\EMEA\Kontrollabfragen\MPS_Reminder.txt','w') as file:
        file.write(f'MPS Reminder wurde zuletzt am {today} verschickt!')