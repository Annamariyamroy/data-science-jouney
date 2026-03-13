'''s= "Data Science Journey 2025"
print(s[::2])'''

'''text = "  Hello, Griffith University!  "
sample="hello griffith university"
print(text)
print(text.strip())#strips from both ends
print(text.lstrip())#strips space only from lefft
print(text.rstrip())#from right only
print(sample.title())  #capitilizes every word
print(text.strip().split(","))
print(text.strip().startswith("He"))
print(text.strip().find("Griffith"))
print(text.strip().count("i"))
print(" -".join(["Data", "Science","2025"]))'''

#string formatting
'''name  = "Priya"
score = 94.6789
rank  = 3
# Float precision
print(f"name : {name}, score:{score:.2f}")
print(f"{name:<16} {score:>8} {rank: ^3}")
#zero padding
for i in range (1,11):
    print(f"Checkpoint_{i:03d}.csv")'''

'''def clean_raw(name):
   name=name.title().split()
   print(" ".join(name))
clean_raw("    Priya   SHARMA  ")'''

#Files 
'''lines = ["Data Science Notes\n", "Week 1, Day 4\n", "Topic: File I/O\n"]
with open("notes.txt","w") as f:
       for x in lines:
           f.write(x)'''
#writelines() take any iterable string as input
'''lines = ["Data Science Notes\n", "Week 1, Day 4\n", "Topic: File I/O\n"]
with open("notes.txt","w") as f:    
     f.writelines(lines)

with open("notes.txt","r") as f:
     print(f.read())'''

#readlines() returns everything or all lines  in the file at once as a list
'''with open("notes.txt","r") as f:
     print(f.readlines())'''

#readline() returns one string at a time
'''with  open("notes.txt","r") as f:
     print(f.readline())
     print(f.readline())
     print(f.readline())

with open("notes.txt","r") as f:
     for x in f :
          print(x.strip())'''

#To write this information into a csv file
import csv
students = [
    {'name': 'Arjun',   'subject': 'ML',     'score': 88},
    {'name': 'Priya',   'subject': 'Stats',  'score': 95},
    {'name': 'Ravi',    'subject': 'Python', 'score': 75},
    {'name': 'Sneha',   'subject': 'SQL',    'score': 91},
    {'name': 'John',    'subject': 'ML',     'score': 45},
    {'name': 'Anna',    'subject': 'Python', 'score': 82},
    {'name': 'Kevin',   'subject': 'Stats',  'score': 55},
    {'name': 'Meera',   'subject': 'SQL',    'score': 98},
]

with open("students.csv","w",newline="") as f:#newline prevents extra blank spaces in windows
    writer= csv.DictWriter(f,fieldnames=["name","subject","score"])#creating a writer object, pass file object and fieldnames ie, keys as column names
    writer.writeheader()
    writer.writerows(students)

#DictReads reads each row as a dictionary,first row header becomes the keys automatically
#csv reads numbers as strings. so convert when printing
'''with open("students.csv" , "r") as f:
    reader=csv.DictReader(f)
    for x in reader:
        print(f"{x['name']:<10} |{x['subject']:<8} | {float(x['score']):.1f} ")'''


#JSON file format
'''import json
data = {
    "course": "Master of Data Science",
    "university": "Griffith",
    "modules": ["Python", "Statistics", "ML", "Deep Learning"],
    "enrolled_count": 45,
    "international": True
}

with open("course_details.json","w") as f:
    json.dump(data,f,indent=2)
with open("course_details.json","r") as f:
    loaded =json.load(f)
print(loaded["course"])
print(loaded["modules"][1])
print(type(loaded["enrolled_count"]))'''


#practise questions
#1.Write a program that creates a file my_notes.txt and writes these 3 lines to it:
'''notes=["Python is fun\n","File I/O is easy\n","I love data science\n"]
with open("samplefile.txt","w") as f:
    f.writelines(notes)

with open("samplefile.txt","a") as f:
    f.write("I love Python!")
with open("samplefile.txt","r",) as f:
    for x in f:
        print(x.strip())'''
    

#2.Create a CSV file fruits.csv with columns name and price:Then read it back and print each fruit with its price.
'''apple, 1.5
banana, 0.5
cherry, 3.0
mango, 2.5'''

'''import csv
fruit_list=[{"name":"apple","price":1.5},
            {"name":"banana","price":0.5},
            {"name":"cherry","price":3.0},
            {"name":"mango","price":2.5}]

with open("fruits.csv","w",newline="") as f :
    writer= csv.DictWriter(f,fieldnames=["name","price"])
    writer.writeheader()
    writer.writerows(fruit_list)
with open("fruits.csv","r") as f :
    reader=csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}, {float(row['price']):.1f}")'''

#4. Read students.csv you created earlier and print only students whose score is above 85.
'''Arjun      | ML       | 88.0
Priya      | Stats    | 95.0
Sneha      | SQL      | 91.0'''

'''import csv
with open("students.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        if float(row ["score"])> 85:
            print(f"{row['name']:<10} |{row['subject']:<8} | {float(row['score']):.1f} ")'''

#5.Create a dictionary of your personal info and save it as profile.json. Then read it back and print each key and value.
'''import json
personal_info={"name": "Anna",
    "age": 24,
    "city": "Kottarakara",
    "hobbies": ["singing", "dancing", "learning"]}

with open("personal_info.json","w") as f:
    json.dump(personal_info,f,indent=2)

with open("personal_info.json","r") as f:
    loader=json.load(f)
    for x,y in enumerate(loader.items()):
        print(f"{x} : {y}")'''

#mini-project


