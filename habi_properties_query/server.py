from utils import queries
from db import connection

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

HOST = 'localhost'
PORT = 8000


class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        query_maker = queries.QueryMaker()
        db_connection = connection.DBConexion()
        conn = db_connection.get_db_connection()
        cursor = conn.cursor()

        try:
            query, values = query_maker.get_query(json.loads(body) if body else {})

            cursor.execute(query, values)
            results = cursor.fetchall()

            column_names = [i[0] for i in cursor.description]
            records = [dict(zip(column_names, row)) for row in results]
            response = json.dumps(records)

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

            pass

        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    with HTTPServer((HOST, PORT), Handler) as server:
        print(f'Starting server on: {HOST}:{PORT}')
        server.serve_forever()
