# server.py
from itertools import count
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send

import contextlib
import anyio

from collections.abc import AsyncIterator
from typing import Any
import mcp.types as types

from mcp.server.fastmcp import FastMCP, Context
from typing import Optional, Dict, Any, List, AsyncGenerator
from mcp.types import (
    LoggingMessageNotificationParams,
    TextContent
)
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
import logging
import uvicorn

from mcp.server.lowlevel import Server

from event_store import InMemoryEventStore

# set up logging
logger = logging.getLogger(__name__)
# Configure logging
logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# create a store for messages
event_store = InMemoryEventStore()

# Create an MCP server
app = Server("mcp-streamable-http-demo")

# Create the session manager with our app and event store
session_manager = StreamableHTTPSessionManager(
    app=app,
    event_store=event_store,  # Enable resumability
    json_response=True,
)

# ASGI handler for streamable HTTP connections
async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:
    await session_manager.handle_request(scope, receive, send)

@contextlib.asynccontextmanager
async def lifespan(app: Starlette) -> AsyncIterator[None]:
    """Context manager for managing session manager lifecycle."""
    async with session_manager.run():
        logger.info("Application started with StreamableHTTP session manager!")
        try:
            yield
        finally:
            logger.info("Application shutting down...")

files = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
]

# call tool
@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.ContentBlock]:
    ctx = app.request_context
    print("ctx:", ctx)

    no_of_files = len(files)

    # Send the specified number of notifications with the given interval
    for i in range(no_of_files):
        # Include more detailed message for resumability demonstration
        notification_msg = f"[{i + 1}/{no_of_files}] Event from '{files[i]}' - Use Last-Event-ID to resume if disconnected"
        print("ctx log method", ctx.session.send_log_message)
        
        await ctx.session.send_log_message(
            level="info",
            data=notification_msg,
            logger="notification_stream",
            # Associates this notification with the original request
            # Ensures notifications are sent to the correct response stream
            # Without this, notifications will either go to:
            # - a standalone SSE stream (if GET request is supported)
            # - nowhere (if GET request isn't supported)
            related_request_id=ctx.request_id,
        )
        logger.debug(f"Sent notification {i + 1}/{no_of_files}")
        # if i < no_of_files - 1:  # Don't wait after the last notification
        await anyio.sleep(0.1)

    return [
        types.TextContent(
            type="text",
            text=(f"Processed {no_of_files} "),
        )
    ]

# define list tools, what tools we have
@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="process-files",
            description=("Process a number of files"),
            inputSchema={
                "type": "object",
                "required": [],
                "properties": {},
            },
        )
    ]


starlette_app = Starlette(
    debug=True,
    routes=[
        Mount("/mcp", app=handle_streamable_http),
    ],
    lifespan=lifespan,
)

uvicorn.run(starlette_app, host="127.0.0.1", port=3000)