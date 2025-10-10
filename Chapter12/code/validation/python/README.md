# Run sample

## Set up

```sh
python -m venv venv
source venv/bin/activate
pip install "mcp[cli]"
```

## Run server

```sh
python server.py
```

## Run client

```sh
npx @modelcontextprotocol/inspector server.py
```

Connect to the server and run the tool `create_user`.

Try the two different tool payloads to see different validation scenarios.

1 Success case (provides all mandatory fields):

   ```json
   {
     "id": 0,
     "name": "chris",
     "email": "chris@example.com"
   }
   ```

2. Validation error (shows that your validation works as we omit the email):

   ```json
   {
     "id": 0,
     "name": "chris"
   }
   ```
