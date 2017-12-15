import re

string = "inxdonesia"
# string = "http://dmoztools.net/Kids_and_Teens/School_Time/Social_Studies/Geography/Asia/Indonesia/"
result = re.match('indo|indonesian', string,re.I)

if result : 
	print "ada"
else :
	print "nope"