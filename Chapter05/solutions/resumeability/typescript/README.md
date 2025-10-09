# Run sample

## Client

Connection

```bash
curl -X POST "http://127.0.0.1:8000/mcp" -H "Accept: text/event-stream, application/json" -H "Content-Type: application/json" -d '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": { "protocolVersion": "2025-03-26", "capabilities": { "tools": {}, "logging": {} }, "clientInfo": { "name": "ExampleClient", "version": "1.0.0" } }
}'
```

957f11af-4766-4c1c-a1f2-5bd6776cca6a

Initialize

```bash
curl -X POST "http://127.0.0.1:8000/mcp" -H "Content-Type: application/json" -H "Accept: text/event-stream, application/json" -H "mcp-session-id: 957f11af-4766-4c1c-a1f2-5bd6776cca6a" -d '{
    "jsonrpc": "2.0",
    "method": "notifications/initialized"
}'

```

Call tool

```bash
curl -X POST "http://127.0.0.1:8000/mcp" -H "Content-Type: application/json" -H "Accept: text/event-stream, application/json" -H "mcp-session-id: 957f11af-4766-4c1c-a1f2-5bd6776cca6a" -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "process-files",
      "arguments": { "message": "chris" }
    }
}'
```

Call tool again, but this time with last-event-id d622e4d9-cfda-46e3-b784-3f06d44295de_1757284720093_j27nscp1

```bash
curl "http://127.0.0.1:8000/mcp" -H "Content-Type: application/json" -H "Accept: text/event-stream, application/json" -H "mcp-session-id: 957f11af-4766-4c1c-a1f2-5bd6776cca6a" -H "last-event-id: 3a9d76c3-36d8-45f3-bd6e-8b9c82826de8_1757284976940_meh2n52f"
```
