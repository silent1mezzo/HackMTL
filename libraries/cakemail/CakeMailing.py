import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassMailing"

# Creates a mailing
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Deletes a mailing
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Gets the formated email message
def GetEmailMessage(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetEmailMessage", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the formated HTML message
def GetHtmlMessage(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetHtmlMessage", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)["html_message"]

# Gets a mailing
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["mailing"])
	CakeFunctions.ChangeKey(res, "mailing", "mailings")

	return res

# Returns the list of links for a mailing
def GetLinks(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLinks", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["link"])
	CakeFunctions.ChangeKey(res, "link", "links")

	return res

# Returns the total and unique counts of openings for mailing's links
def GetLinksLog(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLinksLog", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["link"])
	CakeFunctions.ChangeKey(res, "link", "links")

	return res

# Retrieves the list of mailings
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["mailing"])
	CakeFunctions.ChangeKey(res, "mailing", "mailings")

	return res

# Returns the logs of a mailing
def GetLog(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetLog", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["count", "log"])
	CakeFunctions.ChangeKey(res, "log", "logs")

	return res

# Gets a mailing information
def GetStats(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetStats", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the formated TEXT message
def GetTextMessage(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetTextMessage", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)["text_message"]

# Resumes a suspended mailing
def Resume(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Resume", parameters, locale)

	return True

# Schedules a mailing
def Schedule(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Schedule", parameters, locale)

	return True

# Suspends a mailing
def Suspend(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Suspend", parameters, locale)

	return True

# Sends a test email
def SendTestEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SendTestEmail", parameters, locale)

	return True

# Sets the parameters for a mailing
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True

# Unschedules a mailing
def Unschedule(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Unschedule", parameters, locale)

	return True
