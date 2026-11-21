USE employee_management;

-- Existing tables are preserved: department(dept_id, dept_name)
-- and employees(emp_id, name, salary, dept_id).

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present','Absent','Half Day','Leave') NOT NULL,
    remarks VARCHAR(255),
    UNIQUE KEY uq_emp_attendance_date (emp_id, attendance_date),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS salary_records (
    salary_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    salary_month DATE NOT NULL,
    basic_salary DECIMAL(10,2) NOT NULL DEFAULT 0,
    allowance DECIMAL(10,2) NOT NULL DEFAULT 0,
    deduction DECIMAL(10,2) NOT NULL DEFAULT 0,
    UNIQUE KEY uq_emp_salary_month (emp_id, salary_month),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS leave_requests (
    leave_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason VARCHAR(255),
    status ENUM('Pending','Approved','Rejected') NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

SHOW TABLES;
