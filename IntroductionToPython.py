# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

### [:] indica toda la lista ###

# Create areas_copy
areas_copy = areas[:]

##################################

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

##################################

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

##################################

# Use slicing to create downstairs pos 0 to 5
downstairs = areas[0:6]

# Use slicing to create upstairs pos 6 hasta la última
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Alternative slicing to create downstairs pos 0 to 5
downstairs = areas[:6]

# Alternative slicing to create upstairs pos 6 hasta la última
upstairs = areas[6:]

print(downstairs)
print(upstairs)

##################################

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] =  "chill zone"

##################################

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse",24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]

print(areas_1)
print(areas_2)
print(areas)

##################################

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1  function type
print(type(var1))

# Print out length of var1  function len
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)

##################################

# Function help: find description of function
help(max)

##################################

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted   functino sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

##################################

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up   function upper
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place      function count
print(place.count("o"))   # answer is 3

##################################

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0   function index
print(areas.index(20.0))  # answer 2

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

##################################

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size     function append
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas       function reverse
areas.reverse()    # voltea la lista lo ultimo de primero y así sucesivamente

# Print out areas
print(areas)

##################################

# Definition of radius     
r = 0.43

# Import the math package    ALL PACKAGE
import math 

# Calculate C
C = 2 * math.pi * r 

# Calculate A
A = math.pi * (r ** 2)

# Build printout
print("Circumference: " + str(C))    # function str
print("Area: " + str(A))

##################################

# Definition of radius
r = 192500

# Import radians function of math package    ONE FUNCTION OF PACKAGE
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

##################################

# from PACKAGE.SUBPACKAGE import FUNCTION as ALIAS_FUNCTION
from scipy.linalg import inv as my_inv




