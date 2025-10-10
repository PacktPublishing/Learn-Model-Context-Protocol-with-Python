class DummyStream:
    async def read(self): pass
    async def write(self, data): pass

class DummyClientSession:
    def __init__(self, read_stream, write_stream):
        self.read_stream = read_stream
        self.write_stream = write_stream

    async def __aenter__(self):
        print("Session started")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Session closed")

    async def initialize(self):
        print("Initializing session...")

    async def list_tools(self):
        class Tool:
            def __init__(self, name): self.name = name
        return type("ToolList", (), {"tools": [Tool("ToolA"), Tool("ToolB")]})()

async def streamablehttp_client(url):
    print(f"Connecting to {url}")
    return DummyStream(), DummyStream(), None

# Main async function
async def main():
    read_stream, write_stream, _ = await streamablehttp_client("http://localhost:8000/mcp")
    async with DummyClientSession(read_stream, write_stream) as session:
        await session.initialize()
        tools = await session.list_tools()
        print(f"Available tools: {[tool.name for tool in tools.tools]}")

# To run the async function
import asyncio
asyncio.run(main())
