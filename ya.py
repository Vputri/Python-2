print'          Program Kondisi UTS'
print
print'      Program Konversi Suhu'
print'      1.Celcius'
print'      2.Fahrenheit'
print'      3.Reamur'
print'      4.Kelvin'
def pilihan():
    print
    x=(raw_input("Masukkan Pilihan Anda[1-4]: "))
    if x=='1':
        print 'Pilihan Anda adalah celcius'
    elif x=='2':
        print 'Pilihan Anda adalah Fahrenheit'
    elif x=='3':
        print 'Pilihan Anda adalah Reamur'
    elif x=='4':
        print 'Pilihan Anda adalah Kelvin'
    else:
        print'Maaf Pilihan Anda Tidak Ada'
        print'Silahkan Masukkan Pilihan Ulang'
        pilihan()
pilihan()
