from fastapi import HTTPException

from database import get_connection
from models import Ticket


def create_ticket(ticket: Ticket):

    try:

        conn = get_connection()
        cur = conn.cursor()

        binary_image = (
            ticket.image_data.encode("utf-8")
            if ticket.image_data
            else None
        )

        cur.execute(
            """
            INSERT INTO tickets (
                name,
                email,
                problem_category,
                problem_sub_category,
                probelem_description,
                issue,
                status,
                image_data
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                ticket.name,
                ticket.email,
                ticket.problem_category,
                ticket.problem_sub_category,
                ticket.probelem_description,
                ticket.issue,
                ticket.status,
                binary_image
            )
        )

        result = cur.fetchone()

        ticket_id = result[0]

        conn.commit()

        cur.close()
        conn.close()

        return {
            "message": "Ticket created successfully",
            "ticket_id": ticket_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to create ticket: {str(e)}"
        )


def get_all_tickets():

    try:

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT
                id,
                name,
                email,
                problem_category,
                problem_sub_category,
                probelem_description,
                issue,
                status
            FROM tickets
            ORDER BY id DESC
            """
        )

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "problem_category": row[3],
                "problem_sub_category": row[4],
                "probelem_description": row[5],
                "issue": row[6],
                "status": row[7]
            }
            for row in rows
        ]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve tickets: {str(e)}"
        )


def update_ticket(ticket_id: int, ticket: Ticket):

    try:

        conn = get_connection()
        cur = conn.cursor()

        binary_image = (
            ticket.image_data.encode("utf-8")
            if ticket.image_data
            else None
        )

        cur.execute(
            """
            UPDATE tickets
            SET
                name=%s,
                email=%s,
                problem_category=%s,
                problem_sub_category=%s,
                probelem_description=%s,
                issue=%s,
                status=%s,
                image_data=%s
            WHERE id=%s
            """,
            (
                ticket.name,
                ticket.email,
                ticket.problem_category,
                ticket.problem_sub_category,
                ticket.probelem_description,
                ticket.issue,
                ticket.status,
                binary_image,
                ticket_id
            )
        )

        if cur.rowcount == 0:

            cur.close()
            conn.close()

            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )

        conn.commit()

        cur.close()
        conn.close()

        return {
            "message": "Ticket updated successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to update ticket: {str(e)}"
        )


def delete_ticket(ticket_id: int):

    try:

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM tickets WHERE id=%s",
            (ticket_id,)
        )

        if cur.rowcount == 0:

            cur.close()
            conn.close()

            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )

        conn.commit()

        cur.close()
        conn.close()

        return {
            "message": "Ticket deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to delete ticket: {str(e)}"
        )