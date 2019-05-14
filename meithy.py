print '     Warung UPNORMAL'
print
print '   Daftar Menu'
print ' 1. Bakso'
print ' 2. Mie Ayam'
print ' 3. Soto'
print ' 4. Rawon'
print

def menu():
    x=(raw_input("Masukkan Pilihan Anda: "));
    if x=="1":
        print 'Bakso'
    elif x=="2":
        print 'Mie Ayam'
    elif x=="3":
        print 'Soto'
    elif x=="4":
        print 'Rawon'
    else:
        print 'Maaf inputan anda salah'
        print
        print 'Silahkan Pilih Ulang'
        print
        menu()

menu()

