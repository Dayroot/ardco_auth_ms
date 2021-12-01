# Example of using the ARDCO authentication microservice

This microservice provides a REST API that allows the authentication of a user by means of an access  token, in addition to this, it has the functionalities of adding, consulting, updating and deleting a record belonging to a user.

# REST API
The functionalities of the REST API are described below.

## User sign up

### Request

`POST /user/`

    'Accept: application/json' https://ardco-auth-ms.herokuapp.com/user/
	body: {
		"username": "pepito",
		"fullname": "fulanito",
		"datebirth": "2000-01-22",
		"email": "fulanito@gmail.com",
		"identification": "906209640",
		"phone_number": "3176740235",
		"address": "Av 42 norte Calle 1# 29-12"
		}

### Response

    HTTP/1.1 201 Created
    Date: Sat, 20 Nov 2021 19:18:49 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 33

    {"error": "", "result": "successful creation"}

## User login

### Request

`POST /login/`

    'Accept: application/json' https://ardco-auth-ms.herokuapp.com/login/
	body:{
		"username": "pepito",
		"password": "1234"
	}

### Response

    HTTP/1.1 200 OK
    Date: Sat, 20 Nov 2021 20:02:54 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 505

    {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzUyNDk3NCwiaWF0IjoxNjM3NDM4NTc0LCJqdGkiOiJlODNhM2FlNTliMDA0ZDZkYjk1ZDM3MDQyOTA5OGY3MiIsInVzZXJfaWQiOjF9.Mv3tz6K7zGp1B2WmJaveTJI6A4wrmEXzMzZhmpowckE",
    	"access":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NDQyMTc0LCJpYXQiOjE2Mzc0Mzg1NzQsImp0aSI6ImQ1NmYwYWY0YTcxODQ2NGQ5ZDI3ZDhiZjE4NmMyMDQzIiwidXNlcl9pZCI6MX0.ua3qtgKZeIlyFjculh03axxsdHnGcjZbvCEuYWaRUhc",
    "fullname": "fulanito"
	}

## Verify token access

### Request

`POST /verifyToken/`

     'Accept: application/json' https://ardco-auth-ms.herokuapp.com/verifyToken/
	 body: {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NDQyMTc0LCJpYXQiOjE2Mzc0Mzg1NzQsImp0aSI6ImQ1NmYwYWY0YTcxODQ2NGQ5ZDI3ZDhiZjE4NmMyMDQzIiwidXNlcl9pZCI6MX0.ua3qtgKZeIlyFjculh03axxsdHnGcjZbvCEuYWaRUhc"
	}

### Response

    HTTP/1.1 200 OK
	Date: Sat, 20 Nov 2021 20:09:36 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 12
	
	{"UserId": 1}
	
## Refresh token access

### Request

`POST /refresh/`

     'Accept: application/json' https://ardco-auth-ms.herokuapp.com/refresh/
	 body: {          
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzUyNTk2NiwiaWF0IjoxNjM3NDM5NTY2LCJqdGkiOiI0NWE2ZDY1MDcwNjg0ZmI3ODVjNmJiZDU4NTliMmI2ZiIsInVzZXJfaWQiOjF9.hLsMHl_i8XGMfSpApRJzUMvrn8L5NFYvAhULaC4ECCk"
	}

### Response

    HTTP/1.1 200 OK
	Date: Sat, 20 Nov 2021 20:19:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 241
	
	{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NDQzMTg4LCJpYXQiOjE2Mzc0Mzk1NjYsImp0aSI6ImVhNTcxOTNjZGNjYzQ2OGQ4NmFjNTFmM2Y5Y2NlMWQ2IiwidXNlcl9pZCI6MX0.Q-dgRQK9xCsRKQEItzCC8AVARLzztgHKnsYKDBQGgGg"
	}
	
## Get user data

### Request

`GET /user/id`

     'Accept: application/json' https://ardco-auth-ms.herokuapp.com/user/1

### Response

    HTTP/1.1 200 OK
	Date: Sat, 20 Nov 2021 19:38:28 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 205
	{
	"error": "", 
	"result":
		"id": 1,
		"username": "pepito",
		"fullname": "fulanito",
		"datebirth": "2000-01-22",
		"email": "fulanito@gmail.com",
		"identification": "906209640",
		"phone_number": "3176740235",
		"address": "Av 42 norte Calle 1# 29-12"
	}

## Update user data

### Request

`PUT /user/:id`

    'Accept: application/json' https://ardco-auth-ms.herokuapp.com/user/1
	body: {
		"address": "Av 52 sur Calle 6# 21-18"
	      }

### Response

    HTTP/1.1 200 OK
    Date: Sat, 20 Nov 2021 19:48:55 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 31
    
    {
      	 "error": "", 
	"result":
		"id": 1,
		"username": "pepito",
		"fullname": "fulanito",
		"datebirth": "2000-01-22",
		"email": "fulanito@gmail.com",
		"identification": "906209640",
		"phone_number": "3176740235",
		"address": "Av 52 sur Calle 6# 21-18"
	}

## Delete user data

### Request

`DELETE /user/id`

    'Accept: application/json' https://ardco-auth-ms.herokuapp.com/user/1

### Response

    HTTP/1.1 200 OK
    Date: Sat, 20 Nov 2021 19:52:11 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 33

    {"error": "", "result": "successful deletion"}
