from CakeHash import CakeHash

CAKE_VERSION = "1.0"
API_CAKE_URL = "http://api.cakemail.com"
CAKE_MCRYPT_ALG = "Blowfish" # Blowfish only
CAKE_MCRYPT_MODE = "ECB" # ECB only
CAKE_INTERFACE_KEY = ""
CAKE_INTERFACE_ID = 0
DEFAULT_LOCALE = "en_US"
DEBUG = False
LOG_FILENAME = ""

# Load the properties from ini file
#
# Rename CakeGlobals.ini.template to CakeGlobals.ini,
# fill each parameter and use CakeGlobals.LoadFromIniFile('CakeGlobals.ini')
def LoadFromIniFile(iniFile):
	props = CakeHash()

	f = open(iniFile)
	try:
		for line in f:
			prop = line.partition('=')
			props[prop[0].strip()] = prop[2].strip()
	finally:
		f.close
		
	import sys
	mod = sys.modules[__name__]
	mod.CAKE_VERSION = props["CAKE_VERSION"]
	mod.API_CAKE_URL = props["API_CAKE_URL"]
	mod.CAKE_MCRYPT_ALG = props["CAKE_MCRYPT_ALG"]
	mod.CAKE_MCRYPT_MODE = props["CAKE_MCRYPT_MODE"]
	mod.CAKE_INTERFACE_KEY = props["CAKE_INTERFACE_KEY"]
	mod.CAKE_INTERFACE_ID = int(props["CAKE_INTERFACE_ID"])
	mod.DEFAULT_LOCALE = props["DEFAULT_LOCALE"]
	mod.LOG_FILENAME = props["LOG_FILENAME"]
	mod.DEBUG = ((props["DEBUG"].upper() == 'TRUE' or props["DEBUG"] == '1') and True or False)
