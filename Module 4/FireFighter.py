class Firefighter:
    count = 0
    def __init__(self, name, surname, staff_number, age):
        self.name = name 
        self.surname = surname
        self.staff_number = staff_number
        self.age = age
        Firefighter.count += 1