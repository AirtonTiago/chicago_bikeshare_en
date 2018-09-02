
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
i=0
for row in data_list:
    print("Row ", i, ":")
    print(data_list[i])
    i+= 1
    if i>19:
        break
# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
print("\nTASK 2: Printing the genders of the first 20 samples")
# TODO: Print the `gender` of the first 20 rows
i=0
for row in data_list:
    print("Gender of the row ", i, ":")
    print(data_list[i][6])
    i+= 1
    if i>19:
        break
# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order

def column_to_list(data, index):
    """
          Function that add the columns of a list in another list, following the same order.
          Args:
              data: The data list.
              index: The column index.
          Returns:
              List of values of the chosen column by the index

    """
    column_list = []
    for column in data:
        column_list.append(column[index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
missing= 0
print(len(data_list))
while (female+male+missing) < len(data_list):
    for row in data_list:
        if row[6]=='Male':
            male+=1
        elif row[6]=='Female':
            female+=1
        elif row[6]=='':
            missing+=1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female, "\nMissing: ", missing)


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):

    """
              Function that count the quantity of each gender
              Args:
                  data_list: The data list.
              Returns:
                  Number of genders

    """
    male = 0
    female = 0
    for gender in data_list:
        if gender[6] == 'Male':
            male+=1
        elif gender[6] == 'Female':
            female+=1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")

# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
              Function that returns the most popular gender.
              Args:
                  data: The data list.
              Returns:
                  String with the most popular gender in the data list.

    """
    male = 0
    female = 0
    for gender in data_list:
        if gender[6] == 'Male':
            male+=1
        elif gender[6] == 'Female':
            female+=1
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    elif male==female:
        answer = "Equal"
    return answer

print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")

# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_type(data_list):
    """
              Function that count the quantity of user types
              Args:
                  data: The data list.
              Returns:
                  the quantity of user type in a format of [quantity of subscriber,quantity of customer]

    """
    Subscriber = 0
    Customer = 0
    for user_type in data_list:
        if user_type [5] == 'Subscriber':
            Subscriber+=1
        elif user_type[5] == 'Customer':
            Customer+=1
    return [Subscriber, Customer]


user_types_list=column_to_list(data_list,-3)
types= ["Subscriber", "Customer"]
quantity= count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by user type')
plt.show(block=True)

input("Press enter to continue...")


# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "The condition is false because there are some missing values in the data list"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.

# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(float, trip_duration_list))

min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
sum_trip = 0

min_trip = float(trip_duration_list[0])
max_trip = float(trip_duration_list[0])

for trip in trip_duration_list:
    sum_trip+=trip

# Sorting the values
trip_duration_list_sort = sorted(trip_duration_list)
length_list = len(trip_duration_list)
# The first element of the sorted list will be the minimum value
min_trip = round(trip_duration_list_sort[0])
# The last element of the sorted list will be the Maximum value
max_trip = round(trip_duration_list_sort[len(trip_duration_list_sort)-1])
# The mean will be the result of the sum of total trips divided by the number os total trip_duration_list_sort
mean_trip = round(sum_trip/length_list)
# The median will be the value which is located in the middle of the sorted List
median_trip = int(trip_duration_list_sort[length_list//2])

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")


# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()

start_stations_list = column_to_list(data_list, 3)
start_stations = set(start_stations_list)

print("\nTASK 10: Printing start stations:")
print(len(start_stations))
print(start_stations)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_stations) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")

# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

"""


input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it? (yes or no)")
answer = "yes"

def count_items(column_list):
    """
                  Function that count the occurrency of each different item in a list, without defining the items.
                  Args:
                      column_list: The data list.
                  Returns:
                      The tuple (item_type, count_items)

    """
    items_set = set (column_list)
    item_types = []
    count_items = []
    for item in items_set:
        item_types.append(item)
        count_items.append(column_list.count(item))
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
