from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
import json
from typing import Optional, Dict, Any, List
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream

from typing import AsyncGenerator

import mcp.types as types

from mcp.types import (
    LoggingMessageNotificationParams,
    TextContent,
)

from mcp.shared.session import RequestResponder

class LoggingCollector:
    def __init__(self):
        self.log_messages: list[LoggingMessageNotificationParams] = []

    async def __call__(self, params: LoggingMessageNotificationParams) -> None:
        self.log_messages.append(params)

logging_collector = LoggingCollector()

port = 3000

# I get normal messages, notifications, and exceptions
async def message_handler(
        message: RequestResponder[types.ServerRequest, types.ClientResult]
        | types.ServerNotification
        | Exception,
    ) -> None:
        print("Received message:", message)
        if isinstance(message, Exception):
            raise message
        else:
            if isinstance(message, types.ServerNotification):
                print("NOTIFICATION:", message)
            elif isinstance(message, RequestResponder):
                print("REQUEST_RESPONDER:", message)
            else:
                print("SERVER_REQUEST:", message)

async def main():
    print("Starting client...")
    # Connect to a streamable HTTP server
    async with streamablehttp_client(f"http://localhost:{port}/mcp") as (
        read_stream,
        write_stream,
        session_callback,
    ): 
        # Create a session using the client streams
        async with ClientSession(
            read_stream, 
            write_stream,
            logging_callback=logging_collector,
            message_handler=message_handler,
        ) as session:

            # not initialized, should be None
            id = session_callback()
            print("ID: ", id)

            # Initialize the connection
            await session.initialize()

            id = session_callback()
            print("ID: ", id)

            print("Session initialized, ready to call tools.")
          
            # Call a tool
            results = []
            tool_result = await session.call_tool("process_files", {})

            gen = None
            # If the tool_result is an async generator, print its items

            # Convert tool_result.text to an AsyncGenerator if it's awaitable or async iterable
           
            print("Tool result:", tool_result)
            # log = logging_collector.log_messages[0]
            # print("Log message:", log)

            


asyncio.run(main())