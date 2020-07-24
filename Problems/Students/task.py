class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + str(birth_year)


first_name = input()
last_name = input()
year_of_birth = int(input())

obj = Student(first_name, last_name, year_of_birth)
print(obj.id)
