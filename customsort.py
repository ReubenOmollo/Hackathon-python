def custom_sort(dict_list, sort_key):#This line defines a function called custom_sort that takes two parameters.
#dict_list: A list of dictionaries that you want to sort.
#sort_key: A string that represents the key in the dictionaries by which you want to sort the list.

    return sorted(dict_list, key=lambda x: x.get(sort_key))
#The sorted() function takes two arguments:dict_list and key.
#the key argument uses a lambda function: lambda x: x.get(sort_key)
# x represents each dictionary in dict_list.
# get() method is called on the dictionary x to retrieve the value associated with the key sort_key.


# Example usage
data = [
    {"name": "Alice", "age": 25, "score": 88},
    {"name": "Bob", "age": 22, "score": 95},
    {"name": "Charlie", "age": 23, "score": 85},
    {"name": "David", "age": 21, "score": 90}
]
#Here, we define a list of dictionaries called data.
# Each dictionary contains information about a person, with keys like name, age, and score.

# Sort by age
sorted_by_age = custom_sort(data, "age") #This line calls the custom_sort function, passing data and the string "age" as argument.
#The function returns a new list called sorted_by_age that contains the dictionaries sorted by the age key.

print("Sorted by age:", sorted_by_age)#This line prints the result of the sorting operation, showing the dictionaries sorted by age.

# Sort by score
sorted_by_score = custom_sort(data, "score")# this line calls the custom_sort function, passing data and the string "score" as arguments.
#It returns a new list called sorted_by_score that contains the dictionaries sorted by the score key.

print("Sorted by score:", sorted_by_score)#This line prints the result of the sorting operation, showing the dictionaries sorted by score.

