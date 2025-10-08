from fastmcp import FastMCP
import asyncio
import uvicorn

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # HTTPサーバーとして起動
    print("Starting MCP server on http://localhost:8000")
    mcp.run(transport="http", host="0.0.0.0", port=8000)