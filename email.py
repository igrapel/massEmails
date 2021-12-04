# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:58:51 2021

@author: ilang
"""

import win32com.client



outlook = win32com.client.Dispatch('outlook.application')

class Email:
    def __init__(self, subject, to, student, gender):
        self.mail = outlook.CreateItem(0)
        self.mail.To = to
        self.mail.Subject = subject
        self.mail.Body = ""
        self.gender = gender
        self.name = student
        #mail.HTMLBody = '<h3>This is HTML Body</h3>'
    
    def send(self):
        if(self.gender == "Male"):
            adj = "his";
            obj = "him";
        elif(self.gender == "Female"):
            adj = "her";
            obj = "her";
        else:
            adj = "they";
            obj = "their";
        message = "Dear parents, " + "\n\nI am " + self.name + "'s computer science teacher. " +\
        self.name + " is not completing " + adj + " work. As a result, " +\
        self.name + " is in danger of failing the class. I hope you can speak with " + obj  + \
        " and encourage " + obj + " to put in the effort to pass the class.\n\n" +\
        "Sincerely, \n\nMr. Ilan Grapel\nIB and AP Computer Science \nCoral Gables Senior High";

        self.mail.Body = message
        self.mail.Send()
        
        
test = Email('Fail', 'ib.ilanc@gmail.com', 'Dan', "Male")
test.send()

