from mcp.server.fastmcp import FastMCP
from db import init_db
from helpers import fetch_ticket_details, create_ticket, update_ticket
from models import Ticket, TicketCreate, TicketUpdate

mcp = FastMCP("Kanban")

@mcp.tool()
def tool_fetch_ticket(ticket_id: int) -> Ticket:
    """Get Kanban ticket details.

    Args:
        ticket_id: ID of the ticket to fetch.
    """
    return fetch_ticket_details(ticket_id)

@mcp.tool()
def tool_create_ticket(ticket: TicketCreate):
    """Create a new Kanban ticket.

    Args:
        ticket: object containing title, description, and status.
    """
    return create_ticket(ticket.title, ticket.description, ticket.status)

@mcp.tool()
def tool_update_ticket(ticket_id: int, ticket: TicketUpdate):
    """Update an existing Kanban ticket.

    Args:
        ticket_id: ID of the ticket to update.
        ticket: object containing updated title and/or description and/or status.
    """
    return update_ticket(ticket_id, ticket.title, ticket.description, ticket.status)

if __name__ == "__main__":
    init_db()
    mcp.run(transport='stdio')
