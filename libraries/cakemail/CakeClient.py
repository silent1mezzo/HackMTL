import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassClient"

# Activates a client
def Activate(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Activate", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Adds credits to a client
def AddCredits(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "AddCredits", parameters, locale)

	return True

# Creates a new client
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the credit balance
def GetCreditBalance(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetCreditBalance", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the credit transactions
def GetCreditTransactions(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetCreditTransactions", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Retrieves the informations about the client
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the list with a specified status
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["client"])
	CakeFunctions.ChangeKey(res, "client", "clients")

	return res

# Gets the timezones
def GetTimezones(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetTimezones", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["timezone"])
	CakeFunctions.ChangeKey(res, "timezone", "timezones")

	return res

# Adds or removes credits to a client for the balance to be 0 at the end of the month
def ResetCredits(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "ResetCredits", parameters, locale)

	return True

# Sets the parameters for a user
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True

# Searchs for clients based on a query string
def Search(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Search", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["client"])
	CakeFunctions.ChangeKey(res, "client", "clients")

	return res
