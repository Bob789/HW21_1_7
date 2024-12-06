# Ex 1:
# Write a for loop that prints the numbers from 12 to 24.
for i in range(12, 24+1):
    print(i)
# Ex 2:
# Write a for loop that prints the ODD numbers from 7 to 31
print("-------------------------------------------")
for i in range(7, 31+1, 2):
    print(i)
print("-------------------------------------------")
# Ex 3:
# Write a for loop that prints the EVEN numbers from 10 to -20.
for i in range(10, -20-1, -2):
    print(i)
print("-------------------------------------------")
# Ex 4:
# Write a for loop that iterates through all numbers from 1 to 45. Print the
# following:
# ● For each number that multiples of 3 print “Fizz”
# ● For each number that multiples of 5 print “Buzz”
# ● For each number that multiples of 3 and 5 print “FizzBuzz”
for i in range(1, 45+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    print(i)
print("-------------------------------------------")
# Ex 5:
# Write a function that receives an array as a parameter and calculates the sum
# of all the numbers in the given array (don’t use sum() function).
# For example if the given array is: [1,13,22,123,49,34,5,24,57,45]
# The result should be 373
def calculate_sum(list_n)-> int:
    sum_n: int = 0
    for i in range(0, len(list_n)):
        sum_n += list_n[i]
    return sum_n
list_n: list[int] = [1,13,22,123,49,34,5,24,57,45]
print(f" The sum is: {calculate_sum(list_n)}")
print("-------------------------------------------")
# Ex 6:
# Write a function that receives an array of objects.
# Each object should represent a student with the properties:
# ● id
# ● first name
# ● last name
# ● age
# ● country
# ● city
# In addition, the function should receive a property to change.

# 1 - The function should check for each property in each object in the array if
# the given property exists and if it does, the function should delete it from the
# object.
def del_property_student(students_l: list[list[type]], key: str) -> None:
    for student in students_l:
         for prop in student:
            if key in prop:
                del(prop[key])
                print(student)

# 2 - Write a function that prints each property of each object in the given array.
def print_properties_student(students_l: list[list[type]]) -> None:
    for student in students_l:
         for prop in student:
            print(prop)

# 3 - Write a function that sorts the array by the students age from the oldest to
# the youngest and return the sorted array.
def sort_properties_student(students_l: list[list[type]]) -> list[list[type]]:
    # Create a matrix of [id, age]
    matrix = []
    for student in students_l:
        student_id = student[0]["id"]  # Access ID
        student_age = student[4]["age"]  # Access Age
        matrix.append([student_id, student_age])

    # Sort the matrix by age in descending order
    sorted_matrix = sorted(matrix, key=lambda x: x[1], reverse=True)

    # Reorder students_l based on the sorted matrix
    sorted_students = []
    for item in sorted_matrix:
        student_id = item[0]
        for student in students_l:
            if student[0]["id"] == student_id:
                sorted_students.append(student)
                print(student)
                break
    print()
    return sorted_students

key: str = "first_name"
students = [
    [{"id": 1}, {"first_name": "John"}, {"last_name": "Smith"}, {"country": "USA"}, {"age": 62}, {"city": "New York"}],
    [{"id": 2}, {"first_name": "Jane"}, {"last_name": "Johnson"}, {"country": "Canada"}, {"age": 21}, {"city": "Toronto"}],
    [{"id": 3}, {"first_name": "Michael"}, {"last_name": "Williams"}, {"country": "UK"}, {"age": 88}, {"city": "London"}],
    [{"id": 4}, {"first_name": "Emily"}, {"last_name": "Brown"}, {"country": "Australia"}, {"age": 43}, {"city": "Sydney"}],
    [{"id": 5}, {"first_name": "David"}, {"last_name": "Jones"}, {"country": "Germany"}, {"age": 52}, {"city": "Berlin"}],
    [{"id": 6}, {"first_name": "Sarah"}, {"last_name": "Davis"}, {"country": "Israel"}, {"age": 77}, {"city": "Tel Aviv"}],
]

print(sort_properties_student(students))# By age
print(print_properties_student(students))# Print properties
print(del_property_student(students, key))# Delete properties off all student

print("-------------------------------------------")
# Ex 7:
# 1 - Write a function that receives the array shown above and prints only
# animalType: cat.
def print_only_cat(our_pets: list[dict[type]])-> None:
    key = "cat"
    for animal in our_pets:
        if animal["animal_type"] == key:
            return animal["names"]

# 2 - Write a function that receives the array shown above and the animal type.
# The function should print all names of that animal type if this type exists in the
# object.

def print_animalType(our_pets: list[dict[type]], key)-> None:
    for animal in our_pets:
        if animal["animal_type"] == key:
            print(animal["names"])

# 3 - Write a function that that receives the array shown above and animal name
# The function should add the specified animal name to each ‘names’ array in
# each animal_type if that name does not exist in the ‘names’ array.

def update_name(our_pets: list[dict[type]], name)-> list[dict[type]]:
    for animal in our_pets:
        if name not in animal["names"]:
            animal["names"].append(name)
    return our_pets

our_pets = [
    {
        "animal_type": "cat",
        "names": ["Meowzer", "Fluffy", "Kit-Cat"]
    },
    {
        "animal_type": "dog",
        "names": ["Spot", "Bowser","Frankie"]
    }
]

print_only_cat(our_pets)
print_animalType(our_pets, "dog")
print(update_name(our_pets, "Puppy"))

