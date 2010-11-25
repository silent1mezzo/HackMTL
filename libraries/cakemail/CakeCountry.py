import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassCountry"

# Gets the list of countries
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["country"])
	CakeFunctions.ChangeKey(res, "country", "countries")

	return res

# Gets the list of provinces for a specified country
def GetProvinces(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetProvinces", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["province"])
	CakeFunctions.ChangeKey(res, "province", "provinces")

	return res
