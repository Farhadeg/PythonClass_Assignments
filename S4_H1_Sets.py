Physic_class = {"Reza", "Ali", "Sima", "Behzad", "Mohammad", "Neda", "Mokhtar", "Babak"}
Math_class = {"Ali", "Farhad", "Sima", "Reza", "Mohammad", "Sadeq", "Babak"}
Intersection_class = Physic_class.intersection(Math_class)
print('Below Students have registered for Physic:\n', Physic_class)
print('Below Students have registered for Math:\n', Math_class)
print('Below Students have registered for Both classes:\n', Intersection_class)
a = Physic_class - Intersection_class
b = Math_class - Intersection_class
Unique_Students = a.union(b)
print('Below Students have registered for one of the classes only:\n', Unique_Students)
