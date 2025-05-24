class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class PhoneBook:
    def __init__(self):
        self.head = None
        self.contacts = []  # For sorting and binary search
        self.hash_table = {}  # For fast search using name

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        new_contact.next = self.head
        self.head = new_contact
        self.contacts.append((name, phone))
        self.hash_table[name] = phone
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        print("All contacts:")
        current = self.head
        while current:
            print(f"Name: {current.name}, Phone: {current.phone}")
            current = current.next

    def edit_contact(self, name, new_phone):
        current = self.head
        found = False
        while current:
            if current.name == name:
                current.phone = new_phone
                found = True
                print(f"Contact '{name}' updated.")
                break
            current = current.next
        if found:
            self.contacts = [(n, new_phone if n == name else p) for n, p in self.contacts]
            self.hash_table[name] = new_phone
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.contacts = [(n, p) for n, p in self.contacts if n != name]
                self.hash_table.pop(name, None)
                print(f"Contact '{name}' deleted.")
                return
            prev = current
            current = current.next
        print("Contact not found.")

    def sort_contacts(self):
        # Bubble sort for demonstration
        n = len(self.contacts)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.contacts[j][0].lower() > self.contacts[j + 1][0].lower():
                    self.contacts[j], self.contacts[j + 1] = self.contacts[j + 1], self.contacts[j]
        print("Contacts sorted by name:")
        for name, phone in self.contacts:
            print(f"Name: {name}, Phone: {phone}")

    def search_contact_linear(self, name):
        for n, p in self.contacts:
            if n.lower() == name.lower():
                print(f"Found (Linear Search): Name: {n}, Phone: {p}")
                return
        print("Contact not found.")

    def search_contact_binary(self, name):
        self.sort_contacts()  # Ensure list is sorted
        low = 0
        high = len(self.contacts) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.contacts[mid][0].lower() == name.lower():
                print(f"Found (Binary Search): Name: {self.contacts[mid][0]}, Phone: {self.contacts[mid][1]}")
                return
            elif self.contacts[mid][0].lower() < name.lower():
                low = mid + 1
            else:
                high = mid - 1
        print("Contact not found.")

    def search_contact_hash(self, name):
        if name in self.hash_table:
            print(f"Found (Hash Table): Name: {name}, Phone: {self.hash_table[name]}")
        else:
            print("Contact not found.")

# ------------------
# Example usage:
pb = PhoneBook()
pb.add_contact("Alice", "1234567890")
pb.add_contact("Bob", "9876543210")
pb.add_contact("Charlie", "5555555555")

pb.view_contacts()
pb.edit_contact("Alice", "1111111111")
pb.delete_contact("Bob")
pb.sort_contacts()
pb.search_contact_linear("Charlie")
pb.search_contact_binary("Charlie")
pb.search_contact_hash("Charlie")



#OUTPUT

# Contact 'Alice' added.
# Contact 'Bob' added.
# Contact 'Charlie' added.
# All contacts:
# Name: Charlie, Phone: 5555555555
# Name: Bob, Phone: 9876543210
# Name: Alice, Phone: 1234567890
# Contact 'Alice' updated.
# Contact 'Bob' deleted.
# Contacts sorted by name:
# Name: Alice, Phone: 1111111111
# Name: Charlie, Phone: 5555555555
# Found (Linear Search): Name: Charlie, Phone: 5555555555
# Contacts sorted by name:
# Name: Alice, Phone: 1111111111
# Name: Charlie, Phone: 5555555555
# Found (Binary Search): Name: Charlie, Phone: 5555555555
# Found (Hash Table): Name: Charlie, Phone: 5555555555