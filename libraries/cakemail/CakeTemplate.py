import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassTemplate"

# Creates a new template
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Deletes a template
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Gets the list of templates specified by status
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["template"])
	CakeFunctions.ChangeKey(res, "template", "templates")

	return res

# Retrieves the template's infos
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Sets the parameters for a template
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True
