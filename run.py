import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Function to setup Google Sheets API
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('school_report_system')

users = {
    'teacher': 'teacher123'
}

# Function to validate user Credentials
def validate_user():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Validation successful!")
            return True
        else:
            print("Failed! Invalid username or password. Please try again.")

# Function to collect student grades
def get_student_grades():
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
                print(f"Invalid input: {e}")
    
    return {'student_name': student_name, 'grades': grades}

# Function to insert grades into Google Sheets
def insert_grades(data, worksheet):
    row = [data['student_name']] + data['grades']
    worksheet.append_row(row)
    