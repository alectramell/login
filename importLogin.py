import os
import sys

def getREPO(url):

	import os
	XCOM = str('wget -nv "'+url+'"')
	os.system(XCOM)

getREPO('https://raw.githubusercontent.com/alectramell/login/master/login.py')

import login
