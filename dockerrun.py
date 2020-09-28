#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi

form = cgi.FieldStorage()
osname = form.getvalue("x")
imagename = form.getvalue("y")
#osname=input("Enter the OS name: ")
cmd = "sudo docker run -d -i -t --name {0} {1}".format(osname,imagename)
import subprocess as sp
output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status==0:
	print("OS launched named {0}..".format(osname))
else:
	print("some error :{1}".format(osname))
