# 🏢 Employee Payroll & Attendance Management System

<p align="center">
  A database-driven employee management application built with Python, Streamlit and TiDB.
</p>

<p align="center">
  <a href="YOUR_STREAMLIT_APP_URL">
    <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-Open_Application-success?style=for-the-badge" alt="Live Demo">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Database-TiDB-4479A1?logo=mysql" alt="TiDB">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

---

## 🌐 Live Demo

**Explore the deployed application:**

🔗 [Launch Employee Payroll & Attendance Management System](YOUR_STREAMLIT_APP_URL)

## 📌 Project Overview

The **Employee Payroll & Attendance Management System** is a web-based application designed to simplify employee administration and management.

It provides a centralized platform to manage employee details, departments, attendance records, salary information and leave requests.

The application is developed using Python and Streamlit, with a MySQL-compatible TiDB database for storing and managing information.

## ✨ Key Features

### 📊 Dashboard
- Overview of total employees.
- Department statistics.
- Attendance record counts.
- Salary record counts.
- Leave request statistics.
- Employee directory.

### 👥 Employee Management
- Add new employees.
- View employee records.
- Update employee information.
- Delete employee records.
- Search employees.

### 🏢 Department Management
- Add departments.
- View department information.
- Update department details.
- Delete departments.

### 📅 Attendance Management
- Record employee attendance.
- Track present and absent employees.
- Update attendance records.
- View attendance history.
- Delete attendance records.

### 💰 Salary Management
- Add employee salary records.
- Manage basic salary.
- Record allowances and deductions.
- Calculate net salary.
- Update and delete salary records.

### 📝 Leave Request Management
- Create leave requests.
- View employee leave records.
- Update leave request status.
- Approve or reject requests.
- Delete leave records.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Pandas | Data handling and processing |
| MySQL Connector | Database connectivity |
| MySQL | Relational database compatibility |
| TiDB Cloud | Cloud database hosting |
| GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

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
│
├── .gitignore
└── README.md
```

## 🗄️ Database Design

The application uses a relational database structure.

### Main Tables

| Table | Description |
|---|---|
| `employees` | Stores employee information |
| `department` | Stores department details |
| `attendance` | Stores attendance records |
| `salary_records` | Stores employee salary information |
| `leave_requests` | Stores leave request information |

### Database View

- `it_employee` – Existing database view.

The database uses relational constraints to maintain data consistency between employees and their associated records.

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/CodeHub010/Employee-Payroll-Attendance-System.git
```

### 2. Navigate to the project directory

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

The application will open in your browser.

## 🔐 Database Configuration

The application supports MySQL-compatible database connectivity.

For cloud deployment, the application uses TiDB Cloud with SSL certificate verification.

Database credentials should be configured securely using Streamlit Secrets.

Example configuration:

```toml
[tidb]
host = "YOUR_TIDB_HOST"
user = "YOUR_TIDB_USERNAME"
password = "YOUR_TIDB_PASSWORD"
```

**Security:** Never commit database passwords, private credentials or local secrets files to GitHub.

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment workflow:

1. Maintain the source code in GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select `app.py` as the application entry point.
4. Configure TiDB credentials through Streamlit Secrets.
5. Deploy the application.
6. Access the application using its public URL.

## 🎯 Project Objectives

- Develop a database-driven management application.
- Implement Create, Read, Update and Delete (CRUD) operations.
- Understand relational database management.
- Integrate Python applications with SQL databases.
- Build an interactive web interface using Streamlit.
- Implement cloud database connectivity.
- Deploy a Python application using Streamlit Community Cloud.

## 🚀 Future Enhancements

- Employee login and authentication.
- Role-based access control.
- Automated monthly payroll processing.
- Attendance analytics and reporting.
- Salary slip generation.
- Excel and PDF report exports.
- Email notifications for leave requests.

## 👨‍💻 Author

**CodeHub010**

GitHub: [@CodeHub010](https://github.com/CodeHub010)

## 📂 Repository

[Employee Payroll & Attendance Management System](https://github.com/CodeHub010/Employee-Payroll-Attendance-System)

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>

<p align="center">
  Built with ❤️ using Python, Streamlit and TiDB.
</p>
