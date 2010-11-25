import CakeGlobals
import CakeFunctions

CLASS_NAME = "ClassList"

# Adds a test e-mail to list
def AddTestEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "AddTestEmail", parameters, locale)

	return True

# Creates a list
def Create(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Create", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["id"])

# Creates a sublist
def CreateSublist(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "CreateSublist", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["sublist_id"])

# Deletes a list
def Delete(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "Delete", parameters, locale)

	return True

# Deletes an e-mail from a list
def DeleteEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "DeleteEmail", parameters, locale)

	return True

# Deletes a record from a list
def DeleteRecord(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "DeleteRecord", parameters, locale)

	return True

# Deletes a sublist from a list
def DeleteSublist(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "DeleteSublist", parameters, locale)

	return True

# Deletes a test e-mail from a list
def DeleteTestEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "DeleteTestEmail", parameters, locale)

	return True

# Edits the structure of the list
def EditStructure(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "EditStructure", parameters, locale)

	return True

# Gets the list's fields
def GetFields(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetFields", parameters, locale)

	return CakeFunctions.ParseXML(methodNode, [], True)

# Gets the list's informations
def GetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetInfo", parameters, locale)

	return CakeFunctions.ParseXML(methodNode.elements[1])

# Gets the lists with a specified status
def GetList(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetList", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Retrieves a single record from a list
def GetRecord(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetRecord", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)

# Gets the sublists of a list
def GetSublists(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetSublists", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["sublist"])
	CakeFunctions.ChangeKey(res, "sublist", "sublists")

	return res

# Gets the list of the test e-mails
def GetTestEmails(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "GetTestEmails", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["test_email"])
	CakeFunctions.ChangeKey(res, "test_email", "test_emails")

	return res

# Imports records into a list
def Import(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Import", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Sets the parameters for a list
def SetInfo(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "SetInfo", parameters, locale)

	return True

# Searchs a list after a set of conditions
def Search(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Search", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Shows a list
def Show(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Show", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Subscribes an e-mail to a list
def SubscribeEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "SubscribeEmail", parameters, locale)

	return int(CakeFunctions.ParseXML(methodNode)["record_id"])

# Tests a sublist before creation
def TestSublist(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "TestSublist", parameters, locale)

	res = CakeFunctions.ParseXML(methodNode, ["record"])
	CakeFunctions.ChangeKey(res, "record", "records")

	return res

# Unsubscribes an e-mail from a list
def UnsubscribeEmail(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "UnsubscribeEmail", parameters, locale)

	return True

# Updates a record into a list
def UpdateRecord(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	CakeFunctions.Proccess(CLASS_NAME, "UpdateRecord", parameters, locale)

	return True

# Uploads a file into a list
def Upload(parameters, locale = CakeGlobals.DEFAULT_LOCALE):
	methodNode = CakeFunctions.Proccess(CLASS_NAME, "Upload", parameters, locale)

	return CakeFunctions.ParseXML(methodNode)
