import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"
import { InMemoryEventStore  } from "./store.js"
import z from "zod";

const port = 8000;

const app = express();
app.use(express.json());

// Map to store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Handle POST requests for client-to-server communication
app.post('/mcp', async (req, res) => {
  // Check for existing session ID
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  const eventStore = new InMemoryEventStore();  

  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Reuse existing transport
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // New initialization request
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      eventStore,
      onsessioninitialized: (sessionId) => {
        // Store the transport by session ID
        console.log("Session Id", sessionId);
        transports[sessionId] = transport;
      }
    });

    // Clean up transport when closed
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    },{ 
      capabilities: { logging: {} }
    });

    let filesToProcess: { name: string, processed: boolean }[] = [
        {
            name: "sales1.csv",
            processed: false
        },
        {
            name: "sales2.csv",
            processed: false
        },
        {
            name: "sales3.csv",
            processed: false
        }
    ];

    server.tool(
        "process-files",
        { message: z.string() },
        async ({ message }, { sendNotification, sessionId }) => {

            let counter = 0;

            for(let file of filesToProcess) {
                if (file.processed) {
                    continue; // Skip already processed files
                }
                counter++;
                await sendNotification({
                    method: "notifications/message",
                    params: { level: "info", data: `${file.name} processed` }
                });
                 await server.sendLoggingMessage({
                    level: "info",
                    data: `Sending first greeting to ${file.name}`
                }, sessionId);

                file.processed = true;
            }

            return {
                content: [{ type: "text", text: `Files processed: ${counter}` }]
            };
        }
    );

    // ... set up server resources, tools, and prompts ...

    // Connect to the MCP server
    await server.connect(transport);
  } else {
    // Invalid request
    res.status(400).json({
      jsonrpc: '2.0',
      error: {
        code: -32000,
        message: 'Bad Request: No valid session ID provided',
      },
      id: null,
    });
    return;
  }

  // Handle the request
  await transport.handleRequest(req, res, req.body);
});

// Reusable handler for GET and DELETE requests
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }

  // Check for Last-Event-ID header for resumability
  const lastEventId = req.headers['last-event-id'] as string | undefined;
  if (lastEventId) {
    console.log(`Client reconnecting with Last-Event-ID: ${lastEventId}`);
  } else {
    console.log(`Establishing new SSE stream for session ${sessionId}`);
  }

  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Handle GET requests for server-to-client notifications via SSE
app.get('/mcp', handleSessionRequest);

// Handle DELETE requests for session termination
app.delete('/mcp', handleSessionRequest);

app.listen(port, () => {
    console.log(`MCP server listening on port ${port}`);
});
