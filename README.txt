# 🏢 Employee Payroll & Attendance Management System

**A database-driven employee management application built with Python, Streamlit and TiDB.**

[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Open_Application-success?style=for-the-badge)](https://employee-payroll-attendance-system-zvtzscqdpx63ohdgvwoaby.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![TiDB](https://img.shields.io/badge/Database-TiDB-4479A1?logo=mysql)
![Status](https://img.shields.io/badge/Status-Deployed-success)

---

## 🌐 Live Demo

🚀 **[Launch Employee Payroll & Attendance Management System](https://employee-payroll-attendance-system-zvtzscqdpx63ohdgvwoaby.streamlit.app/)**

## 📌 Project Overview

The Employee Payroll & Attendance Management System is a web-based application designed to simplify employee administration and management.

It provides a centralized platform to manage employee details, departments, attendance records, salary information and leave requests.

The application is developed using Python and Streamlit, with a MySQL-compatible TiDB database.

## ✨ Key Features

### 📊 Dashboard
- Total employee statistics
- Department statistics
- Attendance and salary record counts
- Leave request statistics
- Employee directory

### 👥 Employee Management
- Add employees
- View employee records
- Update employee information
- Delete employees
- Search employees

### 🏢 Department Management
- Add departments
- View departments
- Update department details
- Delete departments

### 📅 Attendance Management
- Record attendance
- Track present and absent employees
- Update attendance records
- View attendance history

### 💰 Salary Management
- Add salary records
- Manage basic salary
- Record allowances and deductions
- Calculate net salary
- Update and delete salary records

### 📝 Leave Request Management
- Create leave requests
- View leave records
- Update leave status
- Approve or reject requests
- Delete leave records

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Pandas | Data processing |
| MySQL Connector | Database connectivity |
| TiDB Cloud | Cloud database |
| GitHub | Version control |
| Streamlit Community Cloud | Deployment |

## 🗂️ Project Structure

```text
Employee-Payroll-Attendance-System/
│
├── app.py
├── database.py
├── requirements.txt
├── isrgrootx1.pem
├── database/
├── .devcontainer/
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/CodeHub010/Employee-Payroll-Attendance-System.git
```

### 2. Navigate to the project

```bash
cd Employee-Payroll-Attendance-System
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

## 🗄️ Database Design

The application uses the following database tables:

| Table | Description |
|---|---|
| employees | Employee information |
| department | Department details |
| attendance | Attendance records |
| salary_records | Employee salary details |
| leave_requests | Leave information |

Database view:
- `it_employee`

## 🔐 Database Configuration

The cloud application uses TiDB Cloud with SSL-secured connectivity.

Database credentials are configured using Streamlit Secrets.

Example:

```toml
[tidb]
host = "YOUR_TIDB_HOST"
user = "YOUR_TIDB_USERNAME"
password = "YOUR_TIDB_PASSWORD"
```

Never commit actual database passwords or private credentials to GitHub.

## ☁️ Deployment

Deployed using Streamlit Community Cloud.

- GitHub for source code management
- Streamlit Community Cloud for hosting
- TiDB Cloud for database hosting

## 🎯 Project Objectives

- Implement CRUD operations.
- Understand relational database management.
- Integrate Python with SQL databases.
- Build an interactive web application.
- Implement cloud database connectivity.
- Deploy a Python application.

## 🚀 Future Enhancements

- Employee authentication
- Role-based access control
- Automated payroll processing
- Attendance analytics
- Salary slip generation
- Excel and PDF report exports
- Email notifications

## 👨‍💻 Author

**CodeHub010**

GitHub: [@CodeHub010](https://github.com/CodeHub010)

## 📂 Repository

[Employee Payroll & Attendance Management System](https://github.com/CodeHub010/Employee-Payroll-Attendance-System)

---

⭐ If you find this project useful, consider giving it a star!

**Built with ❤️ using Python, Streamlit and TiDB.**
