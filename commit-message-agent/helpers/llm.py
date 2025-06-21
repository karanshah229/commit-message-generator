import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_llm():
    return ChatOpenAI(
      api_key=OPENAI_API_KEY,
      temperature=0,
      model="gpt-4o",
      max_retries=5,
  )

def get_mcp_client():
    llm = get_llm()
    current_dir = os.path.dirname(__file__)
    kanban_server_path = os.path.join(current_dir, '..', '..', 'kanban', 'main.py')

    config = {
      "mcpServers": {
        "Kanban": {
          "command": "python3",
          "args": [kanban_server_path]
        }
      }
    }

    client = MCPClient.from_dict(config)
    return MCPAgent(llm=llm, client=client, max_steps=2)
