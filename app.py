
import streamlit as st
import pandas as pd
import mysql.connector
from pathlib import Path

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Employee Management System",
    page_icon="🏢",
    layout="wide"
)

# =====================================================
# TIDB CLOUD CONNECTION
# =====================================================

CA_CERTIFICATE = Path(__file__).parent / "isrgrootx1.pem"


def load_database_config():
    try:
        secrets = st.secrets["tidb"]

        return {
            "host": secrets["host"],
            "port": 4000,
            "user": secrets["user"],
            "password": secrets["password"],
            "database": "employee_management",
            "ssl_ca": str(CA_CERTIFICATE),
            "ssl_verify_cert": True,
            "ssl_verify_identity": True
        }

    except (KeyError, FileNotFoundError):
        return None

    except Exception as e:
        st.error(f"Unable to load database secrets: {e}")
        return None


if "db_config" not in st.session_state:
    st.session_state.db_config = load_database_config()


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🏢 Employee Manager")
    st.subheader("Database Connection")

    if st.session_state.db_config:

        if CA_CERTIFICATE.exists():
            st.success("TiDB credentials loaded")
        else:
            st.error("CA certificate is missing from repository")

        if st.button("Disconnect"):
            st.session_state.db_config = None
            st.rerun()

    else:
        st.error("Database credentials not configured")
        st.caption("Configure [tidb] in Streamlit Cloud Secrets.")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Employees",
            "Departments",
            "Attendance",
            "Salary",
            "Leave Requests"
        ]
    )


# =====================================================
# DATABASE HELPER FUNCTIONS
# =====================================================

def get_connection():

    if not st.session_state.db_config:
        raise RuntimeError("TiDB connection is not configured.")

    if not CA_CERTIFICATE.exists():
        raise FileNotFoundError(
            f"CA certificate not found: {CA_CERTIFICATE}"
        )

    return mysql.connector.connect(
        **st.session_state.db_config
    )


def read(sql, params=()):

    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(sql, params)

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        return pd.DataFrame(rows, columns=columns)

    finally:
        connection.close()


def execute(sql, params=()):

    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()

        return cursor.rowcount

    finally:
        connection.close()


def get_employees():

    return read("""
        SELECT emp_id, name
        FROM employees
        ORDER BY name
    """)


def get_departments():

    return read("""
        SELECT dept_id, dept_name
        FROM department
        ORDER BY dept_name
    """)


# =====================================================
# MAIN TITLE
# =====================================================

st.title("Employee Payroll & Attendance Management")


# =====================================================
# DASHBOARD
# =====================================================

def dashboard():

    st.header("Dashboard")

    data = [
        ("Total Employees", "SELECT COUNT(*) FROM employees"),
        ("Departments", "SELECT COUNT(*) FROM department"),
        ("Attendance Records", "SELECT COUNT(*) FROM attendance"),
        ("Salary Records", "SELECT COUNT(*) FROM salary_records"),
        ("Leave Requests", "SELECT COUNT(*) FROM leave_requests")
    ]

    columns = st.columns(5)

    for column, (label, sql) in zip(columns, data):

        result = read(sql)
        count = result.iloc[0, 0]

        column.metric(label, count)

    st.divider()

    st.subheader("Employee Directory")

    search = st.text_input(
        "Search employee by name",
        key="dashboard_search"
    )

    if search:

        df = read("""
            SELECT
                e.emp_id,
                e.name,
                e.salary,
                d.dept_name
            FROM employees e
            LEFT JOIN department d
                ON e.dept_id = d.dept_id
            WHERE e.name LIKE %s
            ORDER BY e.emp_id
        """, (f"%{search}%",))

    else:

        df = read("""
            SELECT
                e.emp_id,
                e.name,
                e.salary,
                d.dept_name
            FROM employees e
            LEFT JOIN department d
                ON e.dept_id = d.dept_id
            ORDER BY e.emp_id
        """)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# EMPLOYEE MANAGEMENT
# =====================================================

def employees():

    st.header("Employee Management")

    departments_df = get_departments()

    with st.expander("➕ Add New Employee"):

        if departments_df.empty:

            st.warning("Add a department first.")

        else:

            with st.form("add_employee"):

                name = st.text_input("Employee Name")

                salary = st.number_input(
                    "Monthly Salary",
                    min_value=0.0
                )

                dept = st.selectbox(
                    "Department",
                    departments_df["dept_id"].tolist(),
                    format_func=lambda x: departments_df.loc[
                        departments_df["dept_id"] == x,
                        "dept_name"
                    ].iloc[0]
                )

                submitted = st.form_submit_button("Add Employee")

                if submitted:

                    if name.strip():

                        execute("""
                            INSERT INTO employees
                                (name, salary, dept_id)
                            VALUES (%s, %s, %s)
                        """, (
                            name.strip(),
                            salary,
                            int(dept)
                        ))

                        st.success("Employee added successfully!")
                        st.rerun()

                    else:
                        st.error("Enter employee name.")

    st.subheader("All Employees")

    search = st.text_input(
        "Search employees",
        key="employee_search"
    )

    if search:

        df = read("""
            SELECT
                e.emp_id,
                e.name,
                e.salary,
                d.dept_name
            FROM employees e
            LEFT JOIN department d
                ON e.dept_id = d.dept_id
            WHERE e.name LIKE %s
            ORDER BY e.emp_id
        """, (f"%{search}%",))

    else:

        df = read("""
            SELECT
                e.emp_id,
                e.name,
                e.salary,
                d.dept_name
            FROM employees e
            LEFT JOIN department d
                ON e.dept_id = d.dept_id
            ORDER BY e.emp_id
        """)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    all_employees = read("""
        SELECT emp_id, name, salary, dept_id
        FROM employees
        ORDER BY emp_id
    """)

    if not all_employees.empty:

        st.subheader("Edit / Delete Employee")

        emp_id = st.selectbox(
            "Select Employee",
            all_employees["emp_id"].tolist(),
            format_func=lambda x: (
                f"{x} - "
                f"{all_employees.loc[all_employees.emp_id == x, 'name'].iloc[0]}"
            )
        )

        row = all_employees.loc[
            all_employees["emp_id"] == emp_id
        ].iloc[0]

        if not departments_df.empty:

            dept_ids = departments_df["dept_id"].tolist()

            current_dept = (
                int(row["dept_id"])
                if pd.notna(row["dept_id"])
                and int(row["dept_id"]) in dept_ids
                else dept_ids[0]
            )

            with st.form("edit_employee"):

                new_name = st.text_input(
                    "Name",
                    str(row["name"])
                )

                new_salary = st.number_input(
                    "Monthly Salary",
                    min_value=0.0,
                    value=float(row["salary"] or 0)
                )

                new_dept = st.selectbox(
                    "Department",
                    dept_ids,
                    index=dept_ids.index(current_dept),
                    format_func=lambda x: departments_df.loc[
                        departments_df["dept_id"] == x,
                        "dept_name"
                    ].iloc[0]
                )

                submitted = st.form_submit_button("Update Employee")

                if submitted:

                    if new_name.strip():

                        execute("""
                            UPDATE employees
                            SET name=%s,
                                salary=%s,
                                dept_id=%s
                            WHERE emp_id=%s
                        """, (
                            new_name.strip(),
                            new_salary,
                            int(new_dept),
                            int(emp_id)
                        ))

                        st.success("Employee updated!")
                        st.rerun()

                    else:
                        st.error("Employee name cannot be empty.")

        confirm = st.checkbox(
            "Confirm employee deletion",
            key="delete_employee_confirm"
        )

        if st.button(
            "Delete Employee",
            disabled=not confirm
        ):

            try:

                execute(
                    "DELETE FROM employees WHERE emp_id=%s",
                    (int(emp_id),)
                )

                st.success("Employee deleted!")
                st.rerun()

            except mysql.connector.Error as e:

                st.error(f"Unable to delete employee: {e}")


# =====================================================
# DEPARTMENT MANAGEMENT
# =====================================================

def departments():

    st.header("Department Management")

    with st.form("add_department"):

        name = st.text_input("Department Name")

        submitted = st.form_submit_button("Add Department")

        if submitted:

            if name.strip():

                execute("""
                    INSERT INTO department (dept_name)
                    VALUES (%s)
                """, (name.strip(),))

                st.success("Department added!")
                st.rerun()

            else:
                st.error("Enter department name.")

    df = get_departments()

    st.subheader("All Departments")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    if not df.empty:

        dept_id = st.selectbox(
            "Select Department",
            df["dept_id"].tolist(),
            format_func=lambda x: (
                f"{x} - "
                f"{df.loc[df.dept_id == x, 'dept_name'].iloc[0]}"
            )
        )

        current = df.loc[
            df["dept_id"] == dept_id,
            "dept_name"
        ].iloc[0]

        new_name = st.text_input(
            "Edit Department Name",
            current
        )

        col1, col2 = st.columns(2)

        if col1.button("Update Department"):

            if new_name.strip():

                execute("""
                    UPDATE department
                    SET dept_name=%s
                    WHERE dept_id=%s
                """, (
                    new_name.strip(),
                    int(dept_id)
                ))

                st.success("Department updated!")
                st.rerun()

            else:
                st.error("Department name cannot be empty.")

        if col2.button("Delete Department"):

            try:

                execute("""
                    DELETE FROM department
                    WHERE dept_id=%s
                """, (int(dept_id),))

                st.success("Department deleted!")
                st.rerun()

            except mysql.connector.Error:

                st.error(
                    "This department is assigned to employees. "
                    "Reassign them first."
                )


# =====================================================
# ATTENDANCE MANAGEMENT
# =====================================================

def attendance():

    st.header("Attendance Management")

    employees_list = get_employees()

    if employees_list.empty:

        st.warning("Add employees first.")
        return

    with st.form("attendance_form"):

        emp = st.selectbox(
            "Employee",
            employees_list["emp_id"].tolist(),
            format_func=lambda x: employees_list.loc[
                employees_list["emp_id"] == x,
                "name"
            ].iloc[0]
        )

        day = st.date_input("Attendance Date")

        status = st.selectbox(
            "Status",
            ["Present", "Absent", "Half Day", "Leave"]
        )

        remarks = st.text_input("Remarks")

        submitted = st.form_submit_button("Save Attendance")

        if submitted:

            execute("""
                INSERT INTO attendance
                    (emp_id, attendance_date, status, remarks)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    status=VALUES(status),
                    remarks=VALUES(remarks)
            """, (
                int(emp),
                day,
                status,
                remarks.strip() or None
            ))

            st.success("Attendance saved!")
            st.rerun()

    st.subheader("Attendance Records")

    df = read("""
        SELECT
            a.attendance_id,
            e.name,
            a.attendance_date,
            a.status,
            a.remarks
        FROM attendance a
        JOIN employees e
            ON a.emp_id = e.emp_id
        ORDER BY a.attendance_date DESC
    """)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    ids = read("""
        SELECT attendance_id
        FROM attendance
        ORDER BY attendance_id
    """)

    if not ids.empty:

        aid = st.selectbox(
            "Select Attendance ID",
            ids["attendance_id"].tolist()
        )

        row = read("""
            SELECT *
            FROM attendance
            WHERE attendance_id=%s
        """, (int(aid),)).iloc[0]

        with st.form("edit_attendance"):

            statuses = [
                "Present",
                "Absent",
                "Half Day",
                "Leave"
            ]

            new_status = st.selectbox(
                "Edit Status",
                statuses,
                index=statuses.index(row["status"])
            )

            new_remarks = st.text_input(
                "Edit Remarks",
                row["remarks"] or ""
            )

            submitted = st.form_submit_button("Update Attendance")

            if submitted:

                execute("""
                    UPDATE attendance
                    SET status=%s,
                        remarks=%s
                    WHERE attendance_id=%s
                """, (
                    new_status,
                    new_remarks,
                    int(aid)
                ))

                st.success("Attendance updated!")
                st.rerun()

        confirm = st.checkbox(
            "Confirm attendance deletion",
            key="delete_attendance_confirm"
        )

        if st.button(
            "Delete Attendance",
            disabled=not confirm
        ):

            execute("""
                DELETE FROM attendance
                WHERE attendance_id=%s
            """, (int(aid),))

            st.success("Attendance deleted!")
            st.rerun()


# =====================================================
# SALARY MANAGEMENT
# =====================================================

def salary():

    st.header("Salary Management")

    employees_list = get_employees()

    if employees_list.empty:

        st.warning("Add employees first.")
        return

    with st.form("salary_form"):

        emp = st.selectbox(
            "Employee",
            employees_list["emp_id"].tolist(),
            format_func=lambda x: employees_list.loc[
                employees_list["emp_id"] == x,
                "name"
            ].iloc[0]
        )

        month = st.date_input("Salary Month")

        basic = st.number_input(
            "Basic Salary",
            min_value=0.0
        )

        allowance = st.number_input(
            "Allowance",
            min_value=0.0
        )

        deduction = st.number_input(
            "Deduction",
            min_value=0.0
        )

        submitted = st.form_submit_button("Save Salary")

        if submitted:

            execute("""
                INSERT INTO salary_records
                    (emp_id, salary_month, basic_salary, allowance, deduction)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    basic_salary=VALUES(basic_salary),
                    allowance=VALUES(allowance),
                    deduction=VALUES(deduction)
            """, (
                int(emp),
                month.replace(day=1),
                basic,
                allowance,
                deduction
            ))

            st.success("Salary saved!")
            st.rerun()

    st.subheader("Salary Records")

    df = read("""
        SELECT
            s.salary_id,
            e.name,
            s.salary_month,
            s.basic_salary,
            s.allowance,
            s.deduction,
            (
                s.basic_salary
                + s.allowance
                - s.deduction
            ) AS net_salary
        FROM salary_records s
        JOIN employees e
            ON s.emp_id = e.emp_id
        ORDER BY s.salary_month DESC
    """)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    ids = read("""
        SELECT salary_id
        FROM salary_records
        ORDER BY salary_id
    """)

    if not ids.empty:

        sid = st.selectbox(
            "Select Salary Record",
            ids["salary_id"].tolist()
        )

        row = read("""
            SELECT *
            FROM salary_records
            WHERE salary_id=%s
        """, (int(sid),)).iloc[0]

        with st.form("edit_salary"):

            basic = st.number_input(
                "Edit Basic Salary",
                min_value=0.0,
                value=float(row["basic_salary"])
            )

            allowance = st.number_input(
                "Edit Allowance",
                min_value=0.0,
                value=float(row["allowance"])
            )

            deduction = st.number_input(
                "Edit Deduction",
                min_value=0.0,
                value=float(row["deduction"])
            )

            submitted = st.form_submit_button("Update Salary")

            if submitted:

                execute("""
                    UPDATE salary_records
                    SET basic_salary=%s,
                        allowance=%s,
                        deduction=%s
                    WHERE salary_id=%s
                """, (
                    basic,
                    allowance,
                    deduction,
                    int(sid)
                ))

                st.success("Salary updated!")
                st.rerun()

        confirm = st.checkbox(
            "Confirm salary deletion",
            key="delete_salary_confirm"
        )

        if st.button(
            "Delete Salary",
            disabled=not confirm
        ):

            execute("""
                DELETE FROM salary_records
                WHERE salary_id=%s
            """, (int(sid),))

            st.success("Salary record deleted!")
            st.rerun()


# =====================================================
# LEAVE REQUEST MANAGEMENT
# =====================================================

def leave_requests():

    st.header("Leave Requests")

    employees_list = get_employees()

    if employees_list.empty:

        st.warning("Add employees first.")
        return

    with st.form("leave_form"):

        emp = st.selectbox(
            "Employee",
            employees_list["emp_id"].tolist(),
            format_func=lambda x: employees_list.loc[
                employees_list["emp_id"] == x,
                "name"
            ].iloc[0]
        )

        start = st.date_input("Start Date")

        end = st.date_input("End Date")

        reason = st.text_input("Reason")

        status = st.selectbox(
            "Status",
            ["Pending", "Approved", "Rejected"]
        )

        submitted = st.form_submit_button("Add Leave Request")

        if submitted:

            if end < start:

                st.error("End date cannot be before start date.")

            else:

                execute("""
                    INSERT INTO leave_requests
                        (emp_id, start_date, end_date, reason, status)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    int(emp),
                    start,
                    end,
                    reason,
                    status
                ))

                st.success("Leave request added!")
                st.rerun()

    st.subheader("All Leave Requests")

    df = read("""
        SELECT
            l.leave_id,
            e.name,
            l.start_date,
            l.end_date,
            l.reason,
            l.status
        FROM leave_requests l
        JOIN employees e
            ON l.emp_id = e.emp_id
        ORDER BY l.leave_id DESC
    """)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    ids = read("""
        SELECT leave_id
        FROM leave_requests
        ORDER BY leave_id
    """)

    if not ids.empty:

        lid = st.selectbox(
            "Select Leave Request",
            ids["leave_id"].tolist()
        )

        current = read("""
            SELECT status
            FROM leave_requests
            WHERE leave_id=%s
        """, (int(lid),)).iloc[0, 0]

        statuses = [
            "Pending",
            "Approved",
            "Rejected"
        ]

        status = st.selectbox(
            "Change Status",
            statuses,
            index=statuses.index(current)
        )

        col1, col2 = st.columns(2)

        if col1.button("Update Leave Status"):

            execute("""
                UPDATE leave_requests
                SET status=%s
                WHERE leave_id=%s
            """, (
                status,
                int(lid)
            ))

            st.success("Leave status updated!")
            st.rerun()

        confirm = col2.checkbox(
            "Confirm deletion",
            key="delete_leave_confirm"
        )

        if col2.button(
            "Delete Leave Request",
            disabled=not confirm
        ):

            execute("""
                DELETE FROM leave_requests
                WHERE leave_id=%s
            """, (int(lid),))

            st.success("Leave request deleted!")
            st.rerun()


# =====================================================
# PAGE ROUTING
# =====================================================

if not st.session_state.db_config:

    st.info(
        "Configure your TiDB credentials in Streamlit Cloud Secrets."
    )

else:

    try:

        if page == "Dashboard":
            dashboard()

        elif page == "Employees":
            employees()

        elif page == "Departments":
            departments()

        elif page == "Attendance":
            attendance()

        elif page == "Salary":
            salary()

        elif page == "Leave Requests":
            leave_requests()

    except Exception as e:

        st.error(f"Application error: {e}")
