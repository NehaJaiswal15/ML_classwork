import mysql.connector

def fetch_from_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*Neha2004*",
        database="data_collection_db"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT emp_id, name, department FROM employees LIMIT 5")
    
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    rows = fetch_from_database()
    print("\n---- Database Data ----")
    for row in rows:
        print(row)
