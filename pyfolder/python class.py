#introduction of python
#installtion of python
#running of programs(3 ways)--using command prompt--save in word and run -- ides
#variables(name given to the memory location)
#datatypes(int,str,float)
#list
#list functions
abc = ['suppu','kumar','lucky','mummy','daddy']
print(abc.index('suppu'))

#print(abc.append'tommy')


#print(abc.remove('tommy'))

#dict
sample = {
    'harini': ['data engineer',
                   {
                    'capgemini':'bangalore',
                    'weavesmart':'hyderabad'
                   }
                    ,27,
                   ['banglore','chennai','madras','america']
               ],
    'ivy':['kid','girl baby'],
    'supriya': 'muni'
}
print(sample['harini'][1]['capgemini'])
sample['harini'][1]['tcs']='pune'
print('new sample is',sample)

#tuple
# unchangable collection of data within parantheses #unmodifiable
#count,index
sups = (9,10,11,16,16,16)
count = sups.index(16)
print("count...",count)


#loops
#while and for loops
#while - infinate loops
#while can be suffixed with true or a condition

while True:
    print("******")
    break

a = 3
b = 5
while (a<b) : #3>5
    print("sups is happy")
    break

#for loops
#finite loops
data = ['harini','suppi','ivy','sruthi','kumar','lucky']
#directly looping the list
for name in data:
    print("namess..",name)

# looping the list with len of the data
for name in range(len(data)):
    Name = data[name]
    print("namessss",Name)

# looping the list and stoping the code by condtion
for name in range(len(data)):
    Name = data[name]
    print("namessss",Name)
    if Name == 'suppi':
        print('yesss....!!!!!')
        Index = data.index('suppi')
        print('index.....',Index)
        break


# list is mutable(add,delete,update), collection of data , ordered colletion , indexing
List1 = ['suppi','lucky','muni','mom','dad']
#append,index,pop,update,insert
#appending
List1.append('chaitu')
print('new list....',List1)
#indexing
index1 = List1.index('suppi')
print('index of suppiiii..',index1)
#removing
List1.remove('suppi')
print('second new list....',List1)
#popping
List1.pop(0)
print('new list.......',List1)
#updating
# List1.update('suppi')
# print('new list after updating...',List1)

# tuple is immutable( cant do add, delete,update),ordered collection and indexing
list2 = ('chaituuu','suppi','lucky','kumar','mummyy',6,6,7,7,7)
Count = list2.count(7)
print('count of list2...',Count)
Index = list2.index('chaituuu')
print('index of chaituuu',Index)

# dictionary is ordered , mutable key-value pair combination,indexing

# set is unordered and its self-mutable
# while loop
# for loop
# slicing of list concept
# inner loops
# nested loops
# dictionary loops
# sets
# functions
# classes (OOPS)
# file processing
# csv, txt , json , xlx
 # json
 #load = to read the data from json file
 #loads = to read the data from string object to dictionary(strings cannot be passed or red -- json object)
 #dumps = to convert the dict object to string object
 # dump = to write the dictionary to json file

 #load/loads = read
 #dump and dumps = write

 #load/ dump = to read and write function
 #loads and dumps = convert function

import json
file = open('sample.json')#to read a existing json file
data = json.load(file) #reading the file
print('data',data)

file2 = open('sample2.json','w') #to write in a new json file
dump_data = json.dump(data, file2)#data that we have to write and file path


file_data = json.loads(file)# from string to dict
print('file_data',file_data,type(file_data))

dumps_data = json.dumps(file_data)# from dict to string
print('dumps_data',dumps_data,type(dumps_data))









