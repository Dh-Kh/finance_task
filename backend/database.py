from typing import List
from settings import (DB_NAME, DB_USER, 
                      DB_PASSWORD, DB_HOST)
import psycopg2

def save_toDb(price_value: str) -> None:
    
    connection = psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD,
        host=DB_HOST
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS storageTG (
            id SERIAL PRIMARY KEY,
            exchange_rate VARCHAR(255),
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
    )
    cursor.execute(
        """INSERT INTO storageTG (exchange_rate) VALUES(%s)""",
        (price_value,)
    )
    connection.commit()
    connection.close()
    
def retrieve_fromDb() -> List[str]:
        
    connection = psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD,
        host=DB_HOST
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT datetime, exchange_rate FROM storageTG
        WHERE DATE(datetime) = CURRENT_DATE
        """
    )
    rows = cursor.fetchall()
    connection.close()
    return rows



