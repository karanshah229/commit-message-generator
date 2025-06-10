import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

load_dotenv("../.env.local")
PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
VIRTUAL_KEY = os.getenv("PORTKEY_VIRTUAL_KEY")

def get_portkey_langchain_llm():
    portkey_headers = createHeaders(api_key=PORTKEY_API_KEY, virtual_key=VIRTUAL_KEY)

    return ChatOpenAI(api_key="X", base_url=PORTKEY_GATEWAY_URL, default_headers=portkey_headers, model="gpt-4o-mini", temperature=0.3)

def get_mcp_client():
    llm = get_portkey_langchain_llm()

    config = {
      "mcpServers": {
        "Kanban": {
          "command": "/Users/karan/.local/bin/uv",
          "args": [
            "--directory",
            "/Users/karan/hr/ai-agents/commit-message-generator/kanban",
            "run",
            "main.py"
          ]
        }
      }
    }

    client = MCPClient.from_dict(config)
    return MCPAgent(llm=llm, client=client, max_steps=2)
