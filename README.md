# School Report System

![Website Mockup](assets/images/readme/)

[This is a link to the live website]()
#### - Username- admin
#### - Password- admin123

[This is a link to the live GoogleSheet]()

## Table Of Contents
- [Introduction](#Introduction)
- [Design](#Design) 
  * [FlowChart/Function](#flowchartfunction)
  * [Colorama](#colorama)
  * [User Feedback](#User-feedback)
- [Application Features](#application-features)
  * [Python Logic](#python-logic)
  * [Data/APIs Used](#dataapis-used)
- [UX (User Experience)](#user-experience)
- [Accessibility](#accessibility)
- [Future Features](#future-features)
- [Testing](#testing)  
- [Deployment](#deployment)
- [Clone A Repository](#how-to-run-the-project-locally)
- [Download A Repository](#download-the-repository) 
- [Technologies](#technologies)
- [Credits](#credits)  
- [Acknowledgements](#acknowledgements) 


## Introduction
The School Report System is a Python-based application that leverages Google Sheets to manage and analyze student grades. The system allows for secure user authentication, collection of student grades, computation of average scores, and generation of detailed report cards. This application simplifies the administrative tasks associated with student performance tracking and reporting.

## Design
### FlowChart/Function
![Flowchart](assets/images/readme/school_report_system.png)

1. **User Validation**
- Input username and password.
- Validate against stored credentials.
2. **Grade Input**
- Input student name.
- Input grades for each subject.
3. **Data Insertion**
- Insert grades into Google Sheets.
4. **Grade Collection**
- Retrieve all grades from Google Sheets.
5. **Averages Calculation**
- Calculate student and subject averages.
6. **Averages Update**
- Update Google Sheets with calculated averages.
7. **Student Ranking**
- Rank students based on average grades.
8. **Report Card Generation**
- Generate and update report cards in Google Sheets with comments.

### Colorama
- The application uses the colorama library for colorizing terminal text to enhance user experience with clear visual feedback:
  * **Green for successful actions.**

  ![green](assets/images/readme/colorama_one.png)

  * **Red for errors or invalid inputs.**

  ![red](assets/images/readme/colorama_two.png)

  * **Yellow and Cyan for informational messages.**

  ![yellow & cyan](assets/images/readme/colorama_three.png)

  * **Magenta for highlighting student rankings.**

  ![magenta](assets/images/readme/colorama_four.png)

  ### User Feedback
- Successful validation: Validation successful!
- Invalid login attempt: Failed! Invalid username or password. Please try again.
- Grade entry success: Grades inserted in worksheet.
- Completion of tasks: Comments have been successfully added.

## Application Features
## Python Logic
- User Validation: Ensures secure login for administrators.
- Grade Input: Collects grades for Mathematics, English, Physics and Chemestry.
- Data Insertion: Adds grades to Google Sheets.
- Grade Collection: Retrieves and displays all stored grades.
- Averages Calculation: Calculates the average grade for each student subject.
- Averages Update: Updates Google Sheets with grade average data.
- Student Ranking: Ranks students based on average grades ascending.
- Report Card Generation: Produces report cards with personalized comments.

## Data/APIs Used
- Google Sheets API: For storing, retrieving, and updating grade data.

## User Experience
### As a first time user:

1. **Start the Process by Logging In:**
  - I want to securely log in to the system by entering my username and password.
  - I want to receive immediate feedback on the success or failure of my login attempt.

2. **Input Student Grades:**
  - I want to start the grade input process by entering a student's name.
  - I want to input grades for core subjects  such as Mathematics, English, Physics, and Chemistry.
  - I want to validate my input to ensure grades are between 0 and 100.

3. **Save and View Grades:**
  - I want to save the grades into the system (Google Sheets) by clicking a button.
  - I want to receive confirmation that grades have been successfully saved.
  - I want to view all entered grades to ensure they have been recorded correctly.

4. **Calculate and View Averages:**

  - I want the system to calculate average grades for each student and each subject automatically.
  - I want to see clear feedback on the calculated averages.

5. **Generate and View Report Cards:**
  - I want to generate report cards for each student with their average grades and class ranking.
  - I want to input personalized comments for each student.
  - I want the system to display the final report cards with all necessary details.

6. **Navigate Easily:**

  - I want clear instructions and prompts at each step of the process.
  - I want to go back to the main menu or home page to start a new task without losing previous data.

### As a Returning User:
1. **View Historical Data:**

  - I want to log in and view previously entered grades and report cards.
  - I want to see a leaderboard or ranking of students based on their average grades.

2. **Manage and Update Data:**
  - I want to update existing grades or add new grades for students.
- I want the system to recalculate averages and rankings automatically after updates.

3. **Enhanced Reporting and Analysis:**
  - I want to generate detailed reports covering various aspects such as performance trends over time.
  - I want the option to export reports as PDFs or print them directly.

4. **Receive Notifications:**
  - I want to receive email notifications when new grades are entered or reports are generated.
  - I want to be notified of any system updates or new features.

5. **Additional Features:**
  - I want to track student attendance alongside grades.
  - I want to set up automated alerts for students with grades below a certain threshold.  

## Accessibility
- Visual Feedback: Use of colorama to provide color-coded messages for better clarity and immediate understanding of system status.
-  Ensure that all inputs and interactions can be completed using the keyboard to accommodate users who may have difficulty using a mouse.
- Provide clear instructions and error messages to help users understand what is required and how to correct any mistakes.

## Future Features
- Expanded User Roles: Differentiate between who is logging in
- Grade Visualization: Graphical representation of student performance.
- Email Notifications: Send report cards to students via email.
- Parent Access: Allow parents to view their child's progress.
- Attendance Tracking: Add functionality to track student attendance alongside their grades. This could provide a more comprehensive view of student performance.

## Testing
[CI Python Linter](https://pep8ci.herokuapp.com/#)

![python validation](assets/images/readme/python_validation.png)