from mcp.server.fastmcp import FastMCP
import httpx, json

# https://lichess.org/api#tag/Games/operation/apiGamesUser

mcp_lichess = FastMCP("lichess")
        
@mcp_lichess.tool()
async def get_lichess_games_for_user(username: str, max_games: int) -> str:
    """
    Get lichess games for particular user
    Args:
        username: string
        max_games: int
    """
    async with httpx.AsyncClient() as client:
        try:
            headers = {
                "Accept": "application/json"
            }
            url = f"https://lichess.org/api/games/user/{username}?&max={max_games}"
            response = await client.get(url, headers=headers, timeout=60.0)
            response.raise_for_status()
            return response.text
        except Exception:
            return ""
        
if __name__ == "__main__":
    # Initialize and run the server
    mcp_lichess.run(transport='stdio')