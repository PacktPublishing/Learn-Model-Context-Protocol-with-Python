# Run sample

## Set up virtual environment

```sh
python -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install "mcp[cli]"
```

## Run the server

```sh
uvicorn server:app
```

## Test the server

```bash
mcp dev server.py
```

