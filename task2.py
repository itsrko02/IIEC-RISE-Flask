#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
form = cgi.FieldStorage()
print('<html><form action="http://192.168.43.60/task2.html"><button>Go Back</button></form></html>')
try:
	cmd=form.getvalue('x')
	if ('exit' in cmd):
		exit()
	elif('docker' in cmd and 'launch' in cmd):
		print('<html><form action="http://192.168.43.60/dockerform.html"><button>Launch Docker</button></form></html>')

	else:
		output=sp.getstatusoutput(cmd)
		if output[0]==0:
			print('<html><body><pre>'+output[1]+'</pre></body></html>')
		else:
			print("Error Occurred")
			print('<html><body><pre>'+'Error : '+output[1]+'</pre></body></html>')


except:
	pass 	
