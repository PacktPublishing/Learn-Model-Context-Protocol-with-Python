# Run sample

## Set up environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Start server

```sh
uvicorn server:app --port 3000
```

## Run client

In a different terminal, run the following command:

```sh
python client.py
```

You should see output similar to:

```text
Available tools: ['book_trip']
[CLIENT] Received elicitation data: Not a member? Would you like to sign up?
[CLIENT]: Selecting alternative date: 2025-01-01
Result:  [BOOKED] Booked for 2025-01-02, welcome chris as a member!
````
