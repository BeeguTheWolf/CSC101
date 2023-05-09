#  HOMEWORK 1 TESTING SCRIPT

from hw1 import *
from data import *

# For each function that you write, you must include at least two unit tests 
# (as separate test functions in the hw1_tests.py testing file) 
# to demonstrate that the function works properly.

# PART 1:

result = vowel_count(str("House"))
print("The vowel count in 'House' is: " + str(result))

result = vowel_count(str("Bed"))
print("The vowel count in 'Bed' is: " + str(result))

# PART 2:

lista = [ [1,2], [3,4], [5,6,7,8] ]
listb = [ [1], [3,4], [5,6,7] ]

resulta = short_lists(lista)
resultb = short_lists(listb)

print("The resulting lists of length 2 are: " + str(resulta))
print("The resulting lists of length 2 are: " + str(resultb))

# PART 3: 

Lists = [ [1,2] , [3,2]  ,[1,2,4,0] ]
result = ascening_pairs(Lists)
print("The inputted lists of length 2 rewritten in ascending order are: " + str(result))

Lists = [ [2,5] , [8,2]  ,[0] ]
result = ascening_pairs(Lists)
print("The inputted lists of length 2 rewritten in ascending order are: " + str(result))

# PART 4:

dollar = 5
cent = 40
P1 = Price(dollar,cent)
P2 = Price(dollar,cent)
result = add_prices(P1,P2)
print(result)

dollar = 7
cent = 90
P1 = Price(dollar,cent)
P2 = Price(dollar,cent)
result = add_prices(P1,P2)
print(result)

# PART 5

point1 = Point(5,0)
point2 = Point(10,3)
Rect = Rectangle(point1,point2)

result = rectangle_area(Rect)
print(result)

point1 = Point(5,1)
point2 = Point(8,3)
Rect = Rectangle(point1,point2)

result = rectangle_area(Rect)
print(result)

# PART 6

Book1 = Book(["Stephen King","Justin Mills"],"The Dark Tower")
Book2 = Book(["Stephen King"], "Carrie")
Book3 = Book(["Stephen King"],"The Stand")
Book4 = Book(["George Orwell"],"1984")
Book5 = Book(["J.R.R. Tolkien","Stephen King"], "Lord of The Rings")
list_of_books = [Book1,Book2,Book3,Book4,Book5]

print("Here are some epic books: ")
epic_books = books_by_author("Stephen King", list_of_books)
print(epic_books)

print("Here are not so great books: ")
bad_books = books_by_author("George Orwell", list_of_books)
print(bad_books)

# PART 7

top_left = Point(0,5)
bottom_right = Point(5,0)
Rect = Rectangle(top_left, bottom_right)

result = circle_bound(Rect)
print(result)

top_left = Point(10,5)
bottom_right = Point(20,0)
Rect = Rectangle(top_left, bottom_right)

result = circle_bound(Rect)
print(result)

# PART 8

Employee1 = Employee('Justin', 45000)
Employee2 = Employee('John' , 55000)
Employee3 = Employee('Kieran' , 30000)
Employee4 = Employee('Aidan' , 90000)

List_of_Employees = [Employee1,Employee2,Employee3,Employee4]

result = below_pay_average(List_of_Employees)
print(result)


Employee1 = Employee('Justin', 4000)
Employee2 = Employee('John' , 550000)
Employee3 = Employee('Kieran' , 30000)
Employee4 = Employee('Aidan' , 90000)

List_of_Employees = []

result = below_pay_average(List_of_Employees)
print(result)