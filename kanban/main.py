from mcp.server.fastmcp import FastMCP
from db import init_db
from helpers import fetch_ticket_details, create_ticket, update_ticket
from models import Ticket, TicketCreate, TicketUpdate

# Initialize the MCP server
mcp = FastMCP("Kanban")

# Expose the functions as tools to the MCP server

if __name__ == "__main__":
    print("Starting Kanban MCP server...")
    init_db()
    mcp.run(transport='stdio')
