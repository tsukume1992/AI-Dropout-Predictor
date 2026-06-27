# Project SENTINEL

## Database Normalization

### First Normal Form (1NF)
- All tables store atomic values.
- No repeating groups.
- Each row has a unique primary key.

### Second Normal Form (2NF)
- All non-key attributes depend on the entire primary key.
- Student, Faculty, Course, and Subject information are separated into dedicated tables.

### Third Normal Form (3NF)
- No transitive dependencies exist.
- Foreign keys are used instead of storing duplicate descriptive data.
- The database structure minimizes redundancy and improves integrity.

### Conclusion
The Project SENTINEL database satisfies the requirements of First, Second, and Third Normal Forms (3NF), making it suitable for enterprise deployment and machine learning applications.