"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts

class Contact:
    total_contacts = 0

    def __init__(self, name, Pnumber, email):
        self.name = name
        self.Pnumber = Pnumber
        self.email = email
        Contact.total_contacts += 1

    def check_email(self):
        if "@" in self.email:
            print(f"{self.email} is valid")
            return True
        else:
            print(f"{self.email} is not valid")
            return False

    @classmethod
    def get_contact_count(cls):
        return Contact.total_contacts



Contact1 = Contact("joe", "0478230984", "joe@gmail.com")
Contact2 = Contact("bob", "0482193746", "bob@gmail.com")

print(Contact1.name, Contact1.Pnumber, Contact1.email)
print(Contact2.name, Contact2.Pnumber, Contact2.email)

Contact1.check_email()

print(Contact.get_contact_count())