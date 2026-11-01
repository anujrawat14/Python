# YouTube Manager — Program Flow

## Flow

```text
START
  |
  v
Load Data from youtube.txt
  |
  v
Display Menu
  |
  v
Take User Choice
  |
  +---- 1. List Videos ------> Display All Videos
  |
  +---- 2. Add Video --------> Get Name & Duration
  |                                |
  |                                v
  |                           Save to JSON File
  |
  +---- 3. Update Video -----> Select Video & Edit Details
  |                                |
  |                                v
  |                           Save to JSON File
  |
  +---- 4. Delete Video -----> Select & Remove Video
  |                                |
  |                                v
  |                           Save to JSON File
  |
  +---- 5. Exit -------------> END
  |
  +---- Invalid Choice ------> Display Error
                                  |
                                  v
                              Display Menu
```

## Key Functions

- `load_data()` — Loads videos from JSON; returns an empty list if the file is missing or invalid.
- `save_data_helper()` — Saves the video list to `youtube.txt`.
- `list_all_videos()` — Displays all saved videos.
- `add_video()` — Adds a new video.
- `update_video()` — Updates video details.
- `delete_video()` — Deletes a video.
- `main()` — Controls the menu and program flow.

## Concepts Used

- Functions
- Lists and dictionaries
- File handling (`open`)
- JSON (`json.load`, `json.dump`)
- Exception handling (`try-except`)
- Loops (`while`)
- Pattern matching (`match-case`)
