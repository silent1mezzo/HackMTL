import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassUser"

# Checks for a permission on a user
def CheckPermission(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "CheckPermission", parameters, locale)

	return True

# Creates a user
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Delete a user
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Gets the informations about a user
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["user"])
	CakeFunctions.ChangeKey(res, "user", "users")

	return res

# Gets the list with a specified status
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["user", "group_id"])
	CakeFunctions.ChangeKey(res, "user", "users")

	return res

# Recovers a password for a user
def PasswordRecovery(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "PasswordRecovery", parameters, locale)

	return True

# Logs-in a user
def Login(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Login", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Sets the parameters for a user
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True
