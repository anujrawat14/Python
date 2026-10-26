import sqlite3

con = sqlite3.connect("youtube_video.db")

cursor = con.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS videos (
                                   id INTEGER PRIMARY KEY,
                                   name TEXT NOT NULL,
                                   time TEXT NOT NULL
       )""")
# Triple quotes allow a multi-line SQL query and help preserve its formatting.


def list_all_videos():

    cursor.execute("""
                    SELECT  * FROM videos
             """)

    for row in cursor.fetchall():
        print(row)


def add_video(name, time):

    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)", (name, time))
    con.commit()


def update_video(Id, Name, Time):
    cursor.execute(
        """
                        UPDATE videos SET name = ?,time=? WHERE id = ?   
            """,
        (Name, Time, Id),
    )
    con.commit()


def delete_video(Id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (Id,))
    # Comma makes it a single-element tuple
    con.commit()


def main():
    while True:
        print("\n Youtube Manager with DB | Choose an Options")
        print("1. List a Favorite Video")
        print("2. Add a Youtube video ")
        print("3. Update youtube video details")
        print("4. Delete youtube video ")
        print("5 . Exit The App")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                list_all_videos()

            case "2":
                name = input("Enter Name of video  : ")
                time = input("Enter time of video  : ")
                add_video(name, time)

            case "3":

                list_all_videos()
                Id = int(input("Enter video id : "))

                name = input("Enter Name of updated video   : ")
                time = input("Enter time of updated video  : ")

                update_video(Id, name, time)

            case "4":

                list_all_videos()
                Id = int(input("Enter video id to delete : "))

                delete_video(Id)

            case "5":
                break

            case _:
                print("Invalid Choice")

    con.close()


if __name__ == "__main__":
    try:
        main()
    finally:
        con.close()
