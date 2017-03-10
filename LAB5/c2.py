import sys, crypt, random, string
from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(path, pattern, subst):
	fh, abs_path = mkstemp()
	with open(abs_path, 'w') as new_file:
		with open(path) as old_file:
            		for line in old_file:
                		new_file.write(line.replace(pattern, subst))
    	close(fh)
   	remove(path)
	move(abs_path, path)

user = raw_input('Login: ')
old = raw_input('Old pass: ')
new = raw_input('New pass: ')

salt = ''.join(random.sample(string.ascii_letters, 2))
newCrypted = crypt.crypt(new, salt)

with open ('.htpasswd') as f:
	for line in f:
		t = line.split(':')

		name = t[0]
		passw = t[1]

		if name == user:
			s = ''.join([passw[0], passw[1]])
			oldCrypted = crypt.crypt(old,s)
			
			if (oldCrypted == passw.split('\n')[0]):
				print 'Zmieniam haslo, nowe to %s' % (newCrypted)
				replace('.htpasswd', passw, ''.join([newCrypted, '\n']))			
			else: 
				print 'Zle haslo'
			

	
