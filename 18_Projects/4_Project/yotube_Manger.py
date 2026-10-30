from pymongo import MongoClient

url = "mongodb+srv://youtubepy:youtubepy@youtubemanager.exoczgh.mongodb.net/"

client = MongoClient(url)

db = client["YoutubeManager"]

video_collection = db["videos"]  # it will create a video collection

print(video_collection)  # for debugging purpose

# methods used for choices


def list_videos():
    # print(type(video_collection.find())) it return iterable
    for videos in video_collection.find():
        print(f"ID : {videos["_id"]}, name :{videos["id"]} , time : {videos["time"]}")


def Add_Videos(name, time):
    video_collection.collection.insert_one({name: name, time: time})


def update_videos(video_id, up_name, up_time):
    video_collection.update_one(
        {"_id": video_id},
        {"$set ": {"name": up_name, "time": up_time}}
    )


def delete_videos(id):
    pass


def main():

    while True:

        print("\n Youtube Manager with Mongo DB | Choose an Options")
        print("1. List a Favorite Video")
        print("2. Add a Youtube video ")
        print("3. Update youtube video details")
        print("4. Delete youtube video ")
        print("5 . Exit The App")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                list_videos()

            case "2":
                name = input("Enter Name of video : ")
                time = input("Enter duration  of video : ")
                Add_Videos(name, time)

            case "3":
                list_videos()
                video_id = input("Enter id of video to update : ")
                up_name = input("Enter updated Name of video : ")
                up_time = input("Enter updated duration  of video : ")
                update_videos(video_id, up_name, up_time)

            case "4":
                list_videos()
                video_id = input("Enter which video you want to delete : ")
                delete_videos(video_id)

            case "5":
                break

            case _:
                print("Enter  A valid choice ")


if __name__ == "__main__":
    main()
