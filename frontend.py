
import cx_Oracle
import sys
def insertDoctor():
    first_name = input("Please input doctor's first name\n")
    last_name = input("Please input doctor's last name\n")
    doctor_id = input("Please input the doctor's id number\n")
    ssn = input("Please input the doctor's SSN\n")
    assigned_department = input("Please input the doctor's department\n")
    address = input("Please input the doctor's address\n")
    phone_no = input("Please input the doctor's phone number\n")
    birth_date = input("Please input the doctor's DOB\n")
    contact_no = input("Please input the doctor's contact number\n")
    
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
        connection.commit()
        print("Data Inserted Successfully\n")

    except cx_Oracle.DatabaseError as e:
        # Handle database errors
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}\n")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {str(e)}\n")

def insertPatient():
    first_name = input("Please input the patient's first name\n")
    last_name = input("Please input the patient's last name\n")
    patient_id = input("Please input the patient's ID number\n")
    ssn = input("Please input the patient's SSN\n")
    current_address = input("Please input the patient's Current Address\n")
    permanent_address = input("Please input the patient's Permanent Address\n")
    phone_no = input("Please input the patient's phone number\n")
    permanent_phone = input("Please input the patient's permanent phone number\n")
    birth_date = input("Please input the patient's DOB\n")
    sex = input("Please input the patient's sex\n")
    condition = input("Please input the patient's condition\n")
    primary_care_doctor_id = input ("Please input the ID of the patient's primary care doctor\n")

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
    department_head = input("Please enter the Doctor ID of the department head\n")

    insert_query = """
        INSERT INTO DEPARTMENTS (department_name, department_code, office_number, office_phone, department_head)
        VALUES(:department_name, :department_code, :office_number, :office_phone, :department_head)
    """

    try: 
        cursor.execute(insert_query, {
        'department_name': department_name,
        'department_code': department_code,
        'office_number': office_number,
        'office_phone': office_phone,
        'department_head': department_head
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

def insertProcedure():
    procedure_name = input("Please enter the procedure name\n")
    procedure_description = input("Please enter the procedure description\n")
    procedure_number = input("Please enter the procedure ID\n")
    procedure_duration = input("Please enter the procedure duration\n")
    offering_department = input("Please enter the department ID of the department that provides this procedure\n")

    insert_query = """
        INSERT INTO PROCEDURE (procedure_name, procedure_description, procedure_number, procedure_duration, offering_department)
        VALUES (:procedure_name, :procedure_description, :procedure_number, :procedure_duration, :offering_department)
    """

    try: 
        cursor.execute(insert_query, {
        'procedure_name': procedure_name,
        'procedure_description': procedure_description,
        'procedure_number': procedure_number,
        'procedure_duration': procedure_duration,
        'offering_department': offering_department

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

def insertMedication():
    med_name = input("Please enter the medication name\n")
    med_manufacturer = input("Please enter the medication manufacturer\n")
    med_description = input("Please enter the medication description\n")
        
    insert_query = """
        INSERT INTO MEDICATION (med_name, med_manufacturer, med_description)
        VALUES (:med_name, :med_manufacturer, :med_description)
    """

    try:
        cursor.execute(insert_query, {
            'med_name': med_name,
            'med_manufacturer': med_manufacturer,
            'med_description': med_description
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

def insertPatientProcedure():
    patient_id = input("Please enter the patient ID\n")
    procedure_id = input("Please enter the procedure ID\n")
    procedure_doctor = input("Please enter the doctor ID of the doctor performing the procedure\n")
    notes = input("Please enter any notes\n")
    procedure_date = input("Please enter the date of the procedure\n")
    procedure_time = input("Please enter the time of the procedure\n")

    insert_query = """
        INSERT INTO PATIENT_PROCEDURE_DOCTORS (patient_id, procedure_id, procedure_doctor, notes, procedure_date, procedure_time)
        VALUES (:patient_id, :procedure_id, :procedure_doctor, :notes, :procedure_date, :procedure_time)
    """

    try:
        cursor.execute(insert_query, {
            'patient_id': patient_id,
            'procedure_id': procedure_id,
            'procedure_doctor': procedure_doctor,
            'notes': notes,
            'procedure_date': procedure_date,
            'procedure_time': procedure_time
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
def insertInteraction():
    patient_id = input("Please enter the patient ID\n")
    interaction_id = input("Please enter the interaction ID\n")
    interaction_date = input("Please enter the interaction date\n")
    interaction_time = input("Please enter the interaction time\n")
    interaction_description = input("Please enter the interaction description\n")

    insert_query = """
        INSERT INTO INTERACTION (patient_id, interaction_id, interaction_date, interaction_time, interaction_description)
        VALUES (:patient_id, :interaction_id, :interaction_date, :interaction_time, :interaction_description)
    """

    try:
        cursor.execute(insert_query, {
            'patient_id': patient_id,
            'interaction_id': interaction_id,
            'interaction_date': interaction_date,
            'interaction_time': interaction_time,
            'interaction_description': interaction_description
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

def deleteDoctor():
    var = input("Input doctor ID: ")
    cursor.execute("DELETE FROM Doctors WHERE doctor_id = :doctor_id", {'doctor_id': var})
    print("Operation executed.")
def deletePatient():
    var = input("Input patient ID: ")
    cursor.execute("DELETE FROM Patients WHERE patient_id = :patient_id", {'patient_id': var})
    print( "Operation executed.")
def deleteDepartment():
    var = input("Input department code: ")
    cursor.execute("DELETE FROM Departments WHERE department_code = :department_code", {'department_code': var})
    print("Operation executed.")
def deleteProcedure():
    var = input("Input procedure number : ")
    cursor.execute("DELETE FROM Procedures WHERE procedure_number = :procedure_number", {'procedure_number': var})
    print( "Operation executed.")
def deleteMedication():
    var = input("Input medicine name: ")
    cursor.execute("DELETE FROM Medicine WHERE medicine_name = :medicine_name", {'medicine_name': var})
    print( "Operation executed.")

def deletePatientProcedure():
    var = input("Input patient ID: ")
    cursor.execute("DELETE FROM Patient_Procedure_Doctors WHERE patient_id = :patient_id", {'patient_id': var})
    print( "Operation executed.")

def deleteInteraction():
    var = input("Input interaction ID: ")
    cursor.execute("DELETE FROM Interaction WHERE interaction_id = :interaction_id", {'interaction_id': var})
    print( "Operation executed.")

def displayRecord(choice):
    if choice == '1':
        itemId = input("Please input the DoctorID of the Doctor you are looking for\n")
        cursor.execute("SELECT * FROM Doctors WHERE doctor_id = :doctor_id", {'doctor_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Doctor ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, SSN: {record[3]}, Department: {record[4]}, Address: {record[5]}, Phone No: {record[6]}, Birth Date: {record[7]}, Contact No: {record[8]}")
        else:
            print("No record found with the provided DoctorID")
    elif choice == '2':
        itemId = input("Please input the PatientID of the Patient you are looking for\n")
        cursor.execute("SELECT * FROM Patients WHERE patient_id = :patient_id", {'patient_id': itemId})
        records = cursor.fetchall()
        if records:
            for record in records:
                print(f"Patient ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, SSN: {record[3]}, Current Address: {record[4]}, Permanent Address: {record[5]}, Phone No: {record[6]}, Permanent Phone: {record[7]}, Birth Date: {record[8]}, Sex: {record[9]}, Condition: {record[10]}, Primary Care Doctor ID: {record[11]}")
        else:
            print("No record found with the provided PatientID")
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
    choice = input("\n1.) Doctor\n2.) Patient\n3.) Department\n4.) Procedure\n5.) Medication\n6.) Assign a patient a procedure\n7.) Interaction \n8). Print Health Record\n 9). Print Medication Prescribed\n10.) Quit Program \nPlease select desired field:\n")
    if choice == '1':
        if operation == '1':
            insertDoctor()
        elif operation == '2':
            deleteDoctor()
        else:
            displayRecord(choice)
    elif choice == '2':
        if operation == '1':
            insertPatient()
        elif operation == '2':
            deletePatient()
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
 

