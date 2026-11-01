# MongoDB + PyMongo Notes

A practical reference for using MongoDB with Python. These notes cover
connection, CRUD operations, useful methods, `ObjectId`, query
operators, error handling, and good practices.

## 1. What is MongoDB?

-   **MongoDB** is a NoSQL, document-oriented database.
-   Data is stored as **documents** (BSON, similar to JSON).
-   Documents belong to **collections**.
-   Collections belong to **databases**.

### Basic structure

``` text
MongoDB Server
└── YoutubeManager       # Database
    └── videos           # Collection
        ├── Document 1
        ├── Document 2
        └── Document 3
```

Example document:

``` python
{
    "_id": ObjectId("..."),
    "name": "Python Tutorial",
    "time": "10 min"
}
```

MongoDB automatically creates an `_id` for a document if you do not
provide one.

## 2. Install PyMongo

``` bash
pip install pymongo
```

For MongoDB Atlas connection strings, the standard `mongodb+srv://` URI
is supported by PyMongo.

## 3. Connect to MongoDB

``` python
from pymongo import MongoClient

url = "YOUR_MONGODB_CONNECTION_STRING"

client = MongoClient(url, serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("MongoDB connected!")
except Exception as e:
    print("Connection error:", e)
```

### Access a database and collection

``` python
db = client["YoutubeManager"]
video_collection = db["videos"]
```

  Code                             Meaning
  -------------------------------- --------------------------
  `MongoClient(url)`               Creates a MongoDB client
  `client["YoutubeManager"]`       Accesses a database
  `db["videos"]`                   Accesses a collection
  `client.admin.command("ping")`   Tests connectivity

**Important:** Creating a client object does not prove that the server
is reachable. PyMongo connects lazily; use `ping` to test the
connection.

A database or collection is generally created on the server when data is
first stored, not simply when you access it in Python.

## 4. CRUD operations

CRUD means **Create, Read, Update, Delete**.

Assume this collection:

``` python
video_collection = db["videos"]
```

### A. CREATE --- Insert documents

#### `insert_one()`

Inserts one document.

``` python
video_collection.insert_one({
    "name": "Python Tutorial",
    "time": "10 min"
})
```

Capture the inserted document's ID:

``` python
result = video_collection.insert_one({
    "name": "Python Tutorial",
    "time": "10 min"
})

print(result.inserted_id)
```

#### `insert_many()`

Inserts multiple documents.

``` python
videos = [
    {"name": "Python Basics", "time": "12 min"},
    {"name": "MongoDB Tutorial", "time": "20 min"}
]

result = video_collection.insert_many(videos)
print(result.inserted_ids)
```

### B. READ --- Retrieve documents

#### `find()`

Returns a cursor that can be iterated over. It does not directly return
a list.

``` python
for video in video_collection.find():
    print(video)
```

#### `find_one()`

Returns the first matching document, or `None` if no document matches.

``` python
video = video_collection.find_one({"name": "Python Tutorial"})
print(video)
```

#### Filter documents

``` python
for video in video_collection.find({"name": "Python Tutorial"}):
    print(video)
```

#### Projection --- select fields

The `_id` field is included by default. Set it to `0` to exclude it.

``` python
for video in video_collection.find(
    {},
    {"_id": 0, "name": 1, "time": 1}
):
    print(video)
```

### C. UPDATE --- Modify documents

#### `update_one()`

Updates the first matching document.

``` python
video_collection.update_one(
    {"name": "Python Tutorial"},
    {"$set": {"time": "15 min"}}
)
```

#### `update_many()`

Updates all matching documents.

``` python
video_collection.update_many(
    {"category": "Python"},
    {"$set": {"category": "Programming"}}
)
```

#### `replace_one()`

Replaces the matched document's fields with the supplied replacement
document (while retaining its `_id`).

``` python
video_collection.replace_one(
    {"name": "Old Name"},
    {"name": "New Name", "time": "15 min"}
)
```

**Important:** `update_one()` and `update_many()` normally use update
operators such as `$set`. `replace_one()` takes a replacement document,
not a `$set` update document.

### D. DELETE --- Remove documents

#### `delete_one()`

Deletes the first matching document.

``` python
video_collection.delete_one({"name": "Python Tutorial"})
```

#### `delete_many()`

Deletes all matching documents.

``` python
video_collection.delete_many({"category": "Old"})
```

Be careful: an empty filter `{}` matches every document.

## 5. Important methods and result properties

  Method / property       Purpose
  ----------------------- -------------------------------------
  `insert_one()`          Insert one document
  `insert_many()`         Insert multiple documents
  `find()`                Find matching documents
  `find_one()`            Find one matching document
  `update_one()`          Update one matching document
  `update_many()`         Update all matching documents
  `replace_one()`         Replace one matching document
  `delete_one()`          Delete one matching document
  `delete_many()`         Delete all matching documents
  `count_documents({})`   Count documents matching a filter
  `distinct("name")`      Get distinct values for a field
  `sort()`                Sort cursor results
  `limit()`               Limit cursor results
  `create_index()`        Create an index
  `drop()`                Drop a collection --- use carefully

### Check operation results

``` python
result = video_collection.update_one(
    {"name": "Python Tutorial"},
    {"$set": {"time": "15 min"}}
)

print(result.matched_count)   # Documents that matched
print(result.modified_count)  # Documents actually modified
```

Other useful result properties:

``` python
insert_result.inserted_id
insert_many_result.inserted_ids
delete_result.deleted_count
```

## 6. ObjectId --- very important

MongoDB normally assigns every document a unique `_id` of type
`ObjectId`.

``` python
from bson import ObjectId
```

When an ID is read using `input()`, Python receives a string. Convert it
before querying an `_id` stored as an ObjectId.

``` python
video_id = input("Enter video ID: ").strip()

video_collection.update_one(
    {"_id": ObjectId(video_id)},
    {"$set": {"name": "Updated Name"}}
)
```

### Validate an ID before converting

``` python
from bson import ObjectId

video_id = input("Enter video ID: ").strip()

if ObjectId.is_valid(video_id):
    object_id = ObjectId(video_id)
else:
    print("Invalid MongoDB ID")
```

-   `strip()` removes spaces at the beginning and end.
-   `ObjectId.is_valid()` checks whether the value can be converted to
    an ObjectId.
-   `ObjectId(video_id)` converts a valid string into an ObjectId.

## 7. Useful query operators

Query operators help filter documents.

  ---------------------------------------------------------------------------------------------
  Operator                Meaning                 Example
  ----------------------- ----------------------- ---------------------------------------------
  `$gt`                   Greater than            `{"views": {"$gt": 100}}`

  `$gte`                  Greater than or equal   `{"views": {"$gte": 100}}`

  `$lt`                   Less than               `{"views": {"$lt": 100}}`

  `$lte`                  Less than or equal      `{"views": {"$lte": 100}}`

  `$ne`                   Not equal               `{"category": {"$ne": "Old"}}`

  `$in`                   Matches any value in a  `{"category": {"$in": ["Python", "Java"]}}`
                          list                    
  ---------------------------------------------------------------------------------------------

Example:

``` python
for video in video_collection.find({"views": {"$gt": 100}}):
    print(video)
```

### Update operators

  Operator   Purpose
  ---------- -------------------------------------
  `$set`     Set or change a field
  `$unset`   Remove a field
  `$inc`     Increment a numeric field
  `$push`    Add an item to an array
  `$pull`    Remove matching items from an array

Examples:

``` python
# Change a field
video_collection.update_one(
    {"name": "Python"},
    {"$set": {"time": "20 min"}}
)

# Increment views by 1
video_collection.update_one(
    {"name": "Python"},
    {"$inc": {"views": 1}}
)

# Remove a field
video_collection.update_one(
    {"name": "Python"},
    {"$unset": {"old_field": ""}}
)
```

## 8. Sorting, limiting and counting

``` python
# Sort by name in ascending order (A to Z)
videos = video_collection.find().sort("name", 1)

# Sort by name in descending order (Z to A)
videos = video_collection.find().sort("name", -1)

# Return only the first 5 results
videos = video_collection.find().limit(5)

# Count all documents
total = video_collection.count_documents({})
print(total)
```

Sort direction: - `1` = ascending - `-1` = descending

You can chain cursor operations:

``` python
videos = video_collection.find().sort("name", 1).limit(5)

for video in videos:
    print(video)
```

## 9. Error handling

Common PyMongo exceptions:

  -----------------------------------------------------------------------
  Exception                           Typical reason
  ----------------------------------- -----------------------------------
  `ServerSelectionTimeoutError`       Server unavailable, network, DNS or
                                      configuration issue

  `OperationFailure`                  Authentication or database
                                      operation failure

  `DuplicateKeyError`                 Duplicate value for a unique index

  `InvalidId`                         Invalid ObjectId string
  -----------------------------------------------------------------------

Example:

``` python
from pymongo.errors import PyMongoError
from bson.errors import InvalidId
from bson import ObjectId

try:
    video_id = input("Enter ID: ").strip()
    object_id = ObjectId(video_id)

    result = video_collection.delete_one({"_id": object_id})

    if result.deleted_count:
        print("Video deleted!")
    else:
        print("Video not found!")

except InvalidId:
    print("Invalid video ID")

except PyMongoError as e:
    print("Database error:", e)
```

## 10. Store credentials safely with `.env`

Do not hardcode database usernames and passwords in your Python source
code or upload them to GitHub.

Install:

``` bash
pip install python-dotenv
```

Create a `.env` file:

``` env
MONGO_URL=mongodb+srv://USERNAME:PASSWORD@YOUR_CLUSTER.mongodb.net/
```

Python:

``` python
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

url = os.getenv("MONGO_URL")

if not url:
    raise ValueError("MONGO_URL is missing from .env")

client = MongoClient(url, serverSelectionTimeoutMS=5000)
client.admin.command("ping")
```

Add this to `.gitignore`:

``` gitignore
.env
__pycache__/
```

If your password contains special characters such as `@`, `#`, `/` or
`:`, URL-encode the username and password when constructing the URI.
Prefer the connection string provided by Atlas and encode credentials
correctly.

Never use `tlsAllowInvalidCertificates=True` as a normal connection fix.
It disables certificate verification.

## 11. MongoDB Atlas checklist

When connecting to MongoDB Atlas, check:

1.  **Database Access:** The database username and password must be
    correct.
2.  **Network Access:** Your current IP address must be allowed by the
    Atlas network access rules.
3.  **Connection String:** Use the correct cluster URI and database
    credentials.
4.  **Database Permissions:** The database user must have the required
    read/write permissions.
5.  **Password Encoding:** Special characters in credentials must be
    URL-encoded.
6.  **Connectivity:** Run `client.admin.command("ping")` to test the
    connection.

Never share your connection string publicly. If credentials are exposed,
rotate the database user's password.

## 12. Close the connection

When your application finishes using the client:

``` python
client.close()
```

For a small script, call it when the application exits. In a
long-running application, reuse a client rather than creating a new
client for every database operation.

## 13. Quick revision --- CRUD syntax

``` python
# CREATE
video_collection.insert_one({"name": "Python", "time": "10 min"})

# READ
video_collection.find()

# READ ONE
video_collection.find_one({"name": "Python"})

# UPDATE
video_collection.update_one(
    {"name": "Python"},
    {"$set": {"time": "15 min"}}
)

# DELETE
video_collection.delete_one({"name": "Python"})
```

## 14. Important things to remember

-   MongoDB stores documents inside collections.
-   A collection contains multiple documents.
-   Documents use key-value pairs.
-   MongoDB automatically creates an `_id` if one is not supplied.
-   `find()` returns a cursor, so iterate over it.
-   `find_one()` returns one document or `None`.
-   Use `$set` with `update_one()` and `update_many()`.
-   Convert string IDs to `ObjectId` when querying an ObjectId `_id`.
-   Use `.strip()` to remove accidental spaces from user input.
-   Check `matched_count`, `modified_count` and `deleted_count` to
    verify operations.
-   An empty filter `{}` matches all documents; be careful with bulk
    updates and deletes.
-   Keep database credentials in `.env`, and never commit that file.
-   Test connectivity with `ping`; printing the client object is not a
    connection test.

## 15. Suggested topics to learn next

After CRUD, learn these in order:

1.  Filtering documents with query operators.
2.  Projection, sorting and limiting results.
3.  Update operators such as `$inc`, `$push` and `$pull`.
4.  Indexes and unique constraints.
5.  Aggregation pipeline (`$match`, `$group`, `$sort`, `$project`).
6.  Data validation and schema design.
7.  Connecting MongoDB with Flask or Django.
