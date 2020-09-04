numbers = [1,2,3,4,5,6,6,8,8,6,9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]

def Mode(value):
    return max(set(value), key = value.count)

mostNumbers = Mode(numbers)
mostGrades = Mode(grades)
print(mostNumbers)
print(mostGrades)