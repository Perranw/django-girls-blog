def helloWorld(myString):
	print("hello world")
	myName = input("what is your name?")
	myVar = input("Enter a number: ")

	if(myName == "Kevin" and myVar == "0"):
		print("Kevin is great")
	elif(myName == "Fay"):
		print("Fay is lovely")
	else:
		print("hello "+myName+", you are ok")

helloWorld()