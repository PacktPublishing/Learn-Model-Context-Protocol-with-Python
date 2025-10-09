# Running this sample

There are two types of streaming servers available in this sample:

- SSE (Server-Sent Events)
- Streaming HTTP

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the virtual environment

**On Windows**

```bash
.\venv\Scripts\activate
```

**On macOS/Linux**


```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install Flask requests
```

## Run the SSE sample

Start the server:

```bash
python sse.py
```

Here's what you should see in the server console once the client is connected:

```text
HTTP streaming server running on port 8000
Starting SSE server on port 8000...
```

In a separate terminal, start the client:

```bash
python sse_client.py 
```

You should see output similar to this in the client console:

```text
Received SSE: data: Sun Jun  1 18:48:42 2025
Received SSE: data: Sun Jun  1 18:48:43 2025
Received SSE: data: Sun Jun  1 18:48:44 2025
Received SSE: data: Sun Jun  1 18:48:45 2025
Received SSE: data: Sun Jun  1 18:48:46 2025
Received SSE: data: 5 messages sent, closing connection.
```

## Run the Streaming HTTP sample

Start the server:

```bash
python streaming_http_server.py
```

Here's what you should see in the server console once the client is connected:

```text
Streaming HTTP server running on port 8000
Streaming HTTP connection established
```

In a separate terminal, start the client:

```bash
python streaming_http_client.py
```
You should see output similar to this in the client console:

```text
2025-06-01T15:10:43.193Z
2025-06-01T15:10:44.197Z
2025-06-01T15:10:45.205Z
2025-06-01T15:10:46.209Z
2025-06-01T15:10:47.211Z
```
