import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    print("Available tools:", [t.name for t in tools])

    add_tool = next(t for t in tools if t.name == "add")

    result = await add_tool.arun({"a": 12, "b": 30})
    print("Add result:", result)

if __name__ == "__main__":
    asyncio.run(main())
