"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.

class Contact:
    total_contacts = 0

    def __init__(self, name, Pnumber, email):
        self.name = name
        self.Pnumber = Pnumber
        self.email = email
        Contact.total_contacts += 1

# Create at least two instances of the Contact class with different data.

Contact1 = Contact("joe", "0478230984", "joe@gmail.com")
Contact2 = Contact("bob", "0482193746", "bob@gmail.com")
# Write code that prints out the details of each contact you have created.

print(Contact1.name, Contact1.Pnumber, Contact1.email)
print(Contact2.name, Contact2.Pnumber, Contact2.email)
