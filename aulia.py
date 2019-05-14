
def balok() :
    print " Menghitung Volume Balok "
    p= raw_input ("Masukkan Panjang Balok : ")
    l= raw_input ("Masukkan Lebar Balok : ")
    t= raw_input ("Masukkan Tinggi Balok : ")
    volume = int(p)*int(l)*int(t)
    print "Volume Balok adalah ",volume

def lingkaran() :
    print " Menghitung Volume lingkaran "
    r=raw_input("Masukkan jari-jari lingkaran : ")
    keliling= 3.14*int(r)**2
    print "Keliling lingkaran adalah ",keliling

def kubus() :
    print " Menghitung Volume Kubus "
    s=raw_input("Masukkan Sisi Kubus: ")
    volume = int(s)*int(s)*int(s)
    print "Volume Kubus adalah ",volume


print " PROGRAM HITUNG MATEMATIKA "
print
lingkaran()
print

kubus()
print

balok()

