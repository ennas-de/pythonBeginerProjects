#This is one of the excellent python projects for beginners. 
#Everyone uses a contact book to save contact details, including name, 
#address, phone number, and even email address. This is a command-line 
#project where you will design a contact book application that users 
#can use to save and find contact details. The application should also 
#allow users to update contact information, delete contacts, and list 
#saved contacts. The SQLite database is the ideal platform for saving 
#contacts. To handle a project with Python for beginners can be helpful 
#to build your career with a good start.



### SOLUTION: ###

# 1. Understanding:
# write a phone book program
# the phone book program allow users to:
	# save contacts
	# display contacts 
	# update contacts
	# delete contacts
	# find contacts


# 2. Algorithm:
# create a class   (I really need to re-learn n get FULL understanding op OOP, esp for python)
# we define a constructure to the class (with name, address, phone number, email as parameters)
# we innitialize all the variables involved
# **Breakdown the whole task into smaller functions
# if __name__ = '__main__'
	# run the start function


	# Functions breakdowns:
# a. start the app
# b. prompt the user for interest
# c. get user answer and based on response calls on other functions
# d. save contacts
# e. disply contacts
# f. update contacts
# g. delete contacts
# h. find contacts




    #### THIS CLASS FUNCTION IS INTENDED TO BE DONE USING OOP ###
# class contactBook():
# 	# def __init__ (self, name, address, phone, email):   #constructor initilization
# 	# 	self.fname = fname
# 	# 	self.lname = lname
# 	# 	self.address = address
# 	# 	self.phone = phone
# 	# 	self.email = email

# 	# 	# some variable initializations and manipulations will occur here
# 	# 	fname = input("First Name: ")
# 	# 	lname = input("Last Name: ")
# 	# 	address  = input("Address: ")
# 	# 	phone = input("Phone: ")
# 	# 	email = input("Email: ")
		





# 	def start():
# 		Print("Welcome to Ennas' Personal Contct Book")
# 		Print("Press: 1 for Menu \n 2 to exit")



# 	def save():
# 		pass



# 	def display():
# 		pass


# 	def update():
# 		pass

# 	def delete():
# 		pass


# 	def find():
# 		pass





# if __name__ == '__main__':
# 	print("hey")
# 	# start()





         ###	Trying to Redo the OOP Paradigm  ###


#class contactBook():
#	 def __init__ (self, name, address, phone, email):   #constructor initilization
#	 	self.fname = fname
#	 	self.lname = lname
#	 	self.address = address
#	 	self.phone = phone
#	 	self.email = email
#	 	
#	 	# some variable initializations and manipulations will occur here
#	 	fname = input("First Name: ")
#	 	lname = input("Last Name: ")
#	 	address  = input("Address: ")
#	 	phone = input("Phone: ")
#	 	email = input("Email: ")
#	 	
#	 	
#	 	
#	 def start():
#	 	Print("Welcome to Ennas' Personal Contct Book")
#	 	Print("Press: 1 for Menu \n 2 to exit")
#	 	sui = input('>')
#	 		
#	 	for choice in sui:
#	 		if choice == '1':
#	 			displayMenu()
#	 		elif choice == '2':
#	 			exit()
#	 		else:
#	 			exit()
#	 			
#	 			
#	 			
#	 def displayMenu():
#	 	print("What do you want to do: ")
#	 	print('1. Save a contact')
#	 	print('2. Display all contacts')
#	 	print('3. Update a contact')
#	 	print('4. Delete a contact')
#	 	print('Find a contact')
#	 	
#	 	dmui = input('Select an option: ')
#	 	
#	 	for choice in dmui:
#	 		if choice == '1':
#	 			save()
#	 			
#	 		elif choice == '2':
#	 			display()
#	 			
#	 		elif choice == '3':
#	 			update()
#	 		
#	 		elif choice == '4':
#	 			delete()
#	 			
#	 		elif choice == '5':
#	 			find()
#	 			
#	 		else:
#	 				exit()
#	 				
#	 				
#	 	
#	 		
#	 	def save():
#	 		cont = True
#	 		
#	 		while cont:
#	 			print('Enter The Contact Details Below:	')
#	 			self.fname = input('First name: ')
#	 			self.lname = input('Last name: ')
#	 			self.address = input('Adress: ')
#	 			self.phone = input('Phone Number: ')
#	 			self.email = input('Email Adress: ')
#	 			
#	 			
#	 		pass
#	 		
#	 		
#	 	def display():
#	 		pass
#	 		
#	 		
#	 	def update():
#	 		pass
#	 		
#	 		
#	 	def delete():
#	 		pass
#	 		
#	 		
#	 		
#	 	def find():
#	 		pass
#	 		
#	 		
#	 		
#	 		
#if __name__ == '__main__':
#	print("hey")
#	#app == contactBook()
#	#start()
#	#vn = displayMenu()
#	displayMenu()

#         



			### I DONTKNOW MUCH OF OOP YET, SO I'LL BE USING SCRIPTING PARADIGM ###
import sqlite3

dbConn = sqlite3.connect('contactBookdb.db')

dbCur = dbConn.cursor()

#create the table(s) to store contact information
try:
	dbCur.execute("CREATE TABLE IF NOT EXISTS contact_details(id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT (20) NOT NULL, lname TEXT (20) NOT NULL, address TEXT (150) NOT NULL, phone TEXT (15) NOT NULL UNIQUE, email TEXT (50) UNIQUE, username TEXT (20) NOT NULL UNIQUE)")
	dbConn.commit()
	print('Table successfully created')
except:
	print('error in creating table')
	raise error



def start():
	print("Welcome to Ennas' Personal Contact Book")
	print("Press: 1 for Menu \n2 to exit")
	sui = input('>')
	 		
	for choice in sui:
		if choice == '1':
			displayMenu()
		elif choice == '2':
			exit()
		else:
			exit()
	 			
	 			
	 			
def displayMenu():
	print("What do you want to do: ")
	print('1. Save a contact')
	print('2. Display all contacts')
	print('3. Update a contact')
	print('4. Delete a contact')
	print('5. Find a contact')
	print('\n')
	 	
	dmui = input('Select an option: \n>')
	 	
	for choice in dmui:
		if choice == '1':
			save()
				
		elif choice == '2':
			display()
	 			
		elif choice == '3':
			update()
	 		
		elif choice == '4':
			delete()
	 			
		elif choice == '5':
			find()
	 			
		else:
				exit()
	 				
	 				
	 	
	 		
def save():
	cont = True
	 		
	while cont:
		print('Enter The Contact Details Below:	')
		fname = input('First name: ')
		lname = input('Last name: ')
		address = input('Adress: ')
		phone = input('Phone Number: ')
		email = input('Email Adress: ')
		username = input('Unique Username (Please keep it save): ')
		
		try:
			dbCur.execute("INSERT INTO contact_details(fname, lname, address, phone, email, username) VALUES(?, ?, ?, ?, ?, ?)", (fname, lname, address, phone, email, username))
			dbConn.commit()
			print('A new contact is successfuly inserted into the phone records book.')
			print('Would you like to save another contact?')
			smui = input('1) Yes \n2) No: \n>')
			for choice in smui:
				if choice == '1':
					save()
				elif choice == '2':
					cont = False
					displayMenu()
				else:
					exit()
		except:
			print('error in saving new contact into phone book. \nKindly contact admin.')
			print(error)
			
			print('\n')
			displayMenu()
						
								
				
def display():
	try:
		dbCur.execute("SELECT * FROM contact_details")
		print(dbCur.fetchall())
		
		print('\nReturn to Menu or Exit?')
		dui = input('1. Menu \n2. Exit \n>')
		for choice in dui:
			if choice == '1':
				displayMenu()
			elif choice == '2':
				exit()
			else:
				print('Wrong option. \nReturning to Menu')
				displayMenu()
		
		#if len(query) == 0:
#			print('No records found')
#		else:
#			print(query)
	except:
		print('Error in fetching records. \nContact admin')
		print('\n')
		displayMenu()
	
	 		
	 		
def update(username = " "):
	print('\n')
	print('Enter the username of the contact details you want to update: ')
	username = input('Enter 0 to quit \n>')
		
	try:
		dbCur.execute("SELECT * FROM contact_details WHERE username = ? ", (username)) #username = ?", (username))
		print('Old Records:\n')
		print(dbCur.fetchall())
		print('\nEnter The New Contact Details Below:	')
		#username = username
		fname = input('First name: ')
		lname = input('Last name: ')
		address = input('Adress: ')
		phone = input('Phone Number: ')
		email = input('Email Adress: ')
		
		try:
			dbCur.execute("UPDATE  contact_details SET fname = ?, lname = ?, address = ?, phone = ?, email = ? WHERE username = ?", (fname, lname, address, phone, email, username))
			dbConn.commit()
			print('Contact %s is successfuly updated in the phone records book. '  %(username))
			print('\n')
			displayMenu()
		except:
			print('error in updating contact info in the phone book. \nKindly contact admin.')
			print('\n')
			displayMenu()
						
	except:
		print('No such record found. \nTry again')
		print('\n')
		update()
		
	
	 		
	 		
def delete():
	pass
	 		
	 		
	 		
def find():
	pass
	 		


start()