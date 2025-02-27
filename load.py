import mysql.connector
import logging
# Configure logging

logging.basicConfig(
    filename="etl_pipeline.log",  # Log file name
    level=logging.INFO,  # Log level (INFO, ERROR, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
def load_data(df):
    #connect to Mysql Database

    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password= 'admin',
        database= 'etl_pipeline'
    )

    cursor = conn.cursor()
    #Insert data into the posts table
    logging.info("Connected to MySQL database successfully.")
    for index, row in df.iterrows():
        try:
            cursor.execute("INSERT INTO posts (title, body) VALUES (%s, %s)", (row['title'], row['body']))
        # The cursor takes an SQL command and executes it.
        # The (%s, %s) are placeholders, and row['title'], row['body'] are the actual values.

        except mysql.connector.Error as e:
            logging.error(f"Error inserting row{index}: {e}")
   



    # Commit and close the connection
    conn.commit()

    cursor.close()
    conn.close()