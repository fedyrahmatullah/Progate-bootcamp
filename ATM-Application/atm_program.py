import random
import datetime
from random import Random
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan Pin Anda : "))
    trial = 0
    
    while (id != int(atm.checkPin()) and trial < 3 ):
        id = int(input("Pin Anda Salah, Silahkan Masukkan Lagi : "))
        trial += 1
        
        if trial == 3:
            print("Error. Silahkan Ambil kartu dan coba lagi..")
            exit()
    print('\n Selamat datang di ATM Progate....')
    print(' 1. - Cek Saldo. \n 2. - Debet. \n 3. - Simpan. \n 4. - Ganti Pin. \n 5. - Keluar.')
    selectmenu = int(input('\n Silahkan Pilih Menu : '))
            
    if selectmenu == 1:
        print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n")
    elif selectmenu == 2:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(nominal) + " ")
                
        if verify_withdraw == "y":
            print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
        else:
            break
        if nominal < atm.checkBalance():
            atm.withdrawBalance(nominal)
            print("Transaksi debet berhasil!")
            print("Saldo sisa anda sekarang: Rp. " + str(atm.checkBalance()) + "")
        else:
            print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
            print("Silahkan lakukan penambahan nominal saldo")
    elif selectmenu == 3:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")
                
        if verify_deposit == "y":
            atm.depositBalance(nominal)
            print("Saldo anda sekarang adalah: Rp. " + str(atm.checkBalance()) + "\n")
        else:
            break
                    
    elif selectmenu == 4 :
            verify_pin = int(input('Masukkan Pin Anda : '))

            while verify_pin != int(atm.checkPin()):
                print('Pin Anda Salah, silahkan masukkan pin')
                exit('Status : '+ str(atm.Error))
            updated_pin = int(input("Silahkan masukkan pin baru: "))
            print("Pin anda berhasil diganti")

            verify_newpin = int(input("Coba masukkan pin baru: "))
                    
            if verify_newpin == updated_pin:
                print("Pin anda sukses!")
            else:
                print("Maaf, pin anda salah!")
                break

    elif selectmenu == 5 :
        print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
        print('\nNo. Record : ', random.randint(10000, 1000000))
        print('Tanggal : ', datetime.datetime.now())
        print('Saldo Akhir : Rp. ', atm.checkBalance())
        exit(" \nTerimakasih Telah Menggunakan ATM Progate! ")
    else:
        print("Error. Maaf, menu tidak tersedia")
                        