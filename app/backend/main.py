from fastapi import FastAPI, HTTPException

from database import get_connection, create_tables
from models import Ticket
from tickets import (
    create_ticket,
    get_all_tickets,
    update_ticket,
    delete_ticket
)


app = FastAPI(
    title="CloudAura IT Support API"
)


# =========================================================
# STARTUP
# =========================================================

@app.on_event("startup")
def startup():

    create_tables()


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "message": "CloudAura IT Support API is running"
    }


# =========================================================
# HEALTH
# =========================================================

@app.get("/health")
def health():

    try:

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT 1")
        cur.fetchone()

        cur.close()
        conn.close()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )


# =========================================================
# TICKETS
# =========================================================

@app.post("/tickets")
def create_ticket_endpoint(ticket: Ticket):

    return create_ticket(ticket)


@app.get("/tickets")
def get_tickets_endpoint():

    return get_all_tickets()


@app.put("/tickets/{ticket_id}")
def update_ticket_endpoint(
    ticket_id: int,
    ticket: Ticket
):

    return update_ticket(
        ticket_id,
        ticket
    )


@app.delete("/tickets/{ticket_id}")
def delete_ticket_endpoint(ticket_id: int):

    return delete_ticket(ticket_id)