# RESTful API - Task 1: Consume data from an API using command line tools (curl)

This document explains how to use `curl` to perform various HTTP requests (GET, HEAD, POST)  
on a public RESTful API, observe HTTP headers, send data with POST, and interpret API responses.

---

## Tools used

- `curl`: command-line tool to interact with network servers (HTTP/HTTPS protocols, etc.).
- `jq`: command-line tool to format and color JSON responses (optional but very practical).

---

## Commands executed in this task

| Command | Description |
|---------|-------------|
| `curl --version` | Check if `curl` is installed and list supported protocols. |
| `curl https://jsonplaceholder.typicode.com/posts` | Perform a GET request to the API to retrieve posts. |
| `curl https://jsonplaceholder.typicode.com/posts \| jq` | Perform the same GET request but format and color the JSON with `jq`. |
| `curl -I https://jsonplaceholder.typicode.com/posts` | Perform a HEAD request (using `-I`) to retrieve only HTTP headers. |
| `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts` | Perform a simulated POST request with data sent to the server. |

---

## Step 1: Installation and verification of curl

### Installing `curl`

Curl was installed on WSL with:

```bash
sudo apt update
sudo apt install curl
```

### Verifying installation

Command executed:

```bash
curl --version
```

Response obtained:

```plaintext
curl 8.5.0 (x86_64-pc-linux-gnu) ...
Protocols: dict file ftp ftps gopher http https ...
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 ...
```

✅ `curl` is correctly installed and ready to use.

---

## Step 2: Consuming data from the API JSONPlaceholder

### Simple GET request

Command executed:

```bash
curl https://jsonplaceholder.typicode.com/posts
```

Response obtained:

- JSON data containing a list of posts.
- Each post contains: `userId`, `id`, `title`, `body`.

### GET request with JSON formatting (`jq`)

Command executed:

```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```

Response obtained (formatted):

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit ..."
  },
  ...
]
```

<p align="center">
  <img src="images/curl-jq.png" width="1000" />
</p>

✅ Response correctly formatted with `jq`.  
✅ Clear visibility of fields: `userId`, `id`, `title`, `body`.

---

## Step 3: Using headers and POST with curl

### Step 3.1: Retrieve only headers (HEAD request)

Command executed:

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

Response obtained:

```plaintext
HTTP/2 200
date: Mon, 09 Jun 2025 08:52:28 GMT
content-type: application/json; charset=utf-8
server: cloudflare
...
x-powered-by: Express
cache-control: max-age=43200
etag: ...
```

<p align="center">
  <img src="images/curl-i.png" width="1000" />
</p>

✅ Status code 200 OK.  
✅ Content-Type confirms JSON data.  
✅ Cache-Control, Server, and various additional headers observed.

---

### Step 3.2: Perform a POST request with data

Command executed:

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Response obtained:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

<p align="center">
  <img src="images/curl_post.png" width="1000" />
</p>

✅ Simulated POST request successful.  
✅ The server returns a created post with ID 101 (simulation — the API does not persist data).

---

## Conclusion

- The `curl` tool allows you to easily test and interact with REST APIs from the command line.
- The `jq` tool is very useful for making JSON responses more readable.
- With `curl`, it is possible to:
  - Check server availability (`-I`)
  - Retrieve data (`GET`)
  - Send data (`POST`)
  - Inspect HTTP headers.
- Mastering `curl` is essential for quickly testing endpoints in RESTful API development.

---
