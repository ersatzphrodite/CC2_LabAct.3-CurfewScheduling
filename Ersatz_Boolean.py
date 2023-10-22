#Boolean system thing. Im experimenting with it
#oct/20/2023 17:57

data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}

district_number = int(input("Number: "))
color_map = pd.DataFrame(data)

print(color_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("BOOLEAN SERIES")

#Checks if number is equal to any item in the list through a boolean
boolean_map = color_map['District'] == district_number
print(boolean_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("DISTRICT CHECKER")

#use the boolean map
district_info = color_map[boolean_map]
print(district_info)
