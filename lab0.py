import os
#Ask the user if they even want to decrypt the file 
answer = input("Do you wish to decrypt a message? Type yes or no? ")


if answer == "no":
	print("There is always another time to decrypt your message!") #do not run the decrypt step
elif answer == "yes": #When the user wants to run the program 
	
	#open file encrypt to read the message  
	f = open('encrypt.txt', 'r')

	#read encrypted message into variable, contents 
	contents = f.read()
	f.close()

	#Set the shift equal to 0 from the beginning 
	shift = 0

	#Open the file that you will be writing the decrypted messages to	 
	f = open('decrypt.txt', 'w')

	#while the shift is not 95, meaning it hasn't gone through all the possible shifts yet	
	while shift <= 94:
		#set plainText to a blank string to add things to it, initiate the variable 
		plainText = ""
		#Looking at the characters in the contents from the encrypted file 
		for letter in contents:
			ascii = ord(letter) # take the ascii code of each letter 
			ascii = ascii + shift #Set the new ascii value to ascii + the number of times it shifted
			if ascii >= 127: #If the ascii code is over 126, including the shift, -95 to go back to beginning of ascii table  
				ascii -= 95
			plainText += chr(ascii) #the plain text is the character of the ascii value 
		shift += 1 #increase the shift by one each time the loop goes through
	
		#Keep track of how many time you have shifted and write the decrypted message to the file 
		f.write(plainText + "\n" + " The message shifted " + str(shift - 1) + " times" + "\n")
	#SUPER IMPORTANT!! Close the file!
	f.close()
	#print messages for the user saying they have successfully decrypted
	print("Congratulations, you have successfully decrypted the message!")
	print("Check the decrypt file to view your message.")
else: #If the user does not type yes or no 
	print("Sorry, you typed an unrecognizable character")


