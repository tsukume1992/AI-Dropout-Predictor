USE project_sentinel;

-- ==========================================
-- INSERT ROLES
-- ==========================================

INSERT INTO roles (role_name, description)
VALUES
('Administrator','Full system access'),
('Faculty','Can manage classes and grades'),
('Guidance Counselor','Can monitor student risk and interventions'),
('Program Chair','Can monitor program reports'),
('Dean','Can view institutional reports');

-- ==========================================
-- INSERT ADMIN USER
-- ==========================================

INSERT INTO users
(
role_id,
username,
password_hash,
first_name,
middle_name,
last_name,
email
)

VALUES
(
1,
'admin',
'admin123',
'System',
NULL,
'Administrator',
'admin@sentinel.edu'
);

-- ==========================================
-- INSERT SAMPLE AUDIT LOG
-- ==========================================

INSERT INTO audit_logs
(
user_id,
action,
module,
table_name,
record_id,
ip_address
)

VALUES
(
1,
'LOGIN',
'Authentication',
'users',
1,
'127.0.0.1'
);