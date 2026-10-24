# with open("youtube.txt","w") as file:
#     file.write("heyy !!")


def list_all_videos(videos):
    pass


def add_video(videos):
    pass


def update_video(videos):
    pass


def delete_video(videos):
    pass


videos = []

while True:

    print("\n Youtube Manager  | Choose an Options")
    print("1. List a Favorite Video")
    print("2. Add a Youtube video ")
    print("3. Update youtube video details")
    print("4. Delete youtube video ")
    print("5 . Exit The App")

    choice = input("Enter Your Choice")

    match choice:
        case "1":
            list_all_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            delete_video(videos)

        case "5":
            pass
        case _:
            print("Invalid Input")
