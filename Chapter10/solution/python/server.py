from pydantic import BaseModel, Field, EmailStr

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from starlette.applications import Starlette
from starlette.routing import Mount, Host

mcp = FastMCP(name="Elicitation Example")

# todo: elicitation example, turn it into sse

class MemberPreferences(BaseModel):
    """Schema for collecting user preferences."""

    become_member: bool = Field(description="Want to be a member to receive discounts?")
    name: str = Field(
        default="",
        description="Your name"
    ),
    email: str = Field(
        default="",
        description="Your email address"
    )

@mcp.tool()
async def book_trip(date: str, member_id: str, ctx: Context[ServerSession, None]) -> str:
    """Book a trip check if member is available. If member is not present, ask for sign up."""
    # Check if member is available
    if not member_id or member_id == "guest":
        # Date unavailable - ask user for alternative
        result = await ctx.elicit(
            message=(f"Not a member? Would you like to sign up?"),
            schema=MemberPreferences,
        )

        if result.action == "accept" and result.data:
            if result.data.become_member and result.data.name and result.data.email:
                return f"[BOOKED] Booked for {date}, welcome {result.data.name} as a member!"
            return f"[BOOKED] for {date}, go to www.example.com to sign up if you change your mind on membership."
        return f"[BOOKED] for {date}, go to www.example.com to sign up."

    # Date available
    return f"[SUCCESS] Booked for {date}, for member {member_id}"

app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

if __name__ == "__main__":
    print("Starting Elicitation Example MCP Server...")
    mcp.run()