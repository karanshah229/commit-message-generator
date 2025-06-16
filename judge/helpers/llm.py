import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

load_dotenv("../.env.local")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_mcp_client():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0.2)

    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../kanban/main.py"))
    print(OPENAI_API_KEY)
    print("script_path")
    print(script_path)

    config = {
      "mcpServers": {
        "Kanban": {
          "command": "python3",
          "args": [script_path]
        }
      }
    }

    client = MCPClient.from_dict(config)
    return MCPAgent(llm=llm, client=client, max_steps=2)
