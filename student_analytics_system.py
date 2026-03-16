import csv
import json
from pathlib import Path


student_details = [
    {"name": "Arjun Kumar", "subject": "Machine Learning", "score": 88.5, "email": "arjun@email.com"},
    {"name": "priya SHARMA", "subject": "Statistics", "score": 95.0, "email": "priya@email.com"},
    {"name": "  Ravi S. ", "subject": "Python", "score": 75.25, "email": "ravi@email.com"},
    {"name": "SNEHA Patel", "subject": "Machine Learning", "score": 91.0, "email": "sneha@email.com"},
    {"name": "Mohammed Ali", "subject": "Statistics", "score": 82.5, "email": "mohammed@email.com"},
    {"name": "Chen Wei", "subject": "Python", "score": 69.0, "email": "chen@email.com"},
    {"name": "Fatima Noor", "subject": "Machine Learning", "score": 78.0, "email": "fatima@email.com"},
    {"name": "Lakshmi R.", "subject": "Statistics", "score": 97.5, "email": "lakshmi@email.com"},
    {"name": "James O.", "subject": "Python", "score": 55.5, "email": "james@email.com"},
    {"name": "Sara K.", "subject": "Machine Learning", "score": 63.0, "email": "sara@email.com"},
]

with open("students_raw.csv","w",newline="") as f:
    Writer=csv.DictWriter(f,fieldnames=["name","subject","score","email"])
    Writer.writeheader()
    Writer.writerows(student_details)

def clean_name(name):
    return " ".join(name.title().split())

def assign_grade(score):
    if score>=85:
        return "A"
    elif score>=70:
        return "B"
    elif score>=55:
        return "C"
    elif score>=40:
        return "D"
    else:
        return "F"

def load_and_clean(filepath):
    student_list=[]
    with open(filepath,"r") as f:
        Reader= csv.DictReader(f)
        for row in Reader:
            try:
                row["name"]=clean_name(row["name"])
                row["subject"]= row["subject"].strip()
                row["email"]= row["email"].strip()
                row["score"]= float(row["score"])
                if 0<= row["score"] <=100:
                    row["grade"]= assign_grade(row["score"])
                    student_list.append(row)
                else:
                    raise ValueError ("The score should be between 0 and 100")
                
            except ValueError as e:
                print(f"just skipping row :{e} ")
        return student_list

def compute_class_stats(records):
    scores=[r["score"] for r in records]
    return{
        "total_students": len(records),
        "class_average" : round(sum(scores)/len(scores),2),
        "highest_score" : max(scores),
        "lowest_score"  : min(scores),
        "pass_count"    : sum(1 for s in scores if s >=50),
        "fail_count"    : len([x for x in scores if x<50]),
        "pass_rate"     : float(sum(1 for s in scores if s >=50)/(len(records))*100)
        }

def compute_subject_stats(records):
    subject_score={}
    for r in records:
        if r["subject"] not in subject_score:
            subject_score[r["subject"]]=[]
        subject_score[r["subject"]] .append(r["score"])
    
    for x in subject_score:
        compute={}
        compute["count"]=len(subject_score[x])
        compute["average"]= round(sum(subject_score[x])/len(subject_score[x]),2)
        compute["highest"]= max(subject_score[x])
        compute["lowest"] = min(subject_score[x])
        subject_score[x]= compute
    return subject_score

def rank_student(records):
    ranked=sorted(records,key= lambda x : x["score"],reverse=True)
    count=1
    for r in ranked:
        r["rank"]= count
        count+=1
    return ranked




def write_text_report(ranked,class_stats,subject_score,records,output_path):
    Path("output").mkdir(exist_ok=True)
    with open(output_path,"w") as f:
        f.write("="*75 +"\n")
        f.write("             STUDENT PERFORMANCE REPORT            \n")
        f.write("="*75+ "\n")
        f.write(f"{'Rank':<10} {'Name':<15} {'Subject':<20} {'Score':>10} {'Grade':>10} \n")
        f.write("-"*75 +"\n")
        for r in ranked:
            f.write(f"{r['rank']:<10} {r['name']:<15} {r['subject']:<20} {r['score']:>10.2f} {r['grade']:>10} \n")
        f.write("-"*70+"\n")
        class_stats_string=f"Class Average :  {class_stats['class_average']} \nHighest Score : {class_stats['highest_score']} \nPass Rate : {class_stats['pass_rate']}\nTotal Students : {class_stats['total_students']}\n"
        f.write(class_stats_string)
        f.write("SUBJECT BREAKDOWN \n")
        f.write("-"*75+"\n")
        '''Machine_Learning=f"{'Machine Learning' :<20} Students : {subject_score['Machine Learning']['count']}   Average : {subject_score['Machine Learning']['average']} \n" 
        Statistics= f"{'Statistics' :<20} Students : {subject_score['Statistics']['count']}   Average : {subject_score['Statistics']['average']} \n" 
        Python  = f"{'Python' :<20} Students : {subject_score['Python']['count']}   Average : {subject_score['Python']['average']} \n" 
        f.write(Machine_Learning+Statistics+Python)'''
        for subject,score in subject_score.items():
            f.write(f"{subject:<20}  Students:{score['count']}   Average:{score['average']} \n")

def save_json_summary(class_stats,subject_score,filepath):
    with open(filepath,"w") as f:
        summary={"class_stats": class_stats,
                 "subject_score": subject_score}
        json.dump(summary,f,indent=2)





    
records=load_and_clean("students_raw.csv")
print("="*20)

class_stats=compute_class_stats(records)
subject_score=compute_subject_stats(records)
ranked=rank_student(records)
print(ranked)
write_text_report(ranked,class_stats,subject_score,records,"output/student_grade_report.txt")
save_json_summary(class_stats,subject_score,"output/stats_summary.json")






        
