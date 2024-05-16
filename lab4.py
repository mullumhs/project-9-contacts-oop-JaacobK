"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.

from contact_manager import ContactManager

# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.



# 3. Create two contacts using the ContactManager.

CM = ContactManager()

CM.add_contact("biden", "0489374017", "biden@gmail.com")
CM.add_contact("Malichici", "0481294752", "Malichici@gmail.com")

# 4. Display all contacts.

CM.display_contacts()

# 5. Update the email address of one contact.

CM.update_contact("biden", new_phone="0428015392", new_email="biden@outlook.com")

# 6. Remove one of the contacts.

CM.remove_contact("Malichici")

# 7. Display all contacts again.

CM.display_contacts()
