import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0
    
    while (id != int(atm.checkPin())) and trial < 3):
        id = int(input("Pin anda salah. silakan masukkan lagi: "))
        trial += 1
        
        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()