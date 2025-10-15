# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add a multiply tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("echo://{message}")
def get_greeting(message: str) -> str:
    """Echo out the message"""
    return f"Resource echo, {message}!"
