EMPLOYEE PAYROLL & ATTENDANCE - INTERACTIVE VERSION
===================================================

This version is adapted to the existing MySQL tables shown in your screenshots:
- department(dept_id, dept_name)
- employees(emp_id, name, salary, dept_id)

It adds:
- attendance
- salary_records
- leave_requests

The app includes add, view, edit and delete operations, search, dashboard counts,
and an in-app MySQL connection form.

1. DATABASE
-----------
The three additional tables have already been created in your database.
Do not run schema.sql again unless you need to recreate a missing table.
The SQL file is included for reference.

2. OPEN IN VS CODE
------------------
Open this extracted folder in VS Code.

3. INSTALL (Windows Command Prompt terminal)
--------------------------------------------
    py -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt

4. RUN
------
    streamlit run app.py

5. CONNECT FROM THE APP
-----------------------
In the left sidebar, enter:
Host: localhost
Port: 3306
Username: root
Password: the password you use for MySQL Workbench
Database: employee_management

Click Connect to MySQL. The password is held in the current Streamlit session
and is not written into the project files.

IMPORTANT
---------
Deleting an employee also deletes their linked attendance, salary and leave
records because the foreign keys use ON DELETE CASCADE. Confirm carefully.
This is a local learning project, not production-secured software.
