# 🛡 Project SENTINEL
### AI-Powered Early Dropout Risk Prediction System

Developed by: **Gieron A. Diwa**

---

# System Requirements

Before running the project, install the following software:

| Software | Version |
|----------|----------|
| Python | 3.12 or newer |
| MySQL Server | 8.x |
| MySQL Workbench | Latest |
| Git | Latest |
| VS Code | Latest |

---

# Required VS Code Extensions

Install these extensions:

- Python
- Pylance
- Jinja
- SQLTools (Optional)
- MySQL

---

# Clone the Repository

Open Command Prompt or PowerShell.

```bash
git clone https://github.com/tsukume1992/AI-DROPOUT-PREDICTOR.git
```

Go inside the project.

```bash
cd AI-DROPOUT-PREDICTOR
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

PowerShell

```powershell
venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
venv\Scripts\activate
```

If successful you should see

```
(venv)
```

---

# Install Python Packages

```bash
pip install -r requirements.txt
```

If requirements.txt does not exist:

```bash
pip install flask
pip install mysql-connector-python
pip install Werkzeug
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib
```

Then create it:

```bash
pip freeze > requirements.txt
```

---

# Create Database

Open MySQL Workbench.

Create database.

```sql
CREATE DATABASE project_sentinel;
```

---

# Import Database

Open

```
database/project_sentinel.sql
```

Execute the SQL script.

Verify these tables exist.

- users
- students
- faculty
- attendance
- assessments
- grades
- courses
- sections
- audit_logs

---

# Configure Database Connection

Open

```
app/database.py
```

Update credentials.

```python
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"
DATABASE = "project_sentinel"
```

---

# Generate Admin Password

Run

```bash
python app/generate_password.py
```

Copy the generated password hash.

Update admin account.

```sql
UPDATE users
SET password_hash='PASTE_HASH_HERE'
WHERE username='admin';
```

---

# Run the Project

```bash
python run.py
```

or

```bash
flask run
```

Open browser.

```
http://127.0.0.1:5000
```

---

# Login

Username

```
admin
```

Password

```
your password
```

---

# Folder Structure

```
AI-DROPOUT-PREDICTOR
│
├── app
│   ├── routes
│   ├── services
│   ├── templates
│   ├── static
│   ├── database.py
│   └── __init__.py
│
├── database
│
├── datasets
│
├── machine_learning
│
├── reports
│
├── tests
│
├── docs
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

---

# Current Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 Authentication | ✅ |
| Sprint 2 Dashboard | ✅ |
| Sprint 3 Database | ✅ |
| Sprint 4 Courses | ✅ |
| Sprint 5 Sections | ✅ |
| Sprint 6 Student Database | ✅ |
| Sprint 7 Student List | ✅ |
| Sprint 8 Student CRUD | ✅ |
| Sprint 9 Student Module v2 | ✅ |
| Sprint 10 Faculty Module | ⏳ |

---

# Backup Procedure

Before every major update:

```bash
git add .
```

```bash
git commit -m "Sprint X"
```

```bash
git push origin main
```

---

# Restore on Another PC

Clone

```bash
git clone https://github.com/tsukume1992/AI-DROPOUT-PREDICTOR.git
```

Activate virtual environment.

```bash
venv\Scripts\activate
```

Install packages.

```bash
pip install -r requirements.txt
```

Import SQL database.

Run

```bash
python run.py
```

Done.

---

# Common Errors

## Module Not Found

```bash
pip install -r requirements.txt
```

---

## Database Connection Error

Verify

- MySQL running
- Username
- Password
- Database name

---

## Port Already Used

Run

```bash
flask run --port=5001
```

---

## Reset Virtual Environment

Delete

```
venv
```

Create again.

```bash
python -m venv venv
```

Activate.

```bash
venv\Scripts\activate
```

Install packages.

```bash
pip install -r requirements.txt
```

---

# Git Commands

Check status

```bash
git status
```

Commit

```bash
git add .
git commit -m "message"
```

Push

```bash
git push origin main
```

Pull

```bash
git pull origin main
```

---

# Version History

## Version 0.9.0

- Authentication
- Dashboard
- Student CRUD
- Search
- Pagination
- Validation
- Toast Notifications
- Audit Trail

---

Developed using

- Python
- Flask
- MySQL
- Bootstrap 5
- Scikit-learn
