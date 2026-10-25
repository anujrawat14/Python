import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            # return json.load(file)
            test = json.load(file)
            # print(test) #checking purpose
            # print(type(test)) #checking purpose
            return test

    except FileNotFoundError:
        return []

    #if youtube.txt is empty
    except ( json.JSONDecodeError):
        return []


# this method help with adding video to the file


def save_data_helper(videos):

    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


# def list_all_videos(videos):
#     # for index, video in enumerate(videos, start=1):
#     #     print(f"{index}. {video["name"]}  with duration {video["time"]} ")
#     for vid in videos:
#         print(f"{vid}")
#         # {'name': 'CahiAurPython', 'time': '3:15'}
#         # {'name': 'chai aur react', 'time': '4:20'}


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, vid in enumerate(videos, start=1):
        print(f"{index} . {vid["name"]} having  Duartion : {vid["time"]}")
    print("*" * 70)


def add_video(videos):
    name = input("enter video name : ")
    time = input("enter video time : ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to update : "))

    if 1 <= index <= len(videos):
        name = input("enter new video name : ")
        time = input("enter new video time : ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to delete : "))

    if 1 <= index <= len(videos):
        # videos.remove(index-1)
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def main():

    videos = load_data()

    while True:

        print("\n Youtube Manager  | Choose an Options")
        print("1. List a Favorite Video")
        print("2. Add a Youtube video ")
        print("3. Update youtube video details")
        print("4. Delete youtube video ")
        print("5 . Exit The App")

        choice = input("Enter Your Choice : ")

        # print(videos) #check current videos

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
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
