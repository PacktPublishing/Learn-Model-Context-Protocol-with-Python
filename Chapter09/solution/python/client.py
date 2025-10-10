"""
cd to the `examples/snippets/clients` directory and run:
    uv run client
"""

import asyncio
import os

from pydantic import AnyUrl

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext

import os
from openai import OpenAI

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Using python to run the server
    args=["server.py"]
)

async def call_llm(prompt: str, system_prompt: str) -> str:
    client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"],
)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="openai/gpt-4o-mini",
        temperature=1,
        max_tokens=200,
        top_p=1
    )

    return response.choices[0].message.content


# Optional: create a sampling callback
async def handle_sampling_message(
    context: RequestContext[ClientSession, None], params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    print(f"Sampling request: {params.messages}")

    message = params.messages[0].content.text
    system_prompt = params.systemPrompt or "You're a helpful assistant, keep to the topic, don't make things up too much but definitely create a compelling product description"

    # todo, call an actual llm and change below
    response = await call_llm(message, system_prompt)

    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text=response,
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling_message) as session:
            # Initialize the connection
            await session.initialize()


            # Call a tool (create_product tool from fastmcp_quickstart)
            result = await session.call_tool("talk_to", arguments={"name": "Monsieur Lestrange", "topic": "Tell me about you"})
            print("result:", result.content[0].text)


def main():
    """Entry point for the client script."""
    asyncio.run(run())


if __name__ == "__main__":
    main()