from FireFighter import *

firestaff1 = Firefighter("Jim", "Grant", "88213", 25)
firestaff2 = Firefighter("Melinda", "Jones", "99276", 20)
firestaff3 = Firefighter("Joel", "Baker", "77254", 30)

print("{0}: {1} {2} ({3})".format(firestaff1.staff_number, firestaff1.name, firestaff1.surname, firestaff1.age))
print("{0}: {1} {2} ({3})".format(firestaff2.staff_number, firestaff2.name, firestaff2.surname, firestaff2.age))
print("{0}: {1} {2} ({3})".format(firestaff3.staff_number, firestaff3.name, firestaff3.surname, firestaff3.age))

print("Number of firemen/women in the staff: ", Firefighter.count)