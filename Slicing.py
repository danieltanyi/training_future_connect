#Slicing
name = "najaf zawar"
print(name[0:5])

print(name[5:]) # It will give us extra space as well at the start
print(name[6:])

# List Slicing
car_brands = ["bmw", "honda", "ferrari", "Tesla"]
print(car_brands)
print(car_brands[0:3])
print(car_brands[0:4])
print(car_brands[2:])
print(car_brands[2]) # fetch the 3rd item because indexing starts from zero
print(car_brands[-1]) # start from the end


# Dictionary Slicing
student_dict = {'student_name': 'najaf', 'student_RollNo': 223, 'student_marks':
254}
print(student_dict["student_marks"])
print(student_dict.get("student_RollNo"))