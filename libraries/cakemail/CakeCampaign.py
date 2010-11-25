import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassCampaign"

# Creates a new campaign
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Deletes a campaign
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Gets the list of campaigns specified by status
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["campaign"])
	CakeFunctions.ChangeKey(res, "campaign", "campaigns")

	return res

# Retrieves the campaign's infos
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the count of mailings assigned to a campaign
def GetMailingsCount(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	raise CakeException.new("Not realized")

# Sets the parameters for a campaign
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True
