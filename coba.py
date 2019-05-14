from datetime import datetime
kini=datetime.now()
jam=kini.hour
menit=kini.minute
detik=kini.second

print "{}:{}:{}".format(jam, menit, detik)
