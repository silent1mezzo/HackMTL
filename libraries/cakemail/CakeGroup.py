import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassGroup"

# Adds a user to a group
def AddUser(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "AddUser", parameters, locale)

	return True

# Creates a new group
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Deletes a group
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Gets the informations of a group
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["permission"])
	CakeFunctions.ChangeKey(res, "permission", "permissions")

	return res

# Returns the list of the groups
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["group"])
	CakeFunctions.ChangeKey(res, "group", "groups")

	return res

# Removes a user from a group
def RemoveUser(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "RemoveUser", parameters, locale)

	return True

# Sets the informations of a group
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True
