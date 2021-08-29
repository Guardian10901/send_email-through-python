# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:49:42 2021

@author: vidya v
"""


import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():
    senders_email='vidyav10901@gmail.com'
    password=getpass.getpass()
    subject='AI Mafia -Mechine learning'
    msg=''' 
    
         Hello,thank you for the oppertunity and guidence to learn 
                     and pratice different
         aspects of python and mechine learning.
         
         
    '''
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senders_email, password)
    
    #draft message
    msg=MIMEText(msg)
    msg['Subject'] =subject
    msg['From'] =senders_email
    msg['To']  ='vidyaviswanathan2000@gmail.com'
    recipient='vidyaviswanathan2000@gmail.com'
    server.sendmail(senders_email,recipient, msg.as_string())
send_email()