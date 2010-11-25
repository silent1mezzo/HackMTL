import CakeGlobals
from Crypto.Cipher import Blowfish

class CakeCrypt:
	def __init__(self):
		alg = CakeGlobals.CAKE_MCRYPT_ALG.upper();
		if CakeGlobals.CAKE_MCRYPT_ALG.upper() != 'BLOWFISH':
			raise Exception('Only Blowfish algoritm supported')
		if CakeGlobals.CAKE_MCRYPT_MODE.upper() != 'ECB':
			raise Exception('Only ECB crypt mode supported')

		Blowfish.key_size = len(CakeGlobals.CAKE_INTERFACE_KEY)
		self.block_size = Blowfish.block_size
		self._set_iv("u3rMyC31")
		
	def _get_cryptor(self):
		return Blowfish.new(CakeGlobals.CAKE_INTERFACE_KEY, eval('Blowfish.MODE_' + CakeGlobals.CAKE_MCRYPT_MODE.upper()), self._iv)

	def CakeEncryptHex(self, data):
		return self.CakeEncrypt(data).encode("hex")

	def CakeEncrypt(self, data):
		self._cryptor = self._get_cryptor()
		data = self._AdjustSize(data, self.block_size)
		return self._cryptor.encrypt(data)

	def CakeDecryptHex(self, data):
		return self.CakeDecrypt(data.decode("hex")).replace("\0", "")

	def CakeDecrypt(self, data):
		if CakeGlobals.CAKE_MCRYPT_MODE.upper() != "ECB":
			self.iv = data[0:self._iv_len - 1].decode("hex")
			data = data[self._iv_len:len(data)]
		
		self._cryptor = self._get_cryptor()
		return self._cryptor.decrypt(data)

	def _AdjustSize(self, data, size):
		origSize = len(data)
		if origSize % size != 0 or origSize == 0:
			newSize = ((origSize // size) + 1) * size
			for i in range(origSize, newSize):
				data += "\0"

		return data

	def _get_iv(self):
		return self._iv

	def _set_iv(self, value):
		self._iv = value
		self._iv_len = len(self._iv)
	
	iv = property(_get_iv, _set_iv)
