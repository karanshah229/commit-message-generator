from fastapi import FastAPI, Query
from kanban.db import init_db
from kanban.mcp_tools import fetch_ticket_details, create_ticket, update_ticket
from kanban.models import Ticket, TicketCreate, TicketUpdate

app = FastAPI(title="Kanban MCP Server")

@app.on_event("startup")
def setup():
    init_db()

@app.get("/tools/fetch_ticket")
def tool_fetch_ticket(ticket_id: int):
    return fetch_ticket_details(ticket_id)

@app.post("/tools/create_ticket")
def tool_create_ticket(ticket: TicketCreate):
    return create_ticket(ticket.title, ticket.description, ticket.status)

@app.put("/tools/update_ticket")
def tool_update_ticket(ticket_id: int, ticket: TicketUpdate):
    return update_ticket(ticket_id, ticket.title, ticket.description, ticket.status)
