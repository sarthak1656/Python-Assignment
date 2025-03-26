from collections import namedtuple

Employee=namedtuple("Employee",["name","age","country"])

emp1 = Employee(name="sarthak" , age = 20, country="india")
emp2 = Employee(name="sipun" , age = 20, country="india")
emp3 = Employee(name="subham" , age = 20, country="india")

for emp in [emp1,emp2,emp3]:
    print(f"Name is :{emp.name} \t Country is: {emp.country}")