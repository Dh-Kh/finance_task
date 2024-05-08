import psycopg2

def save_toDb(price_value: str) -> None:

    connection = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute(
        """"
        CREATE TABLE IF NOT EXISTS storageTG (
            id SERIAL PRIMARY KEY,
            exchange_rate VARCHAR(255),
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
    )
    cursor.execute(
        """INSERT INTO storageTG (exchange_rate) VALUES($1)""",
        price_value
    )
    


