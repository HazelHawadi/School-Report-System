import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
""" Function to setup Google Sheets API """
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('school_report_system')

users = {
    'admin': 'teacher123'
}

def validate_user():
    """ Function to validate user Credentials """
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Validation successful!")
            return True
        else:
            print("Failed! Invalid username or password. Please try again.")

def get_student_grades():
    """ Function to collect student grades """
    student_name = input("Enter the student's name: ")
    subjects = ['Mathematics', 'English', 'Physics', 'Chemistry']
    grades = []
    
    for subject in subjects:
        while True:
            grade_input = input(f"Enter the grade for {subject}: ").strip().lower()
            try:
                grade = float(grade_input)
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100.")
                grades.append(grade)
                break
            except ValueError as e:
                print(f"Invalid input, {e}")
    
    return {'student_name': student_name, 'grades': grades}

def insert_grades(data, worksheet):
    """ Function to insert grades into Google Sheets """
    row = [data['student_name']] + data['grades']
    worksheet.append_row(row)

def collect_grades(worksheet):
    """ Function to collect all grades from Google Sheets """
    return worksheet.get_all_records()

def calculate_averages(grades):
    """ Function to calculate average grades """
    student_averages = []
    for entry in grades:
        student = entry['Student Name']
        grade_values = [entry[subject] for subject in ['Mathematics', 'English', 'Physics', 'Chemistry']]
        average = sum(grade_values) / len(grade_values)
        student_averages.append({'student_name': student, 'average': average})

    return student_averages

def main():
    if validate_user():
        data = get_student_grades()
        grades_worksheet = SHEET.worksheet('grades')
        insert_grades(data, grades_worksheet)
        all_grades = collect_grades(grades_worksheet)
        print("Grades successfully inserted into the worksheet.")
        print("All grades in the worksheet:")
        for record in all_grades:
            print(record)
        averages = calculate_averages(all_grades)
        print("Student Averages:")
        for average in averages:
            print(average)

if __name__ == "__main__":
    main()