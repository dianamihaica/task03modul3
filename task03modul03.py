# product.py
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
    
    def check_quantity(self):
        return self.quantity >= 10

# employee.py
class Employee:
    def __init__(self, name, email, salary, address):
        self.name = name
        self.email = email
        self.salary = salary
        self.address = address
    
    def check_email(self):
        return '@' in self.email
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

# user.py
class User:
    def __init__(self, name, username, phone, address):
        self.name = name
        self.username = username
        self.phone = phone
        self.address = address
        self.shopping_history = []
    
    def check_email(self):
        return '@' in self.username
    
    def total_spent(self):
        return sum(product.price for product in self.shopping_history)
    
    def add_product(self, product):
        self.shopping_history.append(product)

# main.py
from product import Product
from employee import Employee
from user import User

# Creare produse
products = [
    Product("Laptop", 3500.99, 15, "Laptop performant"),
    Product("Mouse", 150.50, 5, "Mouse wireless"),
    Product("Tastatura", 200.00, 25, "Tastatura mecanica"),
    Product("Monitor", 1200.75, 8, "Monitor Full HD"),
    Product("Casti", 300.90, 12, "Casti cu noise cancelling")
]

# Creare angajați
employees = [
    Employee("Alex Pop", "alex.pop@example.com", 4500, "Strada Libertății 12"),
    Employee("Maria Ionescu", "maria.ionescu@example.com", 5200, "Bulevardul Unirii 45")
]

# Creare utilizatori
users = [
    User("Ion Georgescu", "ion.geo@example.com", "0722334455", "Strada Victoriei 5"),
    User("Elena Dobre", "elena.dobre@example.com", "0744556677", "Strada Mihai Eminescu 10"),
    User("Radu Dumitru", "radu.d@example.com", "0733667788", "Bulevardul Carol 25")
]

# Testare funcționalități
print("Verificare stoc produse:")
for product in products:
    print(f"{product.name}: {'În stoc' if product.check_quantity() else 'Stoc limitat'}")

print("\nVerificare email angajați:")
for employee in employees:
    print(f"{employee.name}: {'Email valid' if employee.check_email() else 'Email invalid'}")
    employee.increase_salary(10)
    print(f"Salariu nou: {employee.salary}")

print("\nAchiziții utilizatori:")
users[0].add_product(products[0])
users[0].add_product(products[1])
print(f"{users[0].name} a cheltuit: {users[0].total_spent()} RON")
