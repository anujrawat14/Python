# with open("youtube.txt","w") as file:
#     file.write("heyy !!")


def list_all_videos(videos):
    pass


def add_video(video):
    pass


def update_video(video):
    pass


def delete_video(video):
    pass


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
            add_video(video)
        case "3":
            update_video(video)
        case "4":
            delete_video(video)

        case "5":
            pass
        case _:
            print("Invalid Input")
