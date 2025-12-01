import sqlite3

def fetch_from_datawarehouse():
    conn = sqlite3.connect("warehouse.db") 
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees_dw (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM employees_dw")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO employees_dw VALUES (?, ?, ?)
        """, [
            (101, 'Neel', 'AI Research'),
            (102, 'Meera', 'ML Ops'),
            (103, 'David', 'Analytics')
        ])

    conn.commit()

    cursor.execute("SELECT * FROM employees_dw")
    data = cursor.fetchall()
    conn.close()
    return data


if __name__ == "__main__":
    print("\n--- Local Data Warehouse (SQLite) Data ---")
    for row in fetch_from_datawarehouse():
        print(row)
