import urllib.request as url 
import colorama
import time
import os
import requests
from colorama import Fore
from urllib3 import response

colorama.init(autoreset=True)
os.system('cls' or 'clear')

print(r"""        
| | | |          (_)      
| |_| | _____   ___ _ __  
|  _  |/ _ \ \ / / | '_ \ 
| | | |  __/\ V /| | | | |
\_| |_/\___| \_/ |_|_| |_| """)

print("========================================================")

ip = input(Fore.RED + "What's your ip target: ")
url = "https://ipinfo.io/"
response= requests.get(url+ip)
data = response.json()

city = data['city']
IpAddress = data['country']
Timezone = data['timezone']
Org = data['org']
Postal = data['postal']

location = data['loc'].split(',')
lati = location[0]
longi = location[1]

print(Fore.GREEN + "\n IP: ", ip)
time.sleep(0.5)
print(Fore.GREEN + "\n City : ", city)
time.sleep(0.5)
print(Fore.GREEN + "\n Country: ", IpAddress)
time.sleep(0.5)
print(Fore.GREEN + "\n Timezone: ", Timezone)
time.sleep(0.5)
print(Fore.GREEN + '\n Org: ', Org)
time.sleep(0.5)
print(Fore.GREEN + '\n Postal: ', Postal)
time.sleep(0.5)
print(Fore.GREEN + '\n Latitude: ', lati)
time.sleep(0.5)
print(Fore.GREEN + '\n Longitude: ', longi)
time.sleep(0.5)
print(Fore.RED + '\n =============> Location: ', lati, longi)