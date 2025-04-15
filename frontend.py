
import cx_Oracle
import sys
def insertStudent():
    first_name = input("Please input student's first name\n")
    last_name = input("Please input student's last name\n")
    student_id = input("Please input the student's id number\n")
    ssn = input("Please input the student's SSN\n")
    major_department = input("Please input the student's major department\n")
    minor_department = input("Please input the student's minor department\n")
    address = input("Please input the student's address\n")
    phone_no = input("Please input the student's phone number\n")
    birth_date = input("Please input the student's DOB\n")
    student_class = input("Please input the student's class\n")
    degreeProgram = input("Please input the student's degree program\n")
    
    insert_query = """
    INSERT INTO Student 
    (First_name, last_name, student_id, ssn, major_department, minor_department, address, phone_no, birth_date, student_class, degreeProgram)
    VALUES (:fName, :lName, :nNumber, :ssn, :majorDepartment, :minor_department, :currentAddress, :phone, :birthDate, :class, :degreeProgram) )
    """
    try:
        # Execute the query with the provided input values
        cursor.execute(insert_query, {
            'fname': first_name,
            'lname': last_name,
            'nNumber': student_id,
            'ssn': ssn,
            'majorDepartment': major_department,
            'minor_department': minor_department,
            'currentAddress': address,
            'phone': phone_no,
            'birthDate': birth_date,
            'class': student_class,
            'degreeProgram': degreeProgram
            
            })
        connection.commit()
        print("Data Inserted Successfully\n")

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}\n")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}\n")

def insertInstructor():
    first_name = input("Please input the instructor's first name\n")
    last_name = input("Please input the instructor's last name\n")
    instructor_id = input("Please input the instructor's ID number\n")
    ssn = input("Please input the instructor's SSN\n")
    current_address = input("Please input the instructor's Current Address\n")
    phone_no = input("Please input the instructor's phone number\n")
    
    sex = input("Please input the instructor's age\n")
    condition = input("Please input the instructor's condition\n")
    primary_care_doctor_id = input ("Please input the ID of the instructor's primary care doctor\n")

    insert_query = """
    INSERT INTO InstructorsS (first_name, last_name, instructor_id, ssn, current_address, phone_no, birth_date, sex, condition, primary_care_doctor_id)
    VALUES(:first_name, :last_name, :instructor_id, :ssn, :current_address, :phone_no, :age, :condition, :primary_care_doctor_id)
    """

    try:
        cursor.execute(insert_query, {
            'fName': first_name,
            'lName': last_name,
            'nNumber': instructor_id,
            'ssn':ssn,
            'currentAddress': current_address,
            'phoneNumber': phone_no,
            
           
            'sex': sex,
            'condition': condition,
            'primary_care_doctor_id': primary_care_doctor_id
            })
        connection.commit()
        print("Data Inserted Successfully\n")

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}\n")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}\n") 

def insertDepartment():
    department_name = input("Please enter the department name\n")
    department_code = input("Please enter the department code\n")
    office_number = input("Please enter the office number\n")
    office_phone = input("Please enter the office phone number\n")
    college = input("Please enter the college the department belongs to\n")

    insert_query = """
        INSERT INTO DEPARTMENTS (department_name, department_code, office_number, office_phone, college)
        VALUES(:dName, :dCode, :officeNumber, :officePhone, :college)
    """

    try: 
        cursor.execute(insert_query, {
        'dName': department_name,
        'dCode': department_code,
        'officeNumber': office_number,
        'officePhone': office_phone,
        'college': college
        })
        connection.commit()
        print("Data Inserted Successfully\n")    

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}\n")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}\n") 

def insertCourse():
    cName = input("Please enter the course name\n")
    cNumber = input("Please enter the course number\n")
    description = input("Please enter the course description\n")
    semesterHours = input("Please enter the semester hours\n")
    levels = input("Please enter the course level\n")
    offeringDepartment = input("Please enter the department ID of the department that offers this course\n")

    insert_query = """
        INSERT INTO Course (cName, cNumber, description, semesterHours, levels, offeringDepartment)
        VALUES (:cName, :cNumber, :description, :semesterHours, :levels, :offeringDepartment)
    """

    try: 
        cursor.execute(insert_query, {
            'cName': cName,
            'cNumber': cNumber,
            'description': description,
            'semesterHours': semesterHours,
            'levels': levels,
            'offeringDepartment': offeringDepartment
        })
        connection.commit()
        print("Data Inserted Successfully\n")

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}\n")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}\n")

def insertCoursePrerequisite():
    courseNumber = input("Please enter the course number\n")
    prerequisiteNumber = input("Please enter the prerequisite course number\n")
        
    insert_query = """
        INSERT INTO CoursePrerequisite (courseNumber, prerequisiteNumber)
        VALUES (:courseNumber, :prerequisiteNumber)
    """

    try:
        cursor.execute(insert_query, {
            'courseNumber': courseNumber,
            'prerequisiteNumber': prerequisiteNumber
        })
        connection.commit()
        print("Data Inserted Successfully\n")
    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}") 

def insertStudentGrade():
    nNumber = input("Please enter the student's N-Number\n")
    courseNumber = input("Please enter the course number\n")
    grade = input("Please enter the grade\n")

    insert_query = """
        INSERT INTO StudentGrade (nNumber, courseNumber, grade)
        VALUES (:nNumber, :courseNumber, :grade)
    """

    try:
        cursor.execute(insert_query, {
            'nNumber': nNumber,
            'courseNumber': courseNumber,
            'grade': grade
        })
        connection.commit()
        print("Data Inserted Successfully\n")
    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}")


def deleteStudent():
    var = input("Input student ID: ")
    cursor.execute("DELETE FROM Student WHERE nNumber = :nNumber", {'nNumber': var})
    print("Operation executed.")
def deleteInstructor():
    var = input("Input instructor ID: ")
    cursor.execute("DELETE FROM Instructor WHERE nNumber = :nNumber", {'nNumber': var})
    print( "Operation executed.")
def deleteDepartment():
    var = input("Input department code: ")
    cursor.execute("DELETE FROM Department WHERE dCode = :dCode", {'dCode': var})
    print("Operation executed.")
def deleteCourse():
    var = input("Input course number : ")
    cursor.execute("DELETE FROM Course WHERE courseNumber = :courseNumber", {'courseNumber': var})
    print( "Operation executed.")
def deleteCoursePrerequisite():
    var = input("Input course number: ")
    cursor.execute("DELETE FROM CoursePrerequisite WHERE courseNumber = :courseNumber", {'courseNumber': var})
    print( "Operation executed.")

def deleteStudentGrade():
    var = input("Input Student ID: ")
    cursor.execute("DELETE FROM StudentGrade WHERE nNumber = :nNumber", {'nNumber': var})
    print( "Operation executed.")


def displayRecord(choice):
    if choice == '1':
        itemId = input("Please input the StudentID of the Student you are looking for\n")
        cursor.execute("SELECT * FROM Students WHERE student_id = :student_id", {'student_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Student ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, SSN: {record[3]}, Department: {record[4]}, Address: {record[5]}, Phone No: {record[6]}, Birth Date: {record[7]}, Contact No: {record[8]}")
        else:
            print("No record found with the provided student ID")
    elif choice == '2':
        itemId = input("Please input the InstructorID of the Instructor you are looking for\n")
        cursor.execute("SELECT * FROM Instructors WHERE instructor_id = :instructor_id", {'instructor_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Instructor ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, SSN: {record[3]}, Current Address: {record[4]}, Permanent Address: {record[5]}, Phone No: {record[6]}, Permanent Phone: {record[7]}, Birth Date: {record[8]}, Sex: {record[9]}, Condition: {record[10]}, Primary Care Doctor ID: {record[11]}")
        else:
            print("No record found with the provided InstructorID")
    elif choice == '3':
        itemId = input("Please input the Department ID for the Department you are looking for\n")
        cursor.execute("SELECT * FROM Departments WHERE department_code = :department_code", {'department_code': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Department Name: {record[0]}, Department Code: {record[1]}, Office Number: {record[2]}, Office Phone: {record[3]}, Department Head: {record[4]}")
        else:
            print("No record found with the provided Department")
    elif choice == '4': 
        selector = input("Would you like to find Operations by\n1) Procedure Number\n2) Offering Department\n")
        if selector == '1':
            itemId = input("Please input the Operation ID for the Operation you are looking for\n")
            cursor.execute("SELECT * FROM Procedure WHERE procedure_number = :procedure_number", {'procedure_number': itemId})
            records = cursor.fetchall()
            if records:
                for record in records:
                    print(f"Procedure Name: {record[0]}, Description: {record[1]}, Procedure Number: {record[2]}, Duration: {record[3]}, Offering Department: {record[4]}")
            else: 
                print("No record found with the provided Procedure")
        elif selector == '2':
            itemId = input("Please input the department code for the department who's procedures you would like to view\n")
            cursor.execute("SELECT * FROM Procedure WHERE offering_department = :offering_department", {'offering_department': itemId})
            records = cursor.fetchall()
            if records:
                for record in records:
                    print(f"Procedure Name: {record[0]}, Description: {record[1]}, Procedure Number: {record[2]}, Duration: {record[3]}, Offering Department: {record[4]}")
            else: 
                print("No record found with the provided Procedure")
    elif choice == '5':
        itemId = input("Please input the name of the medication you are looking for\n")
        cursor.execute("SELECT * FROM Medication WHERE med_name = :med_name", {'med_name': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Medication Name: {record[0]}, Manufacturer: {record[1]}, Description: {record[2]}")
        else:
            print("No record found with the provided Medication Name")
    elif choice == '6':
        choice = input("Would you like to find\n 1) All Procedure Performed on a Patient\n 2) All procedures performed by a doctor\n")
        if choice == '1':
            itemId = input("Please input the Patient ID of the Patient you are looking for\n")
            cursor.execute("SELECT * FROM Patient_Procedure_Doctors WHERE patient_id = :patient_id", {'patient_id': itemId})
        elif choice == '2':
            itemId = input("Please input the Doctor ID of the Doctor you are looking for \n")
            cursor.execute("SELECT * FROM Patient_Procedure_Doctors WHERE procedure_doctor = :procedure_doctor", {'procedure_doctor': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Procedure ID: {record[1]}, Procedure Doctor: {record[2]}, Notes: {record[3]}, Procedure Date: {record[4]}, Procedure Time: {record[5]}")
        else:
            print("No record found with the provided PatientID or Doctor ID")
    elif choice == '7':
        itemId = input("Please input the Interaction ID of the Interaction you are looking for\n")
        cursor.execute("SELECT * FROM Interaction WHERE interaction_id = :interaction_id", {'interaction_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Interaction ID: {record[1]}, Interaction Date: {record[2]}, Interaction Time: {record[3]}, Interaction Description: {record[4]}")
        else:
            print("No record found with the provided Interaction ID")
    elif choice == '8':
        itemId = input("Please input the Patient ID of the Patient you are looking for\n")
        print("\nPatient Information\n")
        
        cursor.execute("SELECT * FROM Patients WHERE patient_id = :patient_id", {'patient_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, First Name: {record[1]}, Last Name: {record[3]}, SSN: {record[4]}, Current Address: {record[5]}, Permanent Address: {record[6]}, \nPhone No: {record[7]}, Permanent Phone: {record[8]}, Birth Date: {record[9]}, Sex: {record[10]}, Condition: {record[11]}, Primary Care Doctor ID: {record[12]}")
        else:
            print("No record found with the provided PatientID")
            sys.exit()
        
        print("\nAll Operations Performed on Patient\n")

        cursor.execute("SELECT * FROM Patient_Procedure_Doctors WHERE patient_id = :patient_id", {'patient_id': itemId})
        
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Procedure ID: {record[1]}, Procedure Doctor: {record[2]}, Notes: {record[3]}, Procedure Date: {record[4]}, Procedure Time: {record[5]}")
        else:
            print("No record found with the provided PatientID or Doctor ID")
            sys.exit()
        
        print("\nAll medication prescribed to patient\n")
        cursor.execute("SELECT * FROM Patient_Medication WHERE patient_id = :patient_id", {'patient_id': itemId})   
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Medication Name: {record[1]}, Presribing Doctor: {record[2]},Prescribing Date: {record[3]}")
        else:
            print("No record found with the provided Interaction ID")
            sys.exit()
    
        print("\nAll interactions involving the patient\n")    
        cursor.execute("SELECT * FROM Interaction WHERE patient_id = :patient_id", {'patient_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Interaction ID: {record[1]}, Interaction Date: {record[2]}, Interaction Time: {record[3]}, Interaction Description: {record[4]}")
        else:
            print("No record found with the provided Interaction ID")
            sys.exit()
        
    elif choice == '9':
        itemId = input("Please input the Patient ID of the Patient you are looking for\n")
        cursor.execute("SELECT * FROM Patient_Medication WHERE patient_id = :patient_id", {'patient_id': itemId})   
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, Medication Name: {record[1]}, Presribing Doctor: {record[2]},Prescribing Date: {record[3]}")
        else:
            print("No record found with the provided Interaction ID")
    
def promptUser():
    operation = input("Would you like to\n1). Insert\n2). Delete \n3) Display Record\n4). Quit Program\n")
    if operation == '4':
        sys.exit()
    choice = input("\n1.) Student\n2.) Department\n3.) Course\n4.) Instructor\n5.) Course Section\n6.) Assign a patient a procedure\n7.) Interaction \n8). Print Grade Report\n 9). Print Medication Prescribed\n10.) Quit Program \nPlease select desired field:\n")
    if choice == '1':
        if operation == '1':
            insertStudent()
        elif operation == '2':
            deleteStudent()
        else:
            displayRecord(choice)
    elif choice == '2':
        if operation == '1':
            insertInstructor()
        elif operation == '2':
            deleteInstructor()
        else: 
            displayRecord(choice)
    elif choice == '3':
        if operation == '1':
            insertDepartment()
        elif operation == '2':
            deleteDepartment()
        else:
            displayRecord(choice)
    elif choice == '4':
        if operation == '1':
            insertProcedure()
        elif operation == '2':
            deleteProcedure()
        else:
            displayRecord(choice)
    elif choice == '5':
        if operation == '1':
            insertMedication()
        elif operation == '2':
            deleteMedication()
        else:
            displayRecord(choice)
    elif choice == '6':
        if operation == '1':
            insertPatientProcedure()
        elif operation == '2':
            deletePatientProcedure()
        else:
            displayRecord(choice)
    elif choice == '7':
        if operation == '1':
            insertInteraction()
        elif operation == '2':
            deleteInteraction()
        else:
            displayRecord(choice)
    elif choice == '8':
        displayRecord(choice)
    elif choice == '9':
        displayRecord(choice)
    elif choice == '10':
        sys.exit()
    else:
        print("\nInvalid input please try again\n")
        
    promptUser()



dsn_tns = cx_Oracle.makedsn("cisvm-oracle.unfcsd.unf.edu",1521, "ORCL")
connection = cx_Oracle.connect("G26", "ayjmnHx7", dsn_tns)
cursor = connection.cursor()



promptUser()
 

