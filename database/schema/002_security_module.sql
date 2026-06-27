USE project_sentinel;

-- ==========================================
-- TABLE: roles
-- ==========================================

CREATE TABLE roles (

    role_id INT AUTO_INCREMENT PRIMARY KEY,

    role_name VARCHAR(50) NOT NULL UNIQUE,

    description VARCHAR(255),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

);

-- ==========================================
-- TABLE: users
-- ==========================================

CREATE TABLE users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    role_id INT NOT NULL,

    username VARCHAR(50) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    first_name VARCHAR(100) NOT NULL,

    middle_name VARCHAR(100),

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE,

    profile_photo VARCHAR(255),

    status ENUM('Active','Inactive')
        DEFAULT 'Active',

    last_login DATETIME,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (role_id)
        REFERENCES roles(role_id)

);

-- ==========================================
-- TABLE: audit_logs
-- ==========================================

CREATE TABLE audit_logs (

    log_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    action VARCHAR(100) NOT NULL,

    module VARCHAR(100),

    table_name VARCHAR(100),

    record_id INT,

    ip_address VARCHAR(45),

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(user_id)

);