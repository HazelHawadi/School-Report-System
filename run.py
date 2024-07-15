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
    grades = []
    while True:
        input_grade = input("Enter the grade (or type 'done' to finish): ").strip().lower()
        if grade_input == 'done':
            break
        try:
            # Convert the input to a float and check if it's within valid range
            grade = float(grade_input)
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            grades.append(grade)
        except ValueError as e:
            print(f"Invalid input: {e}")

    return {'student_name': student_name, 'grades': grades}

validate_user()
get_student_grades()