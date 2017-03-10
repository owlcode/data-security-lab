import sys
filename = sys.argv[1]
n = sys.argv[2]
tab = []
string = ''

with open(filename) as f:
	data = f.read();

for c in data:
	x = ord(c)
	tab.append(x)

for i in range(0,len(tab)):
	string.join('', [string, chr(tab[i])]);

for i in range(0,len(tab)):
	print tab[i]

print string

