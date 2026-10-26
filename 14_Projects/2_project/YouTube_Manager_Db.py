import sqlite3

con = sqlite3.connect("youtube_video.db")

cursor = con.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXIST videos (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                time TEXT NOT NULL
    )
""")
# using 3 string format because it save formatting
