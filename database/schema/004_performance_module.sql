-- Academic Performance Module

USE project_sentinel;

-- ======================================================
-- TABLE: attendance
-- ======================================================

CREATE TABLE attendance (

    attendance_id INT AUTO_INCREMENT PRIMARY KEY,

    enrollment_id INT NOT NULL,

    attendance_date DATE NOT NULL,

    status ENUM(
        'Present',
        'Absent',
        'Late',
        'Excused'
    ) NOT NULL,

    remarks VARCHAR(255),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(enrollment_id)
        REFERENCES enrollments(enrollment_id)

);

-- ======================================================
-- TABLE: assessments
-- ======================================================

CREATE TABLE assessments (

    assessment_id INT AUTO_INCREMENT PRIMARY KEY,

    assignment_id INT NOT NULL,

    assessment_name VARCHAR(100) NOT NULL,

    assessment_type ENUM(
        'Quiz',
        'Assignment',
        'Activity',
        'Laboratory',
        'Midterm',
        'Final'
    ) NOT NULL,

    total_points DECIMAL(6,2),

    assessment_date DATE,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(assignment_id)
        REFERENCES faculty_subjects(assignment_id)

);

-- ======================================================
-- TABLE: assessment_scores
-- ======================================================

CREATE TABLE assessment_scores (

    score_id INT AUTO_INCREMENT PRIMARY KEY,

    assessment_id INT NOT NULL,

    enrollment_id INT NOT NULL,

    score DECIMAL(6,2) NOT NULL,

    remarks VARCHAR(255),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(assessment_id)
        REFERENCES assessments(assessment_id),

    FOREIGN KEY(enrollment_id)
        REFERENCES enrollments(enrollment_id)

);

-- ======================================================
-- TABLE: grade_summary
-- ======================================================

CREATE TABLE grade_summary (

    grade_id INT AUTO_INCREMENT PRIMARY KEY,

    enrollment_id INT NOT NULL,

    prelim_grade DECIMAL(5,2),

    midterm_grade DECIMAL(5,2),

    prefinal_grade DECIMAL(5,2),

    final_grade DECIMAL(5,2),

    overall_grade DECIMAL(5,2),

    remarks ENUM(
        'Passed',
        'Failed',
        'Incomplete'
    ),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(enrollment_id)
        REFERENCES enrollments(enrollment_id)

);