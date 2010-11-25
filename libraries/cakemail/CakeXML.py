from CakeException import CakeException
from CakeHash import CakeHash
from CakeCrypt import CakeCrypt

import CakeGlobals
import CakeErrors
import CakeDebug

from xml.dom.minidom import parseString

import urllib

class CakeXML:
	def AddClass(self, className, locale = "en_US"):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._Insert("<class type=\"" + urllib.quote(className) + "\" locale=\"" + urllib.quote(locale) + "\">")
		self._depth += 2

	def AddMethod(self, methodName):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._Insert("<method type=\"" + urllib.quote(methodName) + "\">")
		self._depth += 2

	def AddParameters(self, parameters, reverseData):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		for key, value in parameters.iteritems():
			if isinstance(value, CakeHash) or isinstance(value, dict):
				customParameters = value
				for customKey, customValue in customParameters.iteritems():
					if isinstance(customValue, CakeHash) or isinstance(customValue, dict):
						self.AddTag(key)
						customParameters2 = customValue
						for customKey2, customValue2 in customParameters2.iteritems():
							self._AddCustomParameter(customKey2, customValue2)
						self.CloseTag(key)
					else:
						if reverseData:
							self.AddCustomParameter(customValue, customKey)
						else:
							self.AddCustomParameter(customKey, customValue)
			else:
				self.AddParameter(key, value)

	def AddParameter(self, name, value):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)
		
		self._Insert("<" + name + ">" + urllib.quote(value) + "</" + name + ">")

	def AddCustomParameter(self, typ, value):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._Insert("<data type=\"" + urllib.quote(typ) + "\">" + urllib.quote(value) + "</data>")

	def AddTag(self, tagName):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._Insert("<" + tagName + ">")
		self._depth += 2

	def Close(self):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._depth -= 2
		self._Insert("</body>")

		self._closed_xml = True

	def CloseClass(self):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._depth -= 2
		self._Insert("</class>")

	def CloseMethod(self):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._depth -= 2
		self._Insert("</method>")

	def CloseTag(self, tagName):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)
		
		self._depth -= 2
		self._Insert("</" + tagName + ">")

	def ExecXML(self):
		if not self._closed_xml:
			raise CakeException(CakeErrors.UNCLOSED_XML)

		CakeDebug.AddMessage(self._xml)

		cakeCrypt = CakeCrypt()

		xml_req = cakeCrypt.CakeEncryptHex(self._xml)

		if CakeGlobals.CAKE_MCRYPT_MODE.upper() == "ECB":
			iv = ""
		else:
			iv = cakeCrypt.iv.encode("hex")

		#CakeDebug.AddMessage(xml_req)

		data = {"id": CakeGlobals.CAKE_INTERFACE_ID, "alg": CakeGlobals.CAKE_MCRYPT_ALG.lower(), "mode": CakeGlobals.CAKE_MCRYPT_MODE.lower(), "request": iv + xml_req}
		f = urllib.urlopen(CakeGlobals.API_CAKE_URL + "/", urllib.urlencode(data))
		try:
			resXML = f.read()
		finally:
			f.close()

		#CakeDebug.AddMessage(resXML)

		idx = resXML.find("<?xml")
		if idx != -1:
			resXML = resXML[idx:len(resXML)]
		else:
			resXML = cakeCrypt.CakeDecryptHex(resXML)

		CakeDebug.AddMessage(resXML)

		self.response = parseString(resXML)

	def Init(self):
		self._depth = 0
		self._closed_xml = False
		self._xml = ""
		self._Insert("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
		self._Insert("<body version=\"" + CakeGlobals.CAKE_VERSION + "\">")
		self._depth = 2

	def _Insert(self, value):
		if self._closed_xml:
			raise CakeException(CakeErrors.CLOSED_XML)

		self._xml += (" " * self._depth) + value + "\n"
