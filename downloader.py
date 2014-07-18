from time import sleep
from ftplib import FTP
from sys import exit
global ftp

def startFTPdownload():
	global ftp
	print "Connecting to host...."
	try:
		ftp = FTP('<host name>', timeout=3600)
	except Exception as e:
		print "Connection could not be established"
		print "Error: {}".format(e)
		print "Rtrying............"
		start()
		# exit(0)
	print "Connection established .."
	print "Logging in......"
	try:
		ftp.login('<username>','<password>')
	except Exception as e:
		print "Login Failed"
		print "Error: {}".format(e)
		exit(0)
	print "Logged in successfully.."
	fl = []
	ftp.retrlines('NLST',fl.append)
	filelist = []
	for i in range(len(fl)):
		if fl[i] !="." and fl[i] !="..":
			filelist.append(fl[i])

	localpath = "C:\\upload\\"
	for fn in filelist:
		lfn = localpath+fn
		fo = open(lfn,'wb')
		ftp.retrbinary('RETR'+fn,fo.write)
		fo.close()
		
def stopFTPdownload():
	global ftp
	ftp.close()

def start():
	startFTPdownload()
	sleep(60)
	stopFTPdownload()

while True:
	start()