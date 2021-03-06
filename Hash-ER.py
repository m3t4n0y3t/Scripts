
#!/usr/bin/python
import hashlib
from os import system
from sys import exit


# About
HashingTypes = ["MD5","SHA1","SHA224","SHA256","SHA384"]
Author = "<HossamHamdy>"
Version = "v0.2"
LastUpdate  = "14/08/2020"


class Color:

	yellow  = '\033[93m'
	red     = '\033[91m'
	green   = '\033[92m'
	blue    = '\033[94m'
	white   = '\033[97m'


def Hash(Text,HashType):

	Hashing = hashlib.new(HashType)
	Hashing.update(Text)
	return Hashing.hexdigest()


def Inro(Author,Version):

	print(f"""{Color.red}
	 __    __       ___           _______. __    __          _______ .______       | Supported Hashing
	|  |  |  |     /   \         /       ||  |  |  |        |   ____||   _  \      | [  MD5 ]
	|  |__|  |    /  ^  \       |   (----`|  |__|  | ______ |  |__   |  |_)  |     | [ SHA1 ]
	|   __   |   /  /_\  \       \   \    |   __   ||______||   __|  |      /      | [ SHA224 ] 
	|  |  |  |  /  _____  \  .----)   |   |  |  |  |        |  |____ |  |\  \----. | [ SHA256 ]
	|__|  |__| /__/     \__\ |_______/    |__|  |__|        |_______|| _| `._____| | [ SHA384 ]
	{Color.yellow}BY: {Author}

	[1]  Hashing Text
	[2]  Hashing File
	[3]  Check File Integrity
	""")


def Process(Command):

	if Command == 1:

		PlainText = str(input("Text~# "))
		while PlainText == "":
			PlainText = str(input("Text~# "))
		PlainText = PlainText.encode("utf-8")

		HashType = str(input("HashType~# "))
		while HashType == "" or HashType.upper() not in HashingTypes:
			HashType = str(input("HashType~# "))
		print(f"{Color.green}OUTPUT :: {Color.yellow}{Hash(PlainText,HashType)}")
		print("-----------------------------------\n")


	elif Command == 2:
		try:
			Content = ""
			FileName = str(input("Drag File Here~# "))
			with open (FileName,'rb') as File:
				Content = File.read()
		except:
			print("\aError")
			system("pause")

		HashType = str(input("Enter Hashing Type~# "))
		while HashType.upper() not in HashingTypes or HashType == "":
			HashType = str(input("Enter Hashing Type~# "))
		print(f"{Color.green}OUTPUT :: {Color.yellow}{Hash(Content,HashType)}")
		print("-----------------------------------\n")

	elif Command == 3:

		TheHash = str(input("File Hash~# "))
		HashType = str(input("Enter Hashing Type~# "))
		while HashType.upper() not in HashingTypes or HashType == "":
			HashType = str(input("Enter Hashing Type~# "))

		try:
			Content = ""
			FileName = str(input("Drag File Here~# "))
			with open (FileName,'rb') as File:
				Content = File.read()
		except:
			print("\aError")
			system("pause")


		Hashed = Hash(Content,HashType)

		if Hashed == TheHash:
			print(Color.green + "The Same File <3")
		else:
			print(Color.red + f"The File Doesn't Match With Hash : {Color.yellow}{TheHash}")
		print("-----------------------------------\n")


def Main():
	while True:
		system("cls")
		Inro(Author,Version)
		Command = int(input(f"{Author}@Hash-ER~# "))
		while Command < 1 or Command > 3 and Command != 0:
			if Command == 0:
				exit()
			Command = int(input(f"{Author}@Hash-ER~# "))
		Process(Command)
		system("pause")


if __name__ == "__main__":
	Main()
