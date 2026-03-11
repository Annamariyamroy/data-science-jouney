'''def maximum(*values):
    max_num= values[0]
    for i in values:
        if i >max_num:
            max_num=i
    return max_num
result=maximum(1,0,51,32,100)  
print(result)'''

'''def greeting(**details):
    print("Hello, I'm" , details['name'] ,"and I'm" ,details['age'], "years old.")
greeting(name="Anna",age=24)'''

#all posotional arguments on line and keyword arguments on the next line
'''def describe(*args,**kwargs):
    print(" ".join(args))
    for x,y in kwargs.items():
        print(x,"=",y, end=" ")

describe('apple',"banana","cherry",name="Anna",age=24,city="Kottarakara")'''

#Write a function multiply_all(*args) that returns the product of all numbers passed.
'''def multiply_all(*args):
    product=1
    if not args:
        return "No numbers given"
    else:
        for i in args:
          product*=i
        return product
print(multiply_all())
print(multiply_all(1,2,3,4,5))'''

#Write a function filter_kwargs(**kwargs) that accepts any keyword arguments but only prints those whose values are integers.
'''def filter_kwargs(**kwargs):
    for key,value in kwargs.items():
        if isinstance(value,int):
            print(f"{key} = {value}",end=" ")

filter_kwargs(name="Anna", age=24, city="Kottarakara", score=95, height=5.6)'''

#calculator

'''def calculator(numbers,label):
    if not numbers:
        return None
    else:
        return{
            "mean": round(sum(numbers)/len(numbers),2),
            "min" : min(numbers),
            "max": max(numbers),
            "range": max(numbers)-min(numbers)


        }



result_dict=calculator([34,45,23,12,40,76],label='exam scores')
for key,values in result_dict.items():
    print(f"{key} : {values}")'''

'''def describe_list(data,*extra_labels,verbose=False):
        if extra_labels:
            print(f"labels : {','.join(extra_labels)}")
        if not data:
            print ("No data given")
        else:
             stats= {
            "mean": round(sum(data)/len(data),2),
            "min" : min(data),
            "max": max(data),
            "range": max(data)-min(data)
            }
        for key,value in stats.items():
            print(f"{key} : {value}")
        
        

        
        
        if verbose==True:
             print("Elements:", end=" ")
             for i in data:
                  print(i, end=" ") 
             print()

        
describe_list([78, 92, 85, 61, 95])
describe_list([78, 92, 85, 61, 95], "Scores")
describe_list([78, 92, 85, 61, 95], "Scores", "Math", "Final")
describe_list([78, 92, 85, 61, 95], verbose=True)
describe_list([78, 92, 85, 61, 95], "Scores", "Math", verbose=True)'''

'''def doubler(n):
        return lambda a: a*n

my_double=doubler(2)
print(my_double(11))'''

'''square= lambda x : x**2
print(square(2))

list1= [1,2,3,4,5]
doubled= list(map(lambda x:x**2,list1))
filtered= list(filter(lambda x: x>=2,list1))
print(doubled)
print(filtered)

#sorted is used to sort iterables using key with lambda
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_list=sorted(students,key=lambda x:x[1])
print(sorted_list)

#zip pairs up into tuples. returns a zip object. but using for loop can loop thorugh zip       
names  = ['Alice', 'Bob']
scores = [88, 72]
print(list(zip(names,scores)))'''

#Given words = ["banana", "apple", "kiwi", "cherry"], 
#sort them by length of the word using sorted() with a lambda key.
'''words = ["banana", "apple", "kiwi", "cherry"]
sorted_list=sorted(words, key=lambda x: len(x) ,reverse=True)
print(sorted_list)'''

#Given numbers = [15, 3, 8, 22, 1, 9], sort them in descending order using sorted().
'''numbers = [15, 3, 8, 22, 1, 9]
print(sorted(numbers,reverse=True))'''

#Given two lists first_names = ["Anna", "Bob", "Carol"] and last_names = ["Smith", "Jones", "White"], use zip() to print full names.
'''first_names = ["Anna", "Bob", "Carol"]
last_names = ["Smith", "Jones", "White"]
name=list(zip(first_names,last_names))
print(name)
for i in name:
    print(" ".join(i))'''

#Alternative
'''first_names = ["Anna", "Bob", "Carol"]
last_names = ["Smith", "Jones", "White"]
for first,last in zip(first_names,last_names):
    print(f"{first} {last}")'''

#Given words = ["apple", "cat", "banana", "dog", "elephant"], use filter() to keep only words longer than 4 characters.
'''words = ["apple", "cat", "banana", "dog", "elephant"]
print(list(filter(lambda x: len(x)>4,words)))'''