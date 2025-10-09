# Running this sample

## Installing dependencies

```sh
pip install "mcp[cli]"
```

## Starting the server

First, create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Start the server by running the following command in the terminal:

```bash
python server.py
```

Now run the client in a separate terminal:

```bash
python client.py
```

You will see an output similar to this:

```text
Starting client...
ID:  None
ID:  3b4a5d8fe27947b094d7792acaca1349
Session initialized, ready to call tools.
Received message: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 1/3:'), jsonrpc='2.0')
NOTIFICATION: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 1/3:'), jsonrpc='2.0')
Received message: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 2/3:'), jsonrpc='2.0')
NOTIFICATION: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 2/3:'), jsonrpc='2.0')
Received message: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 3/3:'), jsonrpc='2.0')
NOTIFICATION: root=LoggingMessageNotification(method='notifications/message', params=LoggingMessageNotificationParams(meta=None, level='info', logger=None, data='Processing file 3/3:'), jsonrpc='2.0')
Tool result: meta=None content=[TextContent(type='text', text="Here's the file content: hello", annotations=None)] isError=False
```

This out shows you all your notifications and the result of the tool call.
