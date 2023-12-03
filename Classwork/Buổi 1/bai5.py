class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_contact_info(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

contact1 = Contact(name="Chu", phone="123-456-7890", email="chu@example.com")
contact2 = Contact(name="Minh", phone="987-654-3210", email="Minh@example.com")

print("Contact 1:")
contact1.display_contact_info()

print("\nContact 2:")
contact2.display_contact_info()
