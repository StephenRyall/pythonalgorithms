def gradingStudents(grades):
    # Write your code here
        for i, grade in enumerate(grades):
            if (grade < 38):
                grades[i] = grade
            else:
                y = grade
                while y % 5 != 0:
                    y += 1
                diff = y - grade
                if (diff < 3):
                    grades[i] = grade + diff
        return grades


print(gradingStudents([4, 37, 64, 80]))