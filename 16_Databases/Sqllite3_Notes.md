# SQLite3 in Python

## 1. Import SQLite3

```python
import sqlite3
```

## 2. Create a Connection

```python
# Creates a connection to the database
# If the database file doesn't exist, it creates one.

con = sqlite3.connect("movies.db")
```

## 3. Create a Cursor

```python
# A cursor is used to execute SQL queries
# and fetch query results.

cur = con.cursor()
```

## 4. Execute SQL Queries

```python
# Create a table
cur.execute("CREATE TABLE movie(title, year, score)")
```

## 5. Fetch Database Information

```python
# Get the names of database tables
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch one row
print(res.fetchone())

# Output: ('movie',)
```

## Flow

```text
import sqlite3
      ↓
Create Connection
      ↓
Create Cursor
      ↓
Execute SQL Query
      ↓
Fetch Results (if needed)
      ↓
Commit Changes (if needed)
      ↓
Close Connection
```

## Important Notes

- **Connection (`con`):** Connects to the database.
- **Cursor (`cur`):** Executes SQL queries and retrieves results.
- **`execute()`:** Executes an SQL statement.
- **`fetchone()`:** Returns the next row as a tuple, or `None` if no row remains.
- **`commit()`:** Saves pending database changes.
- **`close()`:** Closes the database connection.

```python
# Save changes and close the connection
con.commit()
con.close()
```
