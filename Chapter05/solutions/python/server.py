# server.py
from mcp.server.fastmcp import FastMCP, Context
from typing import Optional, Dict, Any, List, AsyncGenerator
from mcp.types import (
    LoggingMessageNotificationParams,
    TextContent
)

# Create an MCP server
mcp = FastMCP("Streamable DEMO")

@mcp.tool(description="A simple tool returning file content")
async def echo(message: str, ctx: Context) -> str:

    # ctx2 = mcp.get_context()
    # print(f"Context ID: {ctx2}")

    # await ctx.debug(f"Processing file 1/3: {message}")
    await ctx.info(f"Processing file 1/3:")
    await ctx.info(f"Processing file 2/3:")
    await ctx.info(f"Processing file 3/3:")

    # await ctx.log(
    #         level="info",
    #         message="hello there",
    #         logger_name="Obi Wan",
    #     )

    return f"Here's the file content: {message}"

mcp.run(transport="streamable-http")