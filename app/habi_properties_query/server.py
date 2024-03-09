from app.habi_properties_query.utils import queries
from app.db import connection
from http.server import SimpleHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import json
import os

load_dotenv()

HOST = os.getenv("SERVICE_HOST", "localhost")
PORT = os.getenv("SERVICE_PORT", "8000")


class Handler(SimpleHTTPRequestHandler):
    """
    This class is responsible for generating the server Handler class that  will recive a POST request and a request
    body (if user want it) that will return a response with all the information of Habi's avialble properties for
    the external users.
    """

    @staticmethod
    def response_maker(request_body: str) -> str:
        """
        This method is responsible for generating the response for the POST method of this microservice. It works
        getting the request body sent by the user and use it to generate a SQL query, the data needed to be sent
        to Habi's MySQL and also, this method generates the JSON response body to be sent to the user.

        :param request_body: string containing the request body that was sent by the user through the POST method.
        :return: a JSON response body in str format to be sent to the user.
        """
        query_maker = queries.QueryMaker()
        db_connection = connection.DBConexion()

        conn = db_connection.get_db_connection()

        if conn:
            cursor = conn.cursor()

            query, values = query_maker.get_query(json.loads(request_body) if request_body else {})
            cursor.execute(query, values)
            results = cursor.fetchall()

            column_names = [item[0] for item in cursor.description]
            records = [dict(zip(column_names, row)) for row in results]

            cursor.close()
            conn.close()

            return json.dumps(records)

        else:
            raise ConnectionError(
                "No se pudo establecer conexión con la base de datos, verifique sus credenciales de acceso."
            )

    def do_POST(self):
        """
        This method is responsible for send an HTTP POST response to the user with te information requested.

        :return: a JSON response body in str format to be sent to the user or a text plain response if the server finds
        and error to notify to the user.
        """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        try:
            response = self.response_maker(body)

            if self.path == '/get_properties':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))

        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error en la solicitud realizada. Detalle: {e}'.encode('utf-8'))


def run_server():
    """
    Runs the server and closes when its needed. It uses the static variables HOST and PORT defined through the .env
    values for a more customizable experience using this server.
    :return:
    """
    api_server = HTTPServer((HOST, int(PORT)), Handler)
    print(f'Starting server on: {HOST}:{PORT}')

    try:
        api_server.serve_forever()

    except KeyboardInterrupt:
        pass

    api_server.server_close()
    print('Server closed succesfully')


if __name__ == '__main__':
    run_server()
