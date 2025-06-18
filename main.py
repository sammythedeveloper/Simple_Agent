from mcp import ClientSession , StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langgraph.openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()
model = ChatOpenAI(
    model='gpt-4.1',
    temperature=0,
    openai_api_key=os.getenv('OPENAI_API_KEY'),
)
server_params = StdioServverParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=["firecrawl-mcp"]
)
async def main():