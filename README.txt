
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

Explore the application and its employee management features.

---

## 📌 Project Overview

The **Employee Payroll & Attendance Management System** is a web-based application designed to simplify employee administration and management.

It provides a centralized platform to manage employee details, departments, attendance records, salary information, and leave requests.

The application is developed using Python and Streamlit, with a MySQL-compatible TiDB database for storing and managing information.

---

## ✨ Key Features

### 📊 Dashboard
- Total employee statistics
- Department statistics
- Attendance and salary record counts
- Leave request statistics
- Employee directory

### 👥 Employee Management
- Add new employees
- View employee records
- Update employee information
- Delete employee records
- Search employees

### 🏢 Department Management
- Add departments
- View department details
- Update department information
- Delete departments

### 📅 Attendance Management
- Record employee attendance
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

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend programming |
| Streamlit | Web application interface |
| Pandas | Data processing |
| MySQL Connector | Database connectivity |
| TiDB Cloud | Cloud database |
| GitHub | Version control |
| Streamlit Community Cloud | Application deployment |

---

## 🗂️ Project Structure

```text
Employee-Payroll-Attendance-System/
│
├── app.py
├── database.py
├── requirements.txt
├── isrgrootx1.pem
│
├── database/
│
├── .devcontainer/
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/CodeHub010/Employee-Payroll-Attendance-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Employee-Payroll-Attendance-System
```

### 3. Create a Virtual Environment

```bash
py -m venv venv
```

### 4. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🗄️ Database Design

The application uses a relational database hosted on TiDB Cloud.

### Database Tables

| Table Name | Description |
|---|---|
| `employees` | Stores employee information |
| `department` | Stores department details |
| `attendance` | Maintains employee attendance records |
| `salary_records` | Stores employee salary details |
| `leave_requests` | Maintains employee leave information |

### Database View

- `it_employee`

---

## 🔐 Database Configuration

The application uses TiDB Cloud with SSL-secured database connectivity.

Database credentials are configured through Streamlit Secrets.

Example configuration:

```toml
[tidb]
host = "YOUR_TIDB_HOST"
user = "YOUR_TIDB_USERNAME"
password = "YOUR_TIDB_PASSWORD"
```

**Important:** Never upload actual database credentials, passwords, or private configuration files to GitHub.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

| Platform | Purpose |
|---|---|
| GitHub | Source code hosting |
| Streamlit Community Cloud | Application hosting |
| TiDB Cloud | Cloud database hosting |

---

## 🎯 Project Objectives

- Implement database CRUD operations.
- Understand relational database management.
- Integrate Python with SQL databases.
- Build an interactive web application.
- Implement cloud database connectivity.
- Deploy a Python-based application.

---

## 🚀 Future Enhancements

- Employee authentication
- Role-based access control
- Automated payroll processing
- Attendance analytics
- Salary slip generation
- Excel and PDF report exports
- Email notifications

---

## 👨‍💻 Author

**CodeHub010**

GitHub: [@CodeHub010](https://github.com/CodeHub010)

---

## 📂 Repository

[Employee Payroll & Attendance Management System](https://github.com/CodeHub010/Employee-Payroll-Attendance-System)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with ❤️ using Python, Streamlit and TiDB.**
