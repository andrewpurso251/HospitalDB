
import cx_Oracle
import sys
def insertDoctor():

def insertPatient():

def insertDepartment():

def insertProcedure():

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

def promptUser():
    operation = input("Would you like to 1). Insert or 2). Delete
    choice = input ("1.) Doctor\n 2.) Patient\n 3.) Department\n 4.) Procedure\n 5.) Medication\n 6.) Quit Program \nPlease select desired field:")
    if (choice == 1):
        if operation == 1:
            insertDoctor()
        else:
            deleteDoctor()
    elif (choice == 2):
        if operation == 1:
            insertPatient()
        else:
            deletePatient()
    elif (choice == 3):
        if operation == 1:
            insertDepartment()
        else:
            deleteDepartment()
    elif (choice == 4):
        if operation == 1:
            insertProcedure()
        else:
            deleteProcedure()
    elif (choice == 5):
        if operation == 1:
            insertMedication()
        else:
            deleteMedication()
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
