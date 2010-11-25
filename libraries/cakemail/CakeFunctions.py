from CakeException import CakeException
from CakeHash import CakeHash
from CakeXML import CakeXML

import urllib

def Proccess(className, methodName, parameters, locale, reverseData = False):
	cakeXML = CakeXML()

	cakeXML.Init()

	cakeXML.AddClass(className, locale)
	cakeXML.AddMethod(methodName)

	cakeXML.AddParameters(parameters, reverseData)

	cakeXML.CloseMethod()
	cakeXML.CloseClass()
	cakeXML.Close()

	cakeXML.ExecXML()

	resultNode = cakeXML.response.firstChild

	CheckError(resultNode)

	methodNode = GetXMLMethod(resultNode, className, methodName)
	CheckError(methodNode)

	return methodNode

def GetXMLMethod(root, className, methodName):
	for classNode in root.childNodes:
		if classNode.nodeType == classNode.ELEMENT_NODE and classNode.nodeName == "class" and classNode.attributes["type"].value == className:
			for methodNode in classNode.childNodes:
				if methodNode.nodeType == methodNode.ELEMENT_NODE and methodNode.nodeName == "method" and methodNode.attributes["type"].value == methodName:
					return methodNode

	return None

def CheckError(node):
	if node.childNodes and node.childNodes.length > 1 and (node.childNodes[1].nodeName == "error_code" or node.childNodes[1].nodeName == "error_message"):
		raise CakeException(_get_node_text(node.getElementsByTagName("error_code")[0]), _get_node_text(node.getElementsByTagName("error_message")[0]))

def ParseXML(node, subListNames = [], reverseData = False):
	res = CakeHash()

	for itemNode in node.childNodes:
		if itemNode.nodeType == itemNode.ELEMENT_NODE:
			itemName = itemNode.nodeName

			if itemName == "data":
				if reverseData:
					res[_get_node_text(itemNode)] = urllib.unquote(itemNode.attributes["type"].value)
				else:
					res[urllib.unquote(itemNode.attributes["type"].value)] = _get_node_text(itemNode)
			else:
				if itemNode.childNodes and itemNode.childNodes.length > 1:
					if itemName in res and (isinstance(res[itemName], CakeHash) or isinstance(res[itemName], dict)):
						resList = res[itemName]
					else:
						resList = CakeHash()
						res[itemName] = resList

					resList[len(resList)] = ParseXML(itemNode, subListNames)
				else:
					if itemName in res or itemName in subListNames:
						if itemName in res and (isinstance(res[itemName], CakeHash) or isinstance(res[itemName], dict)):
							resList = res[itemName]
						else:
							resList = CakeHash()
							if itemName in res:
								resList[0] = res[itemName]

							res[itemName] = resList

						resList[len(resList)] = _get_node_text(itemNode)
					else:
						res[itemName] = _get_node_text(itemNode)

	return res

def ChangeKey(res, oldName, newName):
	if oldName in res:
		res[newName] = res[oldName]
		del(res[oldName])

def _get_node_text(node):
	return node.childNodes and urllib.unquote(node.childNodes[0].data) or ""
