#!/usr/bin/python2
import cgi,commands,time
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
p=data.getvalue('p')
print "11"
x=commands.getoutput("sudo docker run -itd centos6")

if p=='a':	
	user="a"
	passwd="q"	
	commands.getoutput("sudo docker start "+x)		
	commands.getoutput("sudo docker attach "+x)
	commands.getoutput("sudo useradd -s /usr/bin/python a")
	commands.getoutput("sudo echo q | passwd a --stdin")
	
elif p=='b':
	user="b"
	passwd="q"
	commands.getoutput("sudo docker start "+x)		
	commands.getoutput("sudo docker attach "+x)	
	commands.getoutput("sudo useradd -s /usr/bin/java b")
	commands.getoutput("sudo echo q | passwd b --stdin")
	
else:	
	user="c"
	passwd="q"	
	commands.getoutput("sudo docker start "+x)		
	commands.getoutput("sudo docker attach "+x)
	commands.getoutput("sudo useradd -s /usr/bin/python c")
	commands.getoutput("sudo echo q | passwd c --stdin")
	
ip=commands.getoutput("sudo docker exec "+x+" hostname -i")

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>PAAS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">AMAZON AWS</h1>
  <div class="list-group">
    <p>Container id -> <b> '''+x+'''</b></p>
    <p>USER -> <b>'''+user+'''</b></p>
    <p>PASSWORD -> <b>'''+passwd+'''</b></p>
    <a href="https://'''+ip+''':4200">GO</a>
  </div>
</div>
</body>
</html>
'''

print web
