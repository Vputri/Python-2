print '     Angkringan'
print
print '   Daftar Menu'
print ' 1. Telur'
print ' 2. Sosis'
print ' 3. Nasi Kucing'
print ' 4. Nasi Bakar'
print

def menu():
    x=(raw_input("Masukkan Pilihan Anda: "));
    if x=="1":
        print 'Telur'
    elif x=="2":
        print 'Sosis'
    elif x=="3":
        print 'Nasi Kucing'
    elif x=="4":
        print 'Nasi Bakar'
    else:
        print 'Maaf inputan anda salah'
        print
        print 'Silahkan Pilih Ulang'
        print
        menu()

menu()


