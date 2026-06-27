USE project_sentinel;

-- ======================================================
-- PROJECT SENTINEL
-- Academic Module
-- ======================================================

-- ======================================================
-- TABLE: academic_terms
-- ======================================================

CREATE TABLE academic_terms (

    term_id INT AUTO_INCREMENT PRIMARY KEY,

    school_year VARCHAR(20) NOT NULL,

    semester ENUM(
        'First Semester',
        'Second Semester',
        'Summer'
    ) NOT NULL,

    start_date DATE,

    end_date DATE,

    status ENUM(
        'Upcoming',
        'Active',
        'Closed'
    ) DEFAULT 'Upcoming',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

);

-- ======================================================
-- TABLE: courses
-- ======================================================

CREATE TABLE courses (

    course_id INT AUTO_INCREMENT PRIMARY KEY,

    course_code VARCHAR(20) NOT NULL UNIQUE,

    course_name VARCHAR(150) NOT NULL,

    description TEXT,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

);

-- ======================================================
-- TABLE: sections
-- ======================================================

CREATE TABLE sections (

    section_id INT AUTO_INCREMENT PRIMARY KEY,

    course_id INT NOT NULL,

    term_id INT NOT NULL,

    section_name VARCHAR(50) NOT NULL,

    adviser_name VARCHAR(150),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(course_id)
        REFERENCES courses(course_id),

    FOREIGN KEY(term_id)
        REFERENCES academic_terms(term_id)

);

-- ======================================================
-- TABLE: subjects
-- ======================================================

CREATE TABLE subjects (

    subject_id INT AUTO_INCREMENT PRIMARY KEY,

    subject_code VARCHAR(20) NOT NULL UNIQUE,

    subject_name VARCHAR(150) NOT NULL,

    units DECIMAL(3,1),

    description TEXT,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

);

-- ======================================================
-- TABLE: faculty
-- ======================================================

CREATE TABLE faculty (

    faculty_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT UNIQUE,

    employee_number VARCHAR(20) NOT NULL UNIQUE,

    first_name VARCHAR(100) NOT NULL,

    middle_name VARCHAR(100),

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(100),

    contact_number VARCHAR(20),

    specialization VARCHAR(100),

    employment_status ENUM(
        'Full-Time',
        'Part-Time'
    ) DEFAULT 'Full-Time',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(user_id)

);

-- ======================================================
-- TABLE: students
-- ======================================================

CREATE TABLE students (

    student_id INT AUTO_INCREMENT PRIMARY KEY,

    student_number VARCHAR(20) NOT NULL UNIQUE,

    first_name VARCHAR(100) NOT NULL,

    middle_name VARCHAR(100),

    last_name VARCHAR(100) NOT NULL,

    sex ENUM('Male','Female'),

    birthdate DATE,

    email VARCHAR(100),

    contact_number VARCHAR(20),

    address VARCHAR(255),

    course_id INT NOT NULL,

    section_id INT NOT NULL,

    year_level TINYINT,

    status ENUM(
        'Active',
        'Graduated',
        'Dropped',
        'Inactive'
    ) DEFAULT 'Active',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(course_id)
        REFERENCES courses(course_id),

    FOREIGN KEY(section_id)
        REFERENCES sections(section_id)

);

-- ======================================================
-- TABLE: faculty_subjects
-- ======================================================

CREATE TABLE faculty_subjects (

    assignment_id INT AUTO_INCREMENT PRIMARY KEY,

    faculty_id INT NOT NULL,

    subject_id INT NOT NULL,

    section_id INT NOT NULL,

    term_id INT NOT NULL,

    schedule VARCHAR(100),

    room VARCHAR(50),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(faculty_id)
        REFERENCES faculty(faculty_id),

    FOREIGN KEY(subject_id)
        REFERENCES subjects(subject_id),

    FOREIGN KEY(section_id)
        REFERENCES sections(section_id),

    FOREIGN KEY(term_id)
        REFERENCES academic_terms(term_id)

);

-- ======================================================
-- TABLE: enrollments
-- ======================================================

CREATE TABLE enrollments (

    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,

    student_id INT NOT NULL,

    assignment_id INT NOT NULL,

    enrollment_date DATE,

    status ENUM(
        'Enrolled',
        'Dropped',
        'Completed'
    ) DEFAULT 'Enrolled',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(student_id)
        REFERENCES students(student_id),

    FOREIGN KEY(assignment_id)
        REFERENCES faculty_subjects(assignment_id)

);