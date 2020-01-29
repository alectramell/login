def getUser():

	import os
	import sys
	import getpass
	global xuser
	xuser = str(input('Username: '))

def getPass():

	import os
	import sys
	import getpass
	global xpass
	xpass = str(getpass.getpass('Password: '))

def echoPass():

	import os
	import sys
	import getpass
	return xpass

def echoUser():

	import os
	import sys
	import getpass
	return xuser

def help():

	import os
	import platform
	OSname = str(platform.system())
	if OSname == "Windows":
		def clear():
			import os
			os.system('cls')
	else:
		def clear():
			import os
			os.system('clear')
	clear()
	print('[ Login Python Module v1.0 | Tramell Software Development (r) ]')
	print('Import Login Module..')
	print(' >> import login')
	print('Get Username by Input..')
	print(' >> login.getUser()')
	print('Get Password by Input..')
	print(' >> login.getPass()')
	print('Retrieve Username..')
	print(' >> login.echoUser()')
	print('or..')
	print(' >> print(login.echoUser())')
	print('Retrieve Password..')
	print(' >> login.echoPass()')
	print('or..')
	print(' >> print(login.echoPass())')
