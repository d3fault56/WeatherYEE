#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:52:36 2024

@author: dyllonreyes
"""

import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "c710ce79f2b0a4e7da262a1955374819"
CITY = "San Antonio"

def kelv_to_cel_fah(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_cel, temp_fah = kelv_to_cel_fah(temp_kelvin)

feels_like_kelv = response['main']['feels_like']
feels_like_cel, feels_like_fah = kelv_to_cel_fah(feels_like_kelv)

humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])




x = f"Temperature in {CITY} is {temp_cel:.2f}°C or {temp_fah:.2f}°F"
z = f"Temperature in {CITY} feels like {feels_like_cel:.2f}°C or {feels_like_fah:.2f}°F"
print(x)
print(z)

if temp_fah < 75 and temp_fah >= 70:
    print("Possible jacket needed due to mild weather.")
elif temp_fah <= 69 and temp_fah >= 60:
    print("Recommended jacket needed due to cold weather.")
elif temp_fah <= 59:
    print("Jacket needed due to freezing weather.")
    
    
import smtplib  
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "rowdyhacks1@gmail.com"
    msg['from'] = user
    password = "utarpkvpxmtbonqh"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()
    
if __name__ == '__main__':
    email_alert("Hey", "uwu", "2107277669@vtext.com")