from numbers import *
from grades import *

def Mode(value):
    return max(set(value), key = value.count)

mostNumbers = Mode(numbers)
mostGrades = Mode(grades)
print(mostNumbers)
print(mostGrades)