# Task 1: Use super() properly
# Modify constructors so child classes reuse parent initialization.

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def display(self):
        super().display()
        print(f"Department: {self.dept}, Fees: {self.fees}")


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")


class TempFaculty(Faculty):  
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration  

    def display(self):
        super().display()
        print(f"Duration: {self.duration}")


# objects
s = Student("Sanjay", 101, "IT", 50000)
f = Faculty("Arun", 201, 45000)
t = TempFaculty("Mathi", 111, 25000, "7 months")

print("Student Details:")
s.display()

print("\nFaculty Details:")
f.display()

print("\nTemp Faculty:")
t.display()




# Task 2: Apply Abstraction
# Create an abstract base class.


from abc import ABC, abstractmethod

# Abstract Class
class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass


# Student Class
class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        print(f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}")


# Faculty Class
class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        print(f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}")


# TempFaculty Class
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        print(f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}")


# Objects
s = Student("Sanjay", 101, "IT", 50000)
f = Faculty("Arun", 201, 45000)
t = TempFaculty("Mathi", 111, 25000, "7 months")


s.get_details()
f.get_details()
t.get_details()


# Task 3: Sorting using key
# Create a list of students and sort them.

# Student Class
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


# Faculty Class
class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# List of Students
students = [
    Student("Sanjay", 50000),
    Student("Arun", 30000),
    Student("Mathi", 40000)
]

# List of Faculty
faculties = [
    Faculty("Kumar", 60000),
    Faculty("Ravi", 45000),
    Faculty("Ajay", 70000)
]

# Sort Students by fees
students.sort(key=lambda x: x.fees)

# Sort Faculty by salary
faculties.sort(key=lambda x: x.salary)


print("Sorted Students (by fees):")
for s in students:
    print(s.name, s.fees)

print("\nSorted Faculty (by salary):")
for f in faculties:
    print(f.name, f.salary)





# Task 4: Use map()
# Transform data.

# Extract only student names using map
names = list(map(lambda s: s.name, students))

print("Student Names:")
print(names)





# Task 5: Use filter()
# Filter data.


# Student Class
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


# Faculty Class
class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))


print("Students with fees > 50000:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f.name, f.salary)





# Task 6: Use reduce()
# Aggregate data.

from functools import reduce


# Student Class
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


# Faculty Class
class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Total fees collected
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

# Total salary of faculty
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)


print("Total Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)




# Task 7: Higher Order Function
# Create a function that accepts another function.

# Student Class
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


# Function to extract name
def get_name(s):
    return s.name


# Function to check high fees
def high_fee(s):
    return s.fees > 40000


# Using map (get names)
names = process_users(students, get_name)

# Using filter (high fees)
high_fee_students = list(filter(high_fee, students))


print("Names:", names)

print("\nHigh Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)





# Final Challenge (Important 🔥)
# Build a mini system:

# Abstraction

class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass


# clasess

class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        print(f"Student -> {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}")


class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        print(f"Faculty -> {self.name}, ID: {self.id}, Salary: {self.salary}")


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        print(f"TempFaculty -> {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}")


# Data

students = [
    Student("Sanjay", 101, "IT", 50000),
    Student("Arun", 102, "CSE", 30000),
    Student("Mathi", 103, "ECE", 60000)
]

faculties = [
    Faculty("Kumar", 201, 25000),
    Faculty("Ravi", 202, 45000),
    Faculty("Ajay", 203, 70000)
]


# Print all details

print("=== ALL DETAILS ===")
for s in students:
    s.get_details()

for f in faculties:
    f.get_details()


# Sorting
students.sort(key=lambda x: x.fees)
faculties.sort(key=lambda x: x.salary)

print("\nSORTED DATA ")
for s in students:
    print(s.name, s.fees)

for f in faculties:
    print(f.name, f.salary)


# filter

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("\nFILTERED DATA")
for s in high_fee_students:
    print("Student:", s.name, s.fees)

for f in high_salary_faculty:
    print("Faculty:", f.name, f.salary)


# map

names = list(map(lambda s: s.name, students))
print("\nStudent Names:", names)

# reduce

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)