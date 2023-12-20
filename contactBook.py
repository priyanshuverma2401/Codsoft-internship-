import time
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name} | Phone: {contact.phone} | Email: {contact.email}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts
                   if keyword.lower() in contact.name.lower() or keyword in contact.phone]

        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for i, contact in enumerate(results, 1):
                print(f"{i}. Name: {contact.name} | Phone: {contact.phone} | Email: {contact.email}")

    def update_contact(self, index, new_name, new_phone, new_email):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact '{deleted_contact.name}' deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        time.sleep(3)
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            keyword = input("Enter the name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            contact_book.update_contact(index, new_name, new_phone, new_email)

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)

        elif choice == "6":
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
