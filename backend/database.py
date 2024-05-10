from typing import List
import psycopg2

def save_toDb(price_value: str) -> None:
    
    connection = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='12345',
        host='pgdb'
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
        dbname='postgres', 
        user='postgres', 
        password='12345',
        host='pgdb'
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



