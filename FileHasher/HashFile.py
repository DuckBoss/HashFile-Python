import hashlib
import time

class Hashing:
	"This class handles the hashing of files"
	# 64kb Buffer Chunks
	chunkSize = 65536

	# Initializes the class
	def __init__(self):
		print('HashFile Started...\n{}\n'.format(time.strftime("%d-%m-%Y[%H:%M:%S]")))
		self.chunkSize = 65536

	# Generates and returns a MD5 Hash given a file
	def HashFileIntoMD5(self, fileName):
		md5Hash = hashlib.md5()
		curFile = '{}.txt'.format(fileName)
		with open(fileName, 'rb') as rFile:
			while True:
				readData = rFile.read(self.chunkSize)
				if not readData:
					break
				md5Hash.update(readData)
		md5Digest = md5Hash.hexdigest()
		return md5Digest

	# Generated and returns a SHA1 Hash given a file
	def HashFileIntoSHA1(self, fileName):
		sha1Hash = hashlib.sha1()
		curFile = '{}.txt'.format(fileName)
		with open(fileName, 'rb') as rFile:
			while True:
				readData = rFile.read(self.chunkSize)
				if not readData:
					break
				sha1Hash.update(readData)
		sha1Digest = sha1Hash.hexdigest()
		return sha1Digest