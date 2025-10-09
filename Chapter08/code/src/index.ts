import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// Add an addition tool
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => {
    return {
      content: [{ type: "text", text: String(a + b) }]
    };
  }
);

// Start receiving messages on stdin and sending messages on stdout


async function main() {
    console.log("Starting MCP server...");
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

main();
