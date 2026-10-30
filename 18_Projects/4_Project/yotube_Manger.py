from pymongo import MongoClient

url = "mongodb+srv://youtubepy:youtubepy@youtubemanager.exoczgh.mongodb.net/"

client = MongoClient(url)

db = client["YoutubeManager"]

video_collection = db["videos"]  # it will create a video collection

print(video_collection)  # for debugging purpose


def main():
    pass


if __name__ == "__main__":
    main()
