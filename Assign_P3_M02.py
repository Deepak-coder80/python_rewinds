keys=[]
values=[]
#get the size of keys or list
size = int(input("Enter the length "))
#Read the key and values as sepearte list
for i in range(size):
  data_key=int(input("Enter the key"))
  keys.append(data_key)
  data_value=int(input("Enter the value"))
  values.append(data_value)

d={}



#METHOD 2 - Using Zip Iterator
it = zip(keys,values) #it-an iterator

keys_values_pairs = list(it) #list of 2-tuples

d=dict(keys_values_pairs)

print(d)