import hashlib,sys    

filename = sys.argv[1]      

with open(filename) as f:
    data = f.read()    
 
    md5_returned = hashlib.md5(data).hexdigest()

print md5_returned
