# 🏢 Employee Payroll & Attendance Management System

<p align="center">
  A database-driven employee management application built with Python, Streamlit and TiDB.
</p>

<p align="center">
  <a href="https://employee-payroll-attendance-system-zvtzscqdpx63ohdgvwoaby.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_Application-success?style=for-the-badge" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/Database-TiDB-4479A1?logo=mysql" />
  <img src="https://img.shields.io/badge/Status-Deployed-success" />
</p>

---

## 🌐 Live Demo

**Try the application here:**

🔗 [Launch Employee Payroll & Attendance System](YOUR_STREAMLIT_APP_URL)

## 📌 Overview

The Employee Payroll & Attendance Management System is a web-based application designed to manage employee information, departments, attendance records, salary details and leave requests through a centralized dashboard.

Built using Python and Streamlit, the application provides an interactive interface for performing database operations without manually executing SQL queries.

## ✨ Features

| Module | Functionality |
|---|---|
| 📊 Dashboard | Employee and management statistics |
| 👥 Employees | Add, view, update, delete and search employees |
| 🏢 Departments | Manage department information |
| 📅 Attendance | Record and manage employee attendance |
| 💰 Payroll | Manage salaries, allowances and deductions |
| 📝 Leave Requests | Manage employee leave requests |

### Additional Capabilities
- CRUD operations across management modules
- Employee search functionality
- Relational database integration
- Secure database connection using SSL
- Cloud database connectivity through TiDB

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Data Processing:** Pandas
- **Database:** MySQL-compatible TiDB
- **Connectivity:** MySQL Connector/Python

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

## ⚙️ Local Installation

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

### 4. Activate the environment

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

## 🗄️ Database

The application uses the following database tables:

- `employees`
- `department`
- `attendance`
- `salary_records`
- `leave_requests`

It also includes an `it_employee` database view.

Cloud deployment uses TiDB with SSL-secured connectivity.

## ☁️ Deployment

Deployed using **Streamlit Community Cloud**, with GitHub for source code management and TiDB Cloud for database hosting.

## 🎯 Project Objectives

- Understand relational database management.
- Implement CRUD operations using Python and SQL.
- Build an interactive web application.
- Integrate frontend components with a database.
- Practice cloud database connectivity and deployment.

## 🚀 Future Scope

- Employee authentication and role-based access
- Automated monthly payroll generation
- Attendance reports and analytics
- Salary slip generation
- Export reports to Excel and PDF

## 👨‍💻 Author

**CodeHub010**

GitHub: [@CodeHub010](https://github.com/CodeHub010)

**Repository:** [Employee Payroll & Attendance System](https://github.com/CodeHub010/Employee-Payroll-Attendance-System)

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>

<p align="center">
  Built with ❤️ using Python, Streamlit and SQL.
</p>
