from mcp.server.fastmcp import FastMCP

app = FastMCP()

@app.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b

if __name__ == "__main__":
    print("Starting MCP server on streamable-http...")
    app.run(transport="streamable-http")
