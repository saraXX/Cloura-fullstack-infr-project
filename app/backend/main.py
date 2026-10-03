from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os

# Create the FastAPI application
app = FastAPI(title="CloudAura IT Support API")


# Connect the backend to the PostgreSQL database
def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


# Define the data structure for a support ticket
class Ticket(BaseModel):
    name: str
    issue: str


# Create the tickets table when the application starts
@app.on_event("startup")
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            issue TEXT NOT NULL,
            status VARCHAR(50) DEFAULT 'Open'
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


# Root endpoint to check that the API is running
@app.get("/")
def root():
    return {"message": "CloudAura IT Support API is running"}


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Create a new support ticket
@app.post("/tickets")
def create_ticket(ticket: Ticket):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tickets (name, issue) VALUES (%s, %s) RETURNING id",
        (ticket.name, ticket.issue)
    )

    ticket_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {
        "message": "Ticket created successfully",
        "ticket_id": ticket_id
    }


# Get all support tickets
@app.get("/tickets")
def get_tickets():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, issue, status FROM tickets ORDER BY id DESC"
    )

    tickets = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "issue": row[2],
            "status": row[3]
        }
        for row in tickets
    ]


# Update an existing support ticket
@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE tickets SET name=%s, issue=%s WHERE id=%s",
        (ticket.name, ticket.issue, ticket_id)
    )

    # Return an error if the ticket does not exist
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Ticket updated successfully"}


# Delete an existing support ticket
@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tickets WHERE id=%s",
        (ticket_id,)
    )

    # Return an error if the ticket does not exist
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Ticket deleted successfully"}
