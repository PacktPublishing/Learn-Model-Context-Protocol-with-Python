# Run sample

## Set up virtual environment

```bash
python -m venv venv
```

activate virtual environment:

```bash
source venv/bin/activate
```

or on Windows type:

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
pip install "mcp[cli]"
```

## Run code

```bash
mcp run server.py
```

## Run inspector

```bash
mcp dev server.py
```

You should see a web interface open up. Ensure you select:

- transport with value "stdio":
- command: **mcp**
- arguments: **run server.py**

Then select the "Connect" button.
