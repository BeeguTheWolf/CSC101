
from data import *

#  Homework #1:

# Each function must include, as a comment, a short description of the function's purpose including the function's
# input and output, and the function must include type annotations for the parameters and the function return type.

# PART 1: 
# Function takes a string, testword as input and for each vowel, count increases by one.
# The final ouput is count, the number of vowels in the testword

def vowel_count(testword):
    count = 0
    vowels = 'aeioutAEIOU'
    for char in testword:
        if char in vowels:
            count = count + 1
    return count


# PART 2:
# Function takes an input of a list of lists of ints. 
# For any list of length 2, they are added to a new list
# The final output is the newList, with all lists of length two

def short_lists(inputLists):
    newList = []
    for sublist in inputLists:
         if len(sublist) == 2:
          newList.append(sublist)
    return newList


# PART 3:
# Takes an input of a list of lists of integers
# Function creates a newlist, checks if a list within the list of lists is of length two:
# If so, the order is re-aranged to be in ascending order, otherwise it remains as inputted

def ascening_pairs(inputLists):
    newList = []
    for sublist in inputLists:
        if len(sublist) == 2:
            for i in range(len(sublist)):
                for j in range(len(sublist)-1):
                    if sublist[j] > sublist[j+1]:
                        sublist[j], sublist[j+1] = sublist[j+1], sublist[j]
            newList.append(sublist)
        else:
            newList.append(sublist)
    return newList

# PART 4:
# Input is two Price objects, P1 and P2
# This function totals the amount of cents and dollars
# If the cent total is greater than 99, a dollar is added and cents are adjusted accordingly
# Returns a new Price object, P3, with the total amount of dollars and cents

def add_prices(P1, P2):
    totaldollars = P1.dollars + P2.dollars
    totalcents = P1.cents + P2.cents
    if totalcents > 99:
        totaldollars = totaldollars + 1
        totalcents = totalcents - 100
    P3 = Price(totaldollars,totalcents)
    return P3


# PART 5:  
# Input is a Rectangle Object named Rect
# Function calculates the length and height of the inputted rectangle,
# (which untilizes the Point object) to calcuate the total area
# output is total area

def rectangle_area(Rect):
    length = Rect.bottom_right.x - Rect.top_left.x
    height = Rect.bottom_right.y - Rect.top_left.y
    area = length * height
    return area 


# PART 6:
# Inputs are the desired author name, and a list of Book objects
# Function loops through the list of book to determine if the desired author was a contributing author
# Creates a newList with all 'matches' and returns the newList

def books_by_author(authorname, list_of_books):
    newList = []
    for x in list_of_books:
        if authorname in x.authors:
            newList.append(x)
    return newList

# PART 7:
# Input is a Rectangle object named Rectangle
# calculates the center x point and center y point,
# then creates a new Point object called center
# The radius is then calcuated 
# Using center and radius a new Circle Object is created called circle and returned

def circle_bound(Rectangle):
    centerx = abs(Rectangle.top_left.x-Rectangle.bottom_right.x)/2 + Rectangle.top_left.x
    centery = abs(Rectangle.top_left.y-Rectangle.bottom_right.y)/2 + Rectangle.bottom_right.y
    center = Point(centerx, centery)
    length1 = int(abs(centerx-Rectangle.top_left.x))
    length2 = int(abs(centery-Rectangle.bottom_right.y))
    radius1 = float(math.sqrt((length1*length1)+(length2*length2)))
    radius = float(radius1)
    circle = Circle(center,radius)
    return circle

# PART 8:
# Input is a list of Employee Objects
# loop through list to calculate average pay rate
# loop through list again to compare avg to individual
# If individual pay < average, add to newList
# Return newList

def below_pay_average(List_of_employees):
    newList = []
    money = 0
    for x in List_of_employees:
        money = money + x.pay_rate
    if len(List_of_employees) == 0:
        return
    average_pay = money/len(List_of_employees)
    for x in List_of_employees:
        if x.pay_rate < average_pay:
             newList.append(x)
    return newList