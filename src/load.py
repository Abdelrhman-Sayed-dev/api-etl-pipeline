import os
from dotenv import load_dotenv
import psycopg
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def connect_db():
    logging.info("Connecting to the PostgreSQL database...")

    try:
        conn = psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        logging.info("Successfully connected to the PostgreSQL database.")
        return conn

    except Exception as e:
        logging.error(f"Could not connect to the PostgreSQL database: {e}")
        return None


def load_data(df):
    connection = connect_db()

    if not connection:
        return

    try:
        with connection.cursor() as cursor:

            query = """
                INSERT INTO order_items (
                    product_id,
                    order_id,
                    user_id,
                    title,
                    price,
                    quantity,
                    total,
                    discount_percentage,
                    discounted_total,
                    discount_amount
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id, product_id) DO NOTHING
            """

            cursor.executemany(
                query,
                df.itertuples(index=False, name=None)
            )

            connection.commit()

            logging.info("Data loaded successfully.")

    except Exception as e:
        connection.rollback()
        logging.error(f"Failed to load data: {e}")

    finally:
        connection.close()