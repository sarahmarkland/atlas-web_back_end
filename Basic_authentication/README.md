# General
## What authentication means
- Basic Authentication provides a simple yet effective way to control access to your API by requiring users to authenticate with a username and password for each request.
## What Base64 is
- Base64 is a binary-to-text encoding scheme that is commonly used to encode binary data, such as images, audio files, or any binary content, into a plain text format. This encoding allows data to be transmitted in a text format that is safe for use in text-based protocols, such as email or HTTP, without the risk of data corruption.
## How to encode a string in Base64
- Encoding a string in Base64 involves converting the characters of the string into their corresponding ASCII values and then encoding those values in Base64 format. Most programming languages provide built-in functions or libraries to easily perform Base64 encoding. Here are examples in Python and JavaScript:

Python:
In Python, you can use the base64 module to encode a string in Base64.

```
import base64

# String to be encoded
original_string = "Hello, World!"

# Encode the string in Base64
encoded_bytes = base64.b64encode(original_string.encode('utf-8'))

# Convert the bytes to a string (optional)
encoded_string = encoded_bytes.decode('utf-8')

print(encoded_string)
```
## What Basic authentication means
## How to send the Authorization header

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
