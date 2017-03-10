import sys, re, string, operator

stat = {}
suma = 0
nazwa = sys.argv[1]
text = open(sys.argv[1]).read() 

tab = range(26)
stats = ["e", "t", "a", "o", "i", "s", "n", "h", "r", "d", "l", "u", "m", "c", "f", "g", "w", "y", "p", "b", "k", "v", "j", "x", "q", "z"]

for i in range(26):
	tab[i]=0


for line in text:
	line = re.sub(r'\s', '', line)
	line = line.lower()
	for znak in line:
		suma += 1
		tab[ord(znak)-97] += 1
	#	if znak in stat:
	#		stat[znak] += 1
	#	else:
	#		stat[znak] = 1

tab = sorted(tab, key=int, reverse=True)

for i in range(26):	
	procent = float(tab[i]) / float(suma) * 100
	print "%s <=> %.3f procent" % (chr(i+97), procent)

tab = sorted(tab, key=int, reverse=True)
	
