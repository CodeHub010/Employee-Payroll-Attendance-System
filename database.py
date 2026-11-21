import mysql.connector
import streamlit as st

def get_connection():
    cfg = st.session_state.get("db_config")
    if not cfg:
        raise RuntimeError("Connect to MySQL using the Database Connection panel in the sidebar.")
    return mysql.connector.connect(
        host=cfg["host"],
        port=int(cfg["port"]),
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"],
    )

def test_connection(host, port, user, password, database):
    return mysql.connector.connect(
        host=host, port=int(port), user=user, password=password, database=database
    )
