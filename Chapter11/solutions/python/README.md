# Run sample

## Configure environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```bash
pip install "mcp[cli]" dotenv PyJWT
```

## Generate token

We will use a simple script to generate a JWT token for testing.

```bash
python util.py
```

This should write a token to `.env` file. The client will use this token to authenticate against the server, through using dotenv to load the token from the `.env` file.

## Start server

```bash
python server.py
```

## Start client

In a separate terminal, run:

```bash
python client.py
```

You should see output similar to:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

If you want to see a scenario where the token is invalid, you can change `util.py` and its payload to generate an invalid token, e.g. change the scopes to something else, like so, i.e to "User.Write" instead of "Admin.Write" that the server expects:

```python
payload = {
        "sub": "1234567890",               # Subject (user ID)
        "name": "User Userson",                # Custom claim
        "admin": True,                     # Custom claim
        "iat": datetime.datetime.utcnow(),# Issued at
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Expiry
        "scopes": ["User.Write"]  # Custom claim for scopes/permissions
    }
```
