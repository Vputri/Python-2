print;
from datetime import datetime
sekarang=datetime.now()
hari=sekarang.day
bulan=sekarang.month
tahun=sekarang.year
jam=sekarang.hour
menit=sekarang.minute
detik=sekarang.second
print ''
print '                                                  Tanggal : {}/{}/{}'.format(hari,bulan,tahun)
print "                                                  Jam     : {}:{}:{}".format(jam,menit,detik)
print;
print '                         PROGRAM Bilangan Genap';
print '                          Vika Putri Ariyanti'
print;

string = ""
y = 1

def menu():
    x = int(input("   Masukkan angka : "))
    print;
    if (x % 2) == 0:
        print '  ',x,' adalah bilangan genap';
    else:
        print '  ',x,' adalah bilangan ganjil';

    print
    print '  ===========================================================================';
    print
    n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
    print
    print '  ===========================================================================';
    
    if n in ["Y", "y"]:
        print ''
        menu()
    elif n in ["N", "n"]:
        exit()
    else:
        print ''
        print "   Maaf anda salah menginput"
        print ''
        n = raw_input("   Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
menu()
