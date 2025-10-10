from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

import json


from uuid import uuid4
from typing import List
from pydantic import BaseModel

import json

mcp = FastMCP(name="Sampling Example")

# read file characters.json
with open("../characters.json") as f:
    characters = json.load(f)

@mcp.tool()
async def talk_to(name: str, topic: str, ctx: Context[ServerSession, None]) -> str:
    """Talk to a character and get a response."""

    # load character from characters
    # loop characters to find character with property "name" = name
    character = None
    for c in characters:
        if c["name"] == name:
            character = c
            break

    system_prompt = f" You are {character['name']}, {character['description']}, {character['personality']}"

    prompt = f"Talk to {name}."
    prompt += f" Discuss the topic of {topic}."
    
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        system_prompt=system_prompt,
        temperature=0.9,
        max_tokens=4000,
    )

    return result.content.text

if __name__ == "__main__":
    print("Starting server...")
    mcp.run()