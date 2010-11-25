import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassTrigger"

# Creates a new trigger
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Gets a trigger
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Returns the list of links for a trigger
def GetLinks(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLinks", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["link"])
	CakeFunctions.ChangeKey(res, "link", "links")

	return res

# Returns the total and unique counts of openings for triger's links
def GetLinksLog(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLinksLog", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["link"])
	CakeFunctions.ChangeKey(res, "link", "links")

	return res

# Retrieves the list of triggers
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["trigger"])
	CakeFunctions.ChangeKey(res, "trigger", "triggers")

	return res

# Returns the logs of a trigger
def GetLog(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLog", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["count", "daily", "hourly", "log"])
	CakeFunctions.ChangeKey(res, "log", "logs")

	return res

# Sets the parameters for a trigger
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True

# Unleashes a trigger
def Unleash(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Unleash", parameters, locale)

	return True
