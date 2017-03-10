import sys,string
enc = open(sys.argv[1]).read()
enc = string.split(enc, " ")
string = range(len(enc))

#Bruteforsujemy klucz nie tekst !

for i in range(len(enc)):
	sys.stdout.write(enc[i])
print ""

for i in range(len(enc)):	
	for j in range(26):
		string[i] = chr(j+97)
		print string		
