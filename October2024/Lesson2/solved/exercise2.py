import csv
from collections import defaultdict

input_file = "gradess.csv"
output_file = "averages.csv"

students = defaultdict(list)

with open("grades.csv", newline="") as student_grades:
    reader = csv.DictReader(student_grades)
    
    for row in reader:
        name = row["name"]
        grade = int(row["grade"])
        students[name].append(grade)
    
    with open(output_file, mode="w", newline="") as average_file:
        field_names = ["name", "average"]
        
        writer = csv.DictWriter(average_file, fieldnames=field_names)
        writer.writeheader() # Write the header to the average_file
        
        for name, grades in students.items():
            average = sum(grades) / len(grades)
            writer.writerow({"name": name, "average": round(average, 5)})
            
    print(f"Averages have been computed and written to {output_file}")
