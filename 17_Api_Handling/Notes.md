# Python API Handling — Flow

## Flow

1. **Import library** → `import requests`
2. **Define function** → `fetch_random_user()`
3. **Set API URL** → Store the endpoint in `url`.
4. **Send GET request** → `requests.get(url)`
5. **Parse JSON response** → `response.json()` converts JSON into Python data.
6. **Check response** → Verify `data["success"]` and `"data" in data`.
7. **Extract user data**
   - `data["data"]["data"]` → List of users
   - `user_data[0]` → Select the first user
   - Extract `login.username` and `location.country`
8. **Return values** → `return user_name, user_country`
9. **Call from `main()`** → Receive the returned values and print them.
10. **Handle errors** → `try-except` catches exceptions.
11. **Entry point** → `if __name__ == "__main__":` runs `main()` when the file is executed directly.

## Flowchart

Start  
↓  
Import `requests`  
↓  
Define `fetch_random_user()`  
↓  
Send GET request to API  
↓  
Convert response using `response.json()`  
↓  
Is `success` true and `"data"` present?  
- **Yes** → Extract first user → Get username and country → Return values
- **No** → Raise exception  
↓  
`main()` receives values and prints the result  
↓  
Handle exceptions using `try-except`  
↓  
End

