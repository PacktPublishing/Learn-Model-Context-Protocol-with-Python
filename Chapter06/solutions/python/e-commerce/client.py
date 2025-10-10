from mcp import ClientSession, types
from mcp.client.sse import sse_client



async def run():
    async with sse_client(url="http://127.0.0.1:8000/sse") as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

            print("Session initialized")

            # # List available prompts
            # prompts = await session.list_prompts()

            # # Get a prompt
            # prompt = await session.get_prompt(
            #     "example-prompt", arguments={"arg1": "value"}
            # )

            # # List available resources
            # resources = await session.list_resources()

            # List available tools
            tools = await session.list_tools()
            print(tools)

            result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print("Tool result:", result)

            prompts = await session.list_prompts()
            print("Available prompts:", prompts)

            prompt = await session.get_prompt(
                "example-prompt"
            )

            print("Prompt:", prompt)

            # # Read a resource
            # content, mime_type = await session.read_resource("file://some/path")

            # # Call a tool
            # result = await session.call_tool("tool-name", arguments={"arg1": "value"})


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())