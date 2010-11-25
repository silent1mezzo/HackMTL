import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassRelay"

# Retrieves the logs
def GetLogs(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLogs", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Sends an email
def Send(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Send", parameters, locale)

	return True
