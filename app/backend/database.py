import os
import psycopg2


def get_connection():
    return psycopg2.connect(
        os.getenv("DATABASE_URL")
    )


def create_tables():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            problem_category VARCHAR(100) NOT NULL,
            problem_sub_category VARCHAR(200) NOT NULL,
            probelem_description VARCHAR(200),
            issue TEXT NOT NULL,
            status VARCHAR(50) DEFAULT 'Open',
            image_data BYTEA DEFAULT 'image-holder.jpg',
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()

    cur.close()
    conn.close()