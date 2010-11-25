import CakeGlobals

def AddMessage(message):
	if CakeGlobals.DEBUG:
		f = open(CakeGlobals.LOG_FILENAME, 'a')
		try:
			f.write(message + "\n\n")
		finally:
			f.close
