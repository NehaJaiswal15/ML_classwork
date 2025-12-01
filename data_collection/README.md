# Data Collection

This folder contains three independent scripts used to collect data from different sources:

| Source | Script |
|--------|--------|
| MySQL Database | `database.py` |
| SQLite Data Warehouse | `dataWarehouse.py` |
| Experimental Log File | `experimental.py` |

### How to Run

```bash
python database.py        # Fetch data from MySQL
python dataWarehouse.py   # Fetch data from SQLite warehouse
python experimental.py    # Parse experimental logs
