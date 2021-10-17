'''
Illustrate the Creation of a Dictionary using lists with suitable code.
Consider the example dictionary d={1:10, 2:20, 3:30, 4:40, 5:50},
all the key and values to be read from user and store it in 2 lists
named “keys” and “values”. Further create the dictionary from
these 2 lists and display the items accordingly
'''

#keys list
keys = []

#values list 
values = []

#Read the size of list
size = int(input("Enter size of list:"))

#Read the keys and values
for i in range (size):
    data_key = int (input("Enter the key "))
    keys.append(data_key)
    data_value =int(input("Enter the value"))
    values.append(data_value)

#dict 
d = {}

for i in range(size):
    d[keys[i]]=values[i]

#print dict
print(d)