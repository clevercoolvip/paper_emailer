import schedule
from scraper import *
import time
import smtplib
import pandas as pd

sender_mail = "pundeerutkarsh2001@gmail.com"
sender_password = "vicodblcxcjuohmc"
message = ""


data = pd.read_csv("info.csv")
req = data.iloc[len(data)-1, :].to_list()
to_mail, interest, day = req[0], req[1], req[2]


urls, paras, pdf = fetch_data(to_mail, interest)
message = f"""
    {paras[0]}\n
    \n
    here is the link of the paper of the respective information provided above\n
    {list(pdf.values())[0]}
"""
print(message)

def send_mail(from_mail, to_mail, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    server.sendmail(from_mail, to_mail, message)
    server.quit()


send_mail(sender_mail, to_mail, sender_password, message)



