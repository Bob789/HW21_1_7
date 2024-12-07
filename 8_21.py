# Ex 8:
# 1 - Write a function that prints all the student data (each student property
# should be printed in a new line).
from logging import exception


def student_data(student: dict[type]) -> None:
    for prop, value in student.items():
        if not type(value) == list:
            print(prop, ' :', value)
        else:
            for h in value:
                print(prop, ' :', h)
    print("--------------------------------------------")


# 2 - Write a function that receives the student object and a hobby, the function
# should add the hobby to the student's hobbies array if it’s not exist already.
def student_update_property(student: dict[type], attribute) -> None:
    print("Ex 8.2 :")
    for key, value in attribute.items():
        if key in student:
            if value not in student[key]:
                student[key].append(value)
        else:
            student.update(attribute)
    print("--------------------------------------------")


# 3 - Use the function that you wrote in ex 1 to print the data of the student and
# check that the new hobby has been added.
def student_check_property_exist(student, attribute) -> None:
    print("Ex 8.3 :")
    student_data(student)
    for key, value in attribute.items():
        if key in student:
            if value in student[key]:
                print(f" {value} exist")
            else:
                print(f" {value} not exist")
    print("--------------------------------------------")


# 4 - Write a function that receives an object of a student and hobby, the
# function should delete the hobby from the student's hobbies.
def student_delete_property(student, attribute) -> None:
    print("Ex 8.4 :")
    for key, value in attribute.items():
        if key in student:
            for idx, value in enumerate(student[key]):
                if attribute[key] == value:
                    student[key].pop(idx)
                    print(f" {value} deleted")
    print("--------------------------------------------")


student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding']
}

attribute = {'hobbies': 'programing'}
attributeg = {'hobbies': 'games'}
attribute_family_name = {'family_name': 'Klinthon'}

student_data(student)  # 8.1
student_update_property(student, attribute)  # 8.2 update programing
student_check_property_exist(student, attribute)  # 8.3 check if programing
student_delete_property(student, attributeg)  # 8.4 delete games
# 5 - Use the function that you wrote  in ex 1 to print the data student and check
# that the hobby has been deleted from the object student.
print(print("Ex 8.5 :"))
student_data(student)  # 8.5
# 6 - Add to the object student new property: family_name and add a value.
print("Ex 8.6 :")
student_update_property(student, attribute_family_name)
student_data(student)


# ---------------------------------------------

# Ex 9:
# Write a function that prints all the elements of a 2D array using nested for loops.
# print_matrix(matrix)  → Should print: 1 2 3 4 5 6
def prrint_matrix(matrix: type) -> None:
    print("Ex 9 :")
    for e in matrix:
        for item in e:
            print(item, end=' ')


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

prrint_matrix(matrix)
print()
print("--------------------------------------------")


# ---------------------------------------------

# Ex 10:
# Write a function to count how many numbers of zeros appear in a 2D matrix
# using nested for loops and increment operation.  → Should print: 5
def zero_count(matrix) -> int:
    print("Ex 10: ")
    count_z: int = 0
    for row in matrix:
        for col in row:
            if col == 0:
                count_z += 1
    return count_z


matrix = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]
print(zero_count(matrix))
print("--------------------------------------------")


# Ex 11:
# Write a function to return an array of all the elements that are repeated more
# than once in a given array. Should print: [4, 1]
def find_dup(arr: list) -> list:
    print("Ex 11: ")
    idx: int = 0
    dup_list: list[int] = []
    while idx <= (len(arr) - 1):
        if arr.count(arr[idx]) > 1 and not arr[idx] in dup_list:
            dup_list.append(arr.pop(idx))
        idx += 1
    return dup_list


arr = [4, 2, 34, 4, 1, 12, 1, 4]
print(find_dup(arr))
print("--------------------------------------------")


# Ex 12:
# Write a function using a for loop that gets an array and returns a new array
# with the elements from the given array appearing in reverse order. (Don’t use
# array reverse() method)
def array_reverse(a_r: list[type]) -> list[type]:
    print("Ex 12: ")
    reverse_list: list[int] = []
    for i in range(len(a_r) - 1, -1, -1):
        reverse_list.append(a_r[i])
    return reverse_list


arr = [43, "what", 9, True, "cannot", False, "be", 3, True];
print(array_reverse(arr))
print("--------------------------------------------")


# Ex 13:
# Given two arrays of integers. Add up each element in the same position and
# create a new array containing the sum of each pair.
# Assume both arrays are of the same length.
# For example:
# first_array = [4, 6, 7];
# second_array = [8, 1, 9];
# Function output should be:
# [12, 7, 16]
def array_sum(array1: list[int], array2: list[int]) -> list[int]:
    print("Ex 13: ")
    print(array1)
    print(array2)
    for i in range(0, len(array1)):
        array1[i] += array2[i]
    return array1


array1 = [4, 9, 1, 0, 3, 7, 5]
array2 = [2, 2, 8, 8, 9, 3, 6]
print(array_sum(array1, array2))
print("--------------------------------------------")


# Ex 14:
# Write a program that will check if two strings are palindromes.
# A palindrome is a word that spells the same forward and backward.
# Palindrome: a word, phrase, or sequence that reads the same backward as
# forward, examples for valid palindromes: madam, nurses run.
# For example:
# first_str = "racecar"
# second_str = "Java"
# Function output should be:
# True (for first_str)
# False (for second_str)
def check_is_palindrome(s: str) -> bool:
    print("Ex 14: ")
    if s == s[::-1]:
        return True
    else:
        return False


first_str = "racecar"
second_str = "Java"
print(check_is_palindrome(first_str), " (for first_str)")
print(check_is_palindrome(second_str), " (for second_str)")
print("--------------------------------------------")


# Ex 15:
# Write a while loop that iterates as long as the counter is less than 100, on
# every iteration the counter is multiplied by 2 starting from 1.
## counter = 1, 2, 4, 8, 16, 32, 6, 128
def multiplied_by_2() -> None:
    print("Ex 15: ")
    counter = 1
    print(f" counter = {counter}", end=" ")
    while counter < 100:
        counter *= 2
        print(f" {counter}", end=" ")


multiplied_by_2()
print()
print("--------------------------------------------")


# Ex 16:
# Write a while loop that iterates as long as the counter is greater than 50 , on
# every iteration the counter is divided by 2.
# The counter should start with the value 900000 before the first iteration.
# counter = 900000  450000  225000  112500  56250  28125  14062  7031  3516  1758  879  439  220  110  55  27
def multiplied_by_2() -> None:
    print("Ex 16: ")
    counter = 900000
    print(f" counter = {counter}", end=" ")
    while counter > 50:
        counter /= 2
        print(f" {round(counter)}", end=" ")


multiplied_by_2()
print()
print("--------------------------------------------")


#
# Ex 17:
# Write a function that gets an array of strings as parameter and returns a new
# array containing all the values that appear more than once. In your solution
# use only while loops.
def check_dup(arr: list) -> list:
    print("Ex 17: ")
    idx: int = 0
    dup_list: list[int] = []
    while idx <= (len(arr) - 1):
        if arr.count(arr[idx]) > 1 and not arr[idx] in dup_list:
            dup_list.append(arr.pop(idx))
        idx += 1
    return dup_list


fruits = [
    'apple', 'banana', 'orange', 'strawberry', 'grape',
    'kiwi', 'orange', 'cherry', 'peach', 'pear',
    'apple', 'watermelon', 'strawberry', 'strawberry', 'grape',
]
print(check_dup(fruits))
print("--------------------------------------------")


# Ex 18:
# Write a function that gets an array of strings as parameter and returns a new
# array containing all the values from the provided array in the same order but
# without any duplicated values. In your solution use only while loops.
# For example:
# names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
# Function output should be:
# ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor']
def no_dup(arr: list) -> list:
    print("Ex 18: ")
    idx: int = 0
    dup_list: list[int] = []
    while idx <= (len(arr) - 1):
        if arr.count(arr[idx]) > 1 and not arr[idx] in dup_list:
            dup_list.append(arr.pop(idx))
        idx += 1
    return arr


fruits = [
    'apple', 'banana', 'orange', 'strawberry', 'grape',
    'kiwi', 'orange', 'cherry', 'peach', 'pear',
    'apple', 'watermelon', 'strawberry', 'strawberry', 'grape',
]
print(no_dup(fruits))
print("--------------------------------------------")


# Ex 19:
# Write a function that gets an array of strings as parameter and returns a new
# array containing all the values from the provided array in the same order but
# without any duplicated values.
# If the string ‘pete’ is a value inside the array your function should skip it and
# not copy it to the new array. In your solution use only while loops.
# For example:
# names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
# Function output should be:
# ['Chris', 'Kevin', 'Naveed', 'Victor']
def check_dup(arr: list) -> list:
    print("Ex 19: ")
    idx: int = 0
    dup_list: list[int] = []
    while idx <= (len(arr) - 1):
        if arr.count(arr[idx]) > 1 and not arr[idx] in dup_list or arr[idx] == "Pete":
            dup_list.append(arr.pop(idx))
        idx += 1
    return arr


names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(check_dup(names))
print("--------------------------------------------")

# Ex 20:
# Use a while loop to iterate on a boolean array.
# As long as the next index is different from the previous index the iteration
# continues, otherwise, return the index of the element with the same value.
# If there are not two successive values, the function will return -1.
# For example:
# array= [true, false, false, true, true, false] → return 2
# array= [true, false, true, false, true, true]; → returns 5
# array= [true, false, true, false, true, false]; → returns -1
def two_successive(a1: list[bool]) -> int:
    print("Ex 20: ")
    resualt: int
    flag: bool = False  # Tell as if found two successive values
    idx: int = -1
    while idx <= (len(a1) - 3):
        idx += 1
        if a1[idx] == a1[idx + 1]:
            flag = True
            break
    if flag:
        return idx+1
    else:
        return -1

print(two_successive([True, False, False, True, True, False]))
print(two_successive([True, False, True, False, True, True]))
print(two_successive([True, False, True, False, True, False]))
print("--------------------------------------------")

# Ex 21:
# Write a python program that gets user input (use input() function for this).
# The first input will be the user full name
# Second input will be the user age
# Third input will be the user email
# Write validation for each input provided by the user and allow the user to try
# again in case the user provided invalid input.
# Validation for full name input → string type with 2 words for first name and last
# name.
# Validation for age input → int type between 1 - 130.
# Validation for email input → string type with ‘@’ inside.
def input_inf()->None:
    full_name_v: str = ""
    words: list[str] = []
    while True:
        full_name_v = input("Enter full name: ").strip()
        words = full_name_v.split(" ")
        if len(words) == 2:
            if words[0].isalpha() and words[1].isalpha():
                break

    age_v: int = int
    while True:
        try:
            age_v = int(input("Enter your age: "))
            if 1 <= age_v <= 130:
                break
        except ValueError:
            print("Only integers are allowed")

    email_v: str = str
    while True:
        email_v = str(input("Enter your email: "))
        if '@' in email_v:
            break

    user_id: list[dict[str, str]] = []
    user_f_n: dict[str, str] = {'full_name': full_name_v}
    user_id.append(user_f_n)
    user_age: dict[str, int] = {'age': age_v}
    user_id.append(user_age)
    user_email: dict[str, int] = {'email': email_v}
    user_id.append(user_email)

    return user_id

print(input_inf())