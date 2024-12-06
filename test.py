matrix = [
    [1, 62],
    [2, 21],
    [3, 88],
    [4, 43],
    [5, 52],
    [6, 77]
]

# Remove the row at index id
row_to_move = matrix.pop(2)

# Insert the row at index
matrix.insert(0, row_to_move)
print(matrix)

# Reorder students_l based on the sorted matrix
student_to_move = []
for item in sorted_matrix:
    student_id_matrix = item[0]
    for student in students_l:
        # Data Structure id  == id matrix
        if student[0]["id"] == student_id_matrix:
            # Remove the row at index id
            student_to_move = student_id.pop(student_id)
        else:
            student_to_move.append(student)
            # single_student.append(student)



