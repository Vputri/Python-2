x = int(input("Masukkan angka :"))

while y <= x:
	k = y

	while k > 0:
		string = string + " * "
		k = k- 1
		
	string = string + "\n"
	y = y + 1
print (string)
