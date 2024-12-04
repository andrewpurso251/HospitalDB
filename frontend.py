
import cx_Oracle
import sys
def insertDoctor():
    first_name = input("Please input doctor's first name")
    last_name = input("Please input doctor's last name")
    doctor_id = input("Please input the doctor's id number")
    ssn = input("Please input the doctor's SSN")
    assigned_department = input("Please input the doctor's department")
    address = input("Please input the doctor's address")
    phone_no = input("Please input the doctor's phone number")
    birth_date = input("Please input the doctor's DOB")
    contact_no = input("Please input the doctor's contact number")
   
    insert_query = """
    INSERT INTO Doctors 
    (First_name, last_name, doctor_id, ssn, assigned_department, address, phone_no, birth_date, contact_no)
    VALUES (:first_name, :last_name, :doctor_id, :ssn, :assigned_department, :address, :phone_no, :birth_date, :contact_no)
    """
    try:
        # Execute the query with the provided input values
        cursor.execute(insert_query, {
            'first_name': first_name,
            'last_name': last_name,
            'doctor_id': doctor_id,
            'ssn': ssn,
            'assigned_department': assigned_department,
            'address': address,
            'phone_no': phone_no,
            'birth_date': birth_date,
            'contact_no': contact_no
        })

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}")

def insertPatient():
    first_name = input("Please input the patient's first name")
    last_name = input("Please input the patient's last name")
    patient_id = input("Please input the patient's ID number")
    ssn = input("Please input the patient's SSN")
    current_address = input("Please input the patient's Current Address")
    permanent_address = input("Please input the patient's Permanent Address")
    phone_no = input("Please input the patient's phone number")
    permanent_phone = input("Please input the patient's permanent phone number")
    birth_date = input("Please input the patient's DOB")
    sex = input("Please input the patient's sex")
    condition = input("Please input the patient's condition")
    primary_care_doctor_id = input ("Please input the ID of the patient's primary care doctor")
    
    insert_query = """
    INSERT INTO PATIENTS (first_name, last_name, patient_id, ssn, current_address, permanent_address, phone_no,
    permanent_phone, birth_date, sex, condition, primary_care_doctor_id)
    VALUES(:first_name, :last_name, :patient_id, :ssn, :current_address, :permanent_address, :phone_no, :permanent_phone, :birth_date, :sex, :condition, :primary_care_doctor_id)
    """

    try:
        cursor.execute(insert_query, {
            'first_name': first_name,
            'last_name': last_name,
            'patient_id': patient_id,
            'ssn':ssn,
            'current_address': current_address,
            'permanent_address': permanent_address,
            'phone_no': phone_no,
            'permanent_phone': permanent_phone,
            'birth_date': birth_date,
            'sex': sex,
            'condition': condition,
            'primary_care_doctor_id': primary_care_doctor_id
        })

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}") 

def insertDepartment():
    department_name = input("Please enter the department name")
    department_code = input("Please enter the department code")
    office_number = input("Please enter the office number")
    office_phone = input("Please enter the office phone number")
    department_head = input("Please enter the Doctor ID of the department head")

    insert_query = """
        INSERT INTO DEPARTMENTS (department_name, department_code, office_number, office_phone, department_head)
        VALUES(:department_name, :department_code, :office_number, :office_phone, :department_head)
    """

    try: cursor.execute(insert_query, {
        'department_name': department_name,
        'department_code': department_code,
        'office_number': office_number,
        'office_phone': office_phone,
        'department_head': department_head
    })

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}") 
    
def insertProcedure():
    procedure_name = input("Please enter the procedure name")
    procedure_description = input("Please enter the procedure description")
    procedure_number = input("Please enter the procedure ID")
    procedure_duration = input("Please enter the procedure duration")
    offering_department = input("Please enter the department ID of the department that provides this procedure")

    insert_query = """
        INSERT INTO PROCEDURE (procedure_name, procedure_description, procedure_number, procedure_duration, offering_department)
        VALUES (:procedure_name, :procedure_description, :procedure_number, :procedure_duration, :offering_department)
    """

    try: cursor.execute(insert_query, {
        'procedure_name': procedure_name,
        'procedure_description': procedure_description,
        'procedure_number': procedure_number,
        'procedure_duration': procedure_duration,
        'offering_department': offering_department

    })

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
    
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}") 

def insertMedication():

def deleteDoctor():
    var = input("Input doctor ID: ")
    cursor.execute("DELETE FROM Doctors WHERE doctor_id = " + var)
    print("Operation executed.")
def deletePatient():
    var = input("Input patient ID: ")
    cursor.execute("DELETE FROM Patients WHERE patient_id = " + var)
    print( "Operation executed.")
def deleteDepartment():
    var = input("Input department code: ")
    cursor.execute("DELETE FROM Doctors WHERE department_code = " + var)
    print( "Operation executed.")
def deleteProcedure():
    var = input("Input procedure number : ")
    cursor.execute("DELETE FROM Procedures WHERE procedure_number = " + var)
    print( "Operation executed.")
def deleteMedication():
    var = input("Input medicine name: ")
    cursor.execute("DELETE FROM Medicine WHERE medicine_name = " + var)
    print( "Operation executed.")

def displayRecord(choice):
    if choice == 1:
        itemId = input("Please input the DoctorID of the Doctor you are looking for")
    elif choice == 2:
        itemId = input("Please input the PatientID of the Patient you are looking for")
    elif choice == 3:
        itemId = input("Please input the Department ID for the Department you are looking for")
    elif choice == 4: 
        itemID = input("Please input the Operation ID for the Operatin you are looking for")
    elif choice == 5:
        itemID = input("Please input the name of the medication you are looking for")
def promptUser():
    operation = input("Would you like to 1). Insert\n 2). Delete \n 3) Display Record") 
    choice = input ("1.) Doctor\n 2.) Patient\n 3.) Department\n 4.) Procedure\n 5.) Medication\n 6.) Quit Program \nPlease select desired field:")
    if (choice == 1):
        if operation == 1:
            insertDoctor()
        elif operation == 2:
            deleteDoctor()
        else:
            displayRecord(choice)
    elif (choice == 2):
        if operation == 1:
            insertPatient()
        elif operation == 2:
            deletePatient()
        else: 
            displayRecord(choice)
    elif (choice == 3):
        if operation == 1:
            insertDepartment()
        elif operation == 2:
            deleteDepartment()
        else:
            displayRecord(choice)
    elif (choice == 4):
        if operation == 1:
            insertProcedure()
        elif operation == 2:
            deleteProcedure()
        else:
            displayRecord(choice)
    elif (choice == 5):
        if operation == 1:
            insertMedication()
        elif operation == 2:
            deleteMedication()
        else:
            displayRecord(choice)
    elif (choice == 6):
        sys.exit()
    else:
        print("invalid input please try again")
        promptUser()
        
    



dsn_tns = cx_Oracle.makedsn("cisvm-oracle.unfcsd.unf.edu",1521, "ORCL")
connection = cx_Oracle.connect("G26", "ayjmnHx7", dsn_tns)
cursor = connection.cursor()
cursor.execute("SELECT * FROM doctors")

cursor.execute("SELECT table_name FROM user_tables")
for x in cursor:
    print(x)

promptUser()


