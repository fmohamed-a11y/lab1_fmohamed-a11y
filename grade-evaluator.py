import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"I couldn't find a file named '{filename}'. Please check the name and try again.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"Something went wrong while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    if not data:
        print("This file doesn't have any assignment in it yet.")
        return
    print("Processing the grade data...")

    for a in data:
        if a['score'] < 0 or a['score'] > 100:
            print(f"'{a['assignment']}' has an invalid score of {a['score']} (must be between 0 and 100).")

    total_weight = sum(a['weight'] for a in data)
    formative_weight = sum(a['weight'] for a in data if a['group'] == 'Formative')
    summative_weight = sum(a['weight'] for a in data if a['group'] == 'Summative')

    if total_weight == 100 and formative_weight == 60 and summative_weight == 40:
        print("Weight validation passed: Total=100, Formative=60, Summative=40.")
    else:
        print("Weight validation failed: the weights don't add up correctly.")

    final_grade = sum(a['score'] * (a['weight'] / 100) for a in data)
    gpa = (final_grade / 100) * 5.0
    print(f"Final Grade: {final_grade}")
    print(f"GPA: {gpa}")

    formative_score = sum(a['score'] * a['weight'] for a in data if a['group'] == 'Formative') / formative_weight
    summative_score = sum(a['score'] * a['weight'] for a in data if a['group'] == 'Summative') / summative_weight
    print(f"Formative average: {formative_score}%")
    print(f"Summative average: {summative_score}%")

    if formative_score >= 50 and summative_score >= 50:
        status = "PASSED"
    else:
        status = "FAILED"
    print(f"Final Status: {status}")

    failed_formatives = [a for a in data if a['group'] == 'Formative' and a['score'] < 50]
    if failed_formatives:
        highest_weight = max(a['weight'] for a in failed_formatives)
        resubmission_list = [a for a in failed_formatives if a['weight'] == highest_weight]
        print("Eligible for resubmission:")
        for a in resubmission_list:
            print(f" - {a['assignment']} (Score: {a['score']}, Weight: {a['weight']})")
    else:
        print("No resubmission needed.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
