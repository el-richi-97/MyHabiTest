import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv('../.env')


class DBConexion:
    """
    This class is responsible for connecting to MySQL. Here we connect to the database with the desired
    environment variables that need to be set in our .env file. These variables came from the Habi test requirements.
    """
    @staticmethod
    def get_db_connection():
        """
        This method will connect to the database using the environment variables defined in the .env file and returns
        a conection object that will be used in all the project modules.

        :return: MySQL connection object
        """
        try:
            conexion = mysql.connector.connect(
                host=os.getenv('HABI_SRC_HOST'),
                port=os.getenv('HABI_SRC_PORT'),
                user=os.getenv('HABI_SRC_USER'),
                password=os.getenv('HABI_SRC_PSSW'),
                database=os.getenv('HABI_SRC_DDBB')
            )

            return conexion

        except mysql.connector.Error as e:
            print(f"Sorry, there was an error while instancing the db: {e}")

            return None


if __name__ == '__main__':

    test_db = DBConexion

    test_conn = test_db.get_db_connection()

    print(type(test_conn))

    if test_conn:
        cursor = test_conn.cursor()
        cursor.execute("SELECT * FROM property;")

        test_result = cursor.fetchall()

        for i, item in enumerate(test_result):
            print(f'result # {i + 1}: {item}')

    else:
        print("No connection established. Finishing this execution.")
