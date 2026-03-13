import csv
def load_students(filepath):
    students=[]
    with open(filepath,"r") as f:
        reader= csv.DictReader(f)
        for row in reader:
            row["score"]= float(row["score"])
            students.append(row)
    return students

def compute_stats(students):
    scores=[]
    for x in students:
        scores.append(x["score"])
    #print(scores)
    return{
        "total": len(scores),
        "average": sum(scores)/len(scores),
        "highest": max(scores),
        "lowest" : min(scores),
        "passed" : sum(1 for x in scores if x>=50) 
        }
def write_report(students,stats,output_filepath,highest_average,subject):
    with open(output_filepath,"w") as f:
        f.write("="*45+"\n")
        f.write("         STUDENT GRADE REPORT     \n")
        f.write("="*45+"\n")
        students= sorted(students,key=lambda x:x["score"],reverse=True)
        for x in students:
            if x["score"]>=50:
                grade="PASS"
            else:
                grade="FAIL"
            
            f.write(f"{x['name']:<16} {x['score']:>6.1f}    [{grade}] \n")
        f.write("\n\n")
        f.write("-"*45+"\n")
        f.write(f"Class Average :{stats['average']}\nHighest score: {stats['highest']} \nPass Rate: {stats['passed']}/{stats['total']} \n")
        f.write(f"Highest average subject: {highest_average} -> {sum(subject[highest_average])/len(subject[highest_average])}")

#We need to group subject and marks into a dictionary
def subject_highest_avg(students):
    subject={}
    for x in students:
        if x["subject"] not in subject:
            subject[x["subject"]]=[]
        subject[x["subject"]].append(x["score"])

    highest_average=max(subject, key=lambda x: sum(subject[x])/len(subject[x]) )
    return highest_average,subject

    


students=load_students("students.csv")
#print(students)
stats=compute_stats(students)
#print(stats)
highest_average,subject=subject_highest_avg(students)
write_report(students,stats,"grade_report.txt",highest_average,subject)


