import random 
import os
import time

upper = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
lower = upper.lower()
digits = "0123456789"
symbols = "()[]{};,:/*!.-?#%&"

karisik = upper + lower + digits + symbols

sembolsuz = upper + lower + digits

sayisiz = upper + lower

buyuk = upper

uzun = 5
miktar = 20

os.system("color c")
os.system("cls")
os.system("echo off")
print("Bir Method Seç.")
print("[1] Karışık")
print("[2] Sembolsüz")
print("[3] Rakamsız")
print("[4] Klasik")

kontrol = input("Method: ")

if kontrol == '1':
    os.system("cls")
    os.system("color a")
    for x in range(uzun):
        sif = "".join(random.sample(karisik, miktar))
        print(sif)

if kontrol == '2':
    os.system("cls")
    os.system("color a")
    for x in range(uzun):
        sif1 = "".join(random.sample(sembolsuz, miktar))
        print(sif1)
    
if kontrol == '3':
    os.system("cls")
    os.system("color a")
    for x in range(uzun):
        sif11 = "".join(random.sample(sayisiz, miktar))
        print(sif11)

if kontrol == '4':
    os.system("cls")
    os.system("color a")
    for x in range(uzun):
        sif11 = "".join(random.sample(buyuk, miktar))
        print(sif11)

