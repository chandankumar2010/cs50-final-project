import pytest
import sqlite3
from project import input_validation, db_initialization, update_session, export_csv
import os
from datetime import datetime

def test_db_initialization():
    # Test database initialization
    conn = db_initialization()
    assert isinstance(conn, sqlite3.Connection)

def test_update_session():
    # Test session update
    conn = db_initialization()
    update_session(conn, 1, "TestSession")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_number = ?", (1,))
    result = cursor.fetchone()
    assert result is not None

def test_export_csv():
    """
    Test the export_csv function to ensure it creates a CSV file.
    """
    # Initialize the database and add test data
    conn = db_initialization()
    update_session(conn, 1, "Test Tag")
    
    # Call the export_csv function
    export_csv(conn)

    # Check if the CSV file was created
    csv_file = f'pomodoro_report_{datetime.now().strftime("%Y-%m-%d")}.csv'
    assert os.path.exists(csv_file) 

    # Clean up
    os.remove(csv_file)  
    conn.close()
