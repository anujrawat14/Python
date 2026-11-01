# YouTube Manager — SQLite3 Flow

## 1. Database Setup
- Import `sqlite3`
- Connect to `youtube_video.db`
- Create a cursor
- Create the `videos` table if it doesn't exist

## 2. Main Flow

```text
        START
          |
    Connect to DB
          |
    Create Table
          |
     Display Menu
          |
    Get User Choice
          |
     +----+----+
     |  Choice |
     +----+----+
          |
    +-----+------------------+
    |     |       |     |    |
    1     2       3     4    5
    |     |       |     |    |
  List   Add    Update Delete Exit
    |     |       |     |    |
    +-----+-------+-----+    |
          |                  |
     Show Menu Again    Close DB
                             |
                            END
```

## 3. CRUD Operations

| Operation | SQL Command | Function |
|---|---|---|
| Create | `INSERT` | `add_video()` |
| Read | `SELECT` | `list_all_videos()` |
| Update | `UPDATE` | `update_video()` |
| Delete | `DELETE` | `delete_video()` |

## 4. Important Concepts

- `sqlite3.connect()` — connects to or creates the database.
- `cursor.execute()` — executes SQL queries.
- `?` — placeholder for safely passing values.
- `cursor.fetchall()` — retrieves all result rows.
- `con.commit()` — saves database changes.
- `(Id,)` — single-element tuple used for query parameters.
- `con.close()` — closes the database connection.

## 5. Program Exit

```text
User selects 5
      |
Exit the loop
      |
Close database connection
      |
     END
```
