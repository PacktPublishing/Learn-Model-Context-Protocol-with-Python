import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

import readline from "node:readline";
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});


import {
  LoggingMessageNotificationSchema,
} from '@modelcontextprotocol/sdk/types.js';


const serverUrl = "http://localhost:8000/mcp";
let sessionId: string | undefined = undefined;

async function checkInput(question:string): Promise<string> {
   return new Promise((resolve) => {
      rl.question(question, response => {
         resolve(response);
      
      });
   });
}


async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      {
         sessionId: sessionId
      }
   );

   const client = new Client({
      name: "example-client",
      version: "1.0.0"
   });

   client.setNotificationHandler(LoggingMessageNotificationSchema, (notification) => {
      console.log(`\nNotification: ${notification.params.level} - ${notification.params.data}`);
      
   });

   await client.connect(transport);
   sessionId = transport.sessionId;
   console.log("Connected to MCP server with session ID:", sessionId);

   while(true) {
      // check for input
      let command = "";
      command = await checkInput("Type command> ");
      if (command === "process-files") {
         // Call the tool with the command
         const result = await client.callTool({
            name: "process-files",
            arguments: {
               message: "Process files"
            }
         });
         console.log(result);
      } else if (command === "exit") {
         console.log("Exiting...");
         break;
      } else {
         console.log("Unknown command. Please use 'process-files' or 'exit'.");
      }
    }
    rl.close();

    console.log("Client disconnected.");
   transport.close();
}

main()
   .then(() => {
      console.log("Client is ready to use.");
   })
   .catch((error) => {
      console.error("Error initializing client:", error);
   })
