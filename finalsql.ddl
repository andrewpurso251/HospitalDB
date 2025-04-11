CREATE TABLE STUDENT (
    nNumber VARCHAR(9) PRIMARY KEY NOT NULL,
    ssn VARCHAR(11) UNIQUE NOT NULL,
    fName VARCHAR(20) NOT NULL,
    mInit VARCHAR(1),
    lName VARCHAR(20) NOT NULL,
    currentAddress VARCHAR(50) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip VARCHAR(5) NOT NULL,
    phone VARCHAR(12) NOT NULL,
    birthDate VARCHAR(10) NOT NULL,
    sex VARCHAR(1) NOT NULL,
    class VARCHAR(20) NOT NULL,
    majorDepartment VARCHAR(20) NOT NULL,
    minorDepartment VARCHAR(20),
    degreeProgram VARCHAR(20) NOT NULL
);


CREATE TABLE Department (
    dName VARCHAR(20) UNIQUE NOT NULL,
    dCode VARCHAR(4) UNIQUE NOT NULL,
    PRIMARY KEY (dName, dCode),
    officeNumber VARCHAR(10) NOT NULL,
    officePhone VARCHAR(12) NOT NULL,
    college VARCHAR(20) NOT NULL
);

CREATE TABLE Course (
    cName VARCHAR(20) NOT NULL,
    cNumber VARCHAR(7) PRIMARY KEY NOT NULL,
    description VARCHAR(50),
    semesterHours INT NOT NULL,
    levels VARCHAR(20) NOT NULL,
    offeringDepartment VARCHAR(4) NOT NULL,
    FOREIGN KEY (offeringDepartment) REFERENCES Department(dName)
);

CREATE TABLE CoursePrerequisite (
    courseNumber VARCHAR(7) NOT NULL,
    prerequisiteNumber VARCHAR(7) NOT NULL,
    PRIMARY KEY (courseNumber, prerequisiteNumber),
    FOREIGN KEY (courseNumber) REFERENCES Course(cNumber),
    FOREIGN KEY (prerequisiteNumber) REFERENCES Course(cNumber)
);

CREATE TABLE Instructor (
    department VARCHAR(4) NOT NULL,
    FOREIGN KEY (department) REFERENCES Department(dName),
    ssn VARCHAR(11) UNIQUE NOT NULL,
    nNumber VARCHAR(9) PRIMARY KEY NOT NULL,
    fName VARCHAR(20) NOT NULL,
    mInit VARCHAR(1),
    lName VARCHAR(20) NOT NULL,
    currentAddress VARCHAR(50) NOT NULL,
    phoneNumber VARCHAR(12) NOT NULL,
    age VARCHAR(3) NOT NULL,
    officeNumber VARCHAR(10) NOT NULL

);

CREATE TABLE StudentGrade (
    nNumber VARCHAR(9) NOT NULL,
    courseNumber VARCHAR(7) NOT NULL,
    grade VARCHAR(2) NOT NULL,
    FOREIGN KEY (nNumber) REFERENCES STUDENT(nNumber),
    FOREIGN KEY (courseNumber) REFERENCES Course(cNumber),
    PRIMARY KEY (nNumber, courseNumber)
);

