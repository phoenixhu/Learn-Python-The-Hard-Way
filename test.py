import re
s = raw_input()
if re.match(r'^\w{3, 18}\@qq|vip\.qq\.com', s):
	print "ok"
else:
	print "no"	