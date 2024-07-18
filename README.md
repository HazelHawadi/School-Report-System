# School Report System

![Website Mockup](assets/images/readme/)

[This is a link to the live website]()
#### - Username- admin
#### - Password- admin123

[This is a link to the live GoogleSheet]()

## Table Of Contents
- [Introduction](#Introduction)
- [Goal](#goal)
- [Usage](#usage)
- [Design](#Design) 
  * [FlowChart/Function](#flowchartfunction)
  * [Colorama](#colorama)
  * [User Feedback](#User-feedback)
- [Application Features](#application-features)
  * [Python Logic](#python-logic)
  * [Data/APIs Used](#dataapis-used)
- [Feature testing](#feature-testing)
- [Unfixed Bugs](#unfixed-bugs)  
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