import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassSuppressionList"

# Imports one or more domains into the suppression list
def ImportDomains(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ImportDomains", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Imports one or more emails into the suppression list
def ImportEmails(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ImportEmails", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Imports one or more local-parts into the suppression list
def ImportLocalparts(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ImportLocalparts", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Exports the domains from the suppression list
def ExportDomains(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ExportDomains", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Exports the emails from the suppression list
def ExportEmails(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ExportEmails", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Exports the local-parts from the suppression list
def ExportLocalparts(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "ExportLocalparts", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Deletes one or more domains from the suppression list
def DeleteDomains(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "DeleteDomains", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Deletes one or more emails from the suppression list
def DeleteEmails(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "DeleteEmails", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Deletes one or more local-parts from the suppression list
def DeleteLocalparts(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "DeleteLocalparts", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res
